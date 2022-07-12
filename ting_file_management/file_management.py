import sys


def txt_importer(path_file):
    try:
        file_type = path_file.split('.')[1]

        if file_type != 'txt':
            print("Formato inválido", file=sys.stderr)

        reader = open(path_file, 'r').read().splitlines()

        return reader

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
