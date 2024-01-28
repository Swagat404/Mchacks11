import React, { useState } from 'react';

const BottomWear = () => {
  const [imageIndex, setImageIndex] = useState(0);
  const images = [/* Add your bottomwear images here */];

  const handlePrevClick = () => {
    setImageIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  const handleNextClick = () => {
    setImageIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  return (
    <div className="image-toggle-box bottomwear">
      <button className="left" onClick={handlePrevClick}>&lt;</button>
      <img src={images[imageIndex]} alt="Bottom Wear" />
      <button className="right" onClick={handleNextClick}>&gt;</button>
    </div>
  );
};

export default BottomWear;
