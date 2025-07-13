#!/usr/bin/env python3

import sqlite3
import functools
import logging

# Setup a logger for clear output ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [SQL] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
sql_logger = logging.getLogger('sql_logger')

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Store the original execute method from the sqlite3.Cursor class
        original_execute = sqlite3.Cursor.execute
        # Define our new patched execute method
        def patched_execute(self, sql, params=()):
            # Log the SQL query and its parameters
            sql_logger.info(f"Executing Query: {sql}")
            if params:
                sql_logger.info(f"Parameters: {params}")
            
            # Call the original execute method to actually run the query
            return original_execute(self, sql, params)

        # Replace the original method with our patched version
        sqlite3.Cursor.execute = patched_execute

        try:
            # Execute the original decorated function
            result = func(*args, **kwargs)
            return result
        finally:
            # CRITICAL: Restore original method in a finally block
            # This ensures it's always restored, even if the function fails.
            sqlite3.Cursor.execute = original_execute
            
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
