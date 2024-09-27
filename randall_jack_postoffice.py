'''
Name: Jack Randall
Description: A program that takes the dimensions of a package and the zip codes where the package is coming from/going to, and calculates the price of the shipment.
Log: v1.0, initial version
Bugs: None
Features: None
Sources: Mr. Campbell, Oliver Servidio
'''

def get_type(lth, ht, wth):
    '''
    Takes the dimensions inputted by the user and determines what type of package it is based on the length, height, and thickness

    Args: 
        float: the length, height, and thickness of the package
    Returns:
        str: the type of package it is
    Raises:
        valueError: when the dimensions do not meet the requirements to be identified as any one of these package types, then specify the package as unmailable
    '''
    if 3.5 <= lth <= 4.25 and 3.5 <= ht <= 6 and .007 <= wth <= .016:
        pkg_type = 'pc'
    elif 4.25 <= lth <= 6 and 6 <= ht <= 11.5 and .007 <= wth <= .015:
        pkg_type = 'large_pc'
    elif 3.5 <= lth <= 6.125 and 5 <= ht <= 11.5 and .016 <= wth <= .25:
        pkg_type = 'env'
    elif 6.125 <= lth <= 24 and 11 <= ht <= 18 and .25 <= wth <= .5:
        pkg_type = 'large_env'
    elif 42.5 <= lth + 2*ht + 2*wth <= 84:
        pkg_type = 'pkg'
    elif 84 < lth + 2*ht + 2*wth <= 130:
        pkg_type = 'large_pkg'
    else:
        pkg_type = 'unmailable'
        print('Unmailable')
        exit()
    return pkg_type
def get_distance(out, to, cost):
    '''
    Takes the zip codes inputted by the user and determines the amount of zones being travelled across, while also determining the price of the shipment through its type

    Args:
        int: zip codes where the package is coming from and going to
        str: the type of package the shipment is
    Returns:
        float: the price of the shipment
    Raises:
        valueError: when the zip code out and zip code to inputted do not exist, then inform the user
    '''
    # determines the zone of the zip code from inputted
    if 1 <= out <= 6999:
        out_code = 1
    elif 7000 <= out <= 19999:
        out_code = 2
    elif 20000 <= out <= 35999:
        out_code = 3
    elif 36000 <= out <= 62999:
        out_code = 4
    elif 63000 <= out <= 84999:
        out_code = 5
    elif 85000 <= out <= 99999:
        out_code = 6
    else:
        print('Not a real zone')
        exit()
    
    # determines the zone of the zip code to inputted
    if 1 <= to <= 6999:
        to_code = 1
    elif 7000 <= to <= 19999:
        to_code = 2
    elif 20000 <= to <= 35999:
        to_code = 3
    elif 36000 <= to <= 62999:
        to_code = 4
    elif 63000 <= to <= 84999:
        to_code = 5
    elif 85000 <= to <= 99999:
        to_code = 6
    else:
        print('Not a real zone')
        exit()
    
    # calculates the number of zones the shipment is travelling through and sets a new variable to 0
    difference = abs(out_code - to_code)
    full_cost = 0

    # calculates the cost of the shipment by adding the cost of the package to the amount of zones being traveled multiplied by the cost per zone
    if cost == 'pc':
        full_cost = 0.2 + difference*0.03
    elif cost == 'large_pc':
        full_cost = 0.37 + difference*0.03
    elif cost == 'env':
        full_cost = 0.37 + difference*0.04
    elif cost == 'large_env':
        full_cost = 0.6 + difference*0.05
    elif cost == 'pkg':
        full_cost = 2.95 + difference*0.25
    elif cost == 'large_pkg':
        full_cost = 3.95 + difference*0.35
    return full_cost
def main():
    '''
    Takes in the user's inputted information and runs the functions that determine the type, zones, and cost of the shipment, then gives the user's final price

    Args:
        list: the information inputted by the user, such as length, height, thickness, zip code from, and zip code to
    Returns:
        str: the final cost of the user's shipment
    Raises:
        valueError: if the user has too many or too little inputs, no commas, or their input cannot be classified, inform the user their input is not accepted
    '''
    # give the user an input to enter their information, then delete the commas in betwee the inputs
    info = input('Please enter your package information in the order of length(in), height(in), thickness(in), zip code from, zip code to: ').split(',')
    # if the user doesn't have exactly 5 inputs, inform the user and exit the program
    if len(info) != 5:                                                                                                                                   
        print('Too many inputs, too little inputs, or no commas, please remember to have exactly 5 of inputs seperated by commas')
        exit()
    # try running the type and distance functions and making them equal the final_type and final_cost variables
    try:                                                                                
        final_type = get_type(float(info[0]), float(info[1]), float(info[2]))           
        final_cost = get_distance(int(info[3]), int(info[4]), final_type) 
    # if the try does not run, inform the user and exit the program              
    except:                                                                             
        print('We cannot mail that item, make sure you are typing floats or integers')  
        exit()                                                                          

    end_price = (((str(final_cost)).strip('0')).split('.'))  # make the end_price variable equal a string of the final cost, and remove the zeros in the cost, and split the remaining numbers into a list 

    while len(end_price[1]) <= 1:                            # when the number with the index 1 in the end_price list is less than one
        end_price[1] += '0'                                  # add a zero to the number with the index 1
   
    end_price = '.'.join(end_price)                          # make end_price join back into one variable with a period
    print(end_price)                                         # print the final end_price variable
main()                                                       # run the main function