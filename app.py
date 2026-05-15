from flask import Flask, request, jsonify, render_template
from anthropic import Anthropic
from prompt_builder import build_prompt
import sqlite3
import json

app = Flask(__name__)
client = Anthropic()

# db setup - just storing history so we can look back at explanations
def get_db():
    conn = sqlite3.connect("history.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS explanations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            level TEXT,
            result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.commit()
    db.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    code = data.get("code", "").strip()
    level = data.get("level", "student")

    if not code:
        return jsonify({"error": "no code provided"}), 400

    prompt = build_prompt(code, level)

    # call claude
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text

    # sometimes the model wraps in markdown even when told not to, strip it
    clean = raw.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1]
    if clean.endswith("```"):
        clean = clean.rsplit("```", 1)[0]
    clean = clean.strip()

    result = json.loads(clean)

    # save to db
    db = get_db()
    db.execute(
        "INSERT INTO explanations (code, level, result) VALUES (?, ?, ?)",
        (code, level, json.dumps(result))
    )
    db.commit()
    db.close()

    return jsonify(result)

# bonus endpoint - see past explanations
@app.route("/history")
def history():
    db = get_db()
    rows = db.execute(
        "SELECT * FROM explanations ORDER BY created_at DESC LIMIT 10"
    ).fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)