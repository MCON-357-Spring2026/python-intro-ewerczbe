"""
TODO:
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.
Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.
Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""
coordinates = ('latitude', 'longitude', 'altitude')
lat, lon, alt = coordinates
person_info = ('Alice', 10, 4.8)
name, age, height = person_info
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")
