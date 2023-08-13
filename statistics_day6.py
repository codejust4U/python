import numpy as np
import matplotlib.pyplot as plt

n=10
p=0.5
size=1000

bino_dist = np.random.binomial(n,p,size)

plt.hist(bino_dist,density=True)
plt.show()

n=10
p=0.8
size=1000

bino_dist = np.random.binomial(n,p,size)

plt.hist(bino_dist,density=True)
plt.show()


n=10
p=0.1
size=1000

bino_dist = np.random.binomial(n,p,size)

plt.hist(bino_dist,density=True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt


num_samples = 1000
sample_size = 30
distribution_range = (0,1)

#generate sample from uniform distribution
samples = np.random.uniform(distribution_range[0],distribution_range[1],(num_samples,sample_size))
sample_means = np.mean(samples,axis=1)

plt.hist(sample_means,bins=30,density=True,edgecolor='black')
plt.title("Histogram of sample means")
plt.xlabel('Sample mean')

plt.ylabel('Density')
plt.show()

sample_size2 = 50
lambda_param = 2

samples2 = np.random.exponential(scale=1/lambda_param,size=(num_samples,sample_size2))

sample_mean2 = np.mean(samples2,axis=1)

plt.hist(sample_mean2,bins=30,density=True,edgecolor='black')
plt.title("Histogram of sample means")
plt.xlabel('Sample mean')
plt.ylabel('Density')
plt.show()




# poisson distribution
poisson_lambda = 5

gamma_Shape = 2
gamma_scale = 1

binomial_n = 10
binomial_p = 0.5

poisson_sample = np.random.poisson(lam=poisson_lambda,size=(num_samples,sample_size2))
gamma_Sample = np.random.gamma(shape=gamma_Shape,scale=gamma_scale,size=(num_samples,sample_size2))
binomial_sample = np.random.binomial(n=binomial_n,p=binomial_p,size=(num_samples,sample_size2))

# calculate the sample means
poisson_means = np.mean(poisson_sample,axis=1)
gamma_mean= np.mean(gamma_Sample,axis=1)
binomial_mean = np.mean(binomial_sample,axis=1)

fig,axs = plt.subplots(3,1,figsize=(8,16))

#poisson
axs[0].hist(poisson_means,bins=30,density=True,edgecolor='black')
axs[0].set_title("Histogram of Poisson Distribution")
axs[0].set_xlabel("Sample Means")
axs[0].set_ylabel('Density')
#Gamma
axs[1].hist(gamma_mean,bins=30,density=True,edgecolor='black')
axs[1].set_title("Histogram of Gamma Distribution")
axs[1].set_xlabel("Sample Means")
axs[1].set_ylabel('Density')


#binomial
axs[2].hist(binomial_mean,bins=30,density=True,edgecolor='black')
axs[2].set_title("Histogram of Binomial  Distribution")
axs[2].set_xlabel("Sample Means")
axs[2].set_ylabel('Density')

plt.show()



num_samples3 = 10000
sample_size3 = 50

gamma_Shape3 = 2
gamma_scale3 = 1

# theoretical mean and variance
theoretical_mean = gamma_Shape3 * gamma_scale3
theoretical_variance = (gamma_Shape3 * gamma_scale3 **2)


# sample from gamma distrubtuion
samples3 = np.random.gamma(shape=gamma_Shape3,scale=gamma_scale3,size=(num_samples3,sample_size3))


sample_mean3 =  np.mean(samples3,axis=1)

empirical_mean = np.mean(sample_mean3)
empirical_variance = np.var(sample_mean3)


# compare thoeretical and emperical

print(f"Theoretical mean: {theoretical_mean:.4f}")
print(f"Empirical mean: {empirical_mean :.4f}")

print(f"\n")


print(f"Theoretical variance: {theoretical_variance:.4f}")
print(f"Empirical variance: {empirical_variance :.4f}")


import pandas as pd

train_df = pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day153 Statistics_day6\train.csv')
test_df = pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day153 Statistics_day6\test.csv')
print(train_df)
print(test_df)

df=pd.concat([train_df.drop(columns=['Survived']),test_df]).sample(1309)

df['Fare'].mean()

df['Fare'].plot(kind='kde')
plt.show()


# sample size =50
samples = []
for i in range(100):
    samples.append(df['Fare'].dropna().sample(50).values.tolist())


samples = np.array(samples)

sampling_means =samples.mean(axis=1)

import seaborn as sns
sns.kdeplot(sampling_means)
plt.show()


print(sampling_means.mean())

print(sampling_means.std()/np.sqrt(50))

upper_limit=sampling_means.mean()+2*(sampling_means.std()/np.sqrt(50))
lower_limit=sampling_means.mean()-2*(sampling_means.std()/np.sqrt(50))

print("The range of limit is ",lower_limit,"-",upper_limit)

print(df['Fare'].mean())


import numpy as np

# Set the parameters
population_size = 100000
sample_size = 50
num_samples = 100

# Generate a random representative sample of salaries (in thousands)
# You should replace this with actual collected salary data
np.random.seed(42)  # Setting a seed for reproducibility
population_salaries = np.random.lognormal(mean=4.5, sigma=0.8, size=population_size)

# Generate multiple samples and calculate the sample means and standard deviations
sample_means = []
sample_std_devs = []

for _ in range(num_samples):
  sample_salaries = np.random.choice(population_salaries, size=sample_size)
  sample_means.append(np.mean(sample_salaries))
  sample_std_devs.append(np.std(sample_salaries))

# Calculate the average of the sample means and the standard error
average_sample_means = np.mean(sample_means)
standard_error = np.std(sample_means) / np.sqrt(num_samples)

# Calculate the 95% confidence interval
margin_of_error = 1.96 * standard_error
lower_limit = average_sample_means - margin_of_error
upper_limit = average_sample_means + margin_of_error

# Report the results
print(f"Estimated average salary (in thousands): {average_sample_means:.2f}")
print(f"95% confidence interval (in thousands): ({lower_limit:.2f}, {upper_limit:.2f})")
