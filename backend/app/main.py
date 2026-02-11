from fastapi import FastAPI
from sqlalchemy import text
from backend.app.db.session import SessionLocal

app = FastAPI(title="PermitPulse API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    db = SessionLocal()
    try:
        result = db.execute(text("select now()")).scalar()
        return {"db_time": str(result)}
    finally:
        db.close()
