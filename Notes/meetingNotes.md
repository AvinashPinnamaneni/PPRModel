## Meeting for 04-01-2023:
### Progress of work:
- I have worked in the exploration of Simantha package which turns out to be out of date and requires a lot of effort to customize the code for the present scenario.
- A package called Simpy turns out to be a more efficient solution for DES allowing for the modelling of PPR.
- I have modelled PPR classes following the paper which defined the architecture of PPR Domain. Currently trying to model the current factory into the model.
### Questions:
- The hierarchy of product domain follows as Product -> Variants -> Sub-Assemblies -> Components -> intermediate products(generated during different component states during processing) => each component can have different processing steps based on the product it is assigned to. Since I am following top down approach, how can I determine the processing step for a component considering the assigned product?
**Ans**: Don't complicate the structure as these operations could be explored in the further stages. Stick to minimum viable program structure to explain the structure.

## Meeting for 18-01-2023:
### Progress of work:
- Product class is meant to define overall output product of the system where as the intermediate products are defined as assemblies and components considering the reference which defines PPR in hierarchical model.
- Supplies and consumables are different entities where the supplies don't directly influence the overall product but are necessary for manufacturing,where as the consumables are part of BOM of the product. 
- Excel sheets are being generated and used for the creation of objects.
- The objects will be used for the simulation using simpy and the functional logic for the simulation should be modelled for simulation.
- Simple single line manufacturing process is being considered for the present use case as consideration of complex production networks makes simulation and functional logic complicated.
- The KPIs being considered for the current use case are: 
                    1. Utilization Efficiency
                    2. Throughput rate
                    3. Makespan
                    4. Tardiness
### Questions:
- Can I model assemblies, components and supplies as different classes in different domains and model the functional logic using the structure?
 **Ans**No, the assemblies, components and supplies must be modelled as immediate products which can be classified based on the attribute called type of the datatype string, in the product class which can take the values assembly, component, supply, overall_product.

## Meeting for 01-02-2023:
### Progress of work:
- Start with basic simulation model
- Model the domains
-