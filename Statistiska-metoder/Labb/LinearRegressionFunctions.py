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

    # @property
    # def param_size(self):

    #     return self.d, self.n

    # @param_size.setter
    # def set_param_size (self, _):
    #     self.d = self.X.shape[1] - 1
    #     self.n = self.Y.shape[0]

    @property
    def sample_size(self):

        return self.Y, self.n


    @sample_size.setter
    def sample_size(self, sample):
        """
        arg: list

        Sets the values for the samples to variabel Y

        Sets the size of sampels to varibal n 
        """
        self.Y = self.data[sample].to_numpy()

        self.n = len(self.Y)

    @property
    def params(self):

        return self.X, self.d

    @params.setter
    
    def params(self, params):
        """
        arg: list

        Sets the values for parameters to varibal X

        Sets the number of parameters to varibal d
        """
        X = self.data[params].to_numpy()
        self.X = np.column_stack([np.ones(self.Y.shape[0]),X])

        self.d = len(params)




    @property
    # A property "confidence_level" that stores the selected confidence level.

    def confi_lvl(self):
        return self.confi_lvl
    

    @confi_lvl.setter
    # !!! Check that this level is correctly passed!!!!
    # namn  på variabel Alpha 
    def confi_lvl(self, lvl):
        if 0 < lvl < 1:
            self._confi_lvl = lvl
        else:
            raise ValueError("Confidence level must be between 0 and 1.")

    
    def fit (self):
        """
        Fit the linear regression model with Ordinary Least Squares method
        Sets it to varibal coefficients
        """

        self.param_size = None

        self.coefficients = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y 


    def RSS (self):
        """
        Sum of squared residuals, RSS or SSE
        """

        RSS = np.sum(np.square(self.Y - (self.X @ self.coefficients)))

        return RSS
    

    def Syy (self):
        """
        Variance of the dependent  variable Y
        """
        
        Syy = np.sum(np.square(self.Y)) - (np.square(np.sum(self.Y)))/self.n

        return Syy
    

    def Sxx (self):
        """
        Variance of the independent variable X
        """
        Sxx = np.sum(np.square(self.X)) - (np.square(np.sum(self.X))/self.n)

        return Sxx
    

    def Sxy (self):
        """
        Covariance between XX and YY
        """
        Sxy = (np.sum(self.X[:, 1] * self.Y) - (np.sum(self.X[:, 1])*np.sum(self.Y))/self.n)

        return Sxy


    def SSR (self):
        """
        The sum of squares due to regression
        """
        SSR = self.RSS() - self.Syy()

        return SSR


    def t_statistic (self):
        """
        Gives the t-statistic value
        """

        t = np.linalg.pinv(self.X.T @ self.X) * self.variance()

        return t

    def variance (self):
        """
        Variance for the sample, sigma2
        """
    
        var = self.RSS() / (self.n - self.d - 1)

        return var

    def sigma (self):
        """
        Residual standard error, Sigma
        """
            
        
        S = np.sqrt(self.variance())

        return S



    def significans (self):
        """
        Test the significans of the regression of all paramters
        put through the F-distribution.
        """
       
        F_statistic = (self.SSR()/self.d)/self.sigma()
        p_value = stats.f.sf(F_statistic, self.d, self.n-self.d-1)
       
        # gör en dict som retur
        return p_value

       

    def R2 (self):
        """
        Coefficient of multiple determination, R2
        """

        R2 = self.SSR() / self.Syy()
        return R2
    




    # !!! Inte testa här ifrån !!!
    def confidence_interval_predictor(self):
        # ˆβi ± t_α/2 \hatσ^2 √cii
        # where tα/2 is the appropriate point based on the Tn−d−1 distribution and a confidence level α.

        df = self.n - self.d - 1 
        t = stats.t.ppf(1 - self._confi_lvl/2, df)

        se_b0 = self.variance() * (1/self.n)+(np.square(self.t-statistic()))
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
        
        param_statistic = self.d / (self.sigma*np.sqrt(self.t-statistic()[3, 3]))
        p_beta= 2*min(stats.t.cdf(param_statistic, self.n - self.d - 1), stats.t.sf(param_statistic, self.n - self.d - 1))
        
        return p_beta
