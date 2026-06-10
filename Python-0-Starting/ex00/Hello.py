ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List
ft_list[1] = "World!"

#tuples
my_list = list(ft_tuple)
my_list[1] = "Spain!"
ft_tuple = tuple(my_list)

#set
ft_set.remove("tutu!")
ft_set.add("Barcelona!")

#dict
ft_dict["Hello"] = "42Barcelona!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
