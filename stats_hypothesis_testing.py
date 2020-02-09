import scipy
from scipy import stats
import numpy as np


# NORMAL DISTRIBUTION
# example 1:
xcritical = 6 # mu
x = [7,3,6,4,10,5,6,4,3,8]
alpha = 0.05

# Initial cal
avg = np.mean(x)
sd = np.std(x)*np.sqrt(10/9)
n = len(x)
df = n-1 # degrees of freedom


perc_below_xcrit = stats.norm.cdf(x=xcritical,loc=avg,scale=sd)
z_stats = -stats.norm.ppf(perc_below_xcrit)
t_stats = -stats.norm.ppf(perc_below_xcrit)*np.sqrt(len(x))

'''
for understanding
# ppf=percent point function (inverse of cdf-percentiles)
stats.norm.cdf(1.65, loc = 0, scale = 1) = 0.9505
stats.norm.ppf(0.95, loc =0, scale = 1) = 1.6448

stats.t.cdf(1.8,df=10)
stats.t.ppf(0.95,df=10)

stats.chi2.cdf(14.0,df=7)
stats.chi2.ppf(0.95, df=7)

stats.f.cdf(2.7,dfn=4,dfd=26)
stats.f.ppf(0.95,dfn=4,dfd=26)
'''

# WHEN POPULATION MEAN IS GIVEN
z_critical = -stats.norm.ppf(1-alpha)#, loc=avg, scale=sd)
z_critical = -stats.norm.ppf(1-alpha/2)#, loc=avg, scale=sd)

if z_stats<z_critical:
    print('Reject H0')
else:
    print('not enough evidence to reject H0')

p_values = scipy.stats.norm.sf(abs(z_stats)) #one-sided
p_values = scipy.stats.norm.sf(abs(z_stats ))*2 #twosided
if p_values<alpha:
    print('Reject H0')
else:
    print('not enough evidence to reject H0')


# WHEN POPULATION MEAN IS NOT GIVEN
t_critical = -stats.t.ppf(1-alpha, df) # single tail
t_critical = -stats.t.ppf(1-alpha/2, df) # two-tailed

if t_stats<t_critical:
    print('Reject H0')
else:
    print('not enough evidence to reject H0')

p_values = stats.t.sf(abs(t_stats), df) #one-sided
p_values = stats.t.sf(abs(t_stats), df)*2 #twosided
if p_values<alpha:
    print('Reject H0')
else:
    print('not enough evidence to reject H0')
    




# BINOMIAL DISTRIBUTION
# example 2:
p = 0.75
p_hat = 0.71
n = 460
alpha = 0.05
num_success = p_hat*n
sd = p*(1-p) #not to forget the *, otherwise error: float object is not callable

#alternative{‘two-sided’, ‘greater’, ‘less’}, optional

p_values = stats.binom_test(num_success, n=n, p=p, alternative='less') 
#stats.binom_test(p_hat*n, n=n, p=p, alternative='greater') 
#stats.binom_test(p_hat*n, n=n, p=p, alternative='two-sided') 
if p_values<alpha:
    print('Reject H0')
else:
    print('not enough evidence to reject H0')


# example 3
# A car manufacturer claims that no more than 10% of their cars are unsafe. 15 cars are inspected for safety, 3 were found to be unsafe. Test the manufacturer’s claim:
p_values = stats.binom_test(3, n=15, p=0.1, alternative='greater')
if p_values<alpha:
    print('Reject H0')
else:
    print('not enough evidence to reject H0')





# CHI SQUARE DISTRIBUTIONS
    # TEST FOR INDEPENDENCE
    # TEST FOR






'''
generating random numbers
stats.norm.rvs(loc=0,scale=1, size=1, random_state = 42)
stats.norm.rvs(loc=0,scale=1, size=10, random_state = 42)
'''