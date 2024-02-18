


import random
random.seed()

player_balance = 100


print("Welcome to the Ultimate Coin Flip!")
print("\nHere's how it works:")
print("1. You start with $100 in your pocket.")
print("2. You can bet any amount up to your current balance.")
print("3. Choose 'Heads' or 'Tails' for each round of coin flip.")
print("4. Correct guess, you win your bet; wrong guess, you lose your bet!")
print("\n(☞ﾟヮﾟ)☞ ---------------------------------------- ☜( ﾟヮﾟ☜)")


while player_balance > 0:
    
    print(f"\n👛 Current Balance: ${player_balance}\n")

    
    bet_input = input("💰 Enter your bet amount or type 'quit' to exit: ")

    
    if bet_input.lower() == 'quit':
        print("\n👋 Byebye, thanks for playing!")
        break

    
    if not bet_input.isdigit():   
                                  
        print("❌ Oops! Invalid input. Please enter a numeric value for your bet.")
        continue

    bet = int(bet_input)

    
    if bet > player_balance:
        print("⚠️ Insufficient funds! Try a smaller bet.")
        continue

    
    choice = input("🪙 Heads (H) or Tails (T)? ").upper()

    
    flip = random.choice(['H', 'T'])
    print(f"➡️ The coin flip result is: {flip}")

    
    if choice == flip:
        print("\n🎉 Congrats! You win!")
        player_balance += bet
    else:
        print("\n😢 Sorry, you lose.")
        player_balance -= bet

    print("\n--------------------------------------------------")













