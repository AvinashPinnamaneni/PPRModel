- process states must be defined before and after the timeout function. 
    For example: the resource state must be set to occupied before timeout and active post timeout.

env.process(generator_function) will execute the specified generator function. This method will be prevalent in the definition of simulation methodology.

Normal predefined events can be processed in Environment, realtime simulations can be executed using RealtimeEnvironment

SimPy defines three categories of resources:
**Resources** – can be used by a limited number of processes at a time (e.g., a gas station with a limited number of fuel pumps).

**Containers** – model the production and consumption of a homogeneous, undifferentiated bulk. It may either be continuous (like water) or discrete (like apples).

**Stores** – allow the production and consumption of Python objects.

Skills essentially denotes the possibility of execution of a process using a resource on a given product. The possibility of execution is defined/validated in task which relates processes with skills.

### Python functions and methods to remember:
"globals()[variablenameinstring]" accesses the object through the variable name which equals to the string value

object.__class__.__name__ returns the name of the class