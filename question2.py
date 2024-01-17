#Question 2 
#Gi-hun and ali 
#3
#4 10
#2 13 4 16
#5 8
#9 3 8 8 4
#4 6
#1 2 3 4
def num_player_shot(n, h, list_players):
    
    res = 0
    for i in list_players:
        if i>h:
            res+=1
    if n<res:
        return "Error"
    return res

# x = [4,10]
# y = [2,13,4,16]
# print(num_player_shot(x,y))
res_list = []
#Created a new input file so that it is easier to change any input with ease.
with open('q2_input.txt', 'r') as file:
    lines = file.readlines()

# The first line contains the number of test cases
num_test_cases = int(lines[0].strip())

# Start reading the test cases from the second line
line_index = 1
for _ in range(num_test_cases):
    # Read number of players between and height of both of them from the line
    n, h = map(int, lines[line_index].strip().split())
    line_index += 1

    # Read the list of players heights from the next line
    list_players = list(map(int, lines[line_index].strip().split()))
    line_index += 1

    # Call the function on them
    res_list.append(num_player_shot(n, h, list_players)) #storing the res in a list to be printed together later

for i in res_list:
    print(i) #printing the list of outputs together as per the requirement mentioned in the document
