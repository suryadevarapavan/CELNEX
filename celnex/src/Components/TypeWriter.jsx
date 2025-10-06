import React, { useState, useEffect } from 'react';
import "./Tp.css";

const TypeWriter = ({
  text = '',
  delay = 100,
  noise = true,
  noiseChars = 'adbcdefghijklmnopqrstuvwxyz',
  className = '',
  style = {},
}) => {
  const [displayedText, setDisplayedText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    let timeout;

    const type = () => {
      if (currentIndex < text.length) {
        if (noise) {
          const randomChar = noiseChars.charAt(
            Math.floor(Math.random() * noiseChars.length)
          );

          // Temporarily show noise character
          setDisplayedText((prev) => prev + randomChar);

          timeout = setTimeout(() => {
            // Replace noise with correct character
            setDisplayedText((prev) =>
              prev.slice(0, -1) + text.charAt(currentIndex)
            );
            setCurrentIndex((prev) => prev + 1);
          }, delay / 2);
        } else {
          setDisplayedText((prev) => prev + text.charAt(currentIndex));
          setCurrentIndex((prev) => prev + 1);
        }
      }
    };

    timeout = setTimeout(type, delay);

    return () => clearTimeout(timeout); // Cleanup
  }, [currentIndex, text, delay, noise, noiseChars]);

  return (
    <span className={className} style={style}>
      {displayedText}
    </span>
  );
};

export default TypeWriter;
