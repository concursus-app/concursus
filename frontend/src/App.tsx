import React from 'react';
import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [time, setTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      console.log(data);
      setTime(data.time);
    });
  }, []);

  return (
    <div style={{height: "100vh", width: "100%", alignItems: "center", textAlign: "center", display: "flex", justifyContent: "center"}}>
      <p>The time is {time}</p>
      <button onClick={() => {
        fetch('/time').then(res => res.json()).then(data => {
          console.log(data);
          setTime(data.time);
        })
      }}>Refresh</button>
    </div>
  );
}

export default App;
