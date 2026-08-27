import pytest

CONTENT = b"fake-image-bytes"


def post_file(client, filename="photo.png", content_type="image/png"):
    return client.post(
        "/analyze",
        files={"file": (filename, CONTENT, content_type)},
    )


def test_accepts_supported_file(client, upload_dir):
    response = post_file(client)

    assert response.status_code == 200
    body = response.json()
    assert body["filename"] == "photo.png"
    assert body["content_type"] == "image/png"
    assert body["status"] == "uploaded"
    assert body["prediction"]
    assert "confidence" in body


def test_persists_upload_to_disk(client, upload_dir):
    post_file(client)

    assert (upload_dir / "photo.png").read_bytes() == CONTENT


@pytest.mark.parametrize(
    "content_type",
    ["text/plain", "application/json", "image/gif"],
)
def test_rejects_unsupported_content_type(client, upload_dir, content_type):
    response = post_file(client, filename="notes.txt", content_type=content_type)

    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported file type."


def test_rejected_upload_is_not_written(client, upload_dir):
    post_file(client, filename="notes.txt", content_type="text/plain")

    assert not upload_dir.exists()


def test_requires_file_field(client, upload_dir):
    assert client.post("/analyze").status_code == 422


def test_rejects_get_requests(client):
    assert client.get("/analyze").status_code == 405
