def notation(base, n):
    if n<base:
        print(number_char[n], end=' ')
    else:
        notation(base, n // base)
        print(number_char[n % base], end=' ')


number_char = ['0','1','2','3','4','5','6','7','8','9']
number_char = number_char + ['A','B','C','D','E','F']

number = int(input("10진수를 입력하시오: "))
print('\n2진수:', end=' ')
notation(2, number)
print('\n8진수:', end=' ')
notation(8, number)
print('\n16진수:', end=' ')
notation(16, number)