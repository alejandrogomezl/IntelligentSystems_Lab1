from search import Search
import os
from main import Main


files = []

for t in reversed(os.listdir("./solutions")):
    for p in os.listdir("./solutions/"+t):
        route = f"./problems/{t}/{p}.json"
        files.append(route)

for f in files[:1]:
    for a in ["breadth", "depth", "a", "best"]:
        print(f"\n\n{f} - {a}")
        Main(f, a).run()
        print("\nDONE\n")