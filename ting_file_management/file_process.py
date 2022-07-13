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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
