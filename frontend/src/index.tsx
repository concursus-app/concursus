import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';

import Root from "./root"
import Login from "./pages/login"
import Register from "./pages/register"

import Navbar from "./components/navbar"
import Background from "./components/background"

import {
  Routes,
  Route,
  BrowserRouter
} from "react-router-dom";

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
  <Background/>
  <Navbar/>
  <div style={{width: "80%", marginLeft: "auto", marginRight: "auto"}}>
  <BrowserRouter>
    <Routes>
      <Route path="" element={<Root/>}/>
      <Route path="login" element={<Login/>}/>
      <Route path="register" element={<Register/>}/>
    </Routes>
  </BrowserRouter>
  </div>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
