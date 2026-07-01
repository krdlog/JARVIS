from memory.memory_engine import MemoryEngine

memory = MemoryEngine()

memory.remember("favorite_color", "blue")

print(memory.recall("favorite_color"))