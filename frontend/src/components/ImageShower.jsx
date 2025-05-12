import React from "react";
import { FaFileDownload, FaRegTrashAlt } from "react-icons/fa";

/**
 * Component for displaying the translated image and providing toolbar actions.
 * Allows the user to delete the image or download it.
 *
 * Props:
 * - imageUrl: The URL of the image to display.
 * - onImageDelete: Function to call when the image should be deleted.
 */
const ImageShower = ({ imageUrl, onImageDelete }) => {
  /**
   * Triggers a download of the currently displayed image.
   */
  const downloadImage = () => {
    if (!imageUrl) return;
    const link = document.createElement("a");
    link.href = imageUrl;
    link.download = "downloaded-image";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  /**
   * Toolbar component with delete and download buttons.
   */
  const Toolbar = () => (
    <div className="fixed top-0 right-0 z-50 bg-grey-900 shadow-lg">
      <div className="flex flex-row items-center justify-center">
        <button
          onClick={onImageDelete}
          className="flex justify-center w-32 h-32"
          aria-label="Delete image"
        >
          <FaRegTrashAlt className="w-24 h-24" />
        </button>
        <button
          onClick={downloadImage}
          className="flex justify-center w-32 h-32"
          aria-label="Download image"
        >
          <FaFileDownload className="w-24 h-24" />
        </button>
      </div>
    </div>
  );

  return (
    <div>
      <Toolbar />
      <div className="flex flex-col items-center">
        <img src={imageUrl} alt="No image available (try reloading the page)" />
      </div>
    </div>
  );
};

export default ImageShower;
