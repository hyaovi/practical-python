# bounce.py
#
# Exercise 1.5
total_bounces = 10
current_height = 100  # meters
bounce = 1
while bounce <= total_bounces:
    current_height *= 3 / 5
    print(bounce, current_height)
    bounce += 1
