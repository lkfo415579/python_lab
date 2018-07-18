def fab(max):
    n ,a ,b = 0, 1, 1
    while n < max:
        yield b
        a, b = b , a + b
        n += 1

for result in fab(5):
    print result
