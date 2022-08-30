### ARYAN KARADIA, ADITYA PRASAD, ENDG 233 Final Project

import numpy as np
import matplotlib.pyplot as plt

class Country:

    def __init__(self, name, continent, sub_region, sq_km):
        self.name = name
        self.continent = continent
        self.sub_region = sub_region
        self.sq_km = sq_km
    
    def all_info(self):
        print(f'\n{self.name} resides in {self.continent}, more specifically in {self.sub_region}. {self.name} has an area of {self.sq_km} square Km.\n')

def index_finder(wanted_country, from_list):
     needed_index = 0
     for i in range(len(from_list)):
         if from_list[i] == wanted_country:
             needed_index = i
             return needed_index



        
countries = np.genfromtxt('Country_data.csv', delimiter=',', skip_header = True, dtype = str)
population = np.genfromtxt('Population_data.csv', delimiter=',', skip_header = True, dtype = np.int64) ### Changed dtype for runtimewarning "overflow encountered in long_scalars" https://stackoverflow.com/questions/7559595/python-runtimewarning-overflow-encountered-in-long-scalars
threatened = np.genfromtxt('Threatened_Species.csv', delimiter=',', skip_header = True, dtype = int)

country_list = countries[:,0]

def main():

    print('\n***ENDG 233 Country Information Program***\n')
    while(1):
        
        usr_country = str(input('Enter Country (First letter must be capitalized): '))
        if usr_country in country_list:
            break
        else:
            print('Please enter a valid country.')
    
    usr_index = index_finder(usr_country, country_list)
        
    usr_continent = countries[usr_index][1]
    usr_sub_region = countries[usr_index][2]
    usr_sq_km = countries[usr_index][3]

    usr_info = Country(usr_country, usr_continent, usr_sub_region, usr_sq_km)
    Country.all_info(usr_info)

    while(1):
        usr_stats = str(input('| (1) Popluation Statistics              |\n| (2) Endangered Animals statistics      |\n| (3) Exit Program                       |\n'))

        if usr_stats == '3':
            print("\nThank you for using our Country Information program.")
            break


        while usr_stats != '3':
                if usr_stats == '1':
                    
                        print("\nThis option will allow you to see the mean population over your chosen years, the population between selected years on a graph, as well as the years with the minimum and maximum populations.\n")
                        lwr_bound = int(input('Please input minimum year: '))
                        uppr_bound = int(input('Please input maximum year: '))

                        lwr_index = lwr_bound - 2000 + 1
                        uppr_index = uppr_bound - 2000 + 1
                            
                        pop_row = population[usr_index][lwr_index:uppr_index + 1]

                        pop_mean = sum(pop_row) // len(pop_row)

                        print(f'\nThe mean population for {usr_country} from {lwr_bound} to {uppr_bound} is: {pop_mean} people\n')

                        max_row = population[usr_index][1:]
                        max_pop = max(max_row)
                        year = 0

                        for i in range(len(max_row)):
                            if max_row[i] == max_pop:
                                year = 2000 + i

                        print(f'\nThe maximum population for {usr_country}, was: {max_pop} people, during the year {year}\n')

                        min_row = population[usr_index][1:]
                        min_pop = min(min_row)
                        year = 0

                        for i in range(len(min_row)):
                            if min_row[i] == min_pop:
                                year = 2000 + i

                        print(f'\nThe minimum population for {usr_country}, was: {min_pop} people, during the year {year}\n')

                        ################ Graphing the Population ##########################

                        usr_input_pop_data = pop_row.tolist()

                        year = list(range(lwr_index + 2000 - 1, uppr_index + 2000))
                        
                        plt.plot(year, usr_input_pop_data, '-o', label = 'Number of Citizens')
                        plt.title(f"{usr_country}'s Population From {lwr_bound} to {uppr_bound}")
                        plt.xlabel('Years')
                        plt.ylabel('Population')
                        plt.legend (loc = 'upper left')
                        plt.xticks(year)

                        plt.show()

                        print('\nReturning to Main Menu...\n')
                        break

                elif usr_stats == '2':

                    print(f"\n This option shows you the total amount of endangered animals within {usr_country}, then graphs the total amount of each endagered animal within {usr_country}'s sub region.\n ")

                    ''' 
                    
                    Uses the csv file to find specific endangered species within user country, takes specific amount and finds sum
                        
                    '''

                    usr_species = threatened[usr_index][1:] 
                    total_animals = sum(usr_species)

                    print(f'\nThe total amount of endangered animals in {usr_country} is {total_animals}.\n')

                    sub_region_country = []

                    for i in range(len(countries)):
                        ''' 
                        
                        Creats a list of every country within the sub region of the users country.
                        
                        '''
                        if countries[usr_index][2] == countries[i][2]:
                            sub_region_country.append(countries[i][0])
                        
                    total_plant = 0
                    total_fish = 0
                    total_bird = 0
                    total_mammal = 0

                    for i in range(len(sub_region_country)):
                        '''
                        
                        For every country within the same sub-region, Finds total amount of every type of endangered species.
                        
                        '''
                        
                        country_index = index_finder(sub_region_country[i], country_list)

                        total_plant += threatened[country_index][1]
                        total_fish += threatened[country_index][2]
                        total_bird += threatened[country_index][3]
                        total_mammal += threatened[country_index][4]

                    '''
                    
                    X and Y axis' for the graph
                    
                    '''

                    sub_region_total = [total_plant, total_fish, total_bird, total_mammal] 
                    species = ['Plants', 'Fish', 'Birds', 'Mammals']

                    '''
                    
                    Creates bar graph graphing total amount of endangered species in user countries sub region
                    
                    '''

                    plt.bar(species, sub_region_total, color = 'c')
                    plt.title(f"Total Amount of Endangered Species in the Sub-Region of {countries[usr_index][2]}")
                    plt.xlabel('Species')
                    plt.ylabel('Number of Endangered Species')
                    plt.show()

                    print('\nReturning to Main Menu...\n')
                    break

                else:
                    '''
                    
                    If user's input is not recognized allows for another input from user.
                    
                    '''
                    print('Please enter a valid input.')
                    break
                

        
#No touchy touchy
if __name__ == '__main__':
    main()
