# importing packages
import simpy
import pandas as pd
import os
import sys
sys.path.insert(1, 'H:/My Drive/Thesis/Simulation/customSim')

# import local defined functions 
from PPR import PPRClasses
from PPR.PPRClasses import *
from PPR.Functions import *

'''
This script generates the excel file for giving in the data or uses the data in existing file for generating objects.

Steps for modelling the domains:
- Step 1: Population of all the classes of the domain which can form objects
- Step 2: Generation of attributes defined in the class in the constructor function
- Step 3: check for the availability of a dataframe(df) for the definition of objects.
- Step 4: Create an object for each row of the dataframe.
- Step 5: Create an empty excel sheet if the required df is not available, with class attributes as columns.
- Step 6: Add new columns, if the df misses some attributes of the class.

Notes:
- By default, the dataframes are considered to be in .xlsx format. Please Check "file_path" variable in the domain to modify the file format.
- Please refer the datatypes of all the attributes before modelling the production system in the sheet.
- Validation of value for attributes is not modelled, which can be addded as extension in future versions.
- Additional attributes for the object can be given in kwargs which will be converted to attributes by a function.
'''

env = simpy.Environment()
# Specification of path for the directories of product, process and resources 
directory_path = '../customSim/LES/systemDefinition'

# -------------Modelling the Product domain-------------
domain_classes = get_classes(PPRClasses) # generating classes available in the product domain

for domain_class in domain_classes: # iterating through each of the classes

    object_list  = []

    file_path = os.path.join(directory_path, f'{domain_class.__name__}.xlsx') # file path of excel sheet for the given class

    attribute_list = domain_class(env).attributes # list of atributes of a class
    
    if os.path.isfile(file_path):  # if sheet exists at given path
        class_df = pd.read_excel(file_path, usecols=lambda x: 'Unnamed' not in x) # import excel sheet as a pandas dataframe

        for attribute in attribute_list: # iterating through attributes of the class and add missing columns corresponding to attributes

            if attribute not in class_df.columns:
                new_column = pd.Series(name=attribute, dtype=object)  # Create a new column with the required name
                class_df = pd.concat((class_df, new_column), axis=1) # adding attributes as index in the dataframe

                with pd.ExcelWriter(file_path, engine='openpyxl') as writer:  # Replacing the excel sheet with updated dataframe            
                    class_df.to_excel(writer, sheet_name=f'{domain_class.__name__}', index=True)
        
        # Creating instances of the object
        for index, row in class_df.iterrows():
            # Create an instance of the class dynamically based on class name
            class_instance = domain_class(env)  

            for col_name, value in row.items():  # Iterate through each column of the DataFrame 
                if col_name != 'kwargs':
                    if hasattr(class_instance, col_name):  # Check if the attribute exists in the class

                        setattr(class_instance, col_name, value) # Set the attribute value in the class instance

                    else:
                        setattr(class_instance, col_name, value)
                        print(f'new attribute:{col_name} is added to an instance of {domain_class}')
    
            object_list.append(class_instance)  # Adding the object to object list

            print(f"Instance of {domain_class}: {class_instance.__dict__}")
           

    else:
        new_df = pd.DataFrame({})  # create an empty pandas dataframe
        
        for attribute in attribute_list:
                new_df[f'{attribute}'] = [] # adding attributes as index in the dataframe

                with pd.ExcelWriter(file_path, engine='openpyxl') as writer: # Replacing the excel sheet with updated dataframe 
                    new_df.to_excel(writer, sheet_name=f'{domain_class.__name__}', index=True)

        print(f'Added the sheet: {domain_class.__name__}. Please update the sheet for added functionality')



