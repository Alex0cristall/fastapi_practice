from db.database import sync_engine, Base



def init_models():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
