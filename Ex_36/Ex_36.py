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


def get_clean_list(list_1):
    list_2 = []
    for _ in list_1:
        list_2.append([])
    return list_2

def get_res_line(list_y_values, x, num_now_list):
    res_list = []
    res_list.append(list_y_values[num_now_list])
    for _ in range(x-1):
        res_list.append(res_list[-1] + res_list[0])
    return res_list

x = (int(input("Введите x: ")))
y = (int(input("Введите y: ")))

list_name = ["list_" + str(i) for i in range(1, y+1)]
list_data = get_clean_list(list_name)

list_y_values = [m+1 for m in range(y)]

for i in range(len(list_data)):
    list_data[i] = get_res_line(list_y_values, x, i)

for i in range(len(list_name)):
    print(f"{list_name[i]} - {list_data[i]}")
