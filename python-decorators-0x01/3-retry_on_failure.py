#!/usr/bin/env python3

import sqlite3
import logging
import functools
import time

def retry_on_failure(retries=5, delay=1):
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
