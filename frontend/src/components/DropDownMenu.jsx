import React, { useState, useEffect } from "react";

const languages = [
  { code: "DE", name: "Deutsch", flag: "🇩🇪" },
  { code: "FR", name: "Français", flag: "🇫🇷" },
  { code: "ES", name: "Español", flag: "🇪🇸" },
];

const DropDownMenu = ({ onLangChange }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedLang, setSelectedFile] = useState(languages[0]);

  const handleSelect = (lang) => {
    setSelectedFile(lang);
    onLangChange(lang.code);
    setIsOpen(false);
  };

  return (
    <div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="inline-flex justify-center items-center w-48 px-4 py-2 bg-white text-sm font-medium text-gray-700 rounded-md shadow-md hover:bg-gray-50"
      >
        <span className="mr-2">{selectedLang.flag}</span>
        {selectedLang.name}
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-10">
          <div className="py-1">
            {languages.map((lang) => (
              <button
                key={lang.code}
                onClick={() => handleSelect(lang)}
                className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >
                <span className="mr-2">{lang.flag}</span>
                {lang.name}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default DropDownMenu;
