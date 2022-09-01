# retrieve the most recent tweet and the oldest one

# suppose tweets are stored in an array
# the first one is the oldest 
tweets = ["third", "second", "first"]

print(tweets[0]) # O(1)
print(tweets[len(tweets) - 1]) # O(1)

# Why line 8 is O(1) and not O(n)?
# Because we are doing only one operation without matter the size
# of the input, meanwhile O(n) means that operations decrease or
# increase depending of the input size 

# Second part, comparing dates will be an O(n^2)
# TODO: what is the big O notation?

tweets = [['hi', 2012], ['second', 2014], ['hey', 2018]]

oldest = tweets[0][1]
newest = oldest
for sub_list in tweets: # O(n)
    if sub_list[1] < oldest: # O(1)
        oldest = sub_list[1]
    elif sub_list[1] > newest: # O(1)
        newest = sub_list[1]

# O(n)



