from textcheck.lib import spellcheck


def test_should_find_misspellings():
    input = """
    This text should be checked for mispelling.
    """

    misspellings = spellcheck.check(input, [])

    assert len(misspellings) == 1


def test_should_ignore_special_characters():
    input = """
    The text should be free of misspellings, even with
    special characters like | < > $ ^
    """

    misspellings = spellcheck.check(input, [])

    assert len(misspellings) == 0
