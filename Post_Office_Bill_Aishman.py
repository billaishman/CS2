#Name: Bill Aishman
#Description: This code decides how much a package is worth depending on the size and distance the item going. 
#Bugs: 
#Features:
#Log: 1.0
"""
Sample input            Expected output
4,4,0.009,02893,08516   .23
5,7,0.013,07245,45216   .43
5,7,0.2,45216,07245     .45
10,12,0.4,15623,89175   .8
10,12,30,21505,72400    4.65
"""
def main():
    """
    Takes in user input data and assigns it to various variables
    Args: 
        height : the height of the package
        length : the length of the package
        thickness : the thickness of the package
        zipzonefrom : the begining zipcode
        zipzoneto : the ending zipcode
    Returns:
        prints : the mailtype based on the dimensions
        prints : the starting zipcode
        prints : ending zipcode
        prints : cost to send
    """
#Checks to make sure user input is 5 comma values
    while True:
        while True:
            data = input("Enter the data: ")
            dimensions = data.split(",")
            if len(dimensions) != 5:
                print("Need five pieces of data")
            else:
                break
#checks to see if the user data is 3 floats and two integers
        try:
            height = float(dimensions[1])
            length = float(dimensions[0])
            thickness = float(dimensions[2])
            zip_zone_from = (int(dimensions[3]))
            zip_zone_to = (int(dimensions[4]))
        except ValueError:
            print("Please enter three floats and two integers")
        else:
            break
    mailtype = gettype(length, height, thickness)
    zip_code_from = get_zip_zone_from(zip_zone_from)
    zip_code_to = get_zip_zone_to(zip_zone_to)
    getcost(mailtype, zip_code_from, zip_code_to)
    print ("")
    main()
def get_zip_zone_to(zip_zone_to):
    """
    Assigns a number value to each of the zipcodes
    1-6999 is assigned the value 1
    7000-19999 is assigned the value 2
    20000-35999 is assigned the value 3
    36000-62999 is assigned the value 4
    63000-84999 is assigned the value 5
    85000-99999 is assigned the value 6
    Args: 
        zipzoneto (int) : the starting zipcode
    Returns:
        A number based on the starting zipcode
    """
    if zip_zone_to >= 1 and zip_zone_to <= 6999:
        return 1
    elif zip_zone_to >= 7000 and zip_zone_to <= 19999:
        return 2
    elif zip_zone_to >= 20000 and zip_zone_to <= 35999:
        return 3
    elif zip_zone_to >= 36000 and zip_zone_to <= 62999:
        return 4
    elif zip_zone_to >= 63000 and zip_zone_to <= 84999:
        return 5
    elif zip_zone_to >= 85000 and zip_zone_to <= 99999:
        return 6
def get_zip_zone_from(zip_zone_from):
    """
    Assigns a number value to each of the zipcodes
    1-6999 is assigned the value 1
    7000-19999 is assigned the value 2
    20000-35999 is assigned the value 3
    36000-62999 is assigned the value 4
    63000-84999 is assigned the value 5
    85000-99999 is assigned the value 6
    Args:
        zipzonefrom (int) : the ending zipcode
    Returns:
        A number based on the ending zipcode
    """
    if zip_zone_from >= 1 and zip_zone_from <= 6999:
        return 1
    elif zip_zone_from >= 7000 and zip_zone_from <= 19999:
        return 2
    elif zip_zone_from >= 20000 and zip_zone_from <= 35999:
        return 3
    elif zip_zone_from >= 36000 and zip_zone_from <= 62999:
        return 4
    elif zip_zone_from >= 63000 and zip_zone_from <= 84999:
        return 5
    elif zip_zone_from >= 85000 and zip_zone_from <= 99999:
        return 6
def gettype(length, height, thickness):
    """
    Returns one of seven mailtypes given the user data.
    Args:
        length (int) : the length
        height (int) : the height
        thickness (int) : the thickness
    postcard : (3.5 < length < 4.25) and (3.5  < height < 6) and (0.007 < thickness < 0.016)
    largepostcard  : (4.25 < length < 6) and (6  < height < 11) and (0.007 < thickness < 0.015)
    envelope  : (3.5 < length < 6.125) and (5  < height < 11) and (0.016 < thickness < 0.25)
    large envelope  : (6.125 < length < 24) and (11  < height < 18) and (0.25 < thickness < 0.5)
    package  : (24 < length) or (18  < height) or (0.5 < thickness ) and (length + height*2 + thickness*2 <= 84 )
    large package  : (length + height*2 + thickness*2 >= 84 ) and (length + height*2 + thickness*2 <= 130 )
    or it is unmailable
    Returns:
        one of three mailtypes (char): postcard, largepostcard, envelope, large envelope, package, large package, unmailable
    """
    if length >= 3.25 and length <= 4.25 and height >= 3.5 and height <= 6.0 and thickness >= .007 and thickness <= .016:
        return "postcard"
    elif length > 4.25 and length < 6.0 and height > 6.0 and height < 11.5 and thickness >= .007 and thickness <= .015:
        return "large postcard"
    elif length >= 3.5 and length <= 6.125 and height >= 5.0 and height <= 11.5 and thickness > .016 and thickness < .25:
        return "envelope"
    elif length > 6.125 and length < 24.0 and height >= 11.0 and height <= 18.0 and thickness >= .25 and thickness <= .5:
        return "large envelope"
    elif length > 24.0 and height > 18.0 and thickness > .5 and length + height *2 + thickness*2 < 84.0:
        return "package"
    elif length + height *2 + thickness*2 > 84.0 and length + height *2 + thickness*2 < 130.0:
        return "large package"
    elif length + height *2 + thickness*2 > 130.0:
        return "unmailable"
    elif length < 3.5 or height < 3.5 or thickness < 0.007:
        return "unmailable"
def getcost(mailtype, zip_code_from, zip_code_to):
    """
    Takes the mailtype and how far the item traveled to determine price
    Postcard : .20 + .03 (distance traveled)
    Large Postcard : .37 + .03 (distance traveled)
    Envelope : .37 + .04 (distance traveled)
    Large envelope : .60 + .05 (distance traveled)
    Package : 2.95 + .25 (distance traveled)
    Large Package : 3.95 + .35 (distance traveled)
    Args:
        mailtype (char) : The mail type
        zipcodefrom (int) : The number assigned to the starting zipcode
        zipcodeto (int) : The number assigned to the ending zipcode
    Returns:
        print total(int)
    """
    if mailtype == "postcard":
        total = (.20 + .03* abs(zip_code_to - zip_code_from))
        print(total)
    elif mailtype == "large postcard": 
        total = (.37 + .03* abs(zip_code_to - zip_code_from))
        print(total)
    elif mailtype == "envelope": 
        total = (.37 + .04* abs(zip_code_to - zip_code_from))
        print(total)
    elif mailtype == "large envelope": 
        total = (.60 + .05* abs(zip_code_to - zip_code_from))
        print(total)
    elif mailtype == "package":
        total = (2.95 + .25* abs(zip_code_to - zip_code_from))
        print(total)
    elif mailtype == "large package": 
        total = (3.95 + .35* abs(zip_code_to - zip_code_from)) 
        print(total)
    elif mailtype == "unmailable": 
        print("Unmailable")
main()
