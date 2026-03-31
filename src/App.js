import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./components/LoginPage";
import Register from "./components/Register";
import Assistant from "./components/Assistant";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/assistant" element={<Assistant />} />
      </Routes>
    </Router>
  );
}

export default App;
