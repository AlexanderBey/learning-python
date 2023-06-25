def century(year):
    if year % 100 == 0:
        return year // 100
    else: 
        return year // 100 + 1
    
print(century(1705))
print(century(1900))

