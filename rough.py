#lst = [1,2,3]
#my_str = "mlops playlist"
#my_int = 155

#print(type(my_str))

#my_str=my_str.capitalize()
#print(lst)

#a = 'x'
#b = 'y'

#print(a+b)

from oops_proj import chatbook 

user1 = chatbook()
print(user1.id)

#Using static method directly fromclass rather than object
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

# getter and setter
#print(user1.get_name())
#user1.set_name("Agent X")
#print(user1.get_name())



#print(user1._chatbook__name)

#lst = [1,7,3]

#a1 = len(lst)
#print(a1)

#this how we call a method
#user1 = chatbook()
#user1.sending()

#print(user1.name)