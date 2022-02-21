from pulp import *

prob = LpProblem("test1", LpMinimize)

# Variables
x = LpVariable("x", 0, 4) # 0 <= x <= 4
y = LpVariable("y", -1, 1) # -1 <= y <= 1
z = LpVariable("z", 0) # 0 <= z

# Objective (the name at the end is facultative)
prob += x + 4 * y + 9 * z, "obj"

# Constraints (the names at the end are facultative)
prob += x + y <= 5, "c1"
prob += x + z >= 10, "c2"
prob += -y + z == 7, "c3"

# Solve the problem using the default solver
prob.solve()  # use prob.solve(CPLEX()) instead to use CPLEX 

# Print the value of the objective
print("objective=", value(prob.objective))