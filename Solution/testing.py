from search import Search
import os
from main import Main
import time


files = []

# for t in reversed(os.listdir("./solutions")):
for t in ["huge"]:
    for p in os.listdir("./solutions/"+t):
        route = f"./problems/{t}/{p}.json"
        files.append(route)

# files = []
# for t in reversed(os.listdir("./problems")):
#     for p in os.listdir("./problems/"+t):
#         route = f"./problems/{t}/{p}"
#         files.append(route)

for f in files[:1]:
    for a in ["breadth", "depth", "a", "best"]:
        print(f"\n\n{f} - {a}")
        Main(f, a).run()
        print("\nDONE\n")
