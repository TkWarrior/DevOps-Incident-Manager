import asyncio
from backend.db import engine, Base
from backend.models import Incident

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init())
