# Simple FastAPI on Vercel

A minimal FastAPI application ready for deployment on Vercel.

## Getting Started

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the development server:**
   ```bash
   uvicorn api.index:app --reload
   ```

The API will be available at `http://localhost:8000`

### API Endpoints

- **`GET /`** - Welcome message
- **`GET /api/hello?name=YourName`** - Personalized greeting
- **`GET /api/items/{item_id}`** - Get item by ID
- **`POST /api/items`** - Create a new item (query params: `item_name`, `item_description`)

### Deployment to Vercel

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

The `vercel.json` configuration file handles routing all requests to your FastAPI app.

## Project Structure

```
simple-api/
├── api/
│   └── index.py       # FastAPI application
├── requirements.txt   # Python dependencies
├── vercel.json        # Vercel deployment config
└── .gitignore        # Git ignore rules
```
