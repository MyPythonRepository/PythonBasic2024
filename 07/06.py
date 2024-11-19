text = "Hello, hello"
some_str = "lo"
index1 = text.find(some_str)
if index1 == -1:
    print(None)

index2 = text.find(some_str, index1 + 1)

print(index2 if index2 != -1 else print(None))


# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "find the river") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'



