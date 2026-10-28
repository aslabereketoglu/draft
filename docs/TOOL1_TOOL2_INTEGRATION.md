# Shared AlignAgent interface

Install `.venv/bin/pip install -r requirements-tool1.txt`, then run
`.venv/bin/streamlit run streamlit_app.py --server.address 127.0.0.1 --server.port 8520`.

Overview, Tool 2 Team Diagnostic and Tool 1 Message Coach share the sidebar.
Tool 2's original standalone entry point still works. Its analysis, notes,
privacy controls and evidence records are unchanged.

Tool 1 uses the same teammates' source snapshot as the previous local merge;
see app/tool1/UPSTREAM.md. The source version has not been confirmed by teammates.
Its judge and label rules are preserved. The rewriter and automatic cross-tool
handoff are not implemented. The existing local personal-agent CLI is separate.

For live evaluation, copy .env.example to .env and configure GW_AZURE_OPENAI_KEY,
GW_ENDPOINT, GW_API_VERSION and GW_MODEL from the GW guide. Never commit secrets.
Only explicit draft submission with consent calls the model. Results are kept
in session state and can be explicitly downloaded or cleared. No live model
request is included in integration verification; mocked tests are not a claim
that the GW connection is operational.

This restored merge is local; it has not been pushed or deployed publicly.
