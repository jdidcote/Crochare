import { Button, Checkbox, Label, TextInput } from "flowbite-react";

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
      <div className="flex items-center gap-2">
        <Checkbox id="remember" />
        <Label htmlFor="remember">Remember me</Label>
      </div>
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
    </form>
  );
};

export default LoginPage;
