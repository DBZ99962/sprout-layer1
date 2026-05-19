# Sprout Layer 1 + Layer 2 - Setup Guide

## Prerequisites
- Python 3.10+
- Node.js 18+
- Docker Desktop (for Postgres)
- Git

## Step 1 - Clone the repository

```bash
git clone https://github.com/DBZ99962/sprout-layer1.git
cd sprout-layer1
```

## Step 2 - Start the database

```bash
docker compose up db -d
docker compose ps
```

## Step 3 - Set up and run the API

```bash
cd apps/api
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and set your values. Then:

```bash
alembic upgrade head
uvicorn main:app --reload
```

API runs at: http://127.0.0.1:8000
Docs at: http://127.0.0.1:8000/docs

## Step 4 - Run the Web UI

Open a new terminal:

```bash
cd apps/web
npm install
npm run dev
```

Web UI runs at: http://localhost:5173

## Step 5 - Run the Automation agent

Open a new terminal:

```bash
cd apps/automation
npm install
npx playwright install
```

For a managed run:

```bash
set API_URL=http://127.0.0.1:8000
set USER_ID=your_user_id
set JOB_ID=your_job_id
set TARGET_URL=https://boards.greenhouse.io/company/jobs/123
npm run run:managed
```

## Startup order every time
1. Start Docker Desktop
2. Run: docker compose up db -d
3. Start API: uvicorn main:app --reload
4. Start Web: npm run dev
5. Run automation when needed

## Supported portals
- Greenhouse (boards.greenhouse.io)
- Lever (jobs.lever.co)
- Generic company forms (assisted fill)
- LinkedIn, Naukri (manual only)

## LLM providers
Set LLM_PROVIDER in .env:
- stub (default, no API key needed)
- openai (requires OPENAI_API_KEY)
- anthropic (requires ANTHROPIC_API_KEY)

## Repository
https://github.com/DBZ99962/sprout-layer1
