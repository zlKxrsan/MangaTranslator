import { useState } from "react";
import "./App.css";
import ImageUpload from "./components/ImageLoader";
import ImageShower from "./components/ImageShower";

/**
 * Main application component for ToonLingo.
 * Handles image upload, display, and deletion logic.
 */
function App() {
  // State to store the current image URL
  const [imageUrl, setImageUrl] = useState(null);

  /**
   * Handles the deletion of the currently displayed image.
   * Resets the image URL state and revokes the object URL to free memory.
   */
  const handleImageDelete = () => {
    if (imageUrl) {
      URL.revokeObjectURL(imageUrl);
      setImageUrl(null);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">
        <span className="text-yellow-300">ToonLingo</span> – a translation tool for Webtoons
      </h1>
      {/* Show the upload component if no image is selected, otherwise show the image viewer */}
      {!imageUrl ? (
        <ImageUpload onImageTranslated={setImageUrl} />
      ) : (
        <ImageShower imageUrl={imageUrl} onImageDelete={handleImageDelete} />
      )}
    </div>
  );
}

export default App;
