#!/usr/bin/env python3

import sqlite3
import logging
import functools
import time

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
def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # create a mutable copy of arguments for the loop
            _retries, _delay = retries, delay
            
            while _retries > 0:
                try:
                    # Try to execute the decorated function
                    return func(*args, **kwargs)
                except exceptions as e:
                    # Decrement counter by 1
                    _retries -= 1
                    
                    if _retries == 0:
                        # Raise last exception of we run out of exceptions
                        raise
                    time.sleep(_delay)
        return wrapper
    return decorator
    
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
