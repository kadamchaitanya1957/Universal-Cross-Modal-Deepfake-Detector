import { useEffect, useState } from "react";
import "./Navbar.css";

const NAV_LINKS = ["Home", "Features", "About"];

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 8);
    handleScroll();
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const closeMenu = () => setIsMenuOpen(false);

  return (
    <nav className={`navbar ${isScrolled ? "navbar--scrolled" : ""}`}>
      <div className="navbar__container">
        <a href="#home" className="navbar__logo" onClick={closeMenu}>
          Logo
        </a>

        <ul
          id="navbar-menu"
          className={`navbar__menu ${isMenuOpen ? "navbar__menu--open" : ""}`}
        >
          {NAV_LINKS.map((link) => (
            <li key={link} className="navbar__item">
              <a
                href={`#${link.toLowerCase()}`}
                className="navbar__link"
                onClick={closeMenu}
              >
                {link}
              </a>
            </li>
          ))}
          <li className="navbar__item navbar__item--cta">
            <button type="button" className="navbar__cta" onClick={closeMenu}>
              Get Started
            </button>
          </li>
        </ul>

        <button
          type="button"
          className={`navbar__toggle ${isMenuOpen ? "navbar__toggle--open" : ""}`}
          onClick={() => setIsMenuOpen((prev) => !prev)}
          aria-label="Toggle navigation menu"
          aria-expanded={isMenuOpen}
          aria-controls="navbar-menu"
        >
          <span className="navbar__toggle-bar" />
          <span className="navbar__toggle-bar" />
          <span className="navbar__toggle-bar" />
        </button>
      </div>
    </nav>
  );
}