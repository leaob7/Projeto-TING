def exists_word(word, instance):
    return_data = []
    lines = []
    file_name = instance._data[0]["nome_do_arquivo"]
    file_lines = instance._data[0]["linhas_do_arquivo"]

    for line in file_lines:
        if word.lower() in line.lower():
            lines.append({"linha": file_lines.index(line) + 1})

    if len(lines) > 0:
        return_data.append({
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": lines
        })
    return return_data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
