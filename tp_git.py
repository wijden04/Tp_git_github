a = [("name", "Alice"), ("age", 25), ("city", "New York")]  # List of key-value pairs as tuples

# Use dictionary comprehension to create a dictionary by unpacking each tuple into key and value
res = {key: value for key, value in a}

print(res)
