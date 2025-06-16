import os
import subprocess
import sys

def open_file(filename):
    # Попытка открыть файл в текстовом редакторе
    if not os.path.isfile(filename):
        print("Файл не найден.")
        return
    try:
        if sys.platform.startswith('win'):
            os.startfile(filename)  # Windows
        elif sys.platform.startswith('darwin'):
            subprocess.run(['open', filename])  # macOS
        else:
            subprocess.run(['xdg-open', filename])  # Linux и др.
    except Exception as e:
        print(f"Не удалось открыть файл: {e}")

def show_file_content(filename):
    if not os.path.isfile(filename):
        print("Файл не найден.")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print("Содержимое файла:\n")
        print(content)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def find_files(search_str, start_path='.'):
    matches = []
    for root, dirs, files in os.walk(start_path):
        for name in files:
            if search_str.lower() in name.lower():
                full_path = os.path.join(root, name)
                matches.append(full_path)
    if matches:
        print(f"Найдено {len(matches)} файлов:")
        for path in matches:
            print(path)
    else:
        print("Файлы не найдены.")

def list_directory(path):
    if not os.path.isdir(path):
        print("Указанная директория не найдена.")
        return
    try:
        items = os.listdir(path)
        if not items:
            print("Директория пуста.")
            return
        print(f"Содержимое директории '{path}':")
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"       {item}")
    except Exception as e:
        print(f"Ошибка при чтении директории: {e}")

def main():
    while True:
        print("\nФайловый менеджер - выберите действие:")
        print("1 - Открыть файл")
        print("2 - Показать содержимое файла")
        print("3 - Найти файл/файлы")
        print("4 - Раскрыть директорию")
        print("0 - Выход")

        choice = input("Введите номер пункта: ").strip()
        if choice == '1':
            filename = input("Введите имя файла для открытия: ").strip()
            open_file(filename)
        elif choice == '2':
            filename = input("Введите имя файла для просмотра: ").strip()
            show_file_content(filename)
        elif choice == '3':
            search = input("Введите имя или часть имени файла для поиска: ").strip()
            start_dir = input("Введите путь для поиска (по умолчанию текущая директория): ").strip()
            if not start_dir:
                start_dir = '.'
            find_files(search, start_dir)
        elif choice == '4':
            dir_path = input("Введите путь к директории: ").strip()
            list_directory(dir_path)
        elif choice == '0':
            print("Выход.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
