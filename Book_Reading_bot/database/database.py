# Создаем шаблон заполнения словаря с пользователями
user_dict_template: dict[str, int | set[int]] = {
    'page': 1,
    'bookmarks': set()
}

# Инициализируем "базу данных"
users_db: dict[int, dict[str, int | set[int]]] = {}
