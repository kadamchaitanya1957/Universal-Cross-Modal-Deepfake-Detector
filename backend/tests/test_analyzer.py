import pytest

from services.analyzer import analyze_file


@pytest.fixture
def sample_file(tmp_path):
    path = tmp_path / "sample.png"
    path.write_bytes(b"\x89PNG\r\n\x1a\n")
    return path


def test_returns_expected_keys(sample_file):
    result = analyze_file(str(sample_file))

    assert set(result) == {
        "prediction",
        "confidence",
        "model",
        "processing_time_ms",
    }


def test_result_value_types_and_ranges(sample_file):
    result = analyze_file(str(sample_file))

    assert isinstance(result["prediction"], str)
    assert isinstance(result["confidence"], (int, float))
    assert 0 <= result["confidence"] <= 100
    assert isinstance(result["model"], str)
    assert isinstance(result["processing_time_ms"], int)
    assert result["processing_time_ms"] >= 0


def test_is_deterministic(sample_file):
    assert analyze_file(str(sample_file)) == analyze_file(str(sample_file))


def test_missing_file_does_not_raise():
    """The placeholder model reports a result without touching the file."""
    assert analyze_file("does/not/exist.png")["prediction"]
