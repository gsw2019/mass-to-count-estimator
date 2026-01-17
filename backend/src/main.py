import uvicorn

if __name__ == "__main__":
    # entry point = app.api:app
    # uvicorn server run at 0.0.0.0:8080
    uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)
