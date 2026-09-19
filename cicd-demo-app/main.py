from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Just Checking......")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deployed Successful</title>
    </head>
    <body>
        <h1>🚀 CI/CD  Application</h1>
        <p>Python FastAPI Application</p>
        <p>Application Status: Running on Render</p>
        <p>Deployed using GitHub Actions</p>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "healthy"}
