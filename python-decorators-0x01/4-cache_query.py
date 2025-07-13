#!/usr/bin/env python3

import sqlite3
import functools
import time

query_cache = {} # Dictionary to hold cached results

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        # connect to db, create if not exists
        conn = sqlite3.connect("ALX_prodev")
        return func(conn, *args, **kwargs)
        conn.close()
    return wrapper
    
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            return query_cache[query]
        
        # Call original function to get result from db
        result = func(conn, query, *args, **kwargs)
        
        # Store the result in our cache
        query_cache[query] = result
        
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
