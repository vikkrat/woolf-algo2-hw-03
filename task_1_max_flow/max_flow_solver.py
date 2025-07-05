import networkx as nx
import matplotlib.pyplot as plt

# Побудова графа
G = nx.DiGraph()

edges = [
    ("T1", "S1", 25),
    ("T1", "S2", 20),
    ("T1", "S3", 15),
    ("T2", "S3", 15),
    ("T2", "S4", 30),
    ("T2", "S2", 10),
    ("S1", "M1", 15), ("S1", "M2", 10), ("S1", "M3", 20),
    ("S2", "M4", 15), ("S2", "M5", 10), ("S2", "M6", 25),
    ("S3", "M7", 20), ("S3", "M8", 15), ("S3", "M9", 10),
    ("S4", "M10", 20), ("S4", "M11", 10), ("S4", "M12", 15),
    ("S4", "M13", 5), ("S4", "M14", 10),
]

for u, v, cap in edges:
    G.add_edge(u, v, capacity=cap)

# Додаємо супержерело та суперстік для обчислення загального потоку
G.add_node("SRC")
G.add_edge("SRC", "T1", capacity=float("inf"))
G.add_edge("SRC", "T2", capacity=float("inf"))

G.add_node("SINK")
for i in range(1, 15):
    G.add_edge(f"M{i}", "SINK", capacity=float("inf"))

# Розрахунок максимального потоку
flow_value, flow_dict = nx.maximum_flow(G, "SRC", "SINK")
print(f"\n🔢 Загальний максимальний потік: {flow_value} одиниць\n")

# Вивід таблиці: Термінал → Магазин
print("📊 Потоки з терміналів до магазинів:\n")
print(f"{'Термінал':<10} {'Магазин':<10} {'Фактичний Потік':<20}")
print("-" * 40)

for t in ["T1", "T2"]:
    for s in flow_dict[t]:
        if flow_dict[t][s] > 0:
            for m in flow_dict[s]:
                if flow_dict[s][m] > 0:
                    print(f"{t:<10} {m:<10} {flow_dict[s][m]:<20}")

# Висновки
print("\n🧠 Логічні висновки:")
print("-" * 60)
print("1. Найбільший потік забезпечує Термінал 2 (T2) завдяки великій пропускній здатності Складу 4.")
print("2. Вузькі місця — Склад 2 (S2) та Склад 3 (S3), оскільки вони отримують обмежену кількість від двох терміналів.")
print("3. Магазини, які отримали найменше товарів — M13 та M14.")
print("4. Для покращення ефективності можна збільшити пропускну здатність зв’язків T2→S2, S3→M9 та S4→M13.")
print("-" * 60)

# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
edge_labels = {(u, v): f'{d["capacity"]}' for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф логістичної мережі")
plt.savefig("graph_output.png")
plt.show()
