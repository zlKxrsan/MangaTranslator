import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import ImageUpload from "./components/ImageLoader";
import ImageShower from "./components/ImageShower";

function App() {
  const [imageUrl, setImageUrl] = useState(null);

  const handleImageDelete = () => {
    setImageUrl(null);
    URL.revokeObjectURL(imageUrl);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">
        <span className="text-yellow-300">ToonLingo</span> a translation-tool
        for Webtoons
      </h1>
      {!imageUrl ? (
        <ImageUpload onImageTranslated={setImageUrl} />
      ) : (
        <ImageShower imageUrl={imageUrl} onImageDelete={handleImageDelete} />
      )}
    </div>
  );
}

export default App;
