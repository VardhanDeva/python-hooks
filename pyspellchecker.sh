from spellchecker import SpellChecker
spell = SpellChecker()
spell.word_frequency.load_words(['coddddded', 'sysssstem'])
spelled = spell.known(['coddddded', 'sysssstem', 'morning', 'ahiohrwoiehohwe'])
for word in spelled:
    print(word)