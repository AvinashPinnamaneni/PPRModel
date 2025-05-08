## Underlying functionality:
- This project focusses on the optimization of production system by aligning the domain experts to the common goal set by the stakeholder.
- The logic is built using Python using PPR(Product-Process-Resource) model for modelling the production system. Thus modelled production system is used to configure multiple process configuratons and production system variants. 
- Thus created variants of the production system are then simulated using DES(Discrete event Simulation) using Simpy(Python package for DES) to evaluate multiple KPIs defined by the stakeholder for each variant of the production system. 
- These KPI solutions are then used to find Pareto Optimal solutions which are used to choose the best variant of production system thorugh minimized set of variants.
## File structure:
- The main files for the program are organized as
-   main : Main program which runs in a loop for simulation.
-   Functions : includes all the functions defined for creating resource configurations, process configurations and process variants. 
-   PPR Classes : Contains the PPR classes which store the meta data for the production objects used for simulation. Additionally contains Order class through which demand for the production system is specified which defining a production system instance.
