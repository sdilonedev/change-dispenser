def give_change(amount, denominations):
  change = {}
  for denom in sorted(denominations.keys(), reverse=True):
    if amount >= denom:
      total = min(amount // denom, denominations[denom])
      if total > 0:
        change[denom] = total
        amount -= denom * total
        denominations[denom] -= total
    if amount == 0:
      break
  return change, amount

def main():
  denominations = {1000: 2, 500: 4, 200: 8, 100: 10, 50: 20, 25: 30, 10: 40, 5: 50, 1: 200 }

  change = int(input("Enter the amount of change to give: "))
  
  change, remaining = give_change(change, denominations)

  if remaining == 0:
    print("Change given:")
    for denom in change:
      print(f"{change[denom]} x ${denom}")
  else:
    print("Sorry, exact change cannot be given.")
    for denom in denominations:
      print(f"Remaining {denom}s: {denominations[denom]}")
    print(f"Remaining change: {remaining}")

if __name__ == "__main__":
  main()  