

# ex32 loop and lists


the_count = [1, 2, 3, 4]
fruits =  ['apples', 'oranges', 'pears', 'apricots']
changes = [1, 'pennies', 2, 'dimes', 4, 'quarters']


#this first kind of for-loop goes through a lists
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)


# also we can go through mixed lists Too
# notice we have to use %r since we dont know what's in in
for i in changes:
    print("I got %r" % i)


# then use the range function to generage a lists
elements = range(0,6)

# now we cna print them Too
for i in elements:
    print("Element was %d" % i)
