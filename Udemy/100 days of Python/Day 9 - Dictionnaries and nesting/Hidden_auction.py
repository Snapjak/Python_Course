import os
os.system('clear')

import art
print(art.logo)

bids = {}
end_game = False

def make_dic(bidder, price):
    bids[bidder] = price

while end_game ==  False:
  name = input("Please insert your name: ")
  bid_price = int(input("Please insert your bid price: "))
  make_dic(bidder = name, price = bid_price)
  others = input("Anyone else wants to make a bid? 'Yes' or 'No'").lower()
  if others == "no":
    end_game = True
    max = 0
    for key in bids:
      if bids[key] > max:
        max = bids[key]
    print(f"The highest bid is for {name} with a bid price of {bid_price}$")
  elif others == "yes":
    clear = lambda: os.system('clear')
    clear()
    end_game = False

  