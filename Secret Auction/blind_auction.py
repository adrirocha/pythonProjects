bids = {}
keep = True

def find_highest_bidder(bidding_dictionary):
    maxValue = 0
    winner = ""
    for key, value in bidding_dictionary.items():
        if value > maxValue:
            maxValue = value
            winner = key
    return winner, maxValue

while keep:
    name = input("What is your name?: ").capitalize()
    price = float(input("What is your bind? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "yes":
        print("\n" * 100)
        continue
    else:
        winner, maxValue = find_highest_bidder(bids)
        print(f"The winner is {winner}: ${maxValue}")
        keep = False


