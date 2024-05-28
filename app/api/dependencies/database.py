from db.database import async_session_fabric



async def get_session():
    async with async_session_fabric() as session:
        yield session
