import { useState } from "react";
import Nav from "./components/Nav.js";
import CreatePattern from "./pages/patterns/create-patterns/index.jsx";
import Router from "./pages/Router.js";

function App() {
  return (
    <div className="max-w-full w-sm md:px-36">
      <Nav></Nav>
      <Router />
    </div>
  );
}

export default App;
