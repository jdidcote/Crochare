import React, { useEffect, useState } from "react";
import { getApiPath } from "../../utils";

interface NewPatternForm {
  patternName: string;
  skillLevel: string;
  region: string;
  materials: string;
  details: string;
}

const CreatePatternForm: React.FC = () => {
  const [regions, setRegions] = useState<string[]>([]);
  const [skillLevels, setSkillLevels] = useState<string[]>([]);

  const [formData, setFormData] = useState<NewPatternForm>({
    patternName: "",
    skillLevel: "",
    region: "",
    materials: "",
    details: "",
  });

  const updateFormData = (update: Object): void => {
    const newFormData: NewPatternForm = { ...formData, ...update };
    setFormData(newFormData);
  };

  useEffect(() => {
    fetch(getApiPath("/regions/"))
      .then((res) => res.json())
      .then((data) => setRegions(data.regions));
  }, []);

  useEffect(() => {
    fetch(getApiPath("/skill-level/"))
      .then((res) => res.json())
      .then((data) => setSkillLevels(data.levels));
  }, []);

  return (
    <div>
      {/* <Text>Pattern Name</Text>
      <Input></Input>
      <Text>Skill Level</Text>
      <Select>
        {skillLevels.map((skillLevel: string) => {
          return (
            <option value={skillLevel} key={skillLevel}>
              {skillLevel}
            </option>
          );
        })}
      </Select>
      <Text>Pattern Region</Text>
      <Select>
        {regions.map((region: string) => {
          return (
            <option value={region} key={region}>
              {region}
            </option>
          );
        })}
      </Select>
      <Text>Materials</Text>
      <Textarea placeholder="The equipment needed for the pattern"></Textarea>
      <Text>Details</Text>
      <Textarea placeholder="Guage, finish, size etc."></Textarea>
      <Button colorScheme="teal">Save</Button> */}
    </div>
  );
};

export default CreatePatternForm;
