from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/health')
@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'KDP Advertising Tool API',
        'version': '2.0.0',
        'message': 'Minimal test deployment'
    })

@app.route('/')
def index():
    return jsonify({
        'service': 'KDP Advertising Tool API',
        'status': 'running',
        'endpoints': {
            'health': '/api/health'
        }
    })

# Vercel entry point
def handler(request, context):
    return app

