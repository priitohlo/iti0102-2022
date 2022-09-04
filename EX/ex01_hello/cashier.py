"""Cha-ching."""
amount = int(input("Enter a sum: "))
coins = 0

for i in [50, 20, 10, 5]:
    coins += amount // i
    amount -= i * (amount // i)

coins += amount

print(f"Amount of coins needed: {coins}")
