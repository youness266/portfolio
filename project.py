# importing the tools 
import pyfiglet
import random
# main function 
def main():
    slot_machine()





# currency function
def function_1():
    ...

# slot machine
def slot_machine():
    title = pyfiglet.figlet_format("7️7️7️ Slot Machine ")
    print(title)


    reel1 = ["🍒"]*10 + ["🍋"]*8 + ["⭐"]*6 + ["7️⃣"]*3 + ["🎲"]*2 + ["🎟️"]*2
    reel2 = ["🍒"]*12 + ["🍋"]*9 + ["⭐"]*5 + ["7️⃣"]*4 + ["🎲"]*2 + ["🎟️"]*3
    reel3 = ["🍒"]*3  + ["🍋"]*10 + ["7️⃣"]*3 + ["🎲"]*2 + ["🎟️"]*2


    while True:
        try:
            coins = int(input("Enter number of coins to start: "))
            if coins > 0 :
                break 
            else:
                print("⚠️  Please enter a positive number of coins.")
        except ValueError:
            print("⚠️  Invalid input. Pl;ease enter a valid integer.")

    
    # settings 
    def spin_reels():
        return [random.choice(reel1), random.choice(reel2), random.choice(reel3)]

    def apply_wilds(spin):
        if "🎲" in spin:
            non_wilds = [s for s in spin if s!="🎲"]
            if non_wilds:
                common = max(set(non_wilds), key = non_wilds.count)
                spin = [common if s == "🎲" else s for s in spin]

        return spin
    
    free_spins = 0

    while coins > 0 or free_spins > 0:
        if free_spins > 0:
            play = input(f"🎟️ Free spin round! {free_spins} left. Press Enter: ")
        else:  
            play = input("Press Enter to spin (or type 'q' to quit): ")
        if play == "":
            bet = 10 if free_spins > 0 else None
            if bet is None:
                while True:
                    try:
                        bet = int(input("Enter your bet(coins): "))
                        if bet > 0 and bet <= coins : 
                            break
                        else:
                            print("⚠️  Bet must be positive and not exceed you coins.")
                    except ValueError :
                        print("⚠️  Invalid input. please enter a valid integer.")

            if free_spins > 0:
                free_spins -= 1
            else:
                coins -= bet

            win = 0
            
            spin = spin_reels()
            spin = apply_wilds(spin) 
            print(" | ".join(spin) + "  ↩️" )
            # Scatter check
            scatter_count = spin.count("🎟️")
            if scatter_count >= 3:
                free_spins += 10
                print(f"🎟️  Scatter bonus! You win {free_spins} free spins!")

            # Win check 
            
            if spin[0] == spin[1] == spin[2]:
                if spin[0] ==  "7️⃣" : 
                    win = bet * 10
                    print(f"🔥 JACKPOT! Triple 7! You win {win} coins!")
                    coins += win
                elif spin[0] == "🎲" :
                    win = bet * 20
                    print(f"💥 MEGA WIN! Triple Wilds! You win {win} coins!")
                    coins += win

                else:
                    win = bet * 5
                    print(f"💎 Triple match! You win {win} coins!")
                    coins += win

            elif spin[0] == spin[1] or spin[1] == spin[2] or spin[0] == spin[2]:
                win = bet * 2
                print(f"⭐ Two match! You win {win}!")
                coins += win
            else:
                print("🍋 Not lucky this time.")
            
            net = win - bet
            if net > 0 :
                print("You Won:", net , "coins this spin!")
            elif net < 0 :
                print("You Lost:", abs(net), "coins this spin!")
            else:
                print("No win or loss this spin.")

            print(f"Coins left: {coins} | Free spins: {free_spins}")


        elif play.lower() == "q" :
            break
        else : 
            print("⚠️  Invalid Input . Press Enter to spin or 'q' to quit !")

    print(f"Total coins: {coins}")
    print(pyfiglet.figlet_format("Game Over !"))






# packaging tool
def FitBox():
    title = pyfiglet.figlet_format("Fit"+" ->" +"Box")
    print(title)
    
    # get the user's inputs
       # get the number of items
    while True:
        try:
            n = int(input("Enter the total number of items to package: "))
            if n <= 0 :
                print("⚠️ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid Input. please enter an integer")
        
    # get the package sizes
    while True:
        try:
            sizes_input = input("Enter package sizes ( comma-separated, e.g. 3,5,8): ")
            sizes = [int(x.strip()) for x in sizes_input.split(",")]
            
            if any(s <= 0 or s > n for s in sizes):
                print("⚠️ All box sizes must be positive integers <= total items.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid Input.")
    

    def packaging(n, sizes):
        """ Inner helper : compute best packaging plan using DP . """
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        choice = [-1]*(n + 1)

        for i in range(1, n+1):
            for s in sizes:
                if i -s >= 0 and dp[i-s] + 1 < dp[i]:
                    dp[i] = dp[i - s] + 1
                    choice[i] = s
        
        # Find the best achievable <= n
        best = max(i for i in range(n + 1) if dp[i] != float('inf'))

        result = {}
        curr = best
        while curr > 0:
            s = choice[curr]
            result[s] = result.get(s, 0) + 1
            curr -=s

        return result, n - best # leftover

    result, leftover = packaging(n, sizes)

    print("\n Best packaging plan: ")
    for size, count in result.items():
        print(f"{count} boxes of size {size}")

    if leftover == 0:
        print("Perfect fit! No leftover items")

    else: 
        print(f"Leftover items: {leftover}")



if __name__ == "__main__":
    main()