import numpy as np
import matplotlib.pyplot as plt
import re
import random as rnd


def euclidean(x1, y1, x2, y2):
    # Calculate the distans between two points
    distance_points =np.sqrt((x1-x2)**2+(y1-y2)**2)

    return float(distance_points)


def classifier_nearst_point(nearest_points):
    # Check what class the nearest point hasa 0 = "Pich" or 1 = "Pikachu"
    if nearest_points[0][1] == 0:
        return "Pichu"
    if nearest_points[0][1] == 1:
        return "Pikachu"


def classifier_ten_nearst_point(nearest_points):
    # Finds the majority of ten nearest points classes and classifies the testpoint accordningly 
    count_pichu = sum(1 for vote in nearest_points if vote [1] == 0)
    count_pikachu = sum(1 for vote in nearest_points if vote [1] == 1)

    if count_pichu == count_pikachu:
        return f"{classifier_nearst_point(nearest_points)}, då rösterna är lika gäller närmsta punkten"

    if count_pichu > count_pikachu:
        return f"Pichu med {count_pichu} röster"
    else:
        return f"Pikachu med {count_pikachu} röster"    


def nearst_point(testpoint, traindata):
    # Gives a list on the ten closests training points to test point
    nearst_points =[(euclidean(testpoint[0], testpoint[1], train_point[0], train_point[1]), train_point[2]) for train_point in traindata]

    nearst_points.sort()
    return nearst_points[:10]   
       

def rnd_data():
    # Creats random test and train data lists
    rnd_traindata = rnd.sample(datapoints_0, 50)
    rnd_traindata += rnd.sample(datapoints_1, 50)

    rnd_testdata =[point for point in clean_data if point[:2] not in rnd_traindata]

    return(rnd_testdata, rnd_traindata)


def calculate_accuracy():
    # Gives the accuracy of predictions on random picked data points
    tp_tn = 0
    rnd_testdata, rnd_traindata = rnd_data()
    for test_point in rnd_testdata:
        result = nearst_point(test_point, rnd_traindata)
        if result[0][1] == test_point[2]:
            tp_tn += 1

    accuracy = tp_tn / len(rnd_testdata)

    return accuracy


with open("Labs/Data/datapoints.txt", "r") as data_read:
    # Creat a list of data points from file
    clean_data = [pokemon.replace(" ", "").strip().split(",") for pokemon in data_read if not pokemon.startswith("(")]
    clean_data = [[float(point) for point in pokemon] for pokemon in clean_data]

    # Sort points after class, pokemon, 0 = "Pichu" or 1 = "Pikachu"
    datapoints_1 = [pokemon for pokemon in clean_data if pokemon[2] == 1]
    datapoints_0 = [pokemon for pokemon in clean_data if pokemon[2] == 0]


with open("Labs/Data/testpoints.txt", "r") as test_read:
    # Makes a list of test points
    clean_test = [re.sub(r"[,()]", "", pokemon).strip().split(" ") for pokemon in test_read.readlines() if not pokemon[0].isalpha()]
    clean_test = [[float(point) for point in pokemon[1:]] for pokemon in clean_test]


# Prompt user to put in a x, y cordinate for a point
print("Labb 2 - En Pichus eller en Pikachus")
print("-------------------------------------\n")
print("Detta progarm testar om du har en En Pichus eller en Pikachus i vald punkt")

while True:
    try:
        x = float(input("Skriv in x-värdet för punkt du vill test: "))
        y = float(input("Skriv in y-värdet för punkt du vill test: "))
       
        if x >= 0 or y >= 0:
            test_point = [x, y]
            break
        else:
            print("Måste vara ett positivt värde.")

    except ValueError:
        print("Måste vara en siffra.")
    
    

# Create results from user input
result_nearest = classifier_nearst_point(nearst_point(test_point, clean_data))
result_vote = classifier_ten_nearst_point(nearst_point(test_point, clean_data))

print(f"\nDin valda punkt {test_point} är en: {result_nearest}. Som är den närmsta punkten\n")
print(f"Din valda punkt {test_point} är en: {result_vote}. Efter röstning av dom tio närmsta punkterna")


# Gives reslut from 10 itrations of calculating accuracy and an average 
accuracy_resluts = [calculate_accuracy() for calculation in range(10)]
average_accuracy = sum(accuracy_resluts)/10

# Makes lists with just the cordinates of the traing points
points_1 = [pokemon[:2] for pokemon in clean_data if pokemon[2] == 1]
points_0 = [pokemon[:2] for pokemon in clean_data if pokemon[2] == 0]

nr_loops = range(1, 11)

# Plot for training data, user point and accuracy
fig, ax = plt.subplots(2, 1, dpi=150, figsize=(7, 7))
plt.subplots_adjust(hspace=0.6)

ax[0].scatter(*zip(*points_0), label= "Pichu")
ax[0].scatter(*zip(*points_1), label= "Pickachus")
ax[0].scatter(x, y, label="User point")
ax[0].set_title("Träningspukter för Pichus och Pikachu")
ax[0].set_xlabel("Bredd")
ax[0].set_ylabel("Längd")
ax[0].legend()


ax[1].plot(nr_loops, accuracy_resluts)
ax[1].set_title(f"Träffsäkerheten. Där medelträffsäkerheten är: {average_accuracy:.3f}")
ax[1].set_xlabel("Antal kalkyleringar")
ax[1].set_ylabel("Procent")

plt.show()

