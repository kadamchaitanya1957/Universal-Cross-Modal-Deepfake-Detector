import "./Hero.css";

export default function Hero() {
  return (
    <section className="hero" aria-label="Introduction">
      <div className="hero__glow" aria-hidden="true" />

      <div className="hero__container">
        <h1 className="hero__headline">
          Universal Cross-Modal
          <br />
          Deepfake Detection
        </h1>

        <p className="hero__subheading">
          Detect AI-generated Images, Videos and Documents using advanced
          multimodal intelligence.
        </p>

        <div className="hero__actions">
          <button type="button" className="hero__btn hero__btn--primary">
            Analyze Media
          </button>
          <button type="button" className="hero__btn hero__btn--secondary">
            Learn More
          </button>
        </div>
      </div>
    </section>
  );
}