print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\.
                         `'-------'`
                       .-------------.
                      /_______________\ """)
print("Welcome to silence biding program!")

def get_bidder_info():
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    bidder = {
        "name":name,
        "bid":bid
    }
    return bidder

bidders = []

def winner(bidders):
    highest_bidder = max(bidders, key=lambda x: x['bid'])
    print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}")

while True:
    bidder = get_bidder_info()
    bidders.append(bidder)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if more_bidders == "no":
        winner(bidders)
        break

        



