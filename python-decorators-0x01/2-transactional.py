#!/usr/bin/env python3

import sqlite3
import logging
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        # connect to db, create if not exists
        conn = sqlite3.connect("ALX_prodev")
        return func(conn, *args, **kwargs)
        conn.close()
    return wrapper

@with_db_connection 
def transaction(func):
    @functools.wraps(func)
    def wrapper(self, *args. **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # If error occurs, rollback transaction
            self.conn.rollback()
            raise
        else:
            # Commit if no error occurs
            self.conn.commit()
            return result
    return wrapper
        
@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id= ?", new_email, user_id))

#### Update user's email with automatic transaction handling 
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
