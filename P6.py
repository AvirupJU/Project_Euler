import numpy as np 
import math
sum_of_sq = sum([i*i for i in range(1,101)]) 
sq_of_sum = (100*101/2)**2
print(abs(sq_of_sum-sum_of_sq))