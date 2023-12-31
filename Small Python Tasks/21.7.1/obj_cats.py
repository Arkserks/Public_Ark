from ClassCat_create import ClassCat

import json

cat_catalog = {}  # Создаем словарь для хранения данных из json файла
cat_objects = []  # Создаем список для хранения объектов ClassCat

with open('pets.json', 'r', encoding='utf8') as f:
    all_pets = json.load(f)

    # Перебираем результаты по ключу "results"
    for pet in all_pets["results"]:
        # Проверяем, является ли питомец кошкой
        if pet["species"]["code"] == "cat":
            # Если да, добавляем его в справочник
            pet_id = pet["id"]
            cat_catalog[pet_id] = {
                "name": pet["name"],
                "gender": pet["gender"]["name"],
                "age": pet["age"]
            }

# Создаем экземпляры класса для каждого кота и добавляем в список
for cat_id, cat_info in cat_catalog.items():
    cat_obj = ClassCat()
    cat_obj.init_from_dict(cat_info)
    cat_objects.append(cat_obj)

# Выводим информацию о каждом коте
for cat_obj in cat_objects:
    print(f"Name: {cat_obj.name}")
    print(f"Gender: {cat_obj.gender}")
    print(f"Age: {cat_obj.age}")
    print("---")
