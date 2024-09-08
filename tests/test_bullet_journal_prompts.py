"""Test that the bullet journal prompts are parsed correctly."""

from dataclasses import asdict
import pathlib
import yaml

from syrupy import SnapshotAssertion
import pytest

from bullet_journal_llm.model import Prompt, JournalPage

PROMPTS_DIR = pathlib.Path("bullet_journal_llm/dynamic_prompts")
PROMPT_FILES = list(PROMPTS_DIR.glob("*.yaml"))


@pytest.mark.parametrize("filename", PROMPT_FILES, ids=[f.name for f in PROMPT_FILES])
def test_parse_prompts(filename: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    """Test that the bullet journal prompts are parsed correctly."""

    with open(filename, "r") as file:
        content = file.read()
        docs = list(yaml.load_all(content, Loader=yaml.CSafeLoader))
    assert docs
    assert len(docs) > 0
    
    prompt = Prompt.from_dict(docs[0])
    assert prompt.to_dict() == snapshot

    if len(docs) == 1:
        return

    for doc in docs[1:]:
        page = JournalPage.from_dict(doc)
        assert page
        assert page.to_dict() == snapshot
