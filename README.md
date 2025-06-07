# KDP Advertising Tool - Minimal Test Deployment

This is a minimal test deployment to verify Vercel works with the cleaned requirements.

## Files:
- `requirements.txt` - Only 7 essential dependencies
- `vercel.json` - Simplified configuration
- `api/index.py` - Minimal Flask app for testing

## Test Endpoints:
- `/` - Root endpoint
- `/api/health` - Health check

## Environment Variables:
```
FLASK_ENV=production
```

Once this minimal version works, we can add back the full functionality.

