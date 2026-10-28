# Sharing CommsAlign

## Code review and edits

Repository: https://github.com/BroodrickVM/alignment

The owner can invite a reviewer in GitHub Settings → Collaborators → Add people,
using the reviewer's GitHub username or registered email. A private repository
requires access before cloning. The reviewer accepts the invitation, clones the
repository and follows the root README. Use a feature branch and pull request
for review before merging changes into main. An editor with write access can
change code; this does not give them permission to use private API credentials.

For public code, a fork and pull request is another option without write access.

## Browser-only dashboard access

A local 127.0.0.1 URL is not a shareable hosted dashboard. On Streamlit Community
Cloud, sign in with the repository owner's account and create an app using:

- Repository: BroodrickVM/alignment
- Branch: main
- Main file: streamlit_app.py
- Python: 3.11
- App name/subdomain: choose an available CommsAlign name.

Review visibility and any course hosting requirements before deploying. Use
private reviewer access where appropriate. Share the actual URL provided after
successful deployment; no hosted URL has been verified at preparation time.
The requirements.txt in the repository root installs both tool dependencies.

Tool 2 works without credentials. For Tool 1, add GW_AZURE_OPENAI_KEY,
GW_ENDPOINT, GW_API_VERSION and GW_MODEL as root-level string entries in private
Streamlit deployment secrets. Optional GW_REASONING_EFFORT may also be set.
Root-level Streamlit secrets are available as environment variables. Do not put
actual values in code, GitHub, screenshots or review messages. Do not activate
shared API credentials for unrestricted public use without deciding who may use
them and any associated usage costs.

Official deployment guide:
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

Official secrets guide:
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

## Reviewer checklist

Check survey scoring, tie behavior, suppression and incomplete data; read the
research access limits; test saving and exporting fictional discussion notes.
Tool 1 model quality requires separately configured GW access and live evaluation;
passing offline tests does not establish model quality. Do not add real employee
notes or copyrighted report extracts to GitHub.
