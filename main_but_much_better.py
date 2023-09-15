import re
import unidecode as ud

word = re.sub(
    'X|Y|Z|W',
    lambda match: {'X': 'KS', 'Y': 'I', 'W': 'V', 'Z': 'S'}[match.group(0)],
    ud.unidecode(input('Zadej slovo: ')).upper()
)
priorities = {
    'C': 1,
    'D': 1,
    'H': 1,
    'J': 1,
    'K': 1,
    'Q': 1,
    'S': 1,
    'N': 1,
    'B': 2,
    'F': 3,
    'P': 3,
    'T': 3,
    'R': 3,
    'L': 4,
    'M': 4,
    'V': 5,
    'G': 5
}
word = '|'.join(
    re.findall(
        r'([AEIOU]{1}[^AEIOU]+?(?=[AEIOU])|[AEIOU]{1}[^AEIOU]+$|[^AEIOU]+?[AEIOU]{1}|.+$)',
        word
    )
)

word_components = ''.join(
    [letter + '|'
        if (i + 1 < len(word)
            and letter in priorities
            and word[i + 1] in priorities
            and priorities[letter] >= priorities[word[i + 1]])
        else letter
     for i, letter in enumerate(word)]).split('|')
print(word_components)
