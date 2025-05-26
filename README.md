# CS50P-Final-Project
# PROJECTILE MOTION
    #### Video Demo:  <https://www.youtube.com/watch?v=KTfD4r12Skk>
    #### Description:
    Let’s see what this program does:
    URL and Local Filename:
    I’ve defined two variables:
        url: Contains the URL of the file I want to download inorder to have a file that contains data. But you can change the file to the file you want.
        local_filename: Specifies the name of the local file where the downloaded data will be saved.
    urllib.request.urlretrieve(url, local_filename):
        This line of code uses the urlretrieve() function from the urllib.request module to download a file from the specified URL and save it locally.
    1.	Class Data:
        .	The Data class represents a physical motion scenario (such as projectile motion) with given initial conditions when there is no drag force.
        .	It has three instance variables:
            .	initangle: The initial angle (in degrees) at which the projectile is launched and then it’s converted to radians.
            .	initv: The initial velocity of the projectile in (m/s^2)
            .	gravity: The absolute value of acceleration due to gravity (usually 9.8 m/s² near the Earth’s surface).
        .	The constructor (__init__) initializes these variables based on the input values.
        .	The __str__ method returns a formatted string with calculated values (duration, range, and max altitude).
    2.	Method cal_t():
        .	Calculates the time of flight (duration) for the projectile.
        .	The formula used is:
            t = \frac{{2v_0 \sin(\theta)}}{g}
            where:
            .	(v_0) is the initial velocity.
            .	(\theta) is the initial angle (in radians).
            .	(g) is the absolute value of acceleration due to gravity.
    3.	Method cal_r():
        .	Calculates the range (horizontal distance traveled) by the projectile.
        .	The formula used is:
            r = \frac{{v_0^2 \sin(2\theta)}}{g}
            where the variables have the same meanings as above.
        .	Note: If the initial angle is 0 degrees (horizontal launch), the range is calculated differently (directly proportional to time of      flight) and thus the initial angle must be between zero to 90, 90 includes.
    4.	Method f(x):
        .	Represents the trajectory of the projectile (the function (y(x))).
        .	The formula used is derived from the kinematic equations of motion.
        .	It calculates the vertical position (altitude) of the projectile at a given horizontal position (x).
        .	The equation is:
            y(x) = \tan(\theta) \cdot x - \frac{{g x^2}}{{2(v_0 \cos(\theta))^2}}
    5.	Method max_altitude():
        .	Calculates the maximum altitude reached by the projectile.
        .	It uses the f(x) function to find the altitude at the half-range point (i.e., (x = \frac{r}{2})).
    6.	Function main():
        .	The main entry point of the program.
        .	Reads input (either a CSV file or direct data) and processes it.
        .	Calls other functions (check_input, single, read_data, and output_of_data) based on the input type.
    7.	Function check_input(name):
        .	Validates the input (either a CSV file name or direct data).
        .	Checks if the input is a valid CSV file or a valid comma-separated string of numbers.
        .	Returns the cleaned input or exits the program with an error message.
    8.	Function single(x):
        .	Processes the direct input (comma-separated string of numbers).
        .	Creates a Data object with the provided values.
        .	Calculates and formats the output (duration, range, and max altitude).
    9.	Function read_data(file):
        .	Reads data from a CSV file.
        .	Assumes that the CSV file has columns named “initangle,” “initv,” and “gravity.”
        .	Returns a list of lists, where each inner list contains the data for one row.
    10.	Function output_of_data(data):
        .	Writes the calculated data (duration, range, and max altitude) to an output CSV file named “output.csv.”
        .	The file format includes a header row with column names.
    In summary, this program models projectile motion based on initial conditions (angle, velocity, and gravity), calculates relevant quantities, and either prints the results directly or writes them to a CSV file. The Data class encapsulates the physics calculations, and the other functions handle input validation and file I/O.

