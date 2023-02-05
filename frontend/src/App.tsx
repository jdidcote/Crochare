import { useState } from "react";
import Navbar from "./components/CreatePattern/Navbar.js";
import CreatePattern from "./pages/patterns/create-patterns/index.jsx";

function App() {
  return (
    <div className="App">
      <Navbar></Navbar>
      <CreatePattern></CreatePattern>
    </div>
  );
}

export default App;
