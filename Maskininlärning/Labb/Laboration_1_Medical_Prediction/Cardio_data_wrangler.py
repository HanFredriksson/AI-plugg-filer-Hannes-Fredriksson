import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


class Cardio_data:

    def __init__(self, data, bmi_max_min, pressure_values):

        """
        data - A dataframe with data for cardiovascular diseases
        bmi_max_min - list, A max value and a min value
        blood_pressure - dict, with a list of ap_hi max/min and ap_lo max/min values
        encode_data - Stores the encoded data
        train_test_val - Stores the encoded data 
        """

        self.data = data.copy() # Avoid modifying original data
        self.encoded_data = None
        self.train_test_val = None
        self.bmi = bmi_max_min
        self.blood_pressure = pressure_values



    def bmi_calculator_labels(self):
        """
        Bmi calculator
        
        weight - int, in kilograms
        height - int, in centimeters
        bmi_max_min - list, A max value and a min value

        Lebals are BMI: 18-25 normal range, 25-30 over-weight, 31-35 obese (class I), 36-40 obese (class II), 40 above obese (class III)  

        Retrun int - bmi, kg/m^2
        """

        self.data["BMI"] = self.data["weight"] / (self.data["height"] / 100) ** 2
        self.data = self.data[(self.data["BMI"] <= self.bmi[0]) & (self.data["BMI"] >= self.bmi[1])]
        self.data["BMI cat"] = pd.cut(self.data["BMI"], 
                               bins=[18, 25, 30, 35, 40, float("inf")], 
                               labels= ["normal range", "over-weight", "obese (class I)", "obese (class II)", "obese (class III)"])


    def blood_pressure_labels(self):
        """
        Gives you the lables for an range of blood pressure and removes the outliers from data.
        Given the range for the max values and min values of ap_hi and ap_lo

        Labels ap_hi/ap_lo: below 120/80 Healty, 120-129/80, Elvated, 130-139/80-89 Stage 1 hypertension
        above 140/90, Stage 2 hypertension.
        """

        self.data = self.data[
            (self.data["ap_hi"] <= self.blood_pressure["ap_hi"][0]) & 
            (self.data["ap_hi"] >= self.blood_pressure["ap_hi"][1]) & 
            (self.data["ap_lo"] <= self.blood_pressure["ap_lo"][0]) & 
            (self.data["ap_lo"] >= self.blood_pressure["ap_lo"][1])
        ]
        
        for i in self.data.index:
            ap_hi, ap_lo = self.data.at[i, "ap_hi"], self.data.at[i, "ap_lo"]
        
            if ap_hi < 120 and ap_lo < 80:
                self.data.at[i, "BPR"] = "Healty"
            
            elif 120 <= ap_hi <= 129 and ap_lo < 80:
                self.data.at[i, "BPR"] = "Elevated"
            
            elif (130 <= ap_hi <= 139) or (80 <= ap_lo <= 89):
                self.data.at[i, "BPR"] = "Stage 1 hypertension"
        
            elif ap_hi >= 140 or ap_lo >= 90:
                self.data.at[i, "BPR"] = "Stage 2 hypertension"



    def encode_df(self, categorical_columns):
        """
        Encodes categorical columns into one-hot encoded columns.

        categorical_columns - List of column names to be one-hot encoded.
        """

        encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
        one_hot_encoded = encoder.fit_transform(self.data[categorical_columns])
        one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns), index=self.data.index)
        self.encoded_data = pd.concat([self.data.drop(columns=categorical_columns), one_hot_df], axis=1)

    
    def data_spliter(self, val=True):
        """
        Splits the data into training, validation, and test sets.

        If val=True, it splits into three sets. Else, it only splits into train and test.
        """

        X = self.encoded_data.drop("cardio", axis=1)
        y = self.encoded_data["cardio"]
        
        X_train, X_other, y_train, y_other = train_test_split(X, y, test_size=0.33, random_state=42)
        
        if val:
            X_val, X_test, y_val, y_test = train_test_split(X_other, y_other, test_size=0.5, random_state=42)
            self.train_test_val = [X_train, X_val, X_test, y_train, y_val, y_test]
        else:
            X_test, y_test = X_other, y_other
            self.train_test_val = [X_train, X_test, y_train, y_test]


