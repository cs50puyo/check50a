a, b, c = eval(input('Enter three integers: '))

text = 'The number in ascending order are {}, {}, and {}.'

if a <= b <= c:
    print(text.format(a, b, c))
elif a <= c <= b:
    print(text.format(a, c, b))
elif b <= a <= c:
    print(text.format(b, a, c))
elif b <= c <= a:
    print(text.format(b, c, a))
elif c <= a <= b:
    print(text.format(c, a, b))
else:
    print(text.format(c, b, a))
