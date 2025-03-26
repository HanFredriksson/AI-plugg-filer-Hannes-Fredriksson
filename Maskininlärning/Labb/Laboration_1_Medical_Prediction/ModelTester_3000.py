import pandas as pd
import time
import os
import json
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report, ConfusionMatrixDisplay, confusion_matrix


class ModelTester_3000:
    """
    This tester is made to get the hyperparams, testing against a Voting Classifier and picking the best model. 
    The tester is meant to be used with a data sets with diffrant features from the same original datasets. 
    Possible to weight the scoring according to preferences.

    data - list, A list of data sets with diffrent features.
    
    pipelines - Pipeline, picked models to run and there scalers.
    
    param_grids - dict, All the parameters to run in the GridSearch. 
    
    hyperparams_df - Saves the hyperparameters and test results for each model in the GridSearch
    
    path - Which path to save the CSV file with all of the results and hyper parameters 
    
    scoring - list, What scoring to use to evalueta the models. The first value in the list is used for refittng
    and sorting the for the best preforming model. Example: If recall is most imoprtant. Set racall at index [0]
    of the list.

    """
    def __init__(self, data, param_grids, save_result_path, scoring):
        self.data = data
        self.pipelines = None
        self.param_grids = param_grids
        self.hyperparams_result_df = pd.DataFrame()
        self.path = save_result_path
        self.scoring = scoring
        self.models = {
            "SVM": SVC(),
            "Logistic Regression": LogisticRegression(),
            "Decision Tree": DecisionTreeClassifier(),
            "Random Forest": RandomForestClassifier()
            }


    
    def make_pipelines(self, voting_pipeline = False):

        """
        This make pipeline for a GridSearch or a VotingClassifier.
        The pipeline for VotingClassifier makes sure that only the model gets used once. Also that the correct scaler is used
        For the GridSerch pipeline it makes on pipeline for each scaler. 
        Scalesr used are StandarScaler(Stdz) and MinMaxScaler(Norm).

        voting_pipeline - boolean, To get an pipline for VotingClassifier = True. 
                          Defualt = False, runs a pipeline for a Gridsearch 
        """
        pipelines = {} if not voting_pipeline else []

        if voting_pipeline:
            for _, model in self.hyperparams_result_df.iterrows():
                if self.models[model["Model"]] in [pipe.steps[1][1].__class__.__name__ for pipe in pipelines]:
                    continue
                
                model_class = self.models[model["Model"]] 
                model_instance = model_class(self.hyperparams_result_df["Hyperparams"])
                
                if model["Scaler"] == "Stdz":
                    pipelines.append(Pipeline([("scaler", StandardScaler()), ("model", model_instance)]))
                    
                elif model["Scaler"] == "Norm":
                    pipelines.append(Pipeline([("scaler", MinMaxScaler()), ("model", model_instance)]))
                
                elif len(pipelines) >= len(self.models.keys()):
                    break

        else:
            for name, model in self.models.items():
                pipelines[f"{name}_Stdz"] = Pipeline([("scaler", StandardScaler()), ("model", model)])
                pipelines[f"{name}_Norm"] = Pipeline([("scaler", MinMaxScaler()), ("model", model)])

        return pipelines
    

    def result_handler(self, results, save_to_file=False, load_file=False):
        """
        Rasult handler makes an data frame for results. Can save data frame to CSV file and load the CSV file.
        
        results - DataFrame, With the score results from ran models there hyper parameters, scaler and name of model
        save_to_file - Boolean, To save to a CSV file = True 
                       Defualt = False
        load_file - Boolean, To load file that been previously saved = True
                    Default = False
        """
        sorting_keys = {"precision": "Precisison", "f1": "F1 Score", "recall": "Recall"}

        if save_to_file:
            self.hyperparams_result_df["Hyperparams"] = self.hyperparams_result_df["Hyperparams"].apply(json.dumps)
            self.hyperparams_result_df.to_csv(self.path, index=False) 
            print("Results saved to file.")

        if load_file:
            self.hyperparams_result_df = pd.read_csv(self.path)
            self.hyperparams_result_df["Hyperparams"] = self.hyperparams_result_df["Hyperparams"].apply(json.loads)
            print("Loaded results from file.")

        else: 
            self.hyperparams_result_df = pd.concat(self.hyperparams_result_df, results, ignore_index=True)
            self.hyperparams_result_df.sort_values(by=[sorting_keys[self.scoring[0]]], ascending=False, inplace=True)
            self.hyperparams_result_df.reset_index(inplace=True)
            print("Results added to class hyper parameters data frame")



    def model_hyperparams_scores(self):
        """
        Runs the picked models and gives each an F1, Precision, Recall score
        Gathers the hyper parametars and store in an data frame.
        """
        self.pipelines = self.make_pipelines()        
        grid_results = []
        
        if len(self.model) <= len(self.hyperparams_result_df):
            self.result_handler(load_file=True)

        else:
            for name, model in self.pipelines.items():
                start_time = time.time() 
                grid_search = GridSearchCV(
                    model,
                    self.param_grids[name.split("_")[0]],
                    scoring=self.scoring,
                    refit=self.scoring[0],
                    cv=3,
                    n_jobs=-1
                )
        
                for i, data in enumerate(self.data):
                    grid_search.fit(data[0], data[1])  
                    y_pred = grid_search.predict(data[2])  

                    grid_results.append({
                        "Model": name.split("_")[0],
                        "Dataset": f"Dataset_{i+1}",
                        "Scaler": name.split("_")[-1],
                        "Hyperparams": grid_search.best_params_,
                        "Recall": recall_score(data[3], y_pred),
                        "F1 Score": f1_score(data[3], y_pred),
                        "Precision" : precision_score(data[3], y_pred)
                    })
                    
                elapsed_time = time.time() - start_time
                minutes = int(elapsed_time // 60)
                seconds = int(elapsed_time % 60)
                print(f"Time taken: {minutes}m {seconds}s for model {name}")

            if grid_results:
                grid_results_df = pd.DataFrame(grid_results)
                self.result_handler(grid_results_df)
        

    def hyper_voter(self, predict=False):
        """
        Runs an VotingClassfier and stores the test results in an Data frame. 
        Models run is picked from the top models from an GridSearch and there hyper parameters
        Can also just be run as model if it is the best model to predict with. 
        
        append results - Boolean, use as a predictor = True
                         Default = False
        """
        self.pipelines = self.make_pipelines(voting_pipeline=True)
        X_train, X_test, y_train, y_test = self.data # How do we pick the data set we want 


        model_voter = VotingClassifier(estimators=
            self.pipelines, 
            voting="hard")

        model_voter.fit(X_train, y_train)
        vote_pred = model_voter.predict(X_test)
        results = {
                    "Model": "Voting Classifier",
                    "Dataset": f"Dataset_{i+1}", # Get away to pick dataset
                    "Recall": recall_score(y_test, vote_pred),
                    "F1 Score": f1_score(y_test, vote_pred),
                    "Precision" : precision_score(y_test, vote_pred)
                    }
        
        if predict:
            return vote_pred
        
        else:
            results_df = pd.DataFrame(results)
            self.result_handler(results_df)
            print("All models has run. Good time to save results to file.")
            

    
    def run_best_model(self):
        """
        Takes the best model and runs it. Returns a calssifactio report and confusion matrix
        """

        X_train, X_test, y_train, y_test = self.data
        best_model_row = self.hyperparams_result_df.iloc[0]  

        if  self.hyperparams_result_df.loc[0]["Model"] == "Voting Classifier":
            y_pred = self.hyper_voter(predict=False)


        else:
            best_model = self.models[best_model_row["Model"]]
            best_scaler = best_model_row["Scaler"]
            best_params = best_model_row["Hyperparams"]
            
            scaler = StandardScaler() if best_scaler == "Stdz" else MinMaxScaler()
            best_model_instance = best_model(**best_params)

            best_pipeline = Pipeline([
                ("scaler", scaler),
                ("model", best_model_instance)
            ])


            best_pipeline.fit(X_train, y_train)
            y_pred = best_pipeline.predict(X_test)

        
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(cm)

        print(f"The best model is: {best_model_row["Model"]}\n Scored by: {self.scoring[0]}")
        print(f"Results: {classification_report(y_test, y_pred)}"), disp.plot()
        

