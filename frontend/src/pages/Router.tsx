import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./landing";
import Browse from "./browse";
import LoginPage from "./login";
import Create from "./patterns/create-patterns";
import Register from "./register";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />}></Route>
        <Route path="/browse" element={<Browse />}></Route>
        <Route path="/create" element={<Create />}></Route>
        <Route path="/login" element={<LoginPage />}></Route>
        <Route path="/register" element={<Register />}></Route>
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
