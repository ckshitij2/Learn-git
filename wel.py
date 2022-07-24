from scipy import stats

"""
The number of pizzas sold per day by a food zone "Pazzi per
Pizza" follows a poisson distribution at a rate of 76 pizzas
per day. What is the probability that the number of pizza
sales exceeds 80 in a day? Write Python code to calculate the
probability.

"""

X = 80
lamb = 76

result = stats.poisson.cdf(X, lamb)
print(result)
