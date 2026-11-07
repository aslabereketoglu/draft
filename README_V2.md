# CommsAlign v2

A custom workplace communication dashboard with **Message Coach** and **Team Diagnostic**.

V2 replaces the Streamlit interface with responsive HTML, CSS, and JavaScript, backed by a Python API. It reuses the existing communication review and survey analysis engines.

## Features

### Message Coach

- Review task instructions and performance feedback drafts.
- Inspect rubric ratings, quoted evidence, and review explanations.
- Receive a suggested revision with missing details marked as editable gaps.
- Edit the revision, request a new score, and download results.
- Require explicit consent before sending a draft to the configured GW Azure model.

### Team Diagnostic

- Explore the included synthetic team survey data.
- View hierarchy profiles, relative strengths, and areas to explore.
- Inspect provisional communication signals and their evidence limitations.
- Prepare discussion notes and download a follow-up summary.
- Suppress an entire team/period report when any supplied item falls below the selected reporting threshold.

### Workspace

- Responsive navigation for desktop and mobile.
- A restrained sage, forest-green, and neutral palette.
- An overview with team selection and a snapshot of the demonstration data.
- Drafts, reviews, and discussion notes held in page memory for the current session.

## Run locally

The custom application was tested with Python 3.13. Run these commands from the project root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-web.txt
python server.py --port 8502
```

On Windows, activate the environment with `.venv\Scripts\activate` instead of `source .venv/bin/activate`.

Open **http://127.0.0.1:8502** in your browser. Keep the terminal running while using the app. Stop the server with **Ctrl+C**.

The server listens on this computer's loopback address. It is a local application, not a publicly hosted website. Streamlit is not required to run the custom interface.

## Configure Message Coach

Team Diagnostic works without model credentials. Live Message Coach reviews require your GW Azure configuration.

Copy the example configuration:

```sh
cp .env.example .env
```

Fill in these settings locally using your GW-provided values:

```dotenv
GW_AZURE_OPENAI_KEY=your_key
GW_ENDPOINT=your_endpoint
GW_API_VERSION=your_api_version
GW_MODEL=your_model
```

`GW_REASONING_EFFORT` is optional and defaults to `medium`.

Do not upload `.env` or real API credentials. Opening the app does not trigger a model request. Draft submission and re-scoring require consent.

## Project structure

```text
server.py                 Local application entry point
requirements-web.txt      Custom application dependencies
app/
  web_api.py              Python API and static file serving
  organizational/         Survey analysis and discussion logic
  tool1/                  Review, revision, scoring, and rubric logic
web/
  index.html              Application shell
  app.css                 Design system and responsive styles
  app.js                  Navigation, overview, reports, and discussion notes
  coach.js                Message Coach interface
  helpers.js              Shared browser utilities
  assets/                 SVG branding and icons
data/organizational/      Synthetic survey data and evidence records
knowledge/
  evidence_cards.json     Evidence cards used by the review engine
tests/
  test_web_api.py         Custom API tests
.env.example              Configuration template without real credentials
.gitignore                Files excluded from Git tracking
DESIGN.md                 Visual design reference
```

Earlier Streamlit interface files are retained as development references. They are not used by `server.py`.

## Tests

Install the test tools and run the custom API checks:

```sh
python -m pip install "pytest>=8,<9" "httpx>=0.28,<1"
python -m pytest -q tests/test_web_api.py
```

These checks cover reporting suppression, consent, input validation, exports, model error handling, and application routes. They use mocked model responses rather than making live model requests.

The full repository suite also includes tests for the older Streamlit interfaces. Install `requirements.txt` to run those legacy tests.

## Session behavior and limitations

- The included teams and survey scores are fictional demonstration data.
- Survey interpretations and message ratings are provisional, not validated diagnoses or measures of communication effectiveness.
- Survey patterns do not establish causes.
- The minimum-response reporting rule does not guarantee anonymity.
- Notes and message results are held in memory and are lost on page reload. Download anything you want to keep.
- Save discussion notes in the session before downloading them. Unsaved edits are excluded from the discussion export.
- No server-side note storage, accounts, or automated cross-tool handoff has been added.
- Nothing is automatically sent to employees.
- CommsAlign is not affiliated with or endorsed by Gallup.

## Upload v2 to GitHub manually

You can upload this file as **README.md** in your repository.

To upload the working application as well, include:

- `server.py` and `requirements-web.txt`
- The complete `app/` and `web/` folders
- `data/organizational/` and `knowledge/evidence_cards.json`
- `.env.example` and `.gitignore`
- `tests/` if you want the automated checks
- `DESIGN.md` and other documentation you want to retain

Leave out `.env`, `.venv/`, `__pycache__/`, `.pytest_cache/`, `.streamlit/secrets.toml`, and personal or private team data. Development caches and screenshots in `.impeccable/` can also be omitted.

**Uploading this Markdown file alone documents v2. It does not upload the application code or publish a running website.**
