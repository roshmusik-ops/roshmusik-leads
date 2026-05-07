"""Generate personalized email pitches for leads using Gemini.

Usage:
    python pitcher.py                    # pitch all leads missing a pitch
    python pitcher.py --limit 10         # pitch only 10
    python pitcher.py --regenerate       # regenerate pitches for all
"""
from __future__ import annotations

import argparse
import csv
import os
import time
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

from config import BRAND

load_dotenv()
DATA_DIR = Path(__file__).parent / "data"
LEADS_CSV = DATA_DIR / "leads.csv"
PITCHES_CSV = DATA_DIR / "pitches.csv"

PITCH_FIELDS = ["name", "city", "category", "email_subject", "email_body", "generated_at"]

SYSTEM_PROMPT = f"""You are {BRAND['founder']} — an indie singer, songwriter and composer
behind {BRAND['company']} ({BRAND['website']}). You write & sing original songs in
Malayalam, Tamil and English. {BRAND['artist_bio']}

You are reaching out to a music-industry contact (film production house, recording studio,
ad agency, event company, music label, etc.) to introduce yourself and explore a possible
collaboration — singing, composing, producing, jingles, background score, or playback work.

TASK: Write a SHORT cold email (90-130 words). It must read like a real artist wrote it
in 2 minutes, not like AI marketing copy. Tone: warm, grounded, slightly poetic where it
fits, but never flowery. Confidence without bragging.

REQUIREMENTS:
- Subject line: 5-9 words. Specific. Examples: "Original songs for your next film", "Singer-composer for your ad project", "Malayalam-Tamil-English voice for your studio".
- First line: a genuine note about THEIR work, location or category (NOT "I came across your business" / "I hope this finds you well"). If you don't know specifics, reference the kind of work they do.
- Middle: introduce yourself in 2-3 short lines as an indie artist. Mention 1-2 specific releases by name (pick from: 'Neermathalam Kozhinja Sandhya' Malayalam, 'Neeyen Sakhi' Malayalam, 'En Swaasame' Tamil, 'Oru Kaadhal Kadhai' Tamil, 'Déjà Vu' English). Mention you're available for film, ad, album, or playback work.
- Include this Linktree link naturally (it lists Spotify, YouTube, Bandcamp etc. in one place): {BRAND['links']['linktree']}
- Close: low-pressure CTA. Examples: "Worth a quick listen and a 10-min chat?" or "If you have an upcoming project that could use an original song or voice, I'd love to hear about it."
- Forbidden phrases: revolutionary, leverage, best-in-class, synergy, unlock, in today's world, elevate, unleash, "I hope this email finds you well", "My name is".
- No bullet points, no asterisks, no markdown headings.
- Sound like a South Indian indie artist, not a corporate intern.

OUTPUT STRICTLY:
SUBJECT: <subject>
BODY:
<email body>

Signature MUST be exactly:
Warm regards,
{BRAND['founder']} (roshmusik)
{BRAND['tagline']}
🎵 All music: {BRAND['links']['linktree']}
🎧 {BRAND['links']['spotify']}
📺 {BRAND['links']['youtube']}
{BRAND['phone']} · {BRAND['email']}
{BRAND['website']}
"""


def configure():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY missing in .env")
    genai.configure(api_key=key)
    return genai.GenerativeModel("gemini-flash-latest")


def load_leads() -> list[dict]:
    if not LEADS_CSV.exists():
        raise SystemExit("No leads.csv found. Run scraper.py first.")
    with LEADS_CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_existing_pitches() -> dict:
    if not PITCHES_CSV.exists():
        return {}
    with PITCHES_CSV.open(encoding="utf-8") as f:
        return {(r["name"] + "|" + r["city"]).lower(): r for r in csv.DictReader(f)}


def save_pitches(rows: list[dict]):
    PITCHES_CSV.parent.mkdir(exist_ok=True)
    with PITCHES_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=PITCH_FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in PITCH_FIELDS})


def parse_output(text: str) -> tuple[str, str]:
    import re as _re
    subject = ""
    body = ""
    # Be tolerant of markdown wrappers like **SUBJECT:** or Subject:
    norm = _re.sub(r"\*+", "", text)
    m = _re.search(r"(?im)^\s*subject\s*:\s*(.+)$", norm)
    b = _re.search(r"(?im)^\s*body\s*:\s*$", norm)
    if m:
        subject = m.group(1).strip()
    if b:
        body = norm[b.end():].strip()
    if not subject or not body:
        lines = norm.strip().splitlines()
        if not subject:
            subject = (lines[0] if lines else "A quick note").strip()
        if not body:
            body = "\n".join(lines[1:]).strip() or norm.strip()
    # Final scrub: never let "SUBJECT:" leak into the subject value
    subject = _re.sub(r"(?i)^\s*subject\s*:\s*", "", subject).strip()[:140]
    return subject, body


def build_user_prompt(lead: dict) -> str:
    return (
        f"Business: {lead.get('name','')}\n"
        f"Category: {lead.get('category','')}\n"
        f"City: {lead.get('city','')}\n"
        f"Address: {lead.get('address','')}\n"
        f"Rating: {lead.get('rating','')} ({lead.get('reviews','')} reviews)\n"
        f"Website: {lead.get('website','')}\n\n"
        "Write the personalized cold email now."
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = all")
    ap.add_argument("--regenerate", action="store_true")
    args = ap.parse_args()

    model = configure()
    leads = load_leads()
    existing = {} if args.regenerate else load_existing_pitches()

    out_rows = list(existing.values())
    todo = [l for l in leads if (l["name"] + "|" + l["city"]).lower() not in existing]
    if args.limit:
        todo = todo[: args.limit]

    print(f"Generating pitches for {len(todo)} leads...")
    for i, lead in enumerate(todo, 1):
        try:
            resp = model.generate_content([SYSTEM_PROMPT, build_user_prompt(lead)])
            text = resp.text or ""
            subject, body = parse_output(text)
            out_rows.append({
                "name": lead["name"],
                "city": lead["city"],
                "category": lead["category"],
                "email_subject": subject,
                "email_body": body,
                "generated_at": time.strftime("%Y-%m-%d %H:%M"),
            })
            print(f"  [{i}/{len(todo)}] {lead['name']} → {subject[:60]}")
            time.sleep(1.2)  # gentle rate-limit for free tier
        except Exception as e:
            print(f"  [{i}] ERROR for {lead['name']}: {e}")

    save_pitches(out_rows)
    print(f"\n✓ Saved {len(out_rows)} pitches to {PITCHES_CSV}")


if __name__ == "__main__":
    main()
