import { UploadCloud, Image, Video, FileText } from "lucide-react";
import "./UploadCard.css";

export default function UploadCard() {
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
        <p className="upload-card__dropzone-text">Drag &amp; drop your file here</p>

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

        <button type="button" className="upload-card__button">
          Choose File
        </button>
      </div>
    </section>
  );
}