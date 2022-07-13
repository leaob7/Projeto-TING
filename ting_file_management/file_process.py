import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return None

    read = txt_importer(path_file)

    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(read),
        "linhas_do_arquivo": read
        }

    instance.enqueue(content)

    print(str(content), file=sys.stdout)


def remove(instance):
    if len(instance._data) == 0:
        return print('Não há elementos', file=sys.stdout)

    removed_item = instance.dequeue()
    print(
        f'Arquivo {removed_item["nome_do_arquivo"]} removido com sucesso',
        file=sys.stdout
        )


def file_metadata(instance, position):
    if position:
        return print('Posição inválida', file=sys.stderr)

    selected_item = instance.search(position)

    print(selected_item, file=sys.stdout)
