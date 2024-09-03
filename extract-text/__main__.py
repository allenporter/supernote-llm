"""Supernote LLM."""

from pathlib import Path
import logging
import supernotelib as sn

_LOGGER = logging.getLogger(__name__)

NOTE_DIR = Path("notes/")
TEXT_DIR = Path("texts/")
POLICY = "loose"


def main():
    """Main function."""
    logging.basicConfig(level=logging.INFO)
    _LOGGER.info("Starting supernote-llm")
    for note_file in NOTE_DIR.glob("*.note"):
        notebook = sn.load_notebook(note_file, policy=POLICY)
        total_pages = notebook.get_total_pages()
        _LOGGER.info(f"Converting %s (%s pages)", note_file, total_pages)
        converter = sn.converter.TextConverter(notebook)
        for i in range(total_pages):
            page_id= notebook.get_page(i).get_pageid()
            text = converter.convert(i)
            if text is None:
                _LOGGER.info(f"Skipping page %s/%s", i+1, total_pages)
                continue
            text_filename = TEXT_DIR / f"{note_file.stem}-{i+1}-{page_id}.txt"
            _LOGGER.info(f"Writing page %s/%s as %s %s", i+1, total_pages, text_filename)
            with open(text_filename, 'w', encoding='utf-8') as f:
                f.write(text)
  


    print("Main")

if __name__ == "__main__":
    main();
