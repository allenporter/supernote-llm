# supernote-llm

Consuming contents of a Supernote Notebook for use with LLMs

## Extract text

Using supernote-tool:

Populate `notes/` with supernote files that contain text. The text will be
extracted into `texts/`
```
$ python3 supernote-llm
```

## Development log

Ideas to explore:
- [x] python development environment
- [x] Local respoitory of .note files
- [x] Extract text (autorecg) into a local text dump
- [ ] Create llama index dev environment
- [ ] Index notes into llama index
- [ ] Test queries against llama index
- [ ] Demo: Ask questions / summarize against the index?
