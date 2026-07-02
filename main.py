from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

from model import optimize_hvac

app = FastAPI(title="Gym HVAC Optimizer")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class OptimizationRequest(BaseModel):
    occupancy: int = 0
    outdoor_temp: float = 22.0
    outdoor_humidity: float = 50.0

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/optimize")
async def optimize(req: OptimizationRequest):
    try:
        result = await optimize_hvac(req.occupancy, req.outdoor_temp, req.outdoor_humidity)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
