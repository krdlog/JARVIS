import sqlite3


class MemoryEngine:

    def __init__(self):
        self.connection = sqlite3.connect("memory/jarvis.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        self.connection.commit()

    def remember(self, key, value):

        self.cursor.execute("""
            INSERT OR REPLACE INTO memory(key, value)
            VALUES(?, ?)
        """, (key, value))

        self.connection.commit()

    def recall(self, key):

        self.cursor.execute("""
            SELECT value FROM memory
            WHERE key = ?
        """, (key,))

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None