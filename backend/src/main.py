import uvicorn

if __name__ == "__main__":
    # uvicorn server run at port 8000 with auto-reload enabled
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
