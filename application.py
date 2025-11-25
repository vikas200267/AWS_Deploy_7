from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()

@app.get("/")
def hello():
    return JSONResponse({"message": "Hello from AWS Elastic Beanstalk + FastAPI!"})

# expose FastAPI app as WSGI app
application = WSGIMiddleware(app)
