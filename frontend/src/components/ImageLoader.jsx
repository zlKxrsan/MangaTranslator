import React, { useState, useRef, useEffect } from "react";
import { FaFileUpload, FaTrashAlt } from "react-icons/fa";
import axios from "axios";
import DropDownMenu from "./DropDownMenu";

const ImageUpload = ({ onImageTranslated }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [targetLang, setTargetLang] = useState("DE");

  const handleImageUpload = (event) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
    } else {
      const exampleUrl = "example_panel.png";

      fetch(exampleUrl)
        .then((res) => res.blob())
        .then((blob) => {
          const exampleFile = new File([blob], "example_panel.png", {
            type: blob.type,
          });
          setSelectedFile(exampleFile);
        })
        .catch((err) =>
          console.error("Fehler beim Laden des Fallback-Bildes:", err)
        );
    }
  };

  useEffect(() => {
    if (!selectedFile) return;

    const upload = async () => {
      const formData = new FormData();
      formData.append("file", selectedFile);
      formData.append("target_lang", targetLang);

      try {
        const response = await axios.post(
          "http://localhost:8000/translate/",
          formData,
          {
            responseType: "blob",
          }
        );

        const imageUrl = URL.createObjectURL(response.data);
        onImageTranslated(imageUrl);
      } catch (error) {
        console.error("Upload Fehler:", error);
      }
    };

    upload();
  }, [selectedFile, onImageTranslated]);

  return (
    <div>
      <div className="flex flex-row items-center justify-center">
        <input
          type="file"
          name="data"
          accept=".jpg, .png, .webp"
          id="fileInput"
          onChange={handleImageUpload}
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
        <button
          type="file"
          name="exampleData"
          id="exampleInput"
          onClick={handleImageUpload}
          className="hidden"
        >
          Test
        </button>

        <label
          htmlFor="exampleInput"
          className="cursor-pointer flex-row item-center justify-center w-64 h-64 rounded-lg"
        >
          <img
            src="example_panel.png"
            alt="Use Test Panel"
            className="w-48 h-48 mt-8 ml-8"
          />
          <p className="text-center text-white">Or use example</p>
        </label>
      </div>
      <div>
        <DropDownMenu onLangChange={setTargetLang} />
      </div>
    </div>
  );
};

export default ImageUpload;
