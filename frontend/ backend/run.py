    from fastapi import FastAPI
    import uvicorn

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "GapVault Backend is up and running"}

    if __name__ == "__main__":
        uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True)
