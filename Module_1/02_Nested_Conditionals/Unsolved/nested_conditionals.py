"""Nested Conditionals."""

# @TODO: Create variables with the initial ad price and company type
# YOUR CODE HERE!
ad_price = 10
company_type = "Startup"

# @TODO: Convert the following decision logic into valid Python code.
# if the ad price is affordable (less than 20):
if ad_price < 20:
#     if the company is a startup:
    if company_type == "Startup":
#         print that the expected profit is 500
        print("expected profit is 500")
#     elif the company is existing:
    elif company_type == "existing":
#         print that the expected profit is 100
        print("expected profit is 100")
#     else:
    else:
#         print that the company type is not specified
        print("company type is not specified")
# else:
#     print that the ad price is too expensive
else:
    print("ad price is too expensive")
