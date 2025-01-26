import numpy as np
import scipy.stats as stats

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

    def significans():
        # Test the significans of the regression of all paramters
        # SSR/d/σ2
        # Syy = n∑i=1 (Y −μy)^2 = n∑n i=1 (Y^2) − (∑n i=1 Y )^2 / n
        #SSR = SSE −Syy

        # Test the significans of the regression of one paramters
        #hat{βi} / hat{σ} √cii
        pass

    def R2 ():
        # coefficient of multiple determination
        # R^2 = SSR / Syy
        pass

    def ConfidenceIntervalPredictor():
        # ˆβi ± t_α/2 \hatσ^2 √cii
        # where tα/2 is the appropriate point based on the Tn−d−1 distribution and a confidence level α.
        pass
