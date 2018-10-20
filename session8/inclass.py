# print ('bananas',   chr (36), 52) 
# print ('rice',  chr (36), 35)
# print ('paprika',   chr (36), 72)
# print ('potato chips',  chr (36), 78)
# print ('-------------')
# print ('total', chr (36), 237)

for line in [['bananas',chr (36), 52.00], ['rice',chr(36), 35.00],['paprika', chr(36), 72.00], ['potato chips', chr (36), 78.00], ['total', chr(36), 237.00]]:
    print('{:<20} {:<2} {:<20.2f} '.format(*line))


# for line in [['bananas',chr (36), 52.00], ['rice',chr(36), 35.00],['paprika', chr(36), 72.00],  ['total', chr(36), 237.00]]:
#     print('{:<20} {:<2} {:<20.2f} '.format(*line))