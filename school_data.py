# school_data.py
# ARYAN KARADIA, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here

data_18_19 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)

data_19_20 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)

data_20_21 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)

schl_dict = {
'Centennial High School':                   '1224',
'Robert Thirsk School':                     '1679',
'Louise Dean School':                       '9626',
'Queen Elizabeth High School':              '9806',
'Forest Lawn High School':                  '9813',
'Crescent Heights High School':             '9815',
'Western Canada High School':               '9816',
'Central Memorial High School':             '9823',
'James Fowler High School':                 '9825',
'Ernest Manning High School':               '9826',
'William Aberhart High School':             '9829',
'National Sport School':                    '9830',
'Henry Wise Wood High School':              '9836',
'Bowness High School':                      '9847',
'Lord Beaverbrook High School':             '9850',
'Jack James High School':                   '9856',
'Sir Winston Churchill High School':        '9857',
'Dr. E. P. Scarlett High School':           '9858',
'John G Diefenbaker High School':           '9860',
'Lester B. Pearson High School':            '9865'	    
}

code_list = [
'1224',
'1679',
'9626',
'9806',
'9813',
'9815',
'9816',
'9823',
'9825',
'9826',
'9829',
'9830',
'9836',
'9847',
'9850',
'9856',
'9857',
'9858',
'9860',
'9865'
]

# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    print('Array data for 2020 - 2021:')
    print(data_20_21)

    print('Array data for 2019 - 2020:')
    print(data_19_20)

    print('Array data for 2018 - 2019:')
    print(data_18_19)


    # Add request for user input here

    while (1):
        ''' Asks for user input and checks if it is school dictionary or school code list. 
            Breaks loop if true, else aks user for another input.
        
        '''
        usr_input = str(input('Enter school name or school code: '))
        if usr_input in schl_dict or usr_input in code_list:
            break
        else:
            print('You must enter a valid school name or code.')

    # Print school name and code using the given class

    if usr_input in schl_dict.keys():
        ''' If user inputs school name, check the school dictionary to find schools code. 
        
        '''
        usr_school = usr_input
        usr_code = int(schl_dict[usr_school])
    else:
        usr_code = int(usr_input)
        ''' if user inputs school code, finds index of school code position.
            Goes through list of school names and finds user school at same index.
        
        '''
        usr_school_pos = code_list.index(usr_input)
        schl_list = list(schl_dict.keys())
        usr_school = schl_list[usr_school_pos]
    
    print("\n***Requested School Statistics***\n")

    School.print_all_stats(School(usr_school, usr_code))

    # Add data processing and plotting here

    schl_index = 0
    
    for i in range(len(code_list)):
        ''' Goes through code list to find index of users code.
        
        '''
        if code_list[i] == str(usr_code):
            schl_index = i
            break
    
    grade_10 = (data_18_19[schl_index][1] + data_19_20[schl_index][1] + data_20_21[schl_index][1])//3
    ''' in data set finds number of students for that school over the 3 year period and finds mean.
        Same process for all 3 years.
    
    '''
    
    print(f'Mean enrollment for Grade 10 across all years: {grade_10:.0f}')

    grade_11 = (data_18_19[schl_index][2] + data_19_20[schl_index][2] + data_20_21[schl_index][2])//3

    print(f'Mean enrollment for Grade 11 across all years: {grade_11:.0f}')

    grade_12 = (data_18_19[schl_index][3] + data_19_20[schl_index][3] + data_20_21[schl_index][3])//3

    print(f'Mean enrollment for Grade 12 across all years: {grade_12:.0f}')

    graduated_students = data_18_19[schl_index][3] + data_19_20[schl_index][3] + data_20_21[schl_index][3]

    print(f'Total number of students who graduated from 2019-2021: {graduated_students:.0f}')

    def y_values(index_schl, year):
        ''' A function that returns a list of all mean y values in the graph.
        
        parameters: school index, year
        return: list of mean values at that year
            
        '''
        index_schl = schl_index
        mean_list = []
        if year == 2019:
            mean_10 = data_18_19[index_schl][1]
            mean_20 = data_18_19[index_schl][2]
            mean_30 = data_18_19[index_schl][3]
        elif year == 2020:
            mean_10 = data_19_20[index_schl][1]
            mean_20 = data_19_20[index_schl][2]
            mean_30 = data_19_20[index_schl][3]
        else:
            mean_10 = data_20_21[index_schl][1]
            mean_20 = data_20_21[index_schl][3]
            mean_30 = data_20_21[index_schl][3]
        mean_list.append(mean_10)
        mean_list.append(mean_20)
        mean_list.append(mean_30)
        return mean_list

    grades = list(range(10, 13))
    mean_2019 = y_values(schl_index, 2019)
    mean_2020 = y_values(schl_index, 2020)
    mean_2021 = y_values(schl_index, 2021)

    ''' creates graph with mean points, labelled axis, title, and legend location.
    
    '''
    plt.figure()
    plt.plot(grades, mean_2019, 'ro', label = '2019 Enrollment')
    plt.plot(grades, mean_2020, 'go', label = '2020 Enrollment')
    plt.plot(grades, mean_2021, 'bo', label = '2021 Enrollment')
    plt.xticks(grades)
    plt.xlabel('Grade Level')
    plt.ylabel('Number of Students')
    plt.title('Grade Enrollment by Year')
    plt.legend(loc = 'upper left')
    plt.show()


# Do not modify the code below
if __name__ == '__main__':
    main()

