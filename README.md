# Introduction

This project is focused on implementing and analyzing different graph search algorithms—**Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, **A***, and **Best-First Search**—to solve pathfinding problems represented in road maps. The goal is to find the shortest path between two intersections (nodes) in a graph, where the edges represent roads with associated distances and speeds.

### Problem Overview

The search problem is defined by a road network consisting of intersections and road segments. Each intersection is a node with geographic coordinates (longitude, latitude), and each road segment (edge) connects two intersections, with specific distance and speed. The objective is to find the most efficient route (in terms of travel time) between a given start and goal intersection using various search strategies.

The road network is described in JSON format, specifying the intersections, segments, start, and goal points. The algorithms take this data as input, explore the network, and attempt to find the most optimal path while minimizing the cost, typically measured as the travel time.

### Algorithms Implemented

- **Breadth-First Search (BFS)**: Explores all nodes at the present "depth" level before moving on to nodes at the next depth level. This algorithm is typically used to find the shortest path in terms of the number of steps (or edges) between nodes.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking. DFS can find solutions faster in some cases, but it may not always find the shortest path.
- **A***: A heuristic-based search that uses both the actual cost to reach a node (`g(n)`) and an estimated cost from that node to the goal (`h(n)`) to prioritize the search. This is often the most efficient search when the heuristic is well-chosen.
- **Best-First Search**: A variant that explores nodes based on the heuristic value (`h(n)`), focusing on the nodes that seem to be closer to the goal.

### Technologies Used

- **Python**: The programming language used to implement the algorithms and handle the input/output of road network data.
- **JSON**: Used for representing the road networks, including intersections and road segments.
- **NetworkX** and **Matplotlib**: For visualizing the graph and path found by the algorithms.

This project demonstrates the implementation of these algorithms, comparing their performance in terms of nodes explored, generated, and execution time, and applying them to various road networks of different sizes.

---

# Project Architecture

The project is structured in a modular way to separate concerns and make the code easier to maintain and expand. Each module is responsible for a specific part of the system, such as handling the graph, performing the search, or managing the input/output. This section provides an overview of the project's architecture, describing the purpose of each module and how they interact.

## 1. **Main Modules**

The main modules of the project are as follows:

### 1.1 `main.py`

- **Purpose**: This is the entry point of the application. It initializes the problem by reading the road network data from a JSON file and invokes the selected search algorithm (BFS, DFS, A*, or Best-First).
- **Functionality**:
    - Loads the problem definition (intersections, segments, start, and goal points).
    - Runs the desired search algorithm based on user input.
    - Prints the path found and performance metrics (nodes generated, expanded, solution cost, execution time).

### 1.2 `search.py`

- **Purpose**: Contains implementations of four search algorithms—Breadth-First Search (BFS), Depth-First Search (DFS), A*, and Best-First Search—to find the most efficient route between two points on a road network graph.
- **Key Components**:
    - **Breadth-First Search (BFS)**: Implements BFS using a queue (FIFO), exploring the shallowest nodes first to guarantee the shortest path by steps between nodes.
    - **Depth-First Search (DFS)**: Implements DFS using a stack (LIFO), which explores as far along each path as possible before backtracking. Though faster in some cases, it may not find the shortest path.
    - *A Search*: Uses a priority queue (min-heap) to prioritize nodes based on the sum of the cost to reach a node (`g(n)`) and an estimated cost to reach the goal (`h(n)`), which is calculated using Euclidean distance between nodes. This heuristic guides the algorithm efficiently when well-chosen.
    - **Best-First Search**: Greedily explores nodes based on the heuristic alone (`h(n)`), prioritizing nodes that appear closer to the goal based on Euclidean distance.

### 1.3 `problem.py`

- **Purpose**: Defines the `Problem` class, which represents the search problem. This class handles the start and goal states, the graph structure (intersections and segments), and the methods for expanding nodes and checking goal conditions.
- **Key Components**:
    - `actions(state)`: Returns the possible actions from a given state.
    - `result(state, action)`: Returns the resulting state after applying an action.
    - `goal_test(state)`: Checks if a state is the goal.
    - `path_cost`: Returns the cumulative cost of the actions taken.

### 1.4 `state.py`

- **Purpose**: Defines the `State` class, representing an intersection in the road network. Each state has an identifier, coordinates (latitude and longitude), and a list of neighboring states (connected road segments).
- **Key Components**:
    - `identifier`: Unique ID for the state (intersection).
    - `latitude` and `longitude`: Geographic coordinates of the intersection.
    - `neighbors`: A list of connected states (other intersections).

### 1.5 `action.py`

- **Purpose**: Represents the `Action` class, which models the movement from one state to another. Each action has an associated distance and speed, which can be used to calculate the cost (travel time) of the action.
- **Key Components**:
    - `origin`: The starting state of the action.
    - `destination`: The target state of the action.
    - `distance`: The length of the road segment between the two states.
    - `speed`: The speed limit on the road segment.

### 1.6 `node.py`

- **Purpose**: The `Node` class encapsulates a state in the graph search, along with information about the path to reach the node, the cost of reaching it, and the node's parent in the search tree.
- **Key Components**:
    - `state`: The current state of the node.
    - `parent`: The node that led to this node.
    - `action`: The action taken to reach this node.
    - `path_cost`: The cumulative cost of reaching this node from the start.
    - `depth`: The depth of the node in the search tree.

### 1.7 `readJSON.py`

- **Purpose**: Handles loading and parsing of the road network data from JSON files. It creates instances of `State` and `Action` based on the data and builds the graph of intersections and road segments.
- **Key Components**:
    - `load_json()`: Reads the JSON file, creates the `State` and `Action` objects, and returns a `Problem` instance.

## 2. **Testing Module**

### 2.1 `testing.py`

- **Purpose**: Automates testing across multiple problem instances using various search algorithms, comparing performance metrics across problem sizes and configurations.
- **Key Components**:
    - **`run_tests()`**: Iterates over a predefined set of JSON problem files, applying each algorithm (BFS, DFS, A*, Best-First) to evaluate their performance.
    - **`compare_results()`**: Compares outputs for path cost, nodes generated, and execution time, enabling an efficient assessment of algorithm efficiency and suitability for different problem sizes.

## 3. **Graph Representation**

### 3.1 `graph.py`

- **Purpose**: Provides utilities to visualize the road network (intersections and segments) and solution paths generated by the algorithms, utilizing `NetworkX` for graph layout and `Matplotlib` for rendering.
- **Key Components**:
    - **`create_graph`**: Constructs the graph using intersection coordinates (latitude and longitude) for node positions and edges representing road segments.
    - **`show_graph`**: Renders the entire graph, highlighting the solution path (if available) in red. This visual representation makes it easier to understand the solution route and network structure.

## **4. Interaction Between Modules**

- **`main.py`** initializes the problem by loading a JSON file using `readJSON.py`.
- The `Problem` object is passed to the `Search` class, where the specified algorithm is executed.
- The algorithms use the `Node`, `State`, and `Action` classes to explore the graph.
- The results of the search are printed or returned for further analysis, and in testing, they are compared across different algorithms.

## **5. Data Input Representation**

- **Problem files**: Road networks are described in JSON format, located in the `./problems/` directory. Each JSON file defines:
    - **Intersections**: Representing the nodes (states).
    - **Segments**: Representing the edges (actions) between nodes.
    - **Start and Goal points**: Defining the initial and goal states for the search algorithms.

# **6. Data Output Representation**

- **Path Found**: The path from the start node to the goal is printed as a sequence of transitions between intersections, showing the origin, destination, and distance for each step.
- **Nodes Generated**: Displays the total number of nodes that were generated during the search, including nodes added to the frontier but not necessarily expanded.
- **Nodes Expanded**: Shows the number of nodes that were fully expanded, meaning their neighbors were explored during the search.
- **Solution Depth**: Indicates the number of steps (or edges) in the solution path, reflecting how deep the goal is in the search tree.
- **Solution Cost**: The cumulative cost of the solution path, typically representing the total travel time based on the distance and speed limits between nodes.
- **Execution Time**: The time taken to compute the solution, measured in nanoseconds, and displayed with high precision for performance evaluation.

---

# **Detail of the Components**

This section provides a detailed explanation of the key classes and methods used throughout the project. Each class is responsible for a specific function in the system, and together they implement the graph search algorithms and manage the problem structure.

### **5.1 `Problem` Class**

Defined in `problem.py`, this class represents the overall search problem. It manages the initial and goal states, as well as the road network (intersections and segments).

- **Attributes**:
    - `initial_state`: The starting state of the problem, which is the origin intersection.
    - `goal_state`: The goal state, or the destination intersection.
    - `intersections`: A dictionary where keys are intersection IDs, and values are `State` objects representing intersections.
    - `segments`: A dictionary of road segments that connect intersections, represented by `Action` objects.
- **Methods**:
    - `actions(state)`: Returns the list of valid actions (road segments) from the given state.
    - `result(state, action)`: Returns the state reached by applying the given action from the current state.
    - `goal_test(state)`: Checks if the current state matches the goal state.
    - `path_cost(cost_so_far, state1, action, state2)`: Calculates the cumulative cost of the path from the initial state to the given state.
    - `get_initial_state()`: Returns the initial state of the problem.
    - `is_goal(state)`: Returns `True` if the given state is the goal state, otherwise `False`.

### **5.2 `State` Class**

Defined in `state.py`, this class represents an intersection in the road network.

- **Attributes**:
    - `identifier`: A unique ID for the state, typically the intersection ID.
    - `longitude` and `latitude`: Geographic coordinates of the intersection.
    - `neighbors`: A list of neighboring states connected via road segments (represented by `Action` objects).
- **Methods**:
    - `__eq__(self, other)`: Defines equality between two states based on their identifiers.
    - `__hash__(self)`: Ensures that states can be used in sets and as dictionary keys, making them hashable.
    - `__repr__(self)`: Provides a human-readable representation of the state for debugging purposes.

### **5.3 `Action` Class**

Defined in `action.py`, this class models the road segments between intersections.

- **Attributes**:
    - `origin`: The starting intersection of the road segment.
    - `destination`: The ending intersection of the road segment.
    - `distance`: The distance between the two intersections (in meters or kilometers).
    - `speed`: The speed limit on the road segment, stored in meters per second.
- **Methods**:
    - `cost(self)`: Returns the cost of traversing this road segment, which is calculated as `distance / speed` (representing the travel time).

### **5.4 `Node` Class**

Defined in `node.py`, this class represents a node in the search tree. Each node corresponds to a state and includes information about the path leading to the node, the cumulative cost, and the node's depth in the tree.

- **Attributes**:
    - `state`: The current state (intersection) represented by this node.
    - `parent`: The parent node from which this node was reached.
    - `action`: The action taken to reach this node from its parent.
    - `cost`: The cumulative cost to reach this node from the initial state.
    - `depth`: The depth of the node in the search tree (i.e., the number of steps from the initial state).
- **Methods**:
    - `expand(problem)`: Expands the current node by generating its successor nodes based on the available actions in the problem. Returns a list of child nodes.
    - `path()`: Reconstructs and returns the sequence of nodes from the initial state to the current node.

### **5.5 `Search` Class**

Defined in `search.py`, this class contains implementations of the search algorithms: BFS, DFS, A*, and Best-First.

- **Methods**:
    - **`bfs()`** (Breadth-First Search):
        - Uses a queue (FIFO) to explore the shallowest nodes first. It tracks the number of nodes generated and expanded, and returns the solution path and performance metrics.
    - **`dfs()`** (Depth-First Search):
        - Uses a stack (LIFO) to explore deeper paths before backtracking. Like BFS, it tracks nodes generated and expanded, and returns the solution path and metrics.
    - **`a_star()`** (A* Search):
        - A heuristic-based search that combines the cost from the start (`g(n)`) and an estimated cost to the goal (`h(n)`). It uses a priority queue (heap) to explore the most promising paths first.
    - **`best_first()`** (Best-First Search):
        - A greedy search that uses only the heuristic (`h(n)`) to prioritize nodes based on their estimated distance to the goal.

Each method prints out the number of nodes generated, expanded, the depth of the solution, the cost, and the execution time.

### **5.6 `GraphVisualizer` Class**

Defined in `graph.py`, this class provides utilities for visualizing the road network and the solution path using NetworkX and Matplotlib.

- **Methods**:
    - `show_graph(self)`: Draws the entire graph of intersections and road segments. If a solution path is provided, it highlights the path in red.

### **5.7 JSON Loader**

Handled by `readJSON.py`, this module is responsible for loading the road network data from JSON files and converting them into `State` and `Action` objects.

- **Function**:
    - `load_json(file_path)`: Reads the JSON file, creates the corresponding `State` and `Action` objects, and initializes the `Problem` class with the parsed data.

### **5.8 Testing Module**

Defined in `testing.py`, this module automates the process of testing the different search algorithms on a set of predefined road network problems.

- **Function**:
    - `run_tests()`: Iterates over a directory of problem files and runs each search algorithm (BFS, DFS, A*, Best-First), printing the results for comparison.