# На вхід функції correct_sentence передається два речення. Необхідно
# повернути їх виправлену копію так, щоб вони завжди починалися з великої
# літери та закінчувалися крапкою. Зверніть увагу, що не всі виправлення
# необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не
# потрібно, це буде помилкою
#
# Вхідні аргументи: string.
# Вихідні аргументи: string.
#
#
# Замість pass необхідно написати Ваше рішення.
# def correct_sentence(text):
#      pass
#
#
# correct_sentence("greetings, friends") -> "Greetings, friends."
# correct_sentence("hello") -> "Hello."
# correct_sentence("Greetings. Friends") -> "Greetings. Friends."
# correct_sentence("Greetings, friends.") -> "Greetings, friends."
# correct_sentence("greetings, friends.") -> "Greetings, friends."

def correct_sentence(text):
    sentences = text.split('.')

    new_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
            if not sentence.endswith('.'):
                sentence += '.'
            new_sentences.append(sentence)

    return ' '.join(new_sentences)


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
