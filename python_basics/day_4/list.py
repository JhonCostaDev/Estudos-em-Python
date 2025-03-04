#%%
list_names = ['arthur', 'gustav', 'colin', 'michael', 'anna', 'marie', 'carol']
list_ages = [28, 42, 33, 29, 19, 15, 53]
list_grades = [7.5, 9.2, 6.8, 4.0, 8.7, 5.3, 10.0]

# get the first element
list_names[0]

# get the last element
list_names[-1]

# SLICING
# get between 2 and 5 element
list_names[2:-2]

# Lenght
len(list_ages)
#Sum of elements 
sum(list_ages)

# Average
average = sum(list_ages) / len(list_ages)
average

#Min
min(list_grades)
#Max
max(list_grades)











#%%
employe_header = ['name', 'age', 'married', 'profission', 'weight']
employer_1 = ['Michel', 29, True, 'lawyer', 79.8]
employer_2 = ['artur', 28, False, 'architect', 79.8]
employer_3 = ['carol', 53, True, 'teacher', 59.8]

for camp in employe_header:
    print(f'{camp} |', end=' ')
print('')
for employe in employer_1:
    print(f'{employe}|', end=' ')
print('')
for employe in employer_2:
    print(f'{employe}|', end=' ')
print('')
for employe in employer_3:
    print(f'{employe}|', end=' ')

# %%
#list 
# Build a list with lists
employers = [
    employe_header,
    employer_1,
    employer_2,
    employer_3
]

employers #print this
# %%
# get the employes name
for employ in employers:
    print(employ[0])

# %%
# Get employ profission
for employ in employers:
    print(employ[3])
# %%
