import React, { useState, useRef } from "react";
import { FaFileUpload, FaTrashAlt } from "react-icons/fa";
const ImageUpload = ({ imageUrl, onImageUpload }) => {
  return (
    <div className="flex flex-col items-center">
      <div>
        <input
          type="file"
          name="datei"
          accept=".jpg, .png, .webp"
          id="fileInput"
          onChange={onImageUpload}
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
    </div>
  );
};

export default ImageUpload;
