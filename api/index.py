from flask import Flask
from flask_cors import CORS
import os
import sys

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the main application
from main_supabase import app

# Enable CORS for all routes
CORS(app, origins="*")

# This is the entry point for Vercel
def handler(request):
    return app(request.environ, lambda status, headers: None)

