##1. The number of customer returns in a retail chain per day follows a Poisson distribution at a rate of
##25 returns per day. Write Python code to answer the following questions:
##(a) Calculate the probability that the number of returns exceeds 30 in a day.
##(b) If the chance of fraudulent return is 0.05, calculate the probability that there will be at least 2
##fraudulent returns in any given day.


import scipy.stats as stats
import numpy as np

# Part (a): Probability of more than 30 returns in a day
lambda_returns = 25  # average rate of returns per day

# P(X > 30) = 1 - P(X <= 30)
prob_a = 1 - stats.poisson.cdf(30, lambda_returns)
print(f"(a) Probability of more than 30 returns: {prob_a:.4f}")

# Part (b): Probability of at least 2 fraudulent returns
# First, number of returns follows Poisson(25)
# Then each return has 0.05 probability of being fraudulent
p_fraud = 0.05  # probability of fraudulent return

# We'll calculate this using a compound Poisson-Binomial approach
# P(at least 2 fraudulent) = 1 - P(0 fraudulent) - P(1 fraudulent)
# Sum over possible number of returns (k) from 0 to reasonable upper bound

def prob_at_least_2_fraudulent(lambda_val, p, max_k=100):
    total_prob_0 = 0  # probability of 0 fraudulent returns
    total_prob_1 = 0  # probability of 1 fraudulent return
    
    for k in range(max_k + 1):
        poisson_prob = stats.poisson.pmf(k, lambda_val)
        binom_prob_0 = stats.binom.pmf(0, k, p)  # 0 fraudulent in k returns
        binom_prob_1 = stats.binom.pmf(1, k, p)  # 1 fraudulent in k returns
        total_prob_0 += poisson_prob * binom_prob_0
        total_prob_1 += poisson_prob * binom_prob_1
    
    return 1 - total_prob_0 - total_prob_1

prob_b = prob_at_least_2_fraudulent(lambda_returns, p_fraud)
print(f"(b) Probability of at least 2 fraudulent returns: {prob_b:.4f}")
