import Navbar from "./Navbar";
import Hero from "./Hero";
import UploadCard from "./UploadCard";
import Footer from "./Footer";
import "./LandingPage.css";

export default function LandingPage() {
  return (
    <>
      <Navbar />
      <main className="landing-page">
        <Hero />
        <div className="landing-page__section">
          <UploadCard />
        </div>
      </main>
      <Footer />
    </>
  );
}