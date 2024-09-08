# supernote-llm

Consuming contents of a Supernote Notebook for use with LLMs.

## Bullet Journal + LLM

The `bullet_journal_llm/` directory contains notebooks and libraries for parsing
bullet journal entries using Gemini 1.5 Flash. Using the pipeline needs the 
following steps:

- Download `.note` files and put them in `notes/`
- Extract pngs form the notebooks (see below) in `pages/`
- Run the pipeline which using a dynamic prompt based on the filename
- The results are stored in `docs/` which you can then index for searching

## Tools

The https://github.com/jya-dev/supernote-tool can be used to extract metadata
from a supernote file. We have a couple tools in this repo using the above as 
library to process content in a directory.

See [extract-text/](extract-text/) and [extract-png/](extract-png/). Populate
`notes/` with supernote files that contain text. The text will be extracted
into `texts/` or `pages/`.

```
$ python3 extract-text
```

## Supernote index

See jupyter notebook following the LLama Index https://docs.llamaindex.ai/en/stable/getting_started/starter_example.html tutorial.
