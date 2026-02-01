from fastapi import FastAPI

app = FastAPI(
    title="Decision Systems Lab",
    description="Infrastructure-layer decision interface",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "layer": "api",
        "decision_ready": False
    }
