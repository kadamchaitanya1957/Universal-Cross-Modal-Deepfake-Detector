import { useId, useRef, useState } from "react";
import { UploadCloud, Image, Video, FileText, AlertCircle } from "lucide-react";
import {
  ACCEPT_ATTRIBUTE,
  UNSUPPORTED_FILE_MESSAGE,
  isSupportedMediaFile,
} from "../utils/mediaTypes.js";
import "./UploadCard.css";

export default function UploadCard() {
  const inputRef = useRef(null);
  const dragCounterRef = useRef(0);
  const inputId = useId();
  const errorId = useId();
  const [fileName, setFileName] = useState(null);
  const [error, setError] = useState(null);
  const [isDragActive, setIsDragActive] = useState(false);

  const openFilePicker = () => {
    inputRef.current?.click();
  };

  const processFile = (file) => {
    if (!file) {
      return;
    }

    if (!isSupportedMediaFile(file)) {
      setFileName(null);
      setError(UNSUPPORTED_FILE_MESSAGE);
      return;
    }

    setError(null);
    setFileName(file.name);
  };

  const handleFileChange = (event) => {
    const file = event.target.files?.[0];
    processFile(file);

    if (file && !isSupportedMediaFile(file)) {
      event.target.value = "";
    }
  };

  const handleDragEnter = (event) => {
    event.preventDefault();
    dragCounterRef.current += 1;
    if (event.dataTransfer.types.includes("Files")) {
      setIsDragActive(true);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  const handleDragLeave = (event) => {
    event.preventDefault();
    dragCounterRef.current -= 1;
    if (dragCounterRef.current <= 0) {
      dragCounterRef.current = 0;
      setIsDragActive(false);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    dragCounterRef.current = 0;
    setIsDragActive(false);

    const file = event.dataTransfer.files?.[0];
    processFile(file);
  };

  return (
    <section className="upload-card" aria-labelledby="upload-card-heading">
      <h2 id="upload-card-heading" className="upload-card__heading">
        Upload Media
      </h2>
      <p className="upload-card__description">
        Upload Images, Videos or PDF Documents.
      </p>

      <div
        className={`upload-card__dropzone${
          isDragActive ? " upload-card__dropzone--active" : ""
        }`}
        onDragEnter={handleDragEnter}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <UploadCloud className="upload-card__icon" aria-hidden="true" size={36} />
        <p className="upload-card__dropzone-text">
          {isDragActive ? "Release to upload" : "Drag & drop your file here"}
        </p>

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

        <label htmlFor={inputId} className="visually-hidden">
          Choose an image, video, or PDF file to upload
        </label>
        <input
          ref={inputRef}
          id={inputId}
          type="file"
          className="visually-hidden"
          accept={ACCEPT_ATTRIBUTE}
          aria-describedby={error ? errorId : undefined}
          onChange={handleFileChange}
        />

        <button
          type="button"
          className="upload-card__button"
          onClick={openFilePicker}
        >
          Choose File
        </button>

        {fileName && !error && (
          <p className="upload-card__filename">
            Selected file: <span>{fileName}</span>
          </p>
        )}

        {error && (
          <p id={errorId} className="upload-card__error" role="alert">
            <AlertCircle size={16} aria-hidden="true" />
            <span>{error}</span>
          </p>
        )}
      </div>
    </section>
  );
}