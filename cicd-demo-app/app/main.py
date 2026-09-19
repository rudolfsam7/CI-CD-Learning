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
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f4f4f4;
            }

            .container {
                background: white;
                width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }

            h1 {
                color: #333;
            }

            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 CI/CD Demo Application</h1>

            <p>Python FastAPI Application</p>

            <p class="status">
                Application Status: Running
            </p>

            <p>
                Deployed using GitHub Actions
            </p>
        </div>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
