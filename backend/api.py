from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_db
from backend.models import Incident
from main import run_agent
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder

app = FastAPI()
# history = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run")
async def run(db: AsyncSession = Depends(get_db)):
    result = run_agent()
    # history.append(result)
    incident = Incident(
        error=result["error"],
        root_cause=result["root_cause"],
        patch=result["patch"],
        pr=result["pr"]
    )

    db.add(incident)
    await db.commit()
    return result

@app.get("/incidents")
async def incidents(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Incident).order_by(Incident.created_at.desc()))
    incidents = result.scalars().all()
    return incidents

    # print("Fetched incidents from DB:", incidents)
    # return incidents
    # print("Fetching incident history..."+history)
    # return history
