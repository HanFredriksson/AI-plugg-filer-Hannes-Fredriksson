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


To do
----------------

gå genom vad som behövs för VG
"""


class LinearRegression:
    def __init__(self, data):

        self.data = data
        self.X = None
        self.Y = None
        self.d = None
        self.n = None
        self._confi_lvl = 0
        self.coefficients = None


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
        self.Y = self.data[sample]
        self.Y = np.column_stack([self.Y])
        self.n = len(self.Y)

    @property
    def params (self):

        return self.X, self.d

    @params.setter
    def params (self, params):
        """
        arg: list

        Sets the values for parameters to varibal X

        Sets the number of parameters to varibal d
        """
        X = self.data[params]
        self.X = np.column_stack([np.ones(len(self.Y)), X])

        self.d = len(params)




    @property

    def confidence_lvl(self):
        return self._confi_lvl
    

    @confidence_lvl.setter
    
    def confidence_lvl(self, lvl):
        """
        arg: int - 0 < level < 1.

        Set the confidence level, alpha

        """
        if 0 < lvl < 1:
            self._confi_lvl = lvl
        else:
            raise ValueError("Confidence level must be between 0 and 1.")

    
    def fit (self):
        """
        Fit the linear regression model with Ordinary Least Squares method
        Sets it to varibal coefficients

        returns: array - An array with Beta-0 as [0] and Beta-n [n]
        """
        
        self.coefficients = np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y 
        self.coefficients = self.coefficients.reshape(-1, 1)
        
        return 

    def RSS (self):
        """
        Sum of squared residuals, RSS or SSE

        returns: int
        """

        RSS = np.sum(np.square(self.Y - (self.X @ self.coefficients)))

        return RSS
    

    def Syy (self):
        """
        Variance of the dependent  variable Y

        returns: int
        """
        
        Syy = (self.n*np.sum(np.square(self.Y)) - np.square(np.sum(self.Y)))/self.n

        return Syy
    

    def Sxx (self):
        """
        Variance of the independent variable X

        returns: int
        """
     
        X = np.column_stack([[i[1:] for i in self.X]])

        Sxx = (self.n*np.sum(np.square(X)) - np.square(np.sum(X)))/self.n

        return Sxx
    

    def Sxy (self):
        """
        Covariance between X and Y, cross-product term

        returns: int
        """
        

        X = np.column_stack([[i[1:] for i in self.X]])

        Sxy = np.sum(X * self.Y) - (np.sum(X) * np.sum(self.Y))/self.n

        return Sxy


    def SSR (self):
        """
        The sum of squares due to regression

        returns: int
        """
        SSR = self.Syy() - self.RSS()

        return SSR


    def cii (self):
        """
        Gives the c value, √cii

        retruns: array - with variance/covariance matrix
        """

        cii = np.linalg.pinv(self.X.T @ self.X) * self.variance()

        return cii

    def variance (self):
        """
        Variance for the sample, sigma2

        retruns: int
        """
    
        var = self.RSS() / (self.n - self.d - 1)

        return var

    def sigma (self):
        """
        Residual standard error, Sigma

        retruns: int
        """
            
        
        S = np.sqrt(self.variance())

        return S



    def significans (self):
        """
        Test the significans of the regression of all paramters
        put through the F-distribution.

        returns: int - For P-value
        """
       
        F_statistic = (self.SSR()/self.d)/self.sigma()
        p_value = stats.f.sf(F_statistic, self.d, self.n-self.d-1)
       
      
        return p_value

       

    def R2 (self):
        """
        Coefficient of multiple determination, R2

        returns: int
        """

        R2 = self.SSR() / self.Syy()
        return R2
    

    def Significance_individual_variables (self):
        """
        arg: int - For beta-0 (0) to beta-n (n)

        Significance tests on individual variables

        returns: int - For significance for an induvidul variables.
        """
        b_significance = {}
        
        for beta in range(self.d + 1):
            param_statistic = self.coefficients[beta] / (self.sigma() * np.sqrt(self.cii()[beta, beta]))
            p_beta= 2*min(stats.t.cdf(param_statistic, self.n - self.d - 1), stats.t.sf(param_statistic, self.n - self.d - 1))

            b_significance[f"Beta-{beta}"] = p_beta
        
        return b_significance

    

    def p_value_pairs_param (self):
        """
        A function that calculates the Pearson number between all pairs of parameters.
        Pearson correlation number (r)

        Returns: Dict - With an index key form columns of data frame and keys with 
        columns from dataframe with the Pearson nummber
        """
        p_value_pairs = {"Params":[]}
        original_X = self.X
        original_Y = self.Y
        original_d = self.d


        for param in self.data.columns:
            self.params = [param]
            p_value_pairs[param] = []

            for sample in self.data.columns:
                self.sample_size = [sample]
                rho = self.Sxy() / (np.sqrt(self.Sxx() * self.Syy()))
                p_value_pairs[param].append(rho)

            p_value_pairs["Params"].append(param)
            
        self.X = original_X
        self.Y = original_Y
        self.d = original_d



        return p_value_pairs
    
    def confidence_interval_parameters(self):
        """
        Gives the confdence intervall between all predictors

        returns: Dict - With Beta-0, Column from dataframe name for beta-1 to beta-n +- value
        """


        alpha = 1 - self._confi_lvl 
        df = self.n - self.d - 1 
        t = stats.t.ppf(1 - alpha/2, df)
        confidence_beta = {"Intervals" : ["Parameters value", "Error Margen", "Upper", "Lower"]}
# 
        for param in range(len(self.coefficients)):
            se_b = np.sqrt(self.variance() * self.cii()[param, param])
            confidence = (self.coefficients[param, 0], t * se_b)
            
            if param == 0:
                confidence_beta["Beta-0"] = [confidence[0], confidence[1], confidence[0] + confidence[1], confidence[0] - confidence[1]]
            
            else:
                confidence_beta[f"Beta-{param}"] = [confidence[0], confidence[1], confidence[0] + confidence[1], confidence[0] - confidence[1]]

        return confidence_beta
        