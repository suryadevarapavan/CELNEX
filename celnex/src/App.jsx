import React from 'react';
import TypeWriter from './Components/TypeWriter';
import './App.css'; 

function App() {
  return (
    <div className="app-container">
      <TypeWriter
        text="WELCOME TO CELNEX"
        delay={100}
        noise={true}
        className="typewriter"
      />
    </div>
  );
}

export default App;
