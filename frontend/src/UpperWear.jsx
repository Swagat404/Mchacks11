import React, { useState } from 'react';

const UpperWear = () => {
  const [imageIndex, setImageIndex] = useState(0);
  const images = [/* Add your upperwear images here */];

  const handlePrevClick = () => {
    setImageIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  const handleNextClick = () => {
    setImageIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  return (
    <div className="image-toggle-box upperwear">
      <button className="left" onClick={handlePrevClick}>&lt;</button>
      <img src={images[imageIndex]} alt="Upper Wear" />
      <button className="right" onClick={handleNextClick}>&gt;</button>
    </div>
  );
};

export default UpperWear;
