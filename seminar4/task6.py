import asyncio
from pathlib import Path

async def process_file(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.readlines()
            print(f'{f.name} consists of {len(content)} lines')
    except Exception as e:
        print(f'Error processing file {fname}: {e}')

async def main():
    dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())