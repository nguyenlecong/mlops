# The code base with mlflow
import argparse

import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

import mlflow
import mlflow.sklearn


# Evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    return rmse, mae

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=float, required=False, default=0.5)
    parser.add_argument("--l1_ratio", type=float, required=False, default=0.5)
    args = parser.parse_args()

    # Read the wine-quality csv file
    data = pd.read_csv("winequality-red.csv")

    # Split the data into training and testing sets
    train, test = train_test_split(data, test_size=0.2, random_state=123)

    # The predicted column is "quality"
    train_x = train.drop(['quality'], axis=1)
    test_x = test.drop(['quality'], axis=1)
    train_y = train[['quality']]
    test_y = test[['quality']]

    exp = mlflow.set_experiment(experiment_name='initial_exp')
    with mlflow.start_run(experiment_id=exp.experiment_id):
        model = ElasticNet(alpha=args.alpha, l1_ratio=args.l1_ratio, random_state=123)
        model.fit(train_x, train_y)
        
        predicted = model.predict(test_x)
        rmse, mae = eval_metrics(test_y, predicted)

        print(f'Elasticnet model: alpha={args.alpha}, l1_ratio={args.l1_ratio}')
        print(f'RMSE: {rmse}')
        print(f'MAE: {mae}')
        
        mlflow.log_metric('rmse', rmse)
        mlflow.log_metric('mae', mae)
        mlflow.log_param("alpha", args.alpha)
        mlflow.log_param("l1_ratio", args.l1_ratio)
        mlflow.sklearn.log_model(model, 'elasticnet_model')
