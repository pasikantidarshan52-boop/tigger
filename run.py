"""Start Tigger:  python run.py   (then open http://localhost:8000)"""
import os
from app.main import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, threaded=True)
