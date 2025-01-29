import numpy as np
import scipy.stats as stats

"""
A function or method to calculate the variance.
• A function or method to calculate the standard deviation.
• A function or method that reports the significance of the regression.
• A function or method that reports the relevance of the regression (R2).
- Make this on return of a dict to make an pandas dataframe

• Significance tests on individual variables, in particular categorical variables.
• A function or method that calculates the Pearson number between all pairs of parameters.
• Confidence intervals on individual parameters.
- Make an return of a dict for each of these to make an pandas dataframe.

Testing, do check with testing adv data with this class.
Overkill, try to make it so you can make predictions, if there is time for it.
So a function you can give X values to run againt the regression. See if you can make it
so it also gives the probality and the error for the predicted variable 
"""


class LinearRegression:
    def __init__(self, data):
        self.data = data

    @property
    # d = number of features/parameters/dimensions of the model
    # n = size of the sample

    # @property
    # A property "confidence_level" that stores the selected confidence level.
    
    def OLS ():
        # Ordinary Least Squares
        # beta = (X^T * X)^−1 X^T Y
        pass

    def r_value():
        # Pearson correlation number (r)
        # r = Cov(Xa,Xb) √VarX_a VarX_b
        pass

    def sigma2 ():
        # Variance, sigma2 
        # σ2 = SSE / n −d −1
        # SSE - Sum of Square Errors
        # SSE = n∑i=1 (Yi −Xb)2
        pass
    
    def sigma():
        # Standard deviation, sigma
        # S = √var
        pass


    def significans(self, predictor):
        # Test the significans of the regression of all paramters
        # SSR/d/σ2
        # Syy = n∑i=1 (Y −μy)^2 = n∑n i=1 (Y^2) − (∑n i=1 Y )^2 / n
        #SSR = SSE −Syy

        # Test the significans of the regression of one paramters
        # hat{βi} / hat{σ} √cii
        # $c = (X^TX)^{-1}\sigma^2$

        c = np.linalg.pinv(self.X.T @ self.X) * self.var
        b_statistic = self.data[predictor] / (self.sigma*np.sqrt(c[3, 3]))

        

    def R2 (self):
        # coefficient of multiple determination
        # R^2 = SSR / Syy
        pass

    def confidence_interval_predictor(self):
        # ˆβi ± t_α/2 \hatσ^2 √cii
        # where tα/2 is the appropriate point based on the Tn−d−1 distribution and a confidence level α.
        pass
    
    def p_value_pairs_param(self):
        
        pass

