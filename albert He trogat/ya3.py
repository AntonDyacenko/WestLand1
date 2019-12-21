n = int(input())
for x in input():
    if x.isalpha():
        if x.isupper():
            print((chr(ord(x) - ord('А') + n) % 32), end='')
        else:
            print(chr(ord('а') + n % 32 + ord('а')), end='')
    else:
        print(x, end='')
