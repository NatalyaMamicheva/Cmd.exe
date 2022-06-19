import os
import datetime
import win32api

print("Курсовая работа по Операционным системам. Автор: Мамичева Наталья Дмитриевна - 1")


def dannye(j):
    cm = ''
    arg = ''
    logic = True
    for i in j:
        if i == ' ' and logic:
            logic = False
        elif logic:
            cm += i
        else:
            arg += i
    return operation(cm, arg)


def operation(cm, arg):
    if cm == 'exit':
        return True

    elif cm == 'dir':
        try:
            file_ = input("Введите директорию ")
            dir_count = 0
            file_count = 0
            b = []
            for root, directories, files in os.walk(file_):
                for file in files:
                    fullname = os.path.join(root, file)
                    b.append(os.path.getsize(fullname))
                    print(f"{os.path.getsize(fullname)}  {fullname}")
            print(f"Суммарный объем файлов: {sum(b)}")
            for _, dirs, files in os.walk(file_):
                dir_count += len(dirs)
                file_count += len(files)
            print(f"Папок: {dir_count}")
            onlyfiles = next(os.walk(file_))[2]
            print(f"Файлов: {len(onlyfiles)}")
        except StopIteration:
            print("Ошибка! Проверьте введенные данные")

    elif cm == 'cd/?':
        with open("cd.txt", 'r', encoding="utf-8"):
            print("Смена директории")

    elif cm == 'date/?':
        with open("date.txt", 'r', encoding="utf-8"):
            print("Возвращение и изменение даты в виде строки")

    elif cm == 'attrib/?':
        with open("attrib.txt", 'r', encoding="utf-8"):
            print("Отображение и изменения атрибутов файлов и каталогов")

    elif cm == 'type/?':
        with open("type.txt", 'r', encoding="utf-8"):
            print("Отображение содержимого текстового файла")

    elif cm == 'cd':
        try:
            os.chdir(arg)
        except FileNotFoundError:
            print('Ошибка: Указанный путь не найден.')

    elif cm == 'date':
        print(f"Текущая дата: {datetime.date.today()}")
        print("Введите новую дату")
        day = int(input("День(Формат DD): "))
        month = int(input("Месяц(Формат MM): "))
        year = int(input("Год(Формат YYYY): "))
        try:
            if (year <= datetime.datetime.today().year) and (month >= 1 or month <= 12) and (day >= 1 or day <= 31):
                print(f"Новая дата: {datetime.date(year, month, day)}")
            else:
                print("Некорректная дата")
        except ValueError:
            print("Некорректная дата")

    elif cm == "attrib":
        file_ = input("Введите директорию ")
        attrs = win32api.GetFileAttributes(file_)
        if attrs == 16:
            print("Directory/ Файл является каталогом.")
            for root, directories, files in os.walk(file_):
                for file in files:
                    fullname = os.path.join(root, file)
                    attrs2 = win32api.GetFileAttributes(fullname)
                    if attrs2 == 32:
                        print(f"A       {fullname}")
                    if attrs2 == 2:
                        print(f"H       {fullname}")
                    if attrs2 == 1:
                        print(f"R       {fullname}")
                    if attrs2 == 4:
                        print(f"S       {fullname}")
        if attrs == 32:
            print(f"A       {file_}")
            print("Archive/ Этот файл помечается для включения в операцию добавочного резервного копирования.")
        if attrs == 2:
            print(f"H       {file_}")
            print("Hidden/ Файл скрытый и, таким образом, не включается в обычный список каталога.")
        if attrs == 1:
            print(f"R       {file_}")
            print("ReadOnly/ Файл доступен только для чтения.")
        if attrs == 4:
            print(f"S       {file_}")
            print("System/ Файл является системным.")

    elif cm == "type":
        file_ = input("Введите директорию ")
        with open(file_, 'r', encoding="utf-8") as file:
            if os.stat(file_).st_size == 0:
                print("Файл пустой")
            if os.stat(file_).st_size != 0:
                read_file = file.read()
                print(read_file)

    elif cm == "dir/a:r":
        file_ = input("Введите директорию ")
        from stat import S_IREAD
        os.chmod(file_, S_IREAD)
        print("Атрибут изменен")

    elif cm == "dir/o:n":
        file_ = input("Введите директорию ")
        s = os.listdir(file_)
        for i in s:
            print(*sorted(list(i.split())))

    elif cm == "dir/o:d":
        file_ = input("Введите директорию ")
        print(file_)
        import time
        file_list = os.listdir(file_)
        full_list = [os.path.join(file_, i) for i in file_list]
        time_sorted_list = sorted(full_list, key=os.path.getmtime)
        for i in time_sorted_list:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(i)))}      {i}")

    elif cm == "help":
        help_ = ["dir", "dir/a:r", "dir/o:n", "dir/o:d", "cd/?", "date/?", "attrib/?", "type/?", "cd <директория>",
                 "date", "attrib", "type <файл>"]
        print("Список доступных команд:")
        for q in help_:
            print(q)

    elif cm != 'dir' or cm != 'cd/?' or cm != 'date/?' or cm != 'attrib/?' \
            or cm != 'type/?' or cm != 'cd' or cm != 'date' or cm != 'attrib' or cm != 'type' or cm != 'cd' \
            or cm != "help" \
            or cm != "dir/a:r" or cm != "dir/o:n" or cm != "dir/o:d":
        print("Некорректно введена команда")


while True:
    com = input(os.getcwd() + ' > ')
    if dannye(com):
        break
