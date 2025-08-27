from fastapi import FastAPI
app = FastAPI(title="RRF Dashboard")

@app.get("/status")
def status():
    return {"status": "RRF ready"}
