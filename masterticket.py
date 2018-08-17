TICKET_PRICE = 10
SERVICE_FEE = 5

tickets_remaining = 100  

def calc_price(num):
    return (TICKET_PRICE * num) + SERVICE_FEE

while tickets_remaining:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?  ")
    num_tickets = input("Hello {}, how many tickets would you like?  ".format(name))
    try:
        if not num_tickets.isdigit():
            raise ValueError("That's not a number!")
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("We only have {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! There was a problem! {} Please try again!".format(err))
    else:
        price = calc_price(num_tickets)
        print("That will be ${} for {} tickets with a ${} service fee".format(price, num_tickets, SERVICE_FEE))
        proceed = input("Would you like to proceed {}?  ".format(name))
        if proceed.lower() == "y":
            print("SOLD!")
            #TODO: CC/bitcoin info
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print("Sorry, there are no tickets remaining :(")