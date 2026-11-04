"""The single place where Tool 1 calls the GW model. The judge and the rewriter both go through here."""
from __future__ import annotations



from app.tool1.config import Settings, load_settings


class LLM:
    def __init__(self, settings: Settings | None = None):
        from openai import AzureOpenAI
        self.settings = settings or load_settings()
        self.client = AzureOpenAI(
            api_key=self.settings.api_key,
            azure_endpoint=self.settings.endpoint,
            api_version=self.settings.api_version,
            # GW's deployment has a token rate limit; retry 429/5xx with back-off.
            max_retries=8,
            timeout=180,
        )

    def complete(self, instructions: str, text: str, json_output: bool = False) -> str:
        """Sends standing instructions plus one input text through the Responses API and returns the reply."""
        kwargs = {}
        if self.settings.reasoning_effort:
            kwargs["reasoning"] = {"effort": self.settings.reasoning_effort}
        if json_output:
            kwargs["text"] = {"format": {"type": "json_object"}}
        response = self.client.responses.create(
            model=self.settings.model,
            instructions=instructions,
            input=text,
            **kwargs,
        )
        return response.output_text
