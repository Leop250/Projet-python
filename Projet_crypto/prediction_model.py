from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def build_model_and_predict(X_train, y_train, X_test):
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)
    return rmse, predictions, model
