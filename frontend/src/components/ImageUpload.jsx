import React, { useState, useRef } from "react";
import { FaFileUpload, FaTrashAlt } from "react-icons/fa";
const ImageUpload = () => {
  const [image, setImage] = useState(null);
  const [imageUrl, setImageUrl] = useState(null);

  const handleImageChange = (event) => {
    const selectedImage = event.target.files?.[0];
    if (selectedImage) {
      setImage(selectedImage);
      setImageUrl(URL.createObjectURL(selectedImage));
    }
  };

  const deleteImage = () => {
    setImage(null);
    setImageUrl(null);
    const fileInput = document.getElementById("fileInput");
    if (fileInput) {
      fileInput.value = null; // Clear the file input value
    }
  };

  return (
    <div className="flex flex-col items-center">
      {image == null ? (
        <div>
          <input
            type="file"
            name="datei"
            accept=".jpg, .png, .webp"
            id="fileInput"
            onChange={handleImageChange}
            className="hidden"
          />
          <label
            htmlFor="fileInput"
            className="cursor-pointer flex flex-col items-center justify-center w-64 h-64 border-2 border-dashed border-gray-300 rounded-lg"
          >
            <h1 className="text-16xl">
              <FaFileUpload />
            </h1>
            <p className="text-center text-white">Upload Webtoon here</p>
            <p className="text-center text-white">(jpg, png, webp)</p>
          </label>
        </div>
      ) : (
        <div className="flex flex-col items-center">
          <img src={imageUrl} alt="Selected" className="w-full h-auto" />
          <button onClick={deleteImage}>
            <FaTrashAlt />
          </button>
        </div>
      )}
    </div>
  );
};

export default ImageUpload;
