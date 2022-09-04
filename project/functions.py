import json


def load_data(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def convert_to_link(post: str) -> str:
    """Данная функция заменяет все теги
    в строке вида #tag на ссылку, которую
    можно будет использовать в html шаблоне"""
    post_list = post.split()
    for index, word in enumerate(post_list):
        if word.startswith("#"):
            post_list[index] = f'<a href="/tag/{word[1:]}">{word}</a>'
    return " ".join(post_list)
