from __future__ import annotations

import json

from careers_engine.parsers.base import BaseParser


class JsonParser(BaseParser):
    """Parse JSON content into Python records."""

    def parse(self, content: str) -> list[dict]:
        payload = json.loads(content)

        if not isinstance(payload, list):
            raise ValueError("Expected JSON payload to be a list.")

        return payload
