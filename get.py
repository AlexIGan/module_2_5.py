def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


n = int(input('Введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))
value = input(f'Задайте значение: ')
matrix = get_matrix(n, m, value)

if n <= 0:
    print(":( Задано неверное кол-во строк:", n)
elif m <=0:
    print(":( Задано неверное кол-во столбцов:" ,m)
else:
    print(":) Все получилось: ")
    for i in matrix:
        print(*i)




