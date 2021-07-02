from dataclasses import dataclass
from spacy.lang.en import English
from spacy_hunspell import spaCyHunSpell

nlp = English()
hunspell = spaCyHunSpell(nlp, "linux")
nlp.add_pipe(hunspell)


@dataclass
class MisspelledWord:
    word: str
    suggestions: list[str]
    context: str


def _is_valid_word(nlp, word, ignore_words):
    ignore_symbols = ["|", "<", ">", "$", "^"]
    if word.is_punct:
        return False
    if word.is_space:
        return False
    if str(word) in ignore_symbols:
        return False
    if str(word) in ignore_words:
        return False
    if word._.hunspell_spell is False:
        return True
    return False


def check(text: str, ignore_words: list[str]) -> list[MisspelledWord]:
    doc = nlp(text)
    corrections = []
    word_acc = []
    for word in doc:
        word_acc.append(str(word))
        if not _is_valid_word(nlp, word, ignore_words):
            continue
        index = len(word_acc)
        from_index = index - 5 if index > 5 else 0
        corrections.append(
            MisspelledWord(
                word=str(word),
                suggestions=word._.hunspell_suggest,
                context=" ".join(word_acc[from_index:index]),
            )
        )
    return corrections
