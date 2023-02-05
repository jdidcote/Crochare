import { useState } from "react";
import Nav from "./components/Nav.js";
import CreatePattern from "./pages/patterns/create-patterns/index.jsx";

function App() {
  return (
    <div className="px-32">
      <Nav></Nav>
      <CreatePattern></CreatePattern>
    </div>
  );
}

export default App;
