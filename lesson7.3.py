def second_index(text, some_str):
    n = text.find(some_str)
    num = text.find(some_str, n + 1)
    if num == -1:
        return None
    return num


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')
