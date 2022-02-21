from pyomo.environ import *

model = ConcreteModel()

# declare decision variables
model.x = Var(domain=Reals,bounds=(0,4))
model.y = Var(domain=Reals,bounds=(-1,1))
model.z = Var(domain=NonNegativeReals)

# declare objective
model.profit = Objective(expr = model.x + 4*model.y + 9*model.z, sense = minimize)

# declare constraints
model.c1 = Constraint(expr = model.x + model.y <= 5)
model.c2 = Constraint(expr = model.x + model.z >= 10)
model.c3 = Constraint(expr = -model.y + model.z == 7)

# solve
SolverFactory('cplex').solve(model)
print("objective=", model.profit())