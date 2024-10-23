#!/usr/bin/env python3
'''Task 9 module.
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection based on kwargs.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
