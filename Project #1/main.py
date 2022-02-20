from datetime import date

today_date = date.today()
task_list = []
count_id = 0
print(f'Привет, сегодня {today_date}, посмотри задачи')
print(f'0.Завершення роботи (done)\n' # завершает программу
      f'1.Створити нову задачу (done)\n' #генерирует словарь
      f'2.Переглянути список задач (done)\n' #вывести все словари списком ({id} {title} {status})
      f'3.Переглянути деталі задачі (вызов функции)\n' # запрос значения id (невалидный id - ошибка, запрос заново), вывод запрошенного словаря
      f'4.Редагувати задачу (вызов функции)\n' # запрос значения id (невалидный id - ошибка, запрос заново), поочередное предложение изменений значений ключей
      f'5.Видалити задачу (вызов функции)\n' #запрос значения id (невалидный id - ошибка, запрос заново), удаляет указанный словарь
      f'6.Знайти за назвою (вызов функции)\n' # поиск значения ключа title, ({id} {title} {status}
      f'7.Сортувати за пріоритетом (вызов функции)\n' #сортировка по значению ключа id, {id} {title} {status} {priority}, {priority} от 10 от 1
      f'8.Знайти просрочені задачі (вызов функции)\n' #поиск по значению ключа date который больше чем due_date, {id} {title} {status} {due_date}
      )

users_input = 1
# index = 1
while users_input in range(0, 8):
      # index = len(task_list) - 1
      users_input = int(input('Please enter No. of command (from 0 to 8): '))
      if users_input == 0:
            print('You finished work. Good bye.')
            exit()
      elif users_input == 1:
            f_count_id = len(task_list) + 1
            from _1_create_new_task import create_new_task
            # create_new_task()
            task_list.append(create_new_task())
            task_list[len(task_list) - 1]['id'] = f_count_id
            continue
      elif users_input == 2:
            for i in range(len(task_list)):
                  print(f'''ID: {task_list[i]['id']} Title: {task_list[i]['title']} Status: {task_list[i]['status']}''')
                  i += 1
      elif users_input




# keys: id, title, description (optional), status, due_date, priority

