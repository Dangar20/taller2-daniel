import random

def spin_roulette():
    return random.randint(0, 36), random.choice(['red', 'black'])

def place_bet(amount, bet_type, bet_value):
    number, color = spin_roulette()
    print(f"The roulette landed on {number} {color}")

    if bet_type == 'number' and bet_value == number:
        return amount * 35
    elif bet_type == 'color' and bet_value == color:
        return amount * 2
    else:
        return -amount

def main():
    balance = 20000
    print("Welcome to the Mega Roulette Game!")
    while balance > 0:
        print(f"Your current balance is: ${balance}")
        amount = int(input("Enter your bet amount: "))
        if amount > balance:
            print("You don't have enough balance to place this bet.")
            continue

        bet_type = input("Enter your bet type (number/color): ").lower()
        if bet_type == 'number':
            bet_value = int(input("Enter the number you want to bet on (0-36): "))
        elif bet_type == 'color':
            bet_value = input("Enter the color you want to bet on (red/black): ").lower()
        else:
            print("Invalid bet type.")
            continue

        result = place_bet(amount, bet_type, bet_value)
        balance += result - amount
        if result > 0:
            print(f"You won ${result}!")
        else:
            print(f"You lost ${-result}.")

    print("Game over! You have run out of balance.")

if __name__ == "__main__":
    main()