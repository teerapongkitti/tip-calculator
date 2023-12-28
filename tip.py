# .2f in tip means format the tips to 2 decimal
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# take str input, remove $ and convert into float
def dollars_to_float(d):
    remove_dollars_sign = d.replace("$", "")
    return float(remove_dollars_sign)

# take str input, remove %, convert to float and divided by 100
def percent_to_float(p):
    remove_percent_sign = p.replace("%", "")
    percent_converted = float(remove_percent_sign) / 100
    return percent_converted

main()
