# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, delimiter=','):
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))
    common_participants = sorted(set1 & set2)
    return common_participants

# Пример использования функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(common)  # Output: ['Петров', 'Сидоров']