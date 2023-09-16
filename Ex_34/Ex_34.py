"""Задача 34:
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
“Пам парам”, если с ритмом все не в порядке

*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  """

def test_text(data_count):
    for k in range(len(data_count)-1):
        if data_count[k] == data_count[k+1]:
            return "Парам пам-пам"
        return "Пам парам"

def searh_count_a_in():
    list_1 = list((input("Вводи стих, Пух!: ").split())) # Для ввода руками
    #list_1 = list(("пара-ра-рам рам-пам-папам па-ра-па-да").split()) # Если руками лень)
    count_list = []
    for i in list_1:
        str(i)
        count = 0
        for j in i:
            if j == "а": # Можно исп. множество
                count += 1
        count_list.append(count)
    return test_text(count_list)
        
print(searh_count_a_in())

"""Сделал вариант только для одной буквы, если Винни добавит в свой 
репертуар другие гласные - добавлю множество гласных и буду проверять есть ли 
гласные из множества в фразе, увеличивая count..
Мне пока сложно применять функции высшего порядка, думаю в скором времени привыкну к ним)"""