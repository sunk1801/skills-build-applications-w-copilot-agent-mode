# Repo guidance for AI coding agents (OctoFit Tracker)

Purpose
- Be concise and action-oriented: this file contains the project-specific patterns and commands an AI agent should use to be productive.

Big picture (what to know first)
- Frontend: React app at `octofit-tracker/frontend` (created with CRA). See `.github/instructions/octofit_tracker_react_frontend.instructions.md` for example commands.
- Backend: Django REST API at `octofit-tracker/backend/octofit_tracker`. Backend uses Django + DRF and is intended to run inside a Python venv at `octofit-tracker/backend/venv`.
- Database: MongoDB (project expects `mongodb-org`/`mongosh`). Django is configured to speak to MongoDB via `djongo`/`pymongo`.

Key conventions and project-specific patterns
- Never change directories when running agent-mode commands; always point at the target path. (See `.github/instructions/octofit_tracker_setup_project.instructions.md`.)
- Ports: expose only `8000` (backend public), `3000` (frontend public), `27017` (mongodb private). Do not propose other public ports.
- Django `settings.py` should use `CODESPACE_NAME` to add Codespace hostnames to `ALLOWED_HOSTS` (see `.github/instructions/octofit_tracker_django_backend.instructions.md`).
- `urls.py` should use the Codespace-based `base_url` pattern when present.
- Serializers: convert MongoDB `ObjectId` fields to strings before returning JSON (note: look at `serializers.py` guidance in `.github/instructions`).

Common tasks & exact commands
- Create backend venv:
  - `python3 -m venv octofit-tracker/backend/venv`
- Activate & install backend deps (use exact project path):
  - `source octofit-tracker/backend/venv/bin/activate`
  - `pip install -r octofit-tracker/backend/requirements.txt`
- Create React app / install frontend deps (target the folder):
  - `npx create-react-app octofit-tracker/frontend --template cra-template --use-npm`
  - `npm install bootstrap --prefix octofit-tracker/frontend`
  - `npm install react-router-dom --prefix octofit-tracker/frontend`
- Run backend (development):
  - Point at backend path; example: `python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000` (ensure venv active and settings use `CODESPACE_NAME` if needed).
- Run frontend (development):
  - `npm start --prefix octofit-tracker/frontend` (serves on port 3000).

Debugging, tests, and runtime checks
- Check MongoDB process: `ps aux | grep mongod` before attempting DB connections.
- Test REST endpoints with `curl` (project convention):
  - Example: `curl -sS http://localhost:8000/api/` to check API root.
- When debugging Codespaces-hosted URLs, rely on `CODESPACE_NAME` in `settings.py` and `urls.py`.

Files and places to inspect (high value)
- Start with: `README.md` and `docs/octofit_story.md` for goals and scope.
- Operational guidance: `.github/instructions/octofit_tracker_setup_project.instructions.md`.
- Backend rules: `.github/instructions/octofit_tracker_django_backend.instructions.md`.
- Frontend rules: `.github/instructions/octofit_tracker_react_frontend.instructions.md`.
- Useful prompts/workflow examples: `.github/prompts/*.prompt.md` and `.github/steps/*.md`.

Prompting tips for agents (practical)
- Be explicit about paths and do not assume a default working directory — always include the full repo-relative path in commands.
- When proposing to change network or port settings, reference the forwarded ports policy above and justify exceptions.
- For database schema/data changes, prefer using Django ORM migrations and management commands rather than raw MongoDB scripts.

If you change this file
- Keep it short and factual. Prefer examples and exact commands. Update `.github/instructions/*` references if you add new conventions.

Next step
- Ask for feedback on anything unclear or missing; I can iterate this file with more examples drawn from specific code files.
