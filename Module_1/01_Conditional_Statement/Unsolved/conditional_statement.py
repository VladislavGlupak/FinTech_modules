"""A Logical Processor."""

# 1. @TODO: Create two new variables to hold user data:
# Populate this variable with our first user, who is based in the United States
# and is already registered on the platform.
# YOUR CODE HERE!
location = "US"
is_registered = True

# 2. @TODO: Write a conditional statement. If user is based in the U.S. and
# already registered, advertise the new service. Otherwise, give them
# notice that the feature is coming soon.
# YOUR CODE HERE!
if location == "US" and is_registered:
    print("Please check out new service!")
else:
    print("Feature is coming soon!")

# 3. @TODO: Change the user location to Japan and print the results again.
# Does your conditional statement program work as expected?
# YOUR CODE HERE!
location = "Japan"
if location == "US" and is_registered:
    print("Please check out new service!")
else:
    print("Feature is coming soon!")
