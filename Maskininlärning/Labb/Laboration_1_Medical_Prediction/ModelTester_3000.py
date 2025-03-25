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
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report


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
    def __init__(self, data, param_grids, save_result_path, scoring, models):
        self.data = data
        self.pipelines = None
        self.param_grids = param_grids
        self.hyperparams_result_df = None
        self.path = save_result_path
        self.scoring = scoring
        self.models = models

    
    def make_pipelines(self, voting_pipeline = False):
        pipelines = []

        if voting_pipeline:
            for model in self.hyperparams_result_df:
                if pipelines[1][1] is not self.models.keys():
                    model_class = self.models[model["Model"]]  # Converts string into the actual class
                    model_instance = model_class(**self.hyperparams_result_df["Hyperparams"])
                
                    if model["Scaler"] == "Stdz":
                        pipelines.append(Pipeline([("scaler", StandardScaler()), ("model", model_instance)]))
                    
                    elif model["Scaler"] == "Norm":
                        pipelines.append(Pipeline([("scaler", MinMaxScaler()), ("model", model_instance)]))
                else:
                    break

        else:
            for name, model in self.models.items():
                pipelines[f"{name}_Stdz"] = Pipeline([("scaler", StandardScaler()), ("model", model)])
                pipelines[f"{name}_Norm"] = Pipeline([("scaler", MinMaxScaler()), ("model", model)])

        return pipelines


    def hyperparams_ModelScores(self):
        self.pipelines = self.make_pipelines()        
        sorting_keys = {"precision": "Precisison", "f1": "F1 Score", "recall": "Recall"}
        grid_results = []
        
        if os.path.exists(self.path): # len(self.model) <= len(self.hyperparams_result_df)
            self.hyperparams_result_df = pd.read_csv(self.path)
            self.hyperparams_result_df["Hyperparams"] = self.hyperparams_result_df["Hyperparams"].apply(json.loads)
            print("Loaded GridSearch result csv.")

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

                    best_params = grid_search.best_params_

                    # Remove "model__" from parameter keys and format as a string
                    clean_params = ", ".join([f"{k.replace('model__', '')}: {v}" for k, v in best_params.items()])

                    grid_results.append({
                        "Model": name.split("_")[0],
                        "Dataset": f"Dataset_{i+1}",
                        "Scaler": name.split("_")[-1],
                        "Hyperparams": clean_params,
                        "Recall": recall_score(data[3], y_pred),
                        "F1 Score": f1_score(data[3], y_pred),
                        "Precision" : precision_score(data[3], y_pred)
                    })
                    
                elapsed_time = time.time() - start_time
                minutes = int(elapsed_time // 60)
                seconds = int(elapsed_time % 60)
                print(f"Time taken: {minutes}m {seconds}s for model {name}")

            if grid_results:
                self.hyperparams_result_df = pd.DataFrame(grid_results)
                save_df = pd.DataFrame(grid_results)
                save_df["Hyperparams"] = save_df["Hyperparams"].apply(json.dumps)
                save_df.to_csv(self.path, index=False)
                print("GridSearch completed and results saved.")
        
        self.hyperparams_result_df.sort_values(by=[sorting_keys[self.scoring[0]]], ascending=False)


    def hyper_voter(self):
        
        self.pipelines = self.make_pipelines(voting_pipeline=True)
        X_train, X_test, y_train, y_test = self.data


        model_voter = VotingClassifier(estimators=[
            self.pipelines], 
            voting="hard")

        model_voter.fit(X_train, y_train)
        vote_pred = model_voter.predict(X_test)
        results = {
                    "Model": "Voting Classifier",
                    "Dataset": f"Dataset_{i+1}",
                    "Recall": recall_score(y_test, vote_pred),
                    "F1 Score": f1_score(y_test, vote_pred),
                    "Precision" : precision_score(y_test, vote_pred)
                    }

    def run_best_model(self):
        pass