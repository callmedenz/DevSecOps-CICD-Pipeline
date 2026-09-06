from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="DevSecOps Deployment API")


class DeployRequest(BaseModel):
    repo_url: HttpUrl
    port: int


deployment_status = {
    "status": "idle",
    "repo_url": None,
    "port": None,
}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/deploy")
def deploy(request: DeployRequest):
    deployment_status["status"] = "accepted"
    deployment_status["repo_url"] = str(request.repo_url)
    deployment_status["port"] = request.port

    return deployment_status


@app.get("/status")
def status():
    return deployment_status