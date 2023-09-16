"""Задача 36:
Напишите функцию 
print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую 
элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и 
столбцов таблицы, которые должны быть распечатаны. Нумерация 
строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, 
у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36    """


def copy_list(list_1):
    list_2 = []
    for i in list_1:
        list_2.append(i)
    return list_2

def f(list_y, x, cou):
    res_lis = []
    res_lis.append(list_y[cou])
    for _ in range(x-1):
        res_lis.append(res_lis[-1] + res_lis[0])
    return res_lis

x = (int(input("Введите x: ")))
y = (int(input("Введите y: ")))

list_name = ["list_" + str(i) for i in range(1, y+1)]
list_data = copy_list(list_name)

list_data[0] = [n+1 for n in range(x)]
list_y_nums = [m+1 for m in range(y)]

for i in range(1, len(list_data)):
    list_data[i] = f(list_y_nums, x, i)

for i in range(len(list_name)):
    print(f"{list_name[i]} - {list_data[i]}")
