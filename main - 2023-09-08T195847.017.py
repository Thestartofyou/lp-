import pulp

# Create a Linear Programming problem instance
lp_problem = pulp.LpProblem("My_LP_Problem", pulp.LpMaximize)

# Define the decision variables
x = pulp.LpVariable("x", lowBound=0)  # x >= 0
y = pulp.LpVariable("y", lowBound=0)  # y >= 0

# Define the objective function to maximize
lp_problem += 2 * x + 3 * y, "Objective"

# Define constraints
lp_problem += x + 2 * y <= 8, "Constraint 1"
lp_problem += 3 * x - y <= 6, "Constraint 2"

# Solve the LP problem
lp_problem.solve()

# Print the status of the solution
print("Status:", pulp.LpStatus[lp_problem.status])

# Print the optimal values of the decision variables
print("Optimal values:")
print("x =", x.varValue)
print("y =", y.varValue)

# Print the optimal objective value
print("Optimal Objective Value =", pulp.value(lp_problem.objective))
