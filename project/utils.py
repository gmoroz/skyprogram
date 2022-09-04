from project.functions import convert_to_link, load_data


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


def get_comments_by_post_id(id: str) -> list | list[dict]:
    """Возвращает комментарии определенного поста. Функция
    вызывает ошибку ValueError если такого поста нет и пустой
    список, если у поста нет комментов."""
    is_exist = False
    post_id = int(id)
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


def get_post_by_pk(pk: str) -> dict:
    """Возвращает один пост по его идентификатору"""
    id = int(pk)
    for post in get_post_all():
        if post["pk"] == id:
            post["content"] = convert_to_link(post["content"])
            return post
    return {}


def get_suffix(comments_count: int) -> str:
    # 1 комментарий 2,3,4, комментария 5-20 комментариев 21 комментарий
    checker = comments_count % 100
    if 5 <= checker <= 20:
        return f"{comments_count} комментариев"
    checker %= 10
    if checker == 1:
        return f"{comments_count} комментарий"
    if 2 <= checker <= 4:
        return f"{comments_count} комментария"
    return f"{comments_count} комментариев"


def search_by_tag(tag: str) -> list[dict]:
    """Данная функция получает на вход тег
    и находит все посты с таким тегом"""
    results = []
    for post in get_post_all():
        if tag.lower() in post["content"]:
            results.append(post)
    return results
