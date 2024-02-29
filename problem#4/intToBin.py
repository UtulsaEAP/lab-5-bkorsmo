'''
Name: Brady Korsmo
Date: Thursday @2
'''



def int_to_reverse_binary(user_input):
    binary_val = ''
#write your while loop here
    while user_input > 0:
        #write your code
        new = user_input%2
        user_input = user_input//2
        binary_val += str(new)

        
    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here

    reverse_input = input_string[::-1]

    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    binary_val =0
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)