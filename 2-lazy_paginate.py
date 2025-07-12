#!/usr/bin/env python3

def paginate_users(page_size, offset):
    """ Simulate fetching of a page of users from a database. """
    return USERS[offset : offset + page_size]
    
def def lazy_paginate(page_size):
    """ A generator that lazy fetches pages of users """
    offset = 0
    
    while True:
        # Fetch next page of users using current offset.
        page = paginate_users(page_size=page_size, offset=offset)
        
        if not page:
            break
        
        yield page
        
        # Prepare for next iteration by updating the offset
        offset += page_size
