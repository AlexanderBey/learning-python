def positive_sum(list_of_numbers):
    positive_list_of_numbers = []

    for number in list_of_numbers:
        if number > 0:
            positive_list_of_numbers.append(number)

    if len(positive_list_of_numbers) > 0:
        return sum(positive_list_of_numbers)
    else:
        return 0


print(positive_sum([1,-2,-3,4,5]))
