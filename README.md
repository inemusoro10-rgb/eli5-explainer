# ELI5 Code Explainer

Paste any code snippet and get a plain-English explanation tailored to your level.

A lot of the high school students I tutor want to get into tech but don't know where to start. With AI tools everywhere, most of them just copy-paste generated code without actually understanding what it does. I built this so they could get a simple, human breakdown of any code block, just paste and go.

## What it does

- Paste any code (Python, JavaScript, C++, anything)
- Pick your audience from a 5-year-old, teenager, CS student, or senior dev
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
