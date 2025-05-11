import React, { useState, useRef, useEffect } from "react";
import { FaFileUpload, FaTrashAlt } from "react-icons/fa";
import { fabric } from "fabric";

const Editor = ({ imageUrl, onImageDelete }) => {
  const canvasRef = useRef(null);
  const fabricCanvasRef = useRef(null);

  useEffect(() => {
    if (fabricCanvasRef.current) {
      fabricCanvasRef.current.dispose();
    }

    if (canvasRef.current) {
      fabricCanvasRef.current = new fabric.Canvas(canvasRef.current);
      fabric.Image.fromURL(imageUrl, (img) => {
        fabricCanvasRef.current.setBackgroundImage(img, () => {
          fabricCanvasRef.current.setWidth(img.width);
          fabricCanvasRef.current.setHeight(img.height);

          fabricCanvasRef.current.renderAll();
        });
      });
    }

    return () => {
      if (fabricCanvasRef.current && canvasRef.current) {
        fabricCanvasRef.current.dispose();
      }
    };
  }, [imageUrl]);

  return (
    <div className="flex flex-col items-center">
      <canvas ref={canvasRef} />
      <button onClick={onImageDelete}>
        <FaTrashAlt />
      </button>
    </div>
  );
};

export default Editor;
