# GhostShell AI 👻

A haunted-terminal-themed troubleshooting assistant using a hosted Gemma model. Paste terminal output, choose a response style, and receive an explanation or suggested fix.

## Features
- Diagnose terminal errors in beginner-friendly language.
- Suggest a minimal fix and explain it.
- Haunted mode adds playful spooky commentary.
- Responsive interface with sample errors.
- `/health` endpoint for deployment checks.
- The app analyzes text only; it never executes commands.
- API keys are loaded from environment variables.

## Model and inference
Configured to call Gemma through the Google Gen AI API. This is **hosted inference**, not local/offline inference. Verify current model availability, account access, quota, pricing and provider terms before use or submission. Do not claim offline operation.

## Run locally (Windows PowerShell)
1. Install Python 3.10+.
2. Open this folder in Cursor or a terminal.
3. Create and activate a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
6. Edit `.env` and add your own API key. Never share it or commit `.env`.
7. Start:
   ```powershell
   python app.py
   ```
8. Visit http://127.0.0.1:5000

## Deploy on Render
1. Push this folder to a GitHub repository.
2. Create a Render Web Service from that repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Health check path: `/health`
6. Add environment variables in Render:
   - `GEMINI_API_KEY` = your secret key
   - `GEMMA_MODEL` = `gemma-3-27b-it`
7. Deploy and test the public URL.

## Sample inputs
- `ModuleNotFoundError: No module named 'requests'`
- `! [rejected] main -> main (non-fast-forward)\nerror: failed to push some refs to 'origin'`
- `OSError: [Errno 98] Address already in use`

## Safety and privacy
Only paste text you are comfortable sending to the configured model provider. Never paste passwords, tokens, API keys, personal data or confidential logs. The server sends submitted text to the model provider for inference. AI responses can be wrong; review suggestions before running commands.

## Submission checklist
- [ ] Add API key securely.
- [ ] Test the model with multiple real errors.
- [ ] Confirm model/provider eligibility under the challenge rules.
- [ ] Deploy and test the live demo.
- [ ] Explain that inference is hosted, not local.
- [ ] Don't claim untested features.
