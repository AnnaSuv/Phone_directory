def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt("phon.txt")

    while choice != 9:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input("lastname: ")
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input("number: ")
            print(find_by_number(phone_book, number))
        elif choice == 4:
            last_name = input("lastname: ")
            new_number = input("new  number ")
            print(change_number(phone_book, last_name, new_number))
        elif choice == 5:
            user_data = input("new data: ")
            add_user(phone_book, user_data)
        elif choice == 6:
            write_txt("phonebook.txt", phone_book)
        elif choice == 7:
            lastname = input("lastname: ")
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 8:
            input_file = input("input_file: ")
            output_file = input("output_file: ")
            row_number = input("row_number: ")
            pick_data(input_file, output_file, row_number)
        choice = show_menu()


def show_menu():
    print(
        "Выберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Сменить номер телефона\n"
        "5. Добавить абонента в справочник\n"
        "6. Сохранить справочник в текстовом формате\n"
        "7. Удалить по фамилии\n"
        "8. Перенести запись\n"
        "9. Закончить работу\n"
    )
    choice = int(input())
    return choice


def print_result(data):
    for contact in data:
        print(contact["Фамилия"], contact["Имя"])
        print(contact["Телефон"])
        print(contact["Описание"])
    print()


def pick_data(input_file, output_file, row_number):
    row = read_txt(input_file)[int(row_number) - 1]
    new_row = f"{row['Фамилия']},{row['Имя']},{row['Телефон']},{row['Описание']}"
    with open(output_file, "a") as f:
        f.write(new_row)


def add_user(data, user_data):
    user_data = "\n" + user_data
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(",")))
    data.append(record)
    write_txt("phon.txt", data)


def find_by_lastname(data, lastname):
    for contact in data:
        if contact["Фамилия"] == lastname:
            return (
                f"{contact['Фамилия']} {contact['Имя']}\n"
                f"{contact['Телефон']}\n{contact['Описание']}"
            )
    return "Фамилия не найдена"


def find_by_number(data, number):
    for contact in data:
        if contact["Телефон"] == number:
            return (
                f"{contact['Фамилия']} {contact['Имя']}\n"
                f"{contact['Телефон']}\n{contact['Описание']}"
            )
    return "Номер не найден"


def change_number(data, last_name, new_number):
    for contact in data:
        if contact["Фамилия"] == last_name:
            contact["Телефон"] = new_number
            write_txt("phon.txt", data)
            return (
                f"{contact['Фамилия']} {contact['Имя']}\n"
                f"{contact['Телефон']}\n{contact['Описание']}"
            )
    return "Номер не найден"


def delete_by_lastname(data, lastname):
    for contact in data:
        if contact["Фамилия"] == lastname:
            data.remove(contact)
            write_txt("phon.txt", data)
            return f"Запись о {contact['Фамилия']} {contact['Имя']} удалена"
    return "Фамилия не найдена"


def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.split(",")))
            phone_book.append(record)

    return phone_book


def write_txt(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s = s + v + ","
            phout.write(f"{s[:-1]}")


if __name__ == "__main__":
    work_with_phonebook()
