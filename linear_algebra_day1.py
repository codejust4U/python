
import numpy as np

A= np.array([1,2,3,4,5])
B=np.array([6,7,8,9,10])
d = np.linalg.norm(A)

print("Distance from Origin : ",d)

diff = A-B

print("Difference from A to B ",diff)
euc_d = np.linalg.norm(diff)
print("Euclidean distance between A and B ",euc_d)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import euclidean

vectors = np.random.rand(5,3)

classes = np.random.randint(0,2,5)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

for vec,cls in zip(vectors,classes):
    ax.quiver(0,0,0,vec[0],vec[1],vec[2],color=("r" if cls==1 else "b"))

query_vector = np.array(list(map(float,input('Enter the query point (3D vector) separeted by space :').split())))


distances = [euclidean(query_vector,vec) for vec in vectors]
nearest_neighbour_index = np.argmin(distances)

print("The class of the nearest neighbour is ",classes[nearest_neighbour_index])

ax.quiver(0,0,0,query_vector[0],query_vector[1],query_vector[2],color='g')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")


import numpy as np
import matplotlib.pyplot as plt

# Generate random 2D data with 100 points
data = np.random.rand(100, 2)


# Plot the original data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], label="Original Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Before Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()



# Calculate the mean of the data along each dimension
data_mean = np.mean(data, axis=0)

print(data_mean)
# Perform mean centering
centered_data = data - data_mean

# Plot the mean-centered data
plt.subplot(1, 2, 2)
plt.scatter(centered_data[:, 0], centered_data[:, 1], label="Mean-Centered Data", color="orange")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("After Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate random 2D data with 100 points
data = np.random.rand(100, 2)

# Calculate the mean of the data along each dimension
data_mean = np.mean(data, axis=0)

# Perform mean centering
centered_data = data - data_mean

# Plot the original data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], label="Original Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Before Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

# Plot the mean-centered data
plt.subplot(1, 2, 2)
plt.scatter(centered_data[:, 0], centered_data[:, 1], label="Mean-Centered Data", color="orange")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("After Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random 2D vectors
data = np.random.rand(100, 2) * np.array([500, 0.01])

# Compute the min and max values for each feature
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)

# Apply min-max normalization (scaling)
normalized_data = (data - min_values) / (max_values - min_values)

# Plot the original data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], label="Original Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Before Min-Max Normalization")
plt.legend()

# Plot the normalized data
plt.subplot(1, 2, 2)
plt.scatter(normalized_data[:, 0], normalized_data[:, 1], label="Normalized Data", color="orange")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("After Min-Max Normalization")
plt.legend()

plt.show()


import numpy as np

# Define three vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])

# Calculate dot product using numpy.dot() function
dot_product_AB = np.dot(A, B)
dot_product_BA = np.dot(B, A)

print(dot_product_AB)
print(dot_product_BA)



# Check commutative property: A • B = B • A
if dot_product_AB == dot_product_BA:
    print("The dot product is commutative.")
else:
    print("The dot product is not commutative.")


# Check distributive property: A • (B + C) = A • B + A • C
dot_product_A_BC = np.dot(A, B + C)
dot_product_AB_plus_AC = np.dot(A, B) + np.dot(A, C)

print(dot_product_A_BC)
print(dot_product_AB_plus_AC)


if dot_product_A_BC == dot_product_AB_plus_AC:
    print("The dot product is distributive.")
else:
    print("The dot product is not distributive.")



import numpy as np

# Define two vectors
A = np.array([1, 2, 3])
B = np.array([-4, -5, -6])
C = np.array([5,5,5])


# Calculate the cosine similarity
cosine_similarity = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

print("Cosine similarity between A and B:", cosine_similarity)

# Calculate the cosine similarity
cosine_similarity = np.dot(A, C) / (np.linalg.norm(A) * np.linalg.norm(C))

print("Cosine similarity between A and C:", cosine_similarity)
