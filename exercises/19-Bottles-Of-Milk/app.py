# Your code here!
def number_of_bottles():
    for x in range(99,2,-1):
        print(str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk. Take one down and pass it around, " + str(x-1)+ " bottles of milk on the wall.")
    print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
    print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
    return None

number_of_bottles()

# #my answer
# def number_of_bottles():
#     for i in range (99, 0, -1):        
#         if i <= 99 and i > 2:
#             print(f"{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i-1} bottles of milk on the wall.")
#         elif i == 2:
#             print(f"2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")    
#         else:
#              print(f"1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall. \nNo more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")



# number_of_bottles()