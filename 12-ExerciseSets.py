school = {'Bobby','Tammy','Jammy','Sally','Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

if len(school) == len(attendance_list):
    print("Everyone is Present In class")
else:
    print('This Student is Missing from the class :-' , school.difference(attendance_list))