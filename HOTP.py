import pyotp
import time

# Generate a random base32 secret
key = pyotp.random_base32()

# Create a HOTP object
gen_hotp = pyotp.HOTP(key)
hotp_token = gen_hotp.at(0)
print(f'Initialize HOTP: {hotp_token}')

# Generate a token at counter 0
counter = 0

# Looping 10 times
for i in range(10):
    # Generate token for the current counter
    token = gen_hotp.at(counter)

    print("Token at counter", counter, ":", token)

    # Increment counter for each iteration
    counter += 1

    # Simulate waiting for a new counter value
    time.sleep(1)