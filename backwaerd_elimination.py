"""
# Regression Analysis
A regression analysis involves 40 observatios and 5 independent variables.

SS(fit) = 93.5          

SS(mean) = 150.3

n=no of observation

k=no of IVs

SSR=Sum of square of residual

SSE=sum os square of error

https://github.com/codejust4U/dataset/blob/main/question.png
![WhatsApp Image 2023-06-20 at 15.31.55.jpg](<attachment:WhatsApp Image 2023-06-20 at 15.31.55.jpg>)

Adjusted R^2

1-(n-1/n-k-1)(1-R^2)

1-(39/34)(1-.3779)   = 0.286


# compute standard error
SE

root_over(SSE/n-k-1)

root_over(MSE)=root_over(2.75)=1.658
"""
# importing the libraries
import pandas as pd

# reading the data
df = pd.read_excel(r'D:\datas\excel\Day14\datatab.xlsx')

# initialization
n = 40
k = 5
ss_error = 93.5
ss_total = 150.3

# calculation
Total = n-1
Residual = n-k-1
ssr = ss_total - ss_error
MSR = ssr/k
MSE = ss_error - (n-k-1)
F = MSR/MSE
R_square = ssr/ss_total


plot_ = pd.DataFrame({"\tDF_value\t":[k,Residual,Total,R_square],"SS_value\t":[ssr,ss_error,ss_total,'null'],"MS_value\t":[MSR,MSE,'null','null'],"F_value\t":[F,'null','null','null']})

print(plot_)



import numpy as np
Adjusted_R_sq = 1-((Total/Residual)*(1-R_square))
print("\nThe Adjusted R Squared is: ", Adjusted_R_sq)

CSE = np.sqrt(ss_error/Residual)
print("\nThe computed standard error is: ",CSE)