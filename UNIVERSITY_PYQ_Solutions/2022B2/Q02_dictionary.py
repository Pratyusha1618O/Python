#  Here is an example dictionary. You may insert more data of choice.
# d=[{'name':'Ram', 'phone':'9434141414', 'email':'ram@gmail.com'},
# {'name':'Laksman','phone':'8434151515',"},
# {'name':'Bharat','phone':'7474161616', 'email':'bharat@gmail.com'},
# {'name':'Satrughna','phone':'9478171717', 'email':'satrughna@gmail.com'}]
# Write a program in Python that reads the above dictionary and prints the following:
# (a) All the users whose phone number ends in 5
# (b) All the users that don't have an email address listed
# (c) All the users whose phone number starts with 9


d = [
    {'name':'Ram', 'phone':9434141414, 'email':'ram@gmail.com'},
    {'name':'Laksman', 'phone':8434151515},
    {'name':'Bharat', 'phone':7474161616, 'email':'bharat@gmail.com'},
    {'name':'Satrughna', 'phone':9478171717, 'email':'satrughna@gmail.com'}
]

# (a) All the users whose phone number ends in 5
user_end_5 = [i['name'] for i in d if str(i['phone'])[-1] == '5']


# (b) All the users that don't have an email address listed
user_without_email = [i['name'] for i in d if 'email' not in i]


# (c) All the users whose phone number starts with 9
ph_start_9 = [i['name'] for i in d if str(i['phone'])[0] == '9']


#display
print("User whose phone no. ends with 5: ", user_end_5)
print("User whose don't have email: ", user_end_5)
print("User whose phone no. starts with 9: ", ph_start_9)

