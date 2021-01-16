# 111111111
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)


# 111111111 row label
# 111111111
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)


# 111111111 Panda read from file
# 111111111
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)


# 111111111 specify index
# 111111111
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)


# 111111111
# 111111111 Select data using pandas
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])
# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])


# 111111111 Same
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:4])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])
print(cars.iloc[2])
# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars["cars_per_cap"]
between  = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)








# 111111111
# 111111111
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
      offset -= 1
    else:
        offset += 1
    print(offset)


# 111111111
# 111111111
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))


# 111111111
# 111111111

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height):
    print(str(x) + ' inches')
# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for car, s in cars.iterrows():
    print(car)
    print(s)


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ': ' + str(row['cars_per_cap']))


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)


# 111111111
# 111111111
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# 111111111
# 111111111
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())


# 111111111
# 111111111
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))






# 111111111
# 111111111
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk



# 111111111
# 111111111
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)


# 111111111
# 111111111
# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()


# 111111111
# 111111111
# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


# 111111111
# 111111111
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# 111111111
# 111111111
# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# 111111111
# 111111111
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()


# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
# 111111111
