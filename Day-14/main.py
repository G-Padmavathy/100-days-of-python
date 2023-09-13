
from art import logo, vs
from game_data import data
import random

print(logo)
current_score = 0
print(f"Your current score is: {current_score}")

while True:
    compare_1 = random.choice(data)
    compare_2 = random.choice(data)
    # We can use the continue statement with the if loop to skip the current iteration of the loop.
    if compare_1 == compare_2:
        continue

    print(f"Compare A: {compare_1['name']}, a {compare_1['description']}, from {compare_1['country']}.")
    print(vs)
    print(f"Compare B: {compare_2['name']}, a {compare_2['description']}, from {compare_2['country']}.")

    user = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (user == 'A' and compare_1['follower_count'] > compare_2['follower_count']) or (
            user == 'B' and compare_2['follower_count'] > compare_1['follower_count']):
        current_score += 1
        print(f"You're right! Your current score is: {current_score}")
    else:
        print(f"Sorry, that's incorrect. Your final score is: {current_score}")
        # We can use the break statement else condition to terminate the loop when a certain condition is met. 
        break

