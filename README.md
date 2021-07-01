# textcheck

Run text checks on files from the command line.

```
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Word    ┃ Alternatives                                    ┃ Context                       ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ speling │ spieling, spelling, spewing, peeling, splinting │ should be checked for speling │
└─────────┴─────────────────────────────────────────────────┴───────────────────────────────┘
```
## Installation

Hunspell dictionary files `en_US.dic` and `en_US.aff` need to be placed in `/usr/share/hunspell` directory.

## CLI usage

### `spellcheck`

Run spellcheck for a set of files

**Usage**:

```console
$ textcheck spellcheck [OPTIONS] FILES...
```

**Arguments**:

* `FILES...`: [required]