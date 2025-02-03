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
        self._confi_lvl = 0.975
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
        
        Syy = self.n*np.sum(np.square(self.Y)) - (np.square(np.sum(self.Y)))/self.n

        return Syy
    

    def Sxx (self):
        """
        Variance of the independent variable X

        returns: int
        """
        Sxx = self.n*np.sum(np.square(self.X)) - (np.square(np.sum(self.X)))/self.n

        return Sxx
    

    def Sxy (self):
        """
        Covariance between X and Y, cross-product term

        returns: int
        """
        x_2 = np.column_stack([[i[1:] for i in self.X]])

        Sxy = np.sum(x_2 * self.Y) - (np.sum(x_2) * np.sum(self.Y))/self.n

        return Sxy


    def SSR (self):
        """
        The sum of squares due to regression

        returns: int
        """
        SSR = self.RSS() - self.Syy()

        return SSR


    def cii (self):
        """
        Gives the c value, √cii

        retruns: array - with variance/covariance matrix
        """

        cii = np.linalg.pinv(self.X.T @ self.X)

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
       
        # gör en dict som retur
        return p_value

       

    def R2 (self):
        """
        Coefficient of multiple determination, R2

        returns: int
        """

        R2 = self.SSR() / self.Syy()
        return R2
    

    def Significance_individual_variables (self, beta):
        """
        arg: int - For beta-0 (0) to beta-n (n)

        Significance tests on individual variables

        returns: int - For significance for an induvidul variables.
        """
        
        param_statistic = self.coefficients[beta] / (self.sigma() * np.sqrt(self.cii()[beta, beta]))
        p_beta= 2*min(stats.t.cdf(param_statistic, self.n - self.d - 1), stats.t.sf(param_statistic, self.n - self.d - 1))
        
        return p_beta
    
# !!! Self.params måste bort. Får anropa Sxy, Sxx, Syy annorlunda.!!!!
    def p_value_pairs_param (self):
        """
        A function that calculates the Pearson number between all pairs of parameters.
        Pearson correlation number (r)

        Returns: Dict - With an index key form columns of data frame and keys with 
        columns from dataframe with the Pearson nummber
        """
        p_value_pairs = {"Param":[]}
        

        for param in self.data.columns:
            self.params = [param]
            p_value_pairs[param] = []

            for sample in self.data.columns:
                self.sample_size = [sample]
                rho = self.Sxy() / (np.sqrt(self.Sxx() * self.Syy()))
                p_value_pairs[param].append(rho)

            p_value_pairs["Param"].append(param)
            

        return p_value_pairs
    
    def confidence_interval_predictor(self):
        """
        Gives the confdence intervall between all predictors

        returns: Dict - With Beta-0, Column from dataframe name for beta-1 to beta-n +- value
        """


        alpha = 1 - self._confi_lvl 
        df = self.n - self.d - 1 
        t = stats.t.ppf(1 - alpha/2, df)
        confidence_beta ={}

        for param in range(len(self.coefficients)):
            se_b = np.sqrt(self.variance() * self.cii()[param, param])
            confidence = (self.coefficients[param, 0], t * se_b)
            
            if param == 0:
                confidence_beta[f"The Intercept, Beta-0"] = [f"{confidence[0]:.4f} +- {confidence[1]:.4f}"]
            
            else:
                confidence_beta[f"The Parametar {self.data.columns[param - 1]}, Beta-{param}"] = [f"{confidence[0]:.4f} +- {confidence[1]:.4f}"]

        return confidence_beta
        