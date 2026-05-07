# roshmusik — Music Lead Agent

Automated lead-generation for music gigs (film, album, jingle, event work) across South India — Kerala, Tamil Nadu, Karnataka, Telangana, Andhra Pradesh.

## What it does
- Scrapes Google Maps for film houses, recording studios, ad agencies, event companies, music labels, etc.
- Auto-extracts emails from their websites
- Uses Gemini AI to write personalised pitches in a musician's voice
- Saves drafts to your Gmail (or sends directly)
- WhatsApp click-to-chat dashboard

## Setup

1. Install Python 3.10+ from https://www.python.org/downloads/
2. `pip install -r requirements.txt`
3. `playwright install chromium`
4. Copy `.env.example` → `.env` and fill `GEMINI_API_KEY`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`
5. Run a test:
   ```powershell
   python scraper.py --category "recording studio" --city "Chennai" --limit 25
   python pitcher.py
   streamlit run dashboard.py
   ```

## Deployment
- Push to a private GitHub repo
- Add the 3 secrets to Repo → Settings → Secrets → Actions
- GitHub Actions will scrape + pitch + draft daily
- Deploy `dashboard.py` to Streamlit Cloud (free)
