def correct_sentence(text):
    text = text.split('.', 1)

    if not text.endswith('.'):
        text += '.'

    return text


# Тестування функції
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
# Привести     text = text.strip().capitalize()
