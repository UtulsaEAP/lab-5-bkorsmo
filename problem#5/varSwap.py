'''
Name: Brady Korsmo
Date: Thursday @2
'''


def swap_values(user_input1, user_input2, user_input3, user_input4):   
   #write your code here
   one = user_input1
   two = user_input3
   user_input1 == user_input2
   user_input2 == one
   user_input3 == user_input4
   user_input4 == two
   
   
   return user_input2, user_input1, user_input4, user_input3

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   #print those output
   new = swap_values(user_input1, user_input2, user_input3, user_input4)
   print(*new)
   

 