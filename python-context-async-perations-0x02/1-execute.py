#!/usr/bin/env python3
import sqlite3


class ExecuteQuery:
    def __init__(self, db_name: str, query: str, params: tuple = ()):
        # Initializes the context manager 'with' the database file name.
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
    def __enter__(self):
        # Called with the with block
        # This method connects to the database and executes queries
        
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        
        return self.cursor
    def __exit__(self):
        # Called when exiting 'with' block
        # Handles commits, rollbacks and connection closing
        if exc_type is None:
            # Error occured inside 'with' block
            self.connection.rollback()
        else:
            # No error occured
            self.connection.commit()
            
        # close the connection
        self.connection.close()
        
        return False
        

with ExecuteQuery('ALX_prodev', 'SELECT * FROM users WHERE age > ?', (25,)):
    users = cursor.fetchall()
    
    for user in users:
        print(user)
