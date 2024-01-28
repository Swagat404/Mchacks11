import React, { useState } from 'react';

const Shoes = () => {
  const [imageIndex, setImageIndex] = useState(0);
  const images = [/* Add your shoes images here */];

  const handlePrevClick = () => {
    setImageIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  const handleNextClick = () => {
    setImageIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  return (
    <div className="image-toggle-box shoes">
      <button className="left" onClick={handlePrevClick}>&lt;</button>
      <img src={images[imageIndex]} alt="Shoes" />
      <button className="right" onClick={handleNextClick}>&gt;</button>

    </div>
  );
};

export default Shoes;
