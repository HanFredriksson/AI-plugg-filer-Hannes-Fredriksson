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
        self.X = None
        self.Y = None
        self.d = None
        self.n = None
        self._confi_lvl = None
        self.coefficients = None

    @property
    def param_size(self):
        return self.d, self.n

    @param_size.setter
    def set_param_size (self, _):
        self.d = self.X.shape[1] - 1
        self.n = self.Y.shape[0]


    @property
    def varibals_X_Y(self):
        return self.X, self.Y

    @varibals_X_Y.setter
    def varibals_X_Y(self, param, sample):
        self.Y = self.data[sample].to_numpy()
        X = self.data[param].to_numpy()

        self.X = np.column_stack([np.ones(self.Y.shape[0]),X])


    @property
    # A property "confidence_level" that stores the selected confidence level.

    def confi_lvl(self):
        return self.confi_lvl
    
    @confi_lvl.setter

    # !!! Check that this level is correctly passed!!!!
    # namn  på variabelAlpha 
    def confi_lvl(self, lvl):
        if 0 < lvl < 1:
            self._confi_lvl = lvl
        else:
            raise ValueError("Confidence level must be between 0 and 1.")

    
    def fit (self):
        """Fit the linear regression model with Ordinary Least Squares method
        Formula: b = (X^T*X)^-1 * X^T * Y
        """

        self.param_size = None

        self.coefficients = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y 


    def RSS (self):
        """Sum of squared residuals, RSS or SSE
        """

        RSS = np.sum(np.square(self.Y - (self.X @ self.coefficients)))

        return RSS
    

    def Syy (self):
        """A is a measure of the variability in y.
        Formula: Syy = n∑i=1 (y_i - y_mean)^2"""

        Syy = np.sum((np.square(self.Y)) - (np.square(np.sum(self.Y))/self.n))

        return Syy
    

    def Sxx (self):
        Sxx = np.sum((np.square(self.X)) - (np.square(np.sum(self.X))/self.n))

        return Sxx
    

    def Sxy (self):
        Sxy = (np.sum(self.X[:, 1] * self.Y) - (np.sum(self.X[:, 1])*np.sum(self.Y))/self.n)

        return Sxy


    def SSR (self):
        """The sum of squares due to regression
        SSR = SSE - Syy
        """
        SSR = self.RSS() - self.Syy()

        return SSR


    def c (self):
        c = np.linalg.pinv(self.X.T @ self.X) * self.variance()
        return c


    def sigma (self):
        # Standard deviation, sigma
        # S = √var
        
        S = np.sqrt(self.variance)

        return S


    def variance (self):
        # Variance, sigma2 
        # σ2 = SSE / n −d −1
        # SSE - Sum of Square Errors
        # SSE = n∑i=1 (Yi −Xb)2
        
        var = self.RSS() / (self.n - self.d - 1)

        return var


    def significans (self):
        """Test the significans of the regression of all paramters
        SSR/d/σ^2 put through the F-distribution.
        """
        # Test the significans of the regression of one paramters
        #hat{βi} / hat{σ} √cii

        F_statistic = (self.SSR()/self.d)/self.sigma()
        p_value = stats.f.sf(F_statistic, self.d, self.n-self.d-1)
       
        # gör en dict som retur
        return p_value

       

    def R2 (self):
        # coefficient of multiple determination
        R2 = self.SSR() / self.Syy()
        return R2
    

    def confidence_interval_predictor(self):
        # ˆβi ± t_α/2 \hatσ^2 √cii
        # where tα/2 is the appropriate point based on the Tn−d−1 distribution and a confidence level α.

        df = self.n - self.d - 1 
        t = stats.t.ppf(1 - self._confi_lvl/2, df)

        se_b0 = self.variance() * (1/self.n)+(np.square(self.c()))
        ci_b1 = (self.b[0], t*np.sqrt(se_b0))

        return ci_b1
    

    def p_value_pairs_param (self):
        # A function or method that calculates the Pearson number between all pairs of parameters.
        # Pearson correlation number (r)
        # r = Cov(Xa,Xb) √VarX_a VarX_b
        
        rho = self.Sxy / (np.sqrt(self.Sxx*self.Syy))

        return rho



    def Significance_tests_on_individual_variables (self):
        # Significance tests on individual variables, in particular categorical variables.
        
        param_statistic = self.d / (self.sigma*np.sqrt(self.c()[3, 3]))
        p_beta= 2*min(stats.t.cdf(param_statistic, self.n - self.d - 1), stats.t.sf(param_statistic, self.n - self.d - 1))
        
        return p_beta
