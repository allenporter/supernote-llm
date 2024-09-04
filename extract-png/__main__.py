"""Supernote LLM."""

from pathlib import Path
import logging
import supernotelib as sn
from supernotelib.converter import VisibilityOverlay

_LOGGER = logging.getLogger(__name__)

NOTE_DIR = Path("notes/")
TEXT_DIR = Path("pages/")
POLICY = "loose"


def main():
    """Main function."""
    logging.basicConfig(level=logging.INFO)
    _LOGGER.info("Starting supernote-llm")
    for note_file in NOTE_DIR.glob("*.note"):
        notebook = sn.load_notebook(note_file, policy=POLICY)
        total_pages = notebook.get_total_pages()
        _LOGGER.info(f"Converting %s (%s pages)", note_file, total_pages)
        converter = sn.converter.ImageConverter(notebook)
        vo = sn.converter.build_visibility_overlay(background=VisibilityOverlay.DEFAULT)
        for i in range(total_pages):
            page_id= notebook.get_page(i).get_pageid()
            content = converter.convert(i)
            if content is None:
                _LOGGER.info(f"Skipping page %s/%s", i+1, total_pages)
                continue
            png_filename = TEXT_DIR / f"{note_file.stem}-{i:02d}-{page_id}.png"
            _LOGGER.info(f"Writing page %s/%s as %s", i, total_pages, png_filename)
            content.save(png_filename, format='PNG')
    print("Main")

if __name__ == "__main__":
    main();
