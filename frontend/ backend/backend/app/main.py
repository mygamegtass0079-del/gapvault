    from fastapi import APIRouter, Depends
    from .database import get_db

    router = APIRouter(prefix="/api")

    @router.get("/items")
    def list_items(db=Depends(get_db)):
        return db.query(...).all()
