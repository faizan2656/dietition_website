import sys
import os

# Root directory ko Python path mein add karna:
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
