import subprocess
import sys
from pathlib import Path

def update_dependencies():
    project_root = Path(__file__).parent.parent
    requirements_file = project_root / "requirements.txt"
    
    try:
        # Run uv pip install
        subprocess.run(
            ["uv", "pip", "install", "-r", str(requirements_file)],
            check=True,
            capture_output=True,
            text=True
        )
        print("✅ Dependencies updated successfully")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error updating dependencies: {e.stderr}")
        return 1

if __name__ == "__main__":
    sys.exit(update_dependencies())
