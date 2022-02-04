# Module 3 bonus - Applying variance and standard deviation to temperature data

# Kyle Hudson

import statistics

# data points for temperature readings
temps = (1.8, 1.9, 2, 2.4, 2.5, 2.7, 2.9, 3.2, 3.3, 3.6, 4, 4.4, 4.6, 4.8, 4.8, 4.9, 4.9, 4.8, 4.7, 5.1, 5.5, 5.5, 5.7, 5.8, 5.6, 5.6, 5.5, 5.5, 5.5, 5.5, 5.5, 5.4, 5.4, 5.4, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.2,             5.2, 5.2, 5.2, 5.2, 5.2, 5.2, 5.3, 5.3, 5.3, 5.4, 5.4, 5.5, 5.5, 5.6, 5.6, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7, 5.8, 5.8, 5.7, 5.7, 5.7, 5.7, 5.7, 5.8, 5.8, 5.9, 5.9, 6, 6, 6.1, 6.1, 6.1, 6.1, 5.5,         6, 6, 6, 6, 6, 6, 6, 5.8, 5.6, 5.4, 5.3, 5.3, 5.3, 5.2, 5.2, 5.2, 5.2, 5.1, 5.2, 5.2, 5.9, 6.1, 6.2, 6.2, 6.3, 6.3, 6.4, 6.4, 6.4, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.2, 6.2, 5.6, 5.1, 4.6, 4.5, 4.5, 4.5,
        4.5, 4.5, 4.6, 4.5, 4.6, 4.8, 4.6, 4.6, 4.7, 4.7, 4.7, 4.8, 4.8, 4.9, 4.9, 5, 5, 5.1, 5.3, 5.2, 5.3, 5.4, 5.4, 5.5, 5.6, 5.7, 5.8, 5.8, 5.9, 6, 6.1, 6.1, 6.3, 6.3, 6.4, 6.5, 6.5, 6.7, 6.7,
        6.8, 6.8, 6.9, 7, 7.1, 7, 7.1, 7.2, 7, 6.8, 7.1, 7.3, 7.5, 7.6, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.7, 8.8, 8.9, 9, 9.7, 10.3, 10.5, 11.6, 12.8, 14.9)

# calculating useful information for temperature data analysis
count = len(temps)
hours = count / 15
mean = statistics.mean(temps)
variance = statistics.pvariance(temps)
stdev = statistics.pstdev(temps)
max_temp = max(temps)
min_temp = min(temps)

print(f'Mean Temperature = {mean:.2f} degrees Celsius for {hours:.2f} hours with a variance of {variance:2f} and a standard deviation of {stdev:2f}')

