import numpy as np
new_image = np.array([[1, 2, 3,8,0] , [4, 5,6,3, 6] , [2,2,2,3,6] , [5,8,7,5,4] , [4,6,4,3,8]])
f = np.random.uniform(size=(3,5,5))
 
def convolucion(f):
#	new_image = np.array([[1, 2, 3,8,0] , [4, 5,6,3, 6] , [2,2,2,3,6] , [5,8,7,5,4] , [4,6,4,3,8]])
#	f = np.random.uniform(size=(3,5,5))
	filter_output = []
	
	for i in range(len(new_image)):
		
		for k in range(f.shape[2]):
			
			for j in range(new_image.shape[1]):
				filter_output.append((new_image[i][j]*f[:,:,k]).sum())

	filter_output = np.resize(np.array(filter_output), (len(new_image),f.shape[2],new_image.shape[1]))
	print(filter_output)
#	filter_output_sigmoid = sigmoid(filter_output)

convolucion(f)
