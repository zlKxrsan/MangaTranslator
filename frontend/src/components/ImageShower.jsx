import React, { useState, useRef, useEffect } from "react";
import { FaFileDownload, FaRegTrashAlt } from "react-icons/fa";

const ImageShower = ({ imageUrl, onImageDelete }) => {
  const downloadCanvas = () => {
    if (!imageUrl) return;

    const link = document.createElement("a");
    link.href = imageUrl;
    link.download = "downloaded-image";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const Toolbar = () => {
    return (
      <div className="fixed top-0 right-0 z-50 bg-grey-900 shadow-lg">
        <div className="flex flex-row items-center justify-center">
          <button
            onClick={onImageDelete}
            className="flex justify-center w-32 h-32"
          >
            <FaRegTrashAlt className="w-24 h-24" />
          </button>
          <button
            onClick={downloadCanvas}
            className="flex justify-center w-32 h-32"
          >
            <FaFileDownload className="w-24 h-24" />
          </button>
        </div>
      </div>
    );
  };

  return (
    <div>
      <Toolbar />
      <div className="flex flex-col items-center">
        <img src={imageUrl} alt="there is no picture (reload the page?)" />
      </div>
    </div>
  );
};

export default ImageShower;
