# Напишите функцию для транспонирования матрицы

def matrix_transpose(m):
    new = []
    for i in range(len(m[0])):
        new.append([])
    for i in range(len(m)):
        for j in range(len(m[i])):
            new[j].append(m[i][j])
    return new
                            
                            
print(matrix_transpose([[1, 2], [3, 4], [5, 6]]))
