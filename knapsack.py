from pyomo.environ import * 


v = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11} 
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3} 

W_max = 14 


model = ConcreteModel() 

model.ITEMS = v.keys() 
model.x = Var( model.ITEMS, within=Binary ) 
model.value = Objective( expr = sum( v[i]*model.x[i] for i in model.ITEMS ), sense = maximize ) 
model.weight = Constraint( expr = sum( w[i]*model.x[i] for i in model.ITEMS ) <= W_max )

opt = SolverFactory("bonmin")
Result = opt.solve(model)
print(pyomo.environ.value(model.value))