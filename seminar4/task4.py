import threading
from pathlib import Path


def process_file(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.readlines()
            print(f'{f.name} consists of {len(content)} lines')
    except Exception as e:
        print(f'Error processing file {fname}: {e}')


def main():
    threads = []
    dir_path = Path('./task1')


    if not dir_path.exists() or not dir_path.is_dir():
        print(f'Directory {dir_path} does not exist or is not a directory')
        return

    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]

    for file_path in file_paths:
        thread = threading.Thread(target=process_file, args=(file_path,))
        threads.append(thread)
        thread.start()
        print(f'Thread {thread.name} started')

    for thread in threads:
        thread.join()
        print(f'Thread {thread.name} finished')


if __name__ == '__main__':
    main()
