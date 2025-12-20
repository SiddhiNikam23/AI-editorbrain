from fastapi import FastAPI , UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from llm.planner import generate_edit_plan
from pydantic import BaseModel
from services.video_executor import trim_video


app = FastAPI(title="AI editor brain")
#backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromtRequest(BaseModel):
    prompt: str


@app.post("/plan")
def create_plan(req: PromtRequest):
    plan = generate_edit_plan(req.prompt)
    return plan

@app.get("/")
def health_check():
    return {"status": "BACKEND RUNNING SUCCESFULLLY"}




# 🔴 THIS ENDPOINT MUST EXIST
@app.post("/execute")
async def execute_video(file: UploadFile = File(...)):
    input_path = f"temp_{file.filename}"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = trim_video(input_path, duration=30)

    return {
        "message": "Video processed successfully",
        "output_video": output_path
    }