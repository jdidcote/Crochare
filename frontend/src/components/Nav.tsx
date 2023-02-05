import { Button, Navbar } from "flowbite-react";
import React from "react";

const Nav: React.FC = () => {
  return (
    <Navbar fluid={true} rounded={true}>
      <Navbar.Brand to="/navbars">
        <a
          href="#"
          className="self-center whitespace-nowrap text-2xl font-semibold dark:text-white"
        >
          Crochare
        </a>
      </Navbar.Brand>
      <Navbar.Toggle />
      <Navbar.Collapse>
        <div className="flex items-center">
          <Navbar.Link href="/navbars" active={true}>
            Home
          </Navbar.Link>
        </div>
        <div className="flex items-center">
          <Navbar.Link href="/navbars">Browse</Navbar.Link>
        </div>
        <div className="flex items-center">
          <Navbar.Link href="/navbars">Create</Navbar.Link>
        </div>
        <div className="flex md:order-2">
          <Button size="sm" gradientDuoTone="purpleToBlue" outline={true}>
            Log in
          </Button>
        </div>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Nav;
