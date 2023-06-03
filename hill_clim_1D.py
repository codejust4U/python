"""import numpy as np
import matplotlib.pyplot as plt

# objective function
def objective(x):
    return x[0] ** 2.0

# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size):
    # generate an initial point
    solution = bounds[:, 0] + np.random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    solution_eval = objective(solution)
    # run the hill climb
    solutions = [solution]
    for i in range(n_iterations):
        # take a step
        candidate = solution + np.random.randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = objective(candidate)
        # check if we should keep the new point
        if candidate_eval <= solution_eval:
            # store the new point
            solution, solution_eval = candidate, candidate_eval
        # keep track of solutions
        solutions.append(solution)
        # report progress
        print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
    return solution, solution_eval, solutions

# seed the pseudorandom number generator
np.random.seed(5)
# define range for input
bounds = np.asarray([[-5.0, 5.0]])
# define the total iterations
n_iterations = 1000
n_iterations2 = 100
# define the maximum step size
step_size = 0.1
# perform the hill climbing search
best, score, solutions = hillclimbing(objective, bounds, n_iterations, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))


# sample input range uniformly at 0.1 increments
inputs = np.arange(bounds[0, 0], bounds[0, 1], 0.1)
# create a line plot of input vs result
plt.plot(inputs, [objective([x]) for x in inputs], '--')
# draw a vertical line at the optimal input
plt.axvline(x=0.0, ls='--', color='red')
# plot the sample as black circles
plt.plot([sol[0] for sol in solutions], [objective(sol) for sol in solutions], 'o', color='black')
plt.show()

print("-----------------------------------------------------------------------------------------------------")

best, score, solutions = hillclimbing(objective, bounds, n_iterations2, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))



# sample input range uniformly at 0.1 increments
inputs = np.arange(bounds[0, 0], bounds[0, 1], 0.1)
# create a line plot of input vs result
plt.plot(inputs, [objective([x]) for x in inputs], '--')
# draw a vertical line at the optimal input
plt.axvline(x=0.0, ls='--', color='red')
# plot the sample as black circles
plt.plot([sol[0] for sol in solutions], [objective(sol) for sol in solutions], 'o', color='black')
plt.show()


print("-----------------------------------------------------------------------------------------------------")

best, score, solutions = hillclimbing(objective, bounds, n_iterations+n_iterations2, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))



# sample input range uniformly at 0.1 increments
inputs = np.arange(bounds[0,1], bounds[0,0], 0.1)
# create a line plot of input vs result
plt.plot(inputs, [objective([x]) for x in inputs], '--')
# draw a vertical line at the optimal input
plt.axvline(x=0.0, ls='--', color='red')
# plot the sample as black circles
plt.plot([sol[0] for sol in solutions], [objective(sol) for sol in solutions], 'o', color='black')
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt

# objective function
def objective(x):
    return x[0] ** 2.0

# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size):
    # generate an initial point
    solution = bounds[:, 0] + np.random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    solution_eval = objective(solution)
    # run the hill climb
    solutions = [solution]
    for i in range(n_iterations):
        # take a step
        candidate = solution + np.random.randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = objective(candidate)
        # check if we should keep the new point
        if candidate_eval <= solution_eval:
            # store the new point
            solution, solution_eval = candidate, candidate_eval
        # keep track of solutions
        solutions.append(solution)
        # report progress
        print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
    return solution, solution_eval, solutions

# seed the pseudorandom number generator
np.random.seed(5)
# define range for input
bounds = np.asarray([[-5.0, 5.0]])
# define the total iterations
n_iterations = 1000
n_iterations2 = 100
# define the maximum step size
step_size = 0.1
# perform the hill climbing search
best, score, solutions = hillclimbing(objective, bounds, n_iterations, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))


# sample input range uniformly at 0.1 increments
inputs = np.arange(bounds[0, 0], bounds[0, 1], 0.1)

# create a new figure
plt.figure()

# plot the first graph
plt.subplot(211)
plt.plot(inputs, [objective([x]) for x in inputs], '--')
plt.axvline(x=0.0, ls='--', color='red')
plt.plot([sol[0] for sol in solutions], [objective(sol) for sol in solutions], 'o', color='black')
plt.title('Hill Climbing (n_iterations = 1000)')

# perform the second hill climbing search
best, score, solutions = hillclimbing(objective, bounds, n_iterations2, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))

# plot the second graph
plt.subplot(212)
plt.plot(inputs, [objective([x]) for x in inputs], '--')
plt.axvline(x=0.0, ls='--', color='red')
plt.plot([sol[0] for sol in solutions], [objective(sol) for sol in solutions], 'o', color='black')
plt.title('Hill Climbing (n_iterations = 100)')

# adjust the spacing between subplots
plt.subplots_adjust(hspace=0.5)

# display the figure
plt.show()
