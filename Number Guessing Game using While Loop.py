stuck = "Ha ha! You're stuck in my loop!"
freed = "Well done, muggle! You are free now."

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Guess a number: "))

while guess != secret_number:
    print(stuck)
    
    guess = int(input("Guess a number: "))
    
print(freed)