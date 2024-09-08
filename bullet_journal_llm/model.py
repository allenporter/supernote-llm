"""Data model for bullet journal llm."""

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
