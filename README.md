# Ocean Avenue Double Bay - Listing Page

Simple, fast Dash landing page for the apartment listing at oceanavenuedoublebay.com.au.

## Local setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:8050.

## Deploy on Render
1) Create a new Web Service from this repo/folder.
2) Render will use `render.yaml`:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:server`
3) Add a custom domain in Render:
   - Domain: `oceanavenuedoublebay.com.au`
   - Follow Render's DNS instructions to point your domain.

## Update content
- **Listing links**: edit the URLs in `app.py`.
- **Title and description**: edit the text in `app.py`.
- **Photos**:
  - Add images to `photos/` (the carousel cycles through everything in that folder).
  - Replace the placeholder files in that folder with real photos.

## Files
- `app.py`: Dash app layout and content.
- `assets/style.css`: Styling and fonts.
- `assets/carousel.js`: Lightweight photo carousel.
- `render.yaml`: Render deployment config.
