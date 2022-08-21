# A hash table consist of a hash function and an array.
# A hash function is a function that takes in a string and gives an integer value.
# this value should be consistent 
# different strings should have different values.
# this value is used determines where the item is stored in the array.
                                    #
# A hash function tells the mapped value for a string in constant time 0(1)
# this value tells the position of the mapped object in the array which can be gotten in 
# 0(1) time since the position is known. hence the big 0 of hash table is 0(1).
                                        #
# Most programming languages have a predefined hash table in python it is called a dictionary
# it is one of the most powerful data structures and its very useful in storing key value pairs.


###################################################
#                 use case                         #
# it is used for lookup
# it is used to prevent duplication
# it is used for caching 
# #################################################


# For lookup
# hash table can be used to store key value pairs, given the key one can get its pair at 
# a constant time regardless of the number of keys in the hash table
# An example is seen below

phone_book = dict()

phone_book['Emergency'] = 911
phone_book['clinton'] = 82348
phone_book['Mum'] = 4445

print(phone_book['Mum'])

# used to prevent duplication

voted = {}

def check_voter(name):
    if voted.get(name):
        print("you can not vote twice")
    else:
        voted[name] = True
        print("let him vote")
        
check_voter('clinton')
check_voter('clinton')

# using hash table as a cache
cache = {}

def get_data_from_server(url):
    return "this is your " + url

def caching(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        
#               To recap, hashes are good for
# • Modeling relationships from one thing to another thing
# • Filtering out duplicates
# • Caching/memorizing data instead of making your server do work
        
