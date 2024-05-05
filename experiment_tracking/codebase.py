# Code base: code mà trước đây vẫn thực hiện trianing bình thường mà chưa có mlflow

import argparse

import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error


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

    model = ElasticNet(alpha=args.alpha, l1_ratio=args.l1_ratio, random_state=123)
    model.fit(train_x, train_y)
    
    predicted = model.predict(test_x)
    rmse, mae = eval_metrics(test_y, predicted)

    print(f'Elasticnet model: alpha={args.alpha}, l1_ratio={args.l1_ratio}')
    print(f'RMSE: {rmse}')
    print(f'MAE: {mae}')
    