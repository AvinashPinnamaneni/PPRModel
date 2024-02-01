# this function is called when the component cost is not specified during the definition of component object
def evaluate_cost(obj):
    if obj.component_type == 'plate': # of the component type is plate
        cost = (
            obj.length 
            * obj.width 
            * obj.thickness 
            * 0.8  # Cost coefficient
            * 7.8  # Density factor
            * (10 ** -6)
        )
    # extend the evaluation of component costs based on component using elif conditions
        return cost
    return None  # Return None if the component type is not 'plate'
