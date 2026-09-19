from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="CI/CD Demo Application")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Demo</title>
    </head>
    <body>
        <h1>🚀 CI/CD Demo Application</h1>
        <p>Python FastAPI Application</p>
        <p>Application Status: Running</p>
        <p>Deployed using GitHub Actions</p>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "healthy"}
