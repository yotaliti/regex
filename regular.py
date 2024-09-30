from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts_list = [contacts_list[0]]
# TODO 1: выполните пункты 1-3 ДЗ
# pprint(contacts_list)
contacts_dict = {}
for person in contacts_list[1:]:
    full_name = ' '.join(person[:3]).split()
    name = ' '.join(full_name[:2]).strip()
    phone_number = person[5]
    pattern = r"(\+7|8)?\s*\(*(\d{3})\)*[-\s]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*([^\s]+)?\s*(\d+)?\)*"
    subst = r'+7(\2)\3-\4-\5 \6\7'
    new_phone_number = re.sub(pattern, subst, phone_number).strip()

    if len(full_name) == 3:
        person_information = [full_name[2]]
    else:
        person_information = ['']
    person_information += person[3:5]
    person_information.append(new_phone_number)
    person_information.append(person[6])
    if name not in contacts_dict:
        contacts_dict[name] = person_information
    else:
        for i, v in enumerate(contacts_dict[name]):
            if v == '':
                contacts_dict[name][i] = person_information[i]
                
for k, v in contacts_dict.items():
    new_contacts_list.append(k.split() + v)
pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)
