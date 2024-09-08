"""Test that the bullet journal prompts are parsed correctly."""

from dataclasses import asdict
import pathlib
import yaml

from syrupy import SnapshotAssertion
import pytest

from bullet_journal_llm.model import Prompt, JournalPage, DynamicPrompt

PROMPTS_DIR = pathlib.Path("bullet_journal_llm/dynamic_prompts")
PROMPT_FILES = list(PROMPTS_DIR.glob("*.yaml"))


@pytest.mark.parametrize("filename", PROMPT_FILES, ids=[f.name for f in PROMPT_FILES])
def test_parse_dynamic_prompts(filename: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    """Test that the bullet journal prompts are parsed correctly."""

    dynamic_prompt = DynamicPrompt.from_file(filename)
    assert dynamic_prompt.prompt.to_dict() == snapshot

    for page in dynamic_prompt.pages:
        assert page.to_dict() == snapshot
