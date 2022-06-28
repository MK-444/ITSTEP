import numpy as np


pole1 = np.array([1,3,5,6,8,9])

pole2 = np.arange(2,30,2)

pole3 =  np.linspace(1,10,9)

pole4 = np.zeros((3,7))

pole5 = np.ones((4,5))

print(pole1.max())
print(pole2.min())
print(pole3.sum())

nove_pole = pole4 + 15
jeste_nove_pole = pole5.reshape((2,10))


print(pole1)
pole1 + 10
pole1 - 5
pole1 * 5

np.array([5,6,7,8])
np.zeros(6) #array([0., 0., 0., 0., 0., 0.])
np.zeros((6, 7))
np.zeros((2,6,7))

np.ones((4)) #array([1., 1., 1., 1.])

np.empty(3)
np.full(3,7)

pole2 = np.arange(15)

pole2.reshape(3,5)

np.linspace(1,10,10)

