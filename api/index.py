from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint"""
    return JSONResponse({
        "message": "Welcome to the Simple API",
        "status": "running"
    })


@app.get("/api/hello")
async def hello(name: str = "World"):
    """Simple hello endpoint"""
    return JSONResponse({
        "message": f"Hello, {name}!",
        "timestamp": __import__("datetime").datetime.utcnow().isoformat()
    })


@app.get("/api/items/{item_id}")
async def get_item(item_id: int):
    """Get item by ID"""
    return JSONResponse({
        "item_id": item_id,
        "name": f"Item {item_id}",
        "description": f"This is item number {item_id}"
    })


@app.post("/api/items")
async def create_item(item_name: str, item_description: str = ""):
    """Create a new item"""
    return JSONResponse({
        "success": True,
        "item": {
            "name": item_name,
            "description": item_description
        }
    })


@app.get("/api/date")
async def get_current_date():
    """Get current date and time"""
    from datetime import datetime
    now = datetime.utcnow()
    return JSONResponse({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "datetime": now.isoformat(),
        "timestamp": now.timestamp()
    })
