"""C помощью метода строки str.lower переведите все элементы списка в нижний регистр."""


L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))
# ['this', 'is', 'lower', 'string']
