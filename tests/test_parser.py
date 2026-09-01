import json
from pathlib import Path

import pytest

from careers_engine.parsers import JsonParser, MarkdownTableParser

FIXTURE = Path(__file__).parent / "fixtures" / "intern_intl.md"


def test_markdown_parser():
    parser = MarkdownTableParser()

    rows = parser.parse(FIXTURE.read_text())

    assert rows

    first = rows[0]

    assert "company" in first
    assert "role" in first
    assert "location" in first
    assert "posting" in first
    assert "category" in first


def test_json_parser():
    parser = JsonParser()

    content = """
    [
        {
            "company_name": "Google",
            "title": "Software Engineer Intern"
        }
    ]
    """

    rows = parser.parse(content)

    assert rows
    assert rows[0]["company_name"] == "Google"
    assert rows[0]["title"] == "Software Engineer Intern"


def test_json_parser_rejects_non_list():
    parser = JsonParser()

    with pytest.raises(ValueError, match="Expected JSON payload to be a list."):
        parser.parse('{"company_name": "Google"}')


def test_json_parser_rejects_invalid_json():
    parser = JsonParser()

    with pytest.raises(json.JSONDecodeError):
        parser.parse('{"company_name": "Google"')
