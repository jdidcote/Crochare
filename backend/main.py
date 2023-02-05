import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from models.models import Region, SkillLevels

app = FastAPI(title="Crochare")

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/regions/")
def get_regions():
    return {"regions": [region.value for region in Region]}


@app.get("/skill-level/")
def get_skill_levels():
    return {"levels": [skill.value for skill in SkillLevels]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
