"""Reads connection settings from the .env file so no key is written in the code."""
from __future__ import annotations

import os
from dataclasses import dataclass




@dataclass(frozen=True)
class Settings:
    api_key: str
    endpoint: str
    api_version: str
    model: str
    reasoning_effort: str | None


def load_settings() -> Settings:
    from dotenv import load_dotenv
    load_dotenv()
    values = {name: os.getenv(name, "").strip()
              for name in ("GW_AZURE_OPENAI_KEY", "GW_ENDPOINT", "GW_API_VERSION", "GW_MODEL")}
    missing = [name for name, value in values.items() if not value]
    if missing:
        raise RuntimeError(f"Missing in .env: {', '.join(missing)} (see .env.example).")
    return Settings(
        api_key=values["GW_AZURE_OPENAI_KEY"],
        endpoint=values["GW_ENDPOINT"],
        api_version=values["GW_API_VERSION"],
        model=values["GW_MODEL"],
        reasoning_effort=os.getenv("GW_REASONING_EFFORT", "medium").strip() or None,
    )
