import re
import csv


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern_phone = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_phone = r'+7(\2)-\3-\4-\5 \6\7'


def change(contact_list: list):
    list_new = list()
    for contact in contact_list:
        name = ' '.join(contact[:3]).split(' ')
        result = [name[0], name[1], name[2], contact[3], contact[4], re.sub(pattern_phone,
        sub_phone, contact[5]), contact[6]]
        list_new.append(result)
    return comb(list_new)


def comb(contacts: list):
    for con in contacts:
        first_name = con[0]
        last_name = con[1]
        for cont_new in contacts:
            first_name_new = cont_new[0]
            last_name_new = cont_new[1]
            if first_name == first_name_new and last_name == last_name_new:
                for i in range(len(con)):
                    if con[i] == "": con[i] = cont_new[i]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(change(contacts_list))