from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

_SCHEMA_DIR = Path(__file__).resolve().parents[2] / "schemas"


def load_schema(name: str) -> dict:
    """Load one canonical JSON Schema by contract name."""
    path = _SCHEMA_DIR / f"{name}.schema.json"
    if not path.is_file():
        raise KeyError(f"unknown schema: {name}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate_payload(schema_name: str, payload: dict) -> None:
    """Raise jsonschema.ValidationError when payload violates a contract."""
    Draft202012Validator(load_schema(schema_name)).validate(payload)
