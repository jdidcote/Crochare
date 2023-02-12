import { Button, Checkbox, Label, TextInput } from "flowbite-react";

interface LoginHelpProps {
  text: string;
  link: string;
}

const LoginHelpLink = (props: LoginHelpProps) => {
  return (
    <a href={props.link} className="text-purple-700">
      {props.text}
    </a>
  );
};

const SignUpText: React.FC = () => {
  const signUpLink = (): JSX.Element => {
    return <LoginHelpLink text="Sign up" link=""></LoginHelpLink>;
  };
  return (
    <div className="text-sm flex pt-4">
      <p>New to crochare? {signUpLink()}</p>
    </div>
  );
};

const ForgotCredentials: React.FC = () => {
  const userNameLink = (): JSX.Element => (
    <LoginHelpLink text="username" link=""></LoginHelpLink>
  );
  const passwordLink = (): JSX.Element => (
    <LoginHelpLink text="password" link=""></LoginHelpLink>
  );

  return (
    <div className="text-sm">
      <p>
        Forgot your {userNameLink()} or {passwordLink()}?
      </p>
    </div>
  );
};

const LoginPage: React.FC = () => {
  return (
    <form className="flex flex-col gap-4 pt-12 w-1/2 mx-auto min-w-fit max-w-md">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email1" value="Your email" />
        </div>
        <TextInput
          id="email1"
          type="email"
          placeholder="name@flowbite.com"
          required={true}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password1" value="Your password" />
        </div>
        <TextInput id="password1" type="password" required={true} />
      </div>
      <ForgotCredentials></ForgotCredentials>
      <div className="flex mx-auto w-32 justify-center">
        <Button
          type="submit"
          gradientDuoTone="purpleToBlue"
          outline={true}
          className="w-full"
        >
          Log In
        </Button>
      </div>
      <div className="flex justify-between">
        <SignUpText></SignUpText>
      </div>
    </form>
  );
};

export default LoginPage;
