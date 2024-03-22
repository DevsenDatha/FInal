import hashlib

def hash_function(depaulid, number):
    hash_value = hashlib.sha256(f"{depaulid} {number}".encode()).hexdigest()
    return hash_value

def set_bloom_filter_slots(depaulid, numbers):
    '''TODO: Set a bllom filter with 256000 slots and 6 hash functions. These correspond to the first 6 positions in the hash_value of the number'''



''' TODO: Set this to your DePaulID'''
depaulid = 'tmalik1'

''' TODO: Read the lineordertable'''
''' TODO: Determine which numbers should be in the bloomfilter'''

lineorder_numbers =

bloom_filter = set_bloom_filter_slots(depaulid, lineorder_numbers)
indexes_of_ones = [str(i) for i, val in enumerate(bloom_filter) if val == 1]
print(f"{','.join(indexes_of_ones)} bits have been set \n")

'''TODO: Save your filter in a file'''
