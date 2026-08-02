import { useRef, useState } from "react";
import axios from "axios";
import { UploadCloud, Image, Video, FileText } from "lucide-react";
import "./UploadCard.css";
export default function UploadCard() {
  const fileInputRef = useRef(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const handleChooseFileClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setResult(null);
      setErrorMessage("");
    }
  };

  const handleAnalyze = async () => {
    if (!selectedFile) return;
    setErrorMessage("");
    const formData = new FormData();
    formData.append("file", selectedFile);

    setIsLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );

      setResult(response.data);
    } catch (error) {
      if (error.response) {
        setErrorMessage(error.response.data.detail);
      } else {
        setErrorMessage("Unable to connect to the server.");
      }
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <section className="upload-card" aria-labelledby="upload-card-heading">
      <h2 id="upload-card-heading" className="upload-card__heading">
        Upload Media
      </h2>
      <p className="upload-card__description">
        Upload Images, Videos or PDF Documents.
      </p>
      <div className="upload-card__dropzone">
        <UploadCloud className="upload-card__icon" aria-hidden="true" size={36} />
        <p className="upload-card__dropzone-text">Drag & drop your file here</p>
        <ul className="upload-card__formats">
          <li className="upload-card__format">
            <Image size={16} aria-hidden="true" />
            <span>Images</span>
          </li>
          <li className="upload-card__format">
            <Video size={16} aria-hidden="true" />
            <span>Videos</span>
          </li>
          <li className="upload-card__format">
            <FileText size={16} aria-hidden="true" />
            <span>PDF</span>
          </li>
        </ul>
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          style={{ display: "none" }}
        />
        <button
          type="button"
          className="upload-card__button"
          onClick={handleChooseFileClick}
        >
          Choose File
        </button>
        {selectedFile && (
          <p className="upload-card__filename">{selectedFile.name}</p>
        )}
        <button
          type="button"
          className="upload-card__button upload-card__button--analyze"
          onClick={handleAnalyze}
          disabled={!selectedFile || isLoading}
        >
          {isLoading ? "Analyzing..." : "Analyze"}
        </button>
        {errorMessage && (
          <p className="upload-card__error">
            {errorMessage}
          </p>
        )}
        {result && (
          <div className="upload-card__result">
            <p><strong>Filename:</strong> {result.filename}</p>
            <p><strong>Type:</strong> {result.content_type}</p>
            <p><strong>Status:</strong> {result.status}</p>
            <p><strong>Prediction:</strong> {result.prediction}</p>
            <p><strong>Confidence:</strong> {result.confidence ?? "N/A"}</p>
          </div>
        )}
      </div>
    </section>
  );
}