import click
import os

from reader import process

@click.command()
@click.option('--path', '-p', help='Путь до папки', required=True)
@click.option('--output', '-o', help='Имя файла с базой', required=True)
@click.option('--from-date', '-f', help='Статистику за сколько дней собирать', type=int)
def main(path: str, output: str, from_date: int):
    if not os.path.isdir(path):
        print(f'Нет такой папки с файлами - "{path}"')
    else:
        process(path, output, from_date)

main()