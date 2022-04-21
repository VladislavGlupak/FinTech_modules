# Imports
import hashlib

# Create an instance of the sha256 hashing function
sha = hashlib.sha256()

# Create the data input to be hashed
my_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a nisi et nunc sollicitudin laoreet in sed neque. Proin convallis varius odio, id euismod justo tristique at. Cras at ultricies nisi, sed vulputate ante. Praesent faucibus odio in tortor tincidunt tincidunt. Vivamus interdum, tortor ac semper laoreet, nisl nibh tincidunt ante, vitae iaculis arcu sapien quis turpis. Nunc in ullamcorper enim. Sed in est egestas, pulvinar orci in, laoreet nisl."

# Encode the data using the encode function
encoded_data = my_data.encode()

# Hash the encoded data
sha.update(encoded_data)

# Print the hash code
print(sha.hexdigest())