def correct_sentence(text):
    if '.' in text:
        text_a, text_b = text.split('.', 1)
        text_a, text_b = text_a.strip(), text_b.strip()
        if not text_a.endswith('.'):
            text_a += '.'
        if not text_b.endswith('.'):
            text_b += '.'
        text_a, text_b = text_a.capitalize(), text_b.capitalize()
        second_text = ' ' + text_b if ' ' + text_b != ' .' else ''
        new_text = text_a + second_text
        return new_text
    else:
        if not text.endswith('.'):
            text += '.'
        return text.capitalize()

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
assert correct_sentence("greetings. friends.") == "Greetings. Friends.", 'Test6'
print('ОК')
