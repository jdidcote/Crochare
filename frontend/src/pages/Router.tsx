import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./landing";
import Browse from "./browse";
import CreatePattern from "./patterns/create-patterns";
import Create from "./patterns/create-patterns";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />}></Route>
        <Route path="/browse" element={<Browse />}></Route>
        <Route path="/create" element={<Create />}></Route>
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
