from enum import Enum


class Region(str, Enum):
    US = "US"
    UK = "UK"


class SkillLevels(str, Enum):
    beginner = "Beginner"
    easy = "Easy"
    intermediate = "Intermediate"
    experienced = "Experienced"
