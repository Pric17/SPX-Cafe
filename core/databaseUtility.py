import sqlite3
import os

class Database:
    @staticmethod
    def dbGet(sql, params=()):
        # [Inference] Automatically resolves path relative to this file
        baseDir = os.path.dirname(os.path.abspath(__file__))
        dbPath = os.path.join(baseDir, "..", "database", "SPXCafeDB.db")
        
        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results

    @staticmethod
    def dbSet(sql, params=()):
        baseDir = os.path.dirname(os.path.abspath(__file__))
        dbPath = os.path.join(baseDir, "..", "database", "SPXCafeDB.db")

        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        newId = cursor.lastrowid
        conn.commit()
        conn.close()
        return newId

