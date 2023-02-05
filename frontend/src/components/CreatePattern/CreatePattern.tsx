import { Heading } from "@chakra-ui/react";
import React from "react";
import CreatePatternForm from "./CreatePatternForm";

export default function CreatePattern() {
  return (
    <div>
      <Heading>Create new pattern</Heading>
      <CreatePatternForm></CreatePatternForm>
    </div>
  );
}
