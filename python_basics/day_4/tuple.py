# Data Dog
#%%
dog_head = ['name', 'age', 'race', 'color', 'weight', 'have_collar']
dog_1 = ['fulio', 8, 'undefined', 'black', 10.89, True]
dog_2 = ['bella', 3, 'labrador', 'yellow', 25.4, False]
dog_3 = ['rex', 5, 'beagle', 'brown', 12.6, True]
dog_4 = ['luna', 2, 'husky', 'white', 20.3, True]
dog_5 = ['max', 7, 'poodle', 'grey', 8.7, False]
dog_6 = ['daisy', 4, 'bulldog', 'brindle', 22.1, True]

data_dog = [dog_head, dog_1,dog_2,dog_3,dog_4,dog_5,dog_6]
data_dog 
# %%
#tuples are a list that don't be change
tuple_data_dog = tuple(data_dog) # changing the type to tuple
type(tuple_data_dog)
# %%
