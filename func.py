import re

def get_correct_fio(contact: list) -> list:
    correct_contact = []
    fio = []
    for i in contact[:3]:
        fio.extend(i.split())
    # dif = len(fio) - 3
    for _ in range(3-len(fio)):
        fio.append('')

    correct_contact.extend(fio)
    correct_contact.extend(contact[3:])
    return correct_contact


def get_correct_phone(contact: list) -> list:
    phone = contact[-2]
    if phone:
        pattern = r'(\+7|8)\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб.)?\s?(\d+)?\)?'
        substitution = r'+7(\2)\3-\4-\5 \6\7'
        contact[-2] = re.sub(pattern, substitution, phone).strip()
    return contact


def get_merging_list(lst1, lst2):
    if not lst1:
        return lst2
    res = [elem1 + elem2 if not elem1 or not elem2 else elem1 for elem1, elem2 in zip(lst1, lst2)]
    return res


def remove_duplicates(contact_list: list) -> list:
    dct = {}
    for contact in contact_list[1:]:
        key = tuple(contact[:2])
        vol = contact[2:]
        dct[key] = get_merging_list(dct.get(key, []), vol)
    result = [list(key) + vol for key, vol in dct.items()]
    return [contact_list[0]] + result

