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

```
pip install --user textcheck
```

Hunspell dictionary files `en_US.dic` and `en_US.aff` need to be placed in `/usr/share/hunspell` directory.

## Limitations

* Only console output for now.
* Only English language is supported.
* Only Linux-based systems are supported.

## CLI usage

### `spellcheck`

Example invocation:

```
textcheck spellcheck ~/spellme.txt --ignore-list=/home/user/ignore_list.txt
```

Run spellcheck for a set of files. 

Provided ignore list is a file with ignore words on new lines.

**Usage**:

```console
$ textcheck spellcheck [OPTIONS] FILES...
```

**Arguments**:

* `FILES...`: The list of files to check

**Options**

* `ignore_list`: Path to the ignore list file.