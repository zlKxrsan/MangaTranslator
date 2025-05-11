import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { Canvas } from "fabric";
import ImageUpload from "./components/ImageLoader";
import Editor from "./components/Editor";

function App() {
  const [imageUrl, setImageUrl] = useState(null);

  const handleImageUpload = (event) => {
    const file = event.target.files?.[0];
    if (file) {
      const newImageUrl = URL.createObjectURL(file);
      setImageUrl(newImageUrl);
    }
  };

  const handleIamgeDelete = () => {
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
        <ImageUpload imageUrl={imageUrl} onImageUpload={handleImageUpload} />
      ) : (
        <Editor imageUrl={imageUrl} onImageDelete={handleIamgeDelete} />
      )}
    </div>
  );
}

export default App;
