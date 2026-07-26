#build_query(**filters) turns keyword arguments into a URL query string.
#build_query(city="hyderabad", rating=4, veg=True)
#->  city=hyderabad&rating=4&veg=True
#build_query()
#->  (empty string)
def  build_query(**filters):
    print('&'.join(f"{k}={v}" for k, v in filters.items()))
build_query(city="hyderabad",rating=4,veg=True)
build_query()
#this print the empty string because we don't pass the argument(dictionary) to the function so the dictionary **filters is an empty dictionary,
#so the filters.items() returns empty key-val pairs so the join has only empty iterable so the join return the empty string

