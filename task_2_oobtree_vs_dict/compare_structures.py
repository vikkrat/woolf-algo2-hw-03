import csv
import timeit
from BTrees.OOBTree import OOBTree
import pandas as pd

# === Завантаження CSV-файлу ===
DATA_PATH = "task_2_oobtree_vs_dict/data/generated_items_data.csv"

def load_items_from_csv(path):
    items = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            }
            items.append(item)
    return items

# === Додавання до структур ===
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

# === Діапазонні запити ===
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

# === Основна логіка ===
def run_test():
    items = load_items_from_csv(DATA_PATH)

    # Створення структур
    tree = OOBTree()
    dictionary = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    print("📦 Дані успішно додані до OOBTree та dict.")
    print(f"🔢 Загальна кількість товарів: {len(items)}")

    # Параметри запиту
    min_price = 50
    max_price = 100

    print(f"\n🔎 Діапазонний запит: ціна між {min_price} та {max_price}\n")

    # Замір часу OOBTree
    time_tree = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)

    # Замір часу dict
    time_dict = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

    print("⏱️ Результати продуктивності:\n")
    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict:    {time_dict:.6f} seconds")

    print("\n📈 Логічні висновки:")
    print("-" * 60)
    if time_tree < time_dict:
        print("✅ OOBTree виконує діапазонні запити значно швидше завдяки впорядкованій структурі.")
    else:
        print("⚠️ Dict показав кращий результат, хоча це не типовий випадок.")
    print("🔍 У OOBTree використано метод .items() — ефективний при великих обсягах даних.")
    print("🔎 У dict виконується повний лінійний перебір усіх елементів.")
    print("-" * 60)

if __name__ == "__main__":
    run_test()
