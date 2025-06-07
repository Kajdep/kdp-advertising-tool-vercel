# KDP Advertising Tool - Vercel Backend

This is the backend API for the KDP Advertising Tool, configured for deployment on Vercel.

## Environment Variables Required

Set these in your Vercel project settings:

```


## Deployment Instructions

1. Upload this entire directory to your GitHub repository
2. Connect the repository to your Vercel project
3. Set the environment variables in Vercel dashboard
4. Deploy

## API Endpoints

- `/api/auth/register` - User registration
- `/api/auth/login` - User login
- `/api/reports/upload` - Upload advertising reports
- `/api/analysis/analyze` - Analyze campaign performance
- `/api/optimization/optimize` - Get optimization recommendations
- `/api/export/csv` - Export data as CSV
- `/api/export/pdf` - Export data as PDF

## Features

- Supabase authentication and database
- OpenRouter AI integration for optimization
- CSV/Excel report processing
- Campaign analysis and optimization
- Export capabilities
- CORS enabled for frontend integration

