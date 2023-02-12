import { Button, Checkbox, Label, TextInput } from "flowbite-react";
import React, { useState } from "react";
import { FormEncType } from "react-router-dom";

const Register: React.FC = () => {
  const [email, setEmail] = useState<string>("");
  const [username, setUsername] = useState<string>("");
  const [password1, setPassword1] = useState<string>("");
  const [password2, setPassword2] = useState<string>("");

  // TODO: add endpoints to check email/username do not already exist
  // TODO: Use red/green helper text to signify available/taken
  const validateEmail = (email: string) => {};
  const validateUsername = (username: string) => {};

  const isMatchingPasswords = (
    password1: string,
    password2: string
  ): boolean => {
    return password1 === password2;
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  };

  return (
    <form
      className="flex flex-col gap-4 pt-12 w-1/2 mx-auto min-w-fit max-w-md"
      onSubmit={handleSubmit}
    >
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email1" value="Your email" />
        </div>
        <TextInput
          id="email1"
          type="email"
          placeholder="example@domain.com"
          required={true}
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          helperText={
            <React.Fragment>
              Your email address is <strong>private</strong>.
            </React.Fragment>
          }
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="username" value="Username" />
        </div>
        <TextInput
          id="username"
          placeholder="username"
          required={true}
          addon="@"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          helperText={
            <React.Fragment>
              Your username is <strong>public</strong>.
            </React.Fragment>
          }
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password1" value="Your password" />
        </div>
        <TextInput
          id="password1"
          type="password"
          required={true}
          value={password1}
          onChange={(e) => setPassword1(e.target.value)}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password2" value="Repeat password" />
        </div>
        <TextInput
          id="password2"
          type="password"
          required={true}
          value={password2}
          onChange={(e) => setPassword2(e.target.value)}
          color={
            !isMatchingPasswords(password1, password2) && password2.length > 0
              ? "failure"
              : ""
          }
          helperText={
            !isMatchingPasswords(password1, password2) && (
              <React.Fragment>Password do not match!</React.Fragment>
            )
          }
        />
      </div>

      <div className="flex mx-auto w-32 justify-center">
        <Button
          type="submit"
          gradientDuoTone="purpleToBlue"
          outline={true}
          className="w-full"
        >
          Sign up
        </Button>
      </div>
    </form>
  );
};

export default Register;
