import simpy
import pandas as pd
import sys

# Add the path of customSim directory to the system path
sys.path.insert(1, 'H:/My Drive/Thesis/Simulation')

# Import necessary functions from custom package
from PPR.Functions import *

# __________ Product Domain __________

class Product:
    """
    Represents a product in the simulation model.
    """

    def __init__(self, env, id='default_id', name='default_name', type='default_type',
                 sourcing='inhouse', cost=0, features=[], skills=[], contents={},
                 dimensions={}, specifications={}):
        """
        Initializes a Product object.

        Args:
            env: SimPy Environment object.
            id: Identifier for the product.
            name: Name of the product.
            type: Type of the product (e.g., product, sub-assembly, component).
            sourcing: Sourcing strategy for the product (inhouse or outsourced).
            cost: Cost of producing the product.
            features: List of features of the product.
            skills: List of skills required for manufacturing the product.
            contents: Dictionary containing components and their quantities.
            dimensions: Dictionary containing dimensions of the product.
            specifications: Dictionary containing specifications of the product.
        """
        self.env = env
        self.id = id
        self.name = name
        self.type = type
        self.sourcing = sourcing
        self.cost = cost
        self.upstream_processes = []
        self.downstream_processes = []
        self.features = features
        self.skills = skills
        self.contents = contents if contents is not None else {}
        self.dimensions = dimensions
        self.specifications = specifications

        if self.type == 'component':
            # Create a container for components
            self.container = simpy.Container(env, capacity=5, init=5)

        # List of all attributes (excluding 'env')
        self.attributes = list(locals().keys())[1:]

    def define_processes(self, upstream_processes, downstream_processes):
        """
        Defines the upstream and downstream processes for the product.

        Args:
            upstream_processes: List of upstream processes.
            downstream_processes: List of downstream processes.
        """
        if upstream_processes:
            if isinstance(upstream_processes, list):
                for process in upstream_processes:
                    if process in self.upstream_processes:
                        print(f'{process} already exists in upstream process list')
                    else:
                        self.upstream_processes.append(process)
            else:
                raise TypeError("Invalid datatype for the upstream processes list, expected list")

        if downstream_processes:
            if isinstance(downstream_processes, list):
                for process in downstream_processes:
                    if process in self.downstream_processes:
                        print(f'{process} already exists in downstream process list')
                    else:
                        self.downstream_processes.append(process)
            else:
                raise TypeError("Invalid datatype for the downstream processes list, expected list")

    def add_feature(self, features):
        """
        Adds features to the product.

        Args:
            features: List of features to be added.
        """
        if isinstance(features, list):
            for feature in features:
                if feature in self.features:
                    print(f'{feature} already exists in the feature list')
                else:
                    self.features.append(feature)
        else:
            raise TypeError("Expecting a list for the features")

    def add_skill(self, skills):
        """
        Adds skills required for manufacturing the product.

        Args:
            skills: List of skills to be added.
        """
        if isinstance(skills, list):
            for skill in skills:
                if skill in self.skills:
                    print(f'{skill} already exists for the product')
                else:
                    self.skills.append(skill)
        else:
            raise TypeError("Invalid datatype for the skills list, expected list")

    def add_content(self, contents):
        """
        Adds components and their quantities to the product.

        Args:
            contents: Dictionary containing components and their quantities.
        """
        if isinstance(contents, dict):
            for key, value in contents.items():
                if key in self.contents:
                    ValueError(f'{key} is already defined for the product. '
                               f'Please change the part count in the product definition sheet')
                else:
                    self.contents[key] = value
        else:
            raise TypeError("Invalid datatype for the contents, expected dictionary")

    def add_dimension(self, dimensions):
        """
        Adds dimensions to the product.

        Args:
            dimensions: Dictionary containing dimensions of the product.
        """
        if isinstance(dimensions, dict):
            for key, value in dimensions.items():
                if key in self.dimensions:
                    ValueError(f'{key} is already defined for the product. '
                               f'Please change this in the product definition sheet')
                else:
                    self.dimensions[key] = value
        else:
            raise TypeError("Invalid datatype for the dimensions, expected dictionary")

    def add_specification(self, specifications):
        """
        Adds specifications to the product.

        Args:
            specifications: Dictionary containing specifications of the product.
        """
        if isinstance(specifications, dict):
            for key, value in specifications.items():
                if key in self.specifications:
                    ValueError(f'{key} is already defined for the product. '
                               f'Please change this in the product definition sheet')
                else:
                    self.specifications[key] = value
        else:
            raise TypeError("Invalid datatype for the specifications, expected dictionary")



class Order:
    """
    Represents an order in the simulation model.
    """

    def __init__(self, env, order_date='default_date', customer_name='default_name',
                 id='default_id', products={}):
        """
        Initializes an Order object.

        Args:
            env: SimPy Environment object.
            order_date: Date of the order.
            customer_name: Name of the customer.
            id: ID of the order.
            product: Dictionary of the variants ordered along with their quantities.
        """
        self.env = env
        self.order_date = order_date  # Date of the order
        self.customer_name = customer_name  # Name of the customer
        self.id = id  # ID of the order
        self.products = products  # Dictionary of the variants ordered
        # List of all attributes (excluding 'env')
        self.attributes = list(locals().keys())[1:]

# __________ Process Domain __________
class Process:
    """
    Represents a process in the simulation model.
    """

    def __init__(self, env, id='default_id', name='default_name', proc_time=0,
                 operating_cost=0, operators=0, operating_status=False,
                 upstream_processes=[], downstream_processes=[], sub_processes={},
                 skills=[], input_products={}, output_products={}, resources={}):
        """
        Initializes a Process object.

        Args:
            env: SimPy Environment object.
            id: Identifier for the process.
            name: Name of the process.
            proc_time: Time taken for the process in seconds.
            operating_cost: Cost of operating the process.
            operators: Quantity of operators required for the process.
            operating_status: Status of the process (True if operating, False otherwise).
            upstream_processes: List of upstream processes.
            downstream_processes: List of downstream processes.
            sub_processes: Dictionary of sub-processes or processing steps.
            skills: List of skills required for the process.
            input_products: Dictionary containing input products and their quantities.
            output_products: Dictionary containing output products and their quantities.
            resources: Dictionary containing resources required for the process and their consumption.
        """
        self.env = env
        self.id = id
        self.name = name
        self.proc_time = proc_time
        self.operating_cost = operating_cost
        self.operators = operators
        self.operating_status = operating_status
        self.upstream_processes = upstream_processes
        self.downstream_processes = downstream_processes
        self.sub_processes = sub_processes
        self.skills = skills
        self.input_products = input_products
        self.output_products = output_products
        self.resources = resources
        # List of all attributes (excluding 'env')
        self.attributes = list(locals().keys())[1:]

    def define_processes(self, upstream_processes, downstream_processes):
        """
        Defines the upstream and downstream processes for the process.

        Args:
            upstream_processes: List of upstream processes.
            downstream_processes: List of downstream processes.
        """
        if upstream_processes:
            if isinstance(upstream_processes, list):
                for process in upstream_processes:
                    if process in self.upstream_processes:
                        print(f'{process} already exists in upstream process list')
                    else:
                        self.upstream_processes.append(process)
            else:
                raise TypeError("Invalid datatype for the upstream processes list, expected list")

        if downstream_processes:
            if isinstance(downstream_processes, list):
                for process in downstream_processes:
                    if process in self.downstream_processes:
                        print(f'{process} already exists in downstream process list')
                    else:
                        self.downstream_processes.append(process)
            else:
                raise TypeError("Invalid datatype for the downstream processes list, expected list")

    def add_sub_processes(self, sub_processes):
        """
        Adds sub-processes to the process.

        Args:
            sub_processes: Dictionary of sub-processes or processing steps.
        """
        if isinstance(sub_processes, dict):
            self.sub_processes.update(sub_processes)
        else:
            raise TypeError("Invalid datatype for the sub processes list, expected dictionary")

    def add_skill(self, skills):
        """
        Adds skills required for the process.

        Args:
            skills: List of skills to be added.
        """
        if isinstance(skills, list):
            for skill in skills:
                if skill in self.skills:
                    print(f'{skill} already exists for the process')
                else:
                    self.skills.append(skill)
        else:
            raise TypeError("Invalid datatype for the skills list, expected list")

    def add_products(self, input_products, output_products):
        """
        Adds input and output products to the process.

        Args:
            input_products: Dictionary containing input products and their quantities.
            output_products: Dictionary containing output products and their quantities.
        """
        if isinstance(input_products, dict):
            self.input_products.update(input_products)
        else:
            raise TypeError("Invalid datatype for the input products list, expected dictionary")

        if isinstance(output_products, dict):
            self.output_products.update(output_products)
        else:
            raise TypeError("Invalid datatype for the output products list, expected dictionary")

    def add_resources(self, resources):
        """
        Adds resources required for the process.

        Args:
            resources: Dictionary containing resources required for the process and their consumption.
        """
        if isinstance(resources, dict):
            self.resources.update(resources)
        else:
            raise TypeError("Invalid datatype for the resources, expected dictionary")

# ____________ Resource domain ____________
        
class Resource:
    """
    Represents a resource in the simulation model.
    """

    def __init__(self, env, id='default_id', name='default_name', type='default_type',
                 units='default_units', cost_per_unit=0, parts={}, capacity=float('inf'),
                 holding_capacity=1, upstream_processes=[], downstream_processes=[],
                 skills=[], aggregates={}):
        """
        Initializes a Resource object.

        Args:
            env: SimPy Environment object.
            id: Identifier for the resource.
            name: Name of the resource.
            type: Type of the resource (e.g., machine, supply).
            units: Units of measurement for the resource.
            cost_per_unit: Cost per unit of the resource.
            parts: Dictionary containing parts and their quantities in the resource.
            capacity: Maximum capacity of the resource.
            holding_capacity: Part holding capacity for the resource.
            upstream_processes: List of upstream processes.
            downstream_processes: List of downstream processes.
            skills: List of skills associated with the resource.
            aggregates: Dictionary containing sub-resources or machines and their quantities.
        """
        self.env = env
        self.id = id
        self.name = name
        self.type = type
        self.units = units
        self.cost_per_unit = cost_per_unit
        self.parts = parts
        self.capacity = capacity
        self.upstream_processes = upstream_processes
        self.downstream_processes = downstream_processes
        self.holding_capacity = holding_capacity
        self.skills = skills if skills else []
        self.aggregates = aggregates if aggregates else []
        self.attributes = list(locals().keys())[1:]
        self.add_resource()

    def add_skill(self, skills):
        """
        Adds skills to the resource.

        Args:
            skills: List of skills to be added.
        """
        if isinstance(skills, list):
            for skill in skills:
                if skill in self.skills:
                    print(f'{skill} already exists for the resource')
                else:
                    self.skills.append(skill)
        else:
            raise TypeError("Invalid datatype for the skills list, expected list")

    def add_aggregate(self, aggregates):
        """
        Adds sub-resources or machines to the resource.

        Args:
            aggregates: Dictionary containing sub-resources or machines and their quantities.
        """
        if isinstance(aggregates, dict):
            for key, value in aggregates.items():
                if key in self.aggregates.keys():
                    ValueError(f'{key} is already defined for the resource. '
                               f'Please change this in the resource definition sheet ')
                else:
                    self.aggregates[key] = value
        else:
            raise TypeError("Invalid datatype for the aggregates, expected dictionary")

    def add_resource(self):
        """
        Adds a resource based on its type.

        - For 'supplies', a SimPy Resource is created.
        - For 'machine', a SimPy Container and Resource are created.
        - For other types, only a SimPy Container is created.
        """
        if self.type == 'supplies':
            self.resource = simpy.Resource(self.env, self.capacity)
        elif self.type == 'machine':
            self.container = simpy.Container(self.env, self.holding_capacity, 0)
            self.resource = simpy.Resource(self.env, self.capacity)
        else:
            self.container = simpy.Container(self.env, float('inf'), 0)

    def put_part(self, part, qty):
        """
        Adds parts to the resource.

        Args:
            part: Part object.
            qty: Quantity of parts to be added.
        """
        yield self.container.put(qty)
        if part.id in self.parts:
            self.parts[part.id] += qty
        else:
            self.parts[part.id] = qty

    def get_part(self, part, qty):
        """
        Retrieves parts from the resource.

        Args:
            part: Part object.
            qty: Quantity of parts to be retrieved.

        Returns:
            bool: True if parts are successfully retrieved, False otherwise.
        """
        if self.container.level >= qty and part.id in self.parts:
            self.parts[part.id] -= qty
            yield self.container.get(qty)
            return True
        else:
            return False
