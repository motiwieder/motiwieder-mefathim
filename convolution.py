import numpy as np


f = np.random.uniform(size=(3,5,5))
f = f.T
image = np.random.uniform(size=(6,28,28))

def new_image(image):

	new_image = []

	for k in range(image.shape[2]):

		for i in range(image.shape[0]-f.shape[0]+1):

			for j in range(image.shape[1]-f.shape[1]+1):
				new_image.append(image[:,:,k][i:i+f.shape[0],j:j+f.shape[1]])

	new_image = np.array(new_image)
	new_image.resize((image.shape[2],int(new_image.shape[0]/image.shape[2]),new_image.shape[1],new_image.shape[2]))
	new_image.shape
	return new_image

def convolucion(f,new_image):
	new_image = np.array([[1, 2, 3,8,0] , [4, 5,6,3, 6] , [2,2,2,3,6] , [5,8,7,5,4] , [4,6,4,3,8]])
	f = np.random.uniform(size=(3,5,5))
	filter_output = []
	
	for i in range(len(new_image)):
		
		for k in range(f.shape[2]):
			
			for j in range(new_image.shape[1]):
				filter_output.append((new_image[i][j]*f[:,:,k]).sum())

	filter_output = np.resize(np.array(filter_output), (len(new_image),f.shape[2],new_image.shape[1]))
	print(filter_output)
#	filter_output_sigmoid = sigmoid(filter_output)


ni = new_image(image)
convolucion(f,ni)
