# Write a python code for converting integer values to Indian currency notations, without
# using the currency libraries
# Example:
# input: 504678
# output: 5,04,678


def convert_curr(num):
    num = str(num) #converting the integer to string for easy computation of the notation
    
    #splitting the number into 2 parts, the last 3 which is a special case and will be appended at the end.
    #the remaining numbers which has comma seperation after every 2 digit.

    last_nums = num[-3:] 
    first_nums = num[:-3]
    if len(num)<=3:
        return num #This means the number is less than 1,000
    
    res = "" #initializing an empty string
    first_nums = first_nums[::-1] #reversing the string so that we can place commas at the right place
    for i in range(len(first_nums)):
        res+=first_nums[i]

        if (i+1)%2==0 and (i+1)!=len(first_nums): #since the strings are reverse we check with i+1 and place comma after every 2 digits
            res+=','
    
    return res[::-1] + ',' + last_nums #we append the last nums to the result and return it
    # print(num)

input = 504678 #custom input test case
# input = 5046788 #custom input test case
print(convert_curr(input)) #output for the code
