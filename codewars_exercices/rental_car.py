
'''
After a hard quarter in the office you decide to get some rest on a vacation. 
So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. 
The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. 
If you rent the car for 7 or more days, 
you get $50 off your total. 

Alternatively, if you rent the car for 3 or more days, 
you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''

def rental_car_cost(days):
    price_per_day = 40
    total_price = price_per_day * days

    if days >= 7:
        total_price -= 50

    elif days >= 3:
        total_price -= 20

    return total_price   

#TESTS

# should return 400 - 50 = 350
# if condition
print(rental_car_cost(10))

# should return 200 - 20 = 180
# elif condition
print(rental_car_cost(5))

# should return 80
print(rental_car_cost(2))



rental_car_cost(10)