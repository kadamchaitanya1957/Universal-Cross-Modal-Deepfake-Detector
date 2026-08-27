import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def upload_dir(tmp_path, monkeypatch):
    """Run the request inside a temporary cwd so uploads/ is not polluted."""
    monkeypatch.chdir(tmp_path)
    return tmp_path / "uploads"
