from datetime import datetime


def parametric_logger(file_name='log.txt'):
    def logger(func):
        def wrapper(*args, **kwargs):
            call_time = datetime.now()
            name = func.__name__
            res = func(*args, **kwargs)
            with open(file_name, 'a', encoding='utf-8') as f:
                f.write(
                    f'func_name: {name}, call_time: {str(call_time)}\nargs: {args}\nkwargs: {kwargs}\nresult:{res}\n\n')
            return res

        return wrapper

    return logger


# ПРОШЛОЕ ДЗ c декоратором******************************
import csv
from func import get_correct_fio, get_correct_phone, remove_duplicates


@parametric_logger(file_name='logggg.txt')
def get_fixed_book(contacts_list):
    correct_contact_list = [contacts_list[0]]
    for contact in contacts_list[1:]:
        correct_fio_list = get_correct_fio(contact)
        correct_fio_phone_list = get_correct_phone(correct_fio_list)
        correct_contact_list.append(correct_fio_phone_list)
    result = remove_duplicates(correct_contact_list)
    return result


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    fixed_book = get_fixed_book(contacts_list)

    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(fixed_book)
