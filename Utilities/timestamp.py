import time

# Current time in seconds since the Epoch as a floating point number
current_time = time.time()

# Convert to nanoseconds
current_time_ns = int(current_time * 1e9)

# Let's say we want logs for the past one hour
one_hour_ago_ns:int = current_time_ns - (60 * 60 * 1000000000)

print(f"Current time (ns): {current_time_ns}")
print(f"One hour ago (ns): {one_hour_ago_ns}")
