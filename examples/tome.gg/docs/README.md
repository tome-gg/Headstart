# Readme

## Input

The sample input is defined on `input.json`.

You should ideally edit the data in this format, so that it is simpler (with the VSCode JSON formatting/highlighting enabled).

## Generate output

When ready to prepare it into the format the Open Knowledge Map (OKM) uses, encode the data with the following instructions.

```bash
node encode-string.js input.json
```

## Field details

- `subject_orig` - Used as keywords for the document
- `resulttype` - Used as document type
- `url` - Used as a relative path for the URL, as long as the `url_prefix` is configured on the `data-config.js` of the map.