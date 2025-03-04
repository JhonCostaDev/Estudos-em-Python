#%%

def int_to_binary(number:int) -> int:
    """This function convert a integer in a binary number."""
    binary = '' # To store the mod of division
    
    if number == 0: #Verify if the number is zero
        return 0
    else:   # If the number is not zero
        while number > 0:       # loop while number bigger than zero
            binary += str(number % 2) # Calculate mod and asign the result in the binary string
            number //=  2 # floor division


    result = int(binary[::-1]) #invert the string to the correct order, converto to a integer and asign in result variable.
    return result
# %%

int_to_binary(1029)
# %%
