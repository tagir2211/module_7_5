import os
import time

directory = os.getcwd()
for root, directories, files in os.walk(directory):
    for file in files:
        print(f'Обнаружен файл: {file} ', end='\t')
        filepath = root
        print(f'Путь: {filepath} ', end='\t')
        filesize = os.path.getsize(os.path.join(root, file))
        print(f'Размер: {filesize} байт, ', end='\t')
        filetime = os.path.getatime(os.path.join(root, file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        print(f'Время изменения: {formatted_time}, ', end='\t')
        parent_dir = os.path.basename(os.path.dirname(root))
        print(f'Родительская директория: {parent_dir}')
