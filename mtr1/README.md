
MTRPlanner
The program introduces two advanced ideas beyond the standard curriculum:

Trie Data Structure (Prefix Tree)

Unlike linked lists, stacks, or binary trees, a Trie is specialized for storing strings and supporting prefix queries.

Each node represents a character, and paths form complete words. This allows efficient auto‑completion of station names when a user types only part of the word, e.g. "sha" → "Sha Tin", "Shau Kei Wan".

This demonstrates encapsulation (nodes hide their internal children dictionary) and composition (the Trie is composed of multiple TrieNodes).

A Search Algorithm*

Instead of basic searching or sorting, A* is a heuristic‑driven pathfinding algorithm. It combines the actual cost from the start with an estimated cost to the goal, guiding the search intelligently.

In the program, stations are nodes and travel times are edge weights. A* finds the shortest route between stations, e.g. "Sha Tin → Admiralty → Central → Mong Kok → Yuen Long".

This demonstrates abstraction (the Graph class hides edge details) and polymorphism (heuristics can be swapped or extended).

Together, these show how OOP supports modular design: the Trie handles input processing, while the Graph + A* handle route computation. Each class has a clear responsibility, and they interact through composition.
