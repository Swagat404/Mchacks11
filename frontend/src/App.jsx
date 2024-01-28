import React, { useState } from 'react';
import './style.css';
import BottomWear from './BottomWear';
import UpperWear from './UpperWear';
import Shoes from './Shoes';
import Accessories from './Accessories';

const App = () => {
  const [promptText, setPromptText] = useState('');

  return (
    <div className="app-container">
      <div className="toggle-boxes">
        <BottomWear />
        <UpperWear />
        <Shoes />
        <Accessories />
      </div>
      <div className="text-bar">
        <input
          type="text"
          placeholder="Enter your prompt"
          value={promptText}
          onChange={(e) => setPromptText(e.target.value)}
        />
      </div>
    </div>
  );
};

export default App;
