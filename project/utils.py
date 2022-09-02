from project.functions import load_data


def get_post_all() -> list[dict]:
    """Возвращает все посты"""
    data = load_data("project/data/posts.json")
    return data


def get_posts_by_user(user_name: str) -> list | list[dict]:
    """Возвращает посты определенного пользователя. Функция возвращает
    пустой список, если нет постов, в которых указан автором этот пользователь."""
    results = []
    for post in get_post_all():
        if post["poster_name"] == user_name:
            results.append(post)
    return results


def get_comments_by_post_id(post_id: int) -> list | list[dict]:
    """Возвращает комментарии определенного поста. Функция
    вызывает ошибку ValueError если такого поста нет и пустой
    список, если у поста нет комментов."""
    is_exist = False
    for post in get_post_all():
        if post_id == post["pk"]:
            is_exist = True
            break
    if not is_exist:
        raise ValueError("Такого поста нет")

    results = []
    for comment in load_data("project/data/comments.json"):
        if comment["post_id"] == post_id:
            results.append(comment)
    return results


def search_for_posts(query: str) -> list | list[dict]:
    """Возвращает список постов по ключевому слову
    или пустой список, если ничего не найдено"""
    results = []
    for post in get_post_all():
        post_content = post["content"].lower()
        if query.lower() in post_content:
            results.append(post)
    return results


def get_posts_by_pk(pk: int) -> dict:
    """Возвращает один пост по его идентификатору"""
    for post in get_post_all():
        if post["pk"] == pk:
            return post
