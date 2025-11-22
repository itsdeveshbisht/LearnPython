user={'age':19,'username':'Devesh Bisht','weapons':'Machine Gun','clan':'Pauri ki Gang'}

print(user.keys())

adding_weapon =user['weapons']
user['weapons']= adding_weapon +' and '+ "pistrol"
print(user)

user.update({'is_banned': False})
print(user)

user['is_banned'] = True
print(user)

user2 = user.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user)
print(user2)
