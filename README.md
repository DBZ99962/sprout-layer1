# sprout-layer1
Sprout-like AI job application assistant - Layer 1: Profile ingestion, job analysis, fit scoring, guided Q&amp;A, document generation. Layer 2: Browser automation with Playwright, Greenhouse/Lever adapters, review queue and audit logging.

## How to Run

> Full setup details are in [SETUP.md](./SETUP.md)

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker Desktop (for Postgres)
- Git

### 1. Clone the repo
```bash
git clone https://github.com/DBZ99962/sprout-layer1.git
cd sprout-layer1
```

### 2. Start the database
```bash
docker compose up db -d
```

### 3. Run the API
```bash
cd apps/api
pip install -r requirements.txt
copy .env.example .env   # then edit .env with your values
alembic upgrade head
uvicorn main:app --reload
```
API: http://127.0.0.1:8000 | Docs: http://127.0.0.1:8000/docs

### 4. Run the Web UI
```bash
cd apps/web
npm install
npm run dev
```
Web UI: http://localhost:5173

### 5. Run the Automation agent
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

### Startup order (every time)
1. Start Docker Desktop
2. `docker compose up db -d`
3. `uvicorn main:app --reload` (in `apps/api`)
4. `npm run dev` (in `apps/web`)
5. Run automation when needed
