from dataclasses import dataclass
from spacy.lang.en import English
from spacy_hunspell import spaCyHunSpell


@dataclass
class MisspelledWord:
    word: str
    suggestions: list[str]
    context: str


def _is_valid_word(nlp, word, ignore_words):
    if not word.is_punct and not str(word).isspace() and not str(word) in ignore_words:
        lexeme = nlp.vocab[str(word)]
        if lexeme.is_stop is False and word._.hunspell_spell is False:
            return True
    return False


def check(text: str, ignore_words: list[str]) -> list[MisspelledWord]:
    nlp = English()
    hunspell = spaCyHunSpell(nlp, "linux")
    nlp.add_pipe(hunspell)
    doc = nlp(text)
    corrections = []
    word_acc = []
    for word in doc:
        word_acc.append(str(word))
        if _is_valid_word(nlp, word, ignore_words):
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
