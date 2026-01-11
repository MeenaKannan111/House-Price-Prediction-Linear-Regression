import pickle

# Load saved model
with open("california_house_lr_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Enter house details:")

medinc = float(input("Median Income: "))
houseage = float(input("House Age: "))
averooms = float(input("Average Rooms: "))
avebed = float(input("Average Bedrooms: "))
population = float(input("Population: "))
aveoccup = float(input("Average Occupancy: "))
latitude = float(input("Latitude: "))
longitude = float(input("Longitude: "))

data = [[medinc, houseage, averooms, avebed, population, aveoccup, latitude, longitude]]

price = model.predict(data)

print("Predicted House Price (in $100,000s):", price[0])


