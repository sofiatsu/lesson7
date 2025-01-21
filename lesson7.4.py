def common_elements():
    first = {x for x in range(100) if x % 3 == 0}
    second = {x for x in range(100) if x % 5 == 0}
    return first.intersection(second)
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())