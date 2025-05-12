import React, { useState, useEffect } from "react";
import { FaFileUpload } from "react-icons/fa";
import axios from "axios";
import DropDownMenu from "./DropDownMenu";

/**
 * Component for uploading an image and selecting a target language.
 * Handles both user-uploaded and example images, and sends them to the backend for translation.
 */
const ImageUpload = ({ onImageTranslated }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [targetLang, setTargetLang] = useState("DE");

  /**
   * Handles file input changes or example image selection.
   * If a file is selected, it sets it as the selected file.
   * If not, it loads the example image as a fallback.
   */
  const handleImageUpload = (event) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
    } else {
      // Fallback: load the example image if no file is selected
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
          console.error("Error loading fallback image:", err)
        );
    }
  };

  /**
   * Effect to upload the selected file to the backend for translation.
   * On success, creates a URL for the translated image and passes it to the parent.
   */
  useEffect(() => {
    if (!selectedFile) return;

    const upload = async () => {
      const formData = new FormData();
      formData.append("file", selectedFile);
      formData.append("target_lang", targetLang);

      try {
        const response = await axios.post(
          "http://localhost:8000/translate/", //change backend->localhost if not composed in a container.
          formData,
          { responseType: "blob" }
        );
        const imageUrl = URL.createObjectURL(response.data);
        onImageTranslated(imageUrl);
      } catch (error) {
        console.error("Upload error:", error);
      }
    };

    upload();
  }, [selectedFile, targetLang, onImageTranslated]);

  return (
    <div>
      <div className="flex flex-row items-center justify-center">
        {/* File input for uploading an image */}
        <input
          type="file"
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

        {/* Example image selection */}
        <input
          type="button"
          id="exampleInput"
          onClick={handleImageUpload}
          className="hidden"
        />
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
      {/* Dropdown menu for selecting the target language */}
      <div>
        <DropDownMenu onLangChange={setTargetLang} />
      </div>
    </div>
  );
};

export default ImageUpload;
