import pytest

from utils.file_validation import ALLOWED_MIME_TYPES, is_allowed_file


@pytest.mark.parametrize("content_type", sorted(ALLOWED_MIME_TYPES))
def test_allowed_mime_types_are_accepted(content_type):
    assert is_allowed_file(content_type) is True


@pytest.mark.parametrize(
    "content_type",
    [
        "text/plain",
        "application/json",
        "application/octet-stream",
        "image/gif",
        "IMAGE/PNG",
        "image/png ",
        "application/x-msdownload",
    ],
)
def test_unsupported_mime_types_are_rejected(content_type):
    assert is_allowed_file(content_type) is False


@pytest.mark.parametrize("content_type", [None, ""])
def test_missing_mime_type_is_rejected(content_type):
    assert is_allowed_file(content_type) is False


def test_allowed_set_covers_every_supported_modality():
    assert {t for t in ALLOWED_MIME_TYPES if t.startswith("image/")}
    assert {t for t in ALLOWED_MIME_TYPES if t.startswith("video/")}
    assert {t for t in ALLOWED_MIME_TYPES if t.startswith("audio/")}
    assert "application/pdf" in ALLOWED_MIME_TYPES
