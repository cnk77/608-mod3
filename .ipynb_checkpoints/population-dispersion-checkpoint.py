# Module 3 File 5 - Calculating measures of dispersion

# Kyle Hudson

import statistics

values = (1, 3, 4, 2, 6, 5, 3, 4, 5, 2)

print('Values of 10 six-sided die rolls:', values)
print('Variance of values:', statistics.pvariance(values))
print('Standard deviation of values:', statistics.pstdev(values))