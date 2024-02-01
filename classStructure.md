## Domains:  
    Product Domain, Process domain, Resource domain

### Domain Structure:
    Domains:
        Classes:
            Attributes : data type 
            Methods (arguments)



1. ________Product domain________

      Product:
         self
         env
         id : string
         name : string
         product_family : string
         type : string
         sourcing : string
         cost : int
         upstream_processes : list
         downstream_processes : list
         features : list
         skills : list
         contents: dictionary {content_id : qty}
         dimensions : dictionary {dimension : value}
         specifications : dictionary {specification : value}

         define_processes(self, upstream_processes, downstream_processes)
         add_feature(self, feature)
         add_skill(self, skill)
         add_content(self, part)
         add_dimension(self, dimensions)
         add_specification(self, specification)

     Order:
        self
        env
        order_date : string
        customer_name :string
        order_id : string
        product : dictionary {product_id : qty}


2. ________Process domain________
     Process:
       self
       env
       id : string
       name : string
       proc_time : int
       operating_cost : int
       operators : int
       upstream_operations : list
       downstream_operations : list
       sub_processes : list
       skills : list
       input_products : dictionary {product_id : qty}
       output_products : dictionary {product_id : qty}
       resources : dictionary {resource_id : qty}

       add_tasks(self, tasks) => tasks is a list
       define_processes(self, upstream_processes, downstream_processes)
       add_sub_processes(self, add_sub_processes)
       add_skill(self, skills)
       add_products(self, input_products, output_products)
       add_resources(self, resources)


3. ________Resource domain________
      Resource:
         self
         env
         id : string
         name : string
         type : string
         material_nature : string
         units : string
         cost_per_unit : int
         capacity : int
         skills : list
         aggregates : dictionary {aggregate : qty}

         add_skill(self, skills)
         add_aggregate(self, aggregates)

### Functions:
    add_attribute(self, attribute)
    update_resources(processObject, objectsList)
    update_supplies(processObject, objectsList)
    update_skills(processObject, objectsList)
    add_kwargs(object, **kwargs) -- This function is being called for every init method of the class, to add kwargs as attributes for a class
    get_classes(library_module)
    get_attributes(class_type)
    evaluate_cost(object)

