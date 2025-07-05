import csv
import random

CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys', 'Sports', 'Food']

def generate_item(item_id):
    return {
        "ID": item_id,
        "Name": f"Item-{item_id}",
        "Category": random.choice(CATEGORIES),
        "Price": round(random.uniform(10, 500), 2)
    }

def generate_csv(path, count=10000):
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["ID", "Name", "Category", "Price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, count + 1):
            writer.writerow(generate_item(i))
    print(f"✅ CSV-файл з {count} товарами збережено до: {path}")

if __name__ == "__main__":
    generate_csv("task_2_oobtree_vs_dict/data/generated_items_data.csv")
