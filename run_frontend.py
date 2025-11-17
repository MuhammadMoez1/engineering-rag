"""Run Streamlit frontend."""

import os
import subprocess
from app.core.config import settings

if __name__ == "__main__":
    os.system(f"streamlit run ui/app.py --server.port {settings.STREAMLIT_PORT}")

