# app for translating to and from a secret code

to_translations = {
    'a': '', 'b': '›', 'c': 'ç', 'd': '∂',
    'e': 'é', 'f': 'ƒ', 'g': '¸', 'h': '˛',
    'i': 'ı', 'j': '√', 'k': 'ª', 'l': 'ﬁ',
    'm': '’', 'n': '‘', 'o': 'œ', 'p': 'π',
    'q': '•', 'r': 'r', 's': 'ß', 't': '†',
    'u': 'ü', 'v': '‹', 'w': 'Ω', 'x': '≈',
    'y': 'µ', 'z': 'z', 'æ': 'ä', 'ø': 'ö',
    'å': '˙'
}

from_translations = {value: key for (key, value) in to_translations.items()}

def translate(text, translations):
    return ''.join([translations.get(c, c) for c in text])

def main():
    while True:
        print('1. Translate to secret code')
        print('2. Translate from secret code')
        print('3. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            text = input('Enter text to translate: ')
            print(translate(text, to_translations))
        elif choice == '2':
            text = input('Enter text to translate: ')
            print(translate(text, from_translations))
        elif choice == '3':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()