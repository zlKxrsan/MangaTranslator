import React, { useState, useRef, useEffect } from "react";
import { FaTrashAlt, FaCheck } from "react-icons/fa";

const Toolbar = () => {
  return (
    <div className="fixed top-0 right-0 h-full w-64 bg-white shadow-lg">
      <div className="flex flex-col items-center">
        <h2 className="text-xl font-bold">Toolbar</h2>
        <canvas ref={canvasRef} />
        <button onClick={onImageDelete}>
          <FaTrashAlt />
        </button>
        <button onClick={downloadCanvas}>
          <FaCheck />
        </button>
      </div>
    </div>
  );
};

export default Toolbar;
