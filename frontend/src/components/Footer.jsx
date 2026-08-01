import { Github, Twitter, BookOpen } from "lucide-react";
import "./Footer.css";

const QUICK_LINKS = ["Home", "Features", "About"];

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer__grid">
        <div className="footer__section footer__section--brand">
          <span className="footer__project-name">Cross-Modal Detector</span>
          <p className="footer__description">
            Unified detection for AI-generated media across every modality.
          </p>
        </div>

        <nav className="footer__section" aria-label="Quick links">
          <h3 className="footer__heading">Quick Links</h3>
          <ul className="footer__links">
            {QUICK_LINKS.map((link) => (
              <li key={link}>
                <a href={`#${link.toLowerCase()}`} className="footer__link">
                  {link}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div className="footer__section footer__section--social">
          <h3 className="footer__heading">Connect</h3>
          <div className="footer__icons">
            <a href="#" className="footer__icon-link" aria-label="GitHub">
              <Github size={18} aria-hidden="true" />
            </a>
            <a href="#" className="footer__icon-link" aria-label="Twitter">
              <Twitter size={18} aria-hidden="true" />
            </a>
            <a href="#" className="footer__icon-link" aria-label="Documentation">
              <BookOpen size={18} aria-hidden="true" />
            </a>
          </div>
        </div>
      </div>

      <div className="footer__bottom">
        <p className="footer__copyright">
          &copy; {new Date().getFullYear()} Cross-Modal Detector. All rights reserved.
        </p>
      </div>
    </footer>
  );
}