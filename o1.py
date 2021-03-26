import random #import module

#main words
bigletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallletters = "abcdefghijklmnopqrstuvwxyz"
symbols = "_-.,:"
numbers = "123456789"

#adding all words
all = bigletters +smallletters +symbols +numbers
length = 16

#random from main words
pass = "".join(random.sample(all,lenth))

#show password
print(pass)




