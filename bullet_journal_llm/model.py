"""Data model for bullet journal llm."""

import pathlib

import yaml
from dataclasses import dataclass, field
from mashumaro import DataClassDictMixin
from mashumaro.config import BaseConfig

@dataclass
class Prompt(DataClassDictMixin):
    """A bullet journal prompt."""

    prompt: str | None = None
    filename: str | None = None
    content: str | None = None

    class Config(BaseConfig):
        omit_none = False

@dataclass
class RapidLogEntry:
    """A rapid log entry."""

    type: str
    content: str
    status: str | None = None
    label: str | None = None
    critical: bool = False
    date: str | None = None
    entries: list[str] = field(default_factory=list)

    class Config(BaseConfig):
        omit_none = False


@dataclass
class JournalPage(DataClassDictMixin):
    """A parsed notebook entry."""

    filename: str
    created_at: str
    label: str
    date: str
    records: list[RapidLogEntry]

    class Config(BaseConfig):
        omit_none = False


@dataclass
class DynamicPrompt:
    """A dynamic prompt."""

    prompt: Prompt
    pages: list[JournalPage] = field(default_factory=list)

    @classmethod
    def from_file(cls, filename: pathlib.Path) -> "DynamicPrompt":
        """Create a dynamic prompt from a file."""
        content = filename.read_text()
        docs = list(yaml.load_all(content, Loader=yaml.CSafeLoader))
        if not docs:
            raise ValueError(f"Failed to parse {filename}")

        prompt = Prompt.from_dict(docs[0])
        pages = [JournalPage.from_dict(doc) for doc in docs[1:]]

        return cls(prompt=prompt, pages=pages)
