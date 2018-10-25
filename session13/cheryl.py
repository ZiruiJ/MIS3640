# city = input('please enter a city: ')

# def plane_ride_cost(city):
#     if str(city) == 'Charlotte' :
#         return 183
#     elif str(city) == 'Tampa' :
#         return 220
#     elif  str(city) == 'Pittsburgh':
#         return 222
#     else:
#         return 475

# print (plane_ride_cost('Charlotte'))


city = input("Enter city name: ")
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 'not valid'
print (plane_ride_cost(city))