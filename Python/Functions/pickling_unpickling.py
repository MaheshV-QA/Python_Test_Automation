Decription ="""
Pickling (Serialization): The process of converting a Python object into a byte stream (serialized form)
 that can be stored in a file or sent over a network.

Unpickling (Deserialization): The process of converting the byte stream back into the original Python object.

"""
import pickle

print(Decription)
# Original data
data = {"name": "Alice", "age": 25, "city": "New York"}

# Pickling: Serializing the data and saving it to a file
with open("data.pkl", "wb") as file:   # "wb" means write in binary mode
    pickle.dump(data, file)

print("Data has been pickled and saved to data.pkl")

# Unpickling: Loading the data back into Python
with open("data.pkl", "rb") as file:   # "rb" means read in binary mode
    loaded_data = pickle.load(file)

print("Loaded Data:", loaded_data)
