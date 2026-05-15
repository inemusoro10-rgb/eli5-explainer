# levels and how to talk to each one
# took me a while to get these prompts right lol
LEVELS = {
    "5yo":     "a curious 5-year-old. No technical words, use a fun analogy like toys or food.",
    "teen":    "a teenager who plays video games but hasn't coded before. Keep it casual and relatable.",
    "student": "a first-year CS student who knows variables and basic Python but not much else.",
    "dev":     "an experienced developer. Skip the basics, be direct and precise.",
}

def build_prompt(code, level):
    audience = LEVELS.get(level, LEVELS["student"])

    prompt = (
        f"You are a coding tutor explaining code to {audience}\n\n"
        "Reply ONLY with a JSON object, no extra text or markdown. Structure:\n"
        "{\n"
        '  "summary": "one sentence overview of what the code does",\n'
        '  "breakdown": [\n'
        '    {"line": "code snippet", "explanation": "what it does in plain english"}\n'
        '  ],\n'
        '  "analogy": "a short real-world comparison that makes it click",\n'
        '  "what_breaks": "one thing that would break it and why"\n'
        "}\n\n"
        f"Code:\n{code}"
    )

    return prompt