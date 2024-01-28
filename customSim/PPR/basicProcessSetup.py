import simpy
import pandas as pd
import sys
sys.path.insert(1, 'H:/My Drive/Thesis/Simulation/customSim')

from PPR.PPRClasses import *
from Functions import *
import utils

# Process Map Explanation
'''
- `process_map` is a nested list representing processes modeled on the main branch as objects and sub-processes modeled as dictionaries with keys as part of the spine.
- Resources such as buffers can be added to the process flow model, to which upstream and downstream processes are generated during runtime.
- Processes serve as a pivot connecting resources and products, hence being simulated.
'''

env = simpy.Environment()

# Generating Domains
domains = get_classes(PPRClasses) # Domains defined as classes in PPRClasses

# Directory Path for Definitions
directory_path = '../customSim/LES/systemDefinition'

# Model Domain Objects
for domain in domains:
    domain.object_list = model_domain(env, domain, directory_path) # Defines objects based on attributes defined in the Excel sheet

# Consolidating Object List
object_list = Product.object_list + Process.object_list + Resource.object_list

# Generating Process Flow Model
process_flow_model = make_process_flow_model(domains) # Generates process flow model as a string

# Mapping Processes
map_processes(process_flow_model, domains) # Generates upstream and downstream processes based on process flow model
