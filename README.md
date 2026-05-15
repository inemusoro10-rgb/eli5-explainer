# ELI5 Code Explainer

Paste any code snippet and get a plain-English explanation tailored to your level.

Built this because I kept struggling to explain code to beginners at my Teen Coding Club — 
so I made a tool that does it automatically at whatever level you need.

## What it does

- Paste any code (Python, JavaScript, C++, anything)
- Pick your audience — 5-year-old, teenager, CS student, or senior dev
- Get a line-by-line breakdown, a real-world analogy, and what would break if you changed it

## Tech stack

- Python + Flask (backend API)
- Claude API with custom prompt engineering (AI explanations)
- SQLite (stores explanation history)
- Vanilla JS + HTML/CSS (frontend)

## Run it locally

```bash
git clone https://github.com/inemusoro10-rgb/eli5-explainer.git
cd eli5-explainer
pip install flask anthropic
export ANTHROPIC_API_KEY=your_key_here
python app.py
```

Open http://localhost:5000
