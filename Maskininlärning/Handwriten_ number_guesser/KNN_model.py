import pickle
from sklearn.neighbors import KNeighborsClassifier
import torchvision
import torchvision.transforms as transforms


transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data/', train=True, download=True, transform=transform)
testset = torchvision.datasets.MNIST(root='./data/', train=False, download=True, transform=transform)



X_train = trainset.data.reshape([60000, 784])
y_train = trainset.targets

X_test = testset.data.reshape([10000, 784])
y_test = testset.targets


KNN_model = KNeighborsClassifier(n_neighbors=3)
KNN_model.fit(X_train, y_train)

model_pkl_file = "KNN_model.pkl"  

with open(model_pkl_file, 'wb') as file:  
    pickle.dump(KNN_model, file)