import React, { useState } from "react";

// List of available languages with their codes, names, and flags
const languages = [
  { code: "DE", name: "German", flag: "🇩🇪" },
  { code: "FR", name: "French", flag: "🇫🇷" },
  { code: "ES", name: "Spanish", flag: "🇪🇸" },
  { code: "PT-BR", name: "Portuguese (Brazil)", flag: "🇧🇷" },
  { code: "PL", name: "Polish", flag: "🇵🇱" },
  { code: "TR", name: "Turkish", flag: "🇹🇷" },
];

/**
 * Dropdown menu for selecting a target language.
 * Calls onLangChange with the selected language code.
 *
 * Props:
 * - onLangChange: function to call when the language changes
 */
const DropDownMenu = ({ onLangChange }) => {
  // State for dropdown open/close and selected language
  const [isOpen, setIsOpen] = useState(false);
  const [selectedLang, setSelectedLang] = useState(languages[0]);

  /**
   * Handles selection of a language.
   * Updates the selected language, notifies parent, and closes the dropdown.
   */
  const handleSelect = (lang) => {
    setSelectedLang(lang);
    onLangChange(lang.code);
    setIsOpen(false);
  };

  return (
    <div className="relative inline-block text-left">
      {/* Dropdown button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="inline-flex justify-center items-center w-48 px-4 py-2 bg-white text-sm font-medium text-white rounded-md shadow-md hover:bg-gray-50"
      >
        <span className="mr-2">{selectedLang.flag}</span>
        {selectedLang.name}
      </button>

      {/* Dropdown menu */}
      {isOpen && (
        <div className="absolute left-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-10">
          <div className="py-1">
            {languages.map((lang) => (
              <button
                key={lang.code}
                onClick={() => handleSelect(lang)}
                className="flex items-center w-full px-4 py-2 text-sm text-white hover:bg-gray-100"
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
