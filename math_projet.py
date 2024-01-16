from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataPreparation:
    def __init__(self, dataset_df):
        """
        Cette classe prend en entrée un chemin de fichier csv.
        Elle split le jeu de donnée en 2 bases 
        + une train 75 %
        + une test 25 %
        Ce 2 bases, la classe va les splits en 2 

        + un vecteur x (qui contient les indexs temporels)
        + un vecteur y (qui contient les valeurs à prédire)
        En tout cette va extraire 4 arrays.
        x_train
        y_train
        x_test
        y_test
        """

        self.dataset_df = pd.read_csv('vente_maillots_de_bain.csv', encoding='ISO-8859-1')

        self.dataset_df['Years'] = pd.to_datetime(self.dataset_df['Years'])
        self.dataset_df['month_name'] = self.dataset_df['Years'].dt.strftime('%B')

        self.dataset_df = pd.get_dummies(self.dataset_df, columns=['month_name'], drop_first=True)
        self.dataset_df.replace({True: 1, False: 0}, inplace=True)
        self.dataset_df['times'] = np.arange(1, len(self.dataset_df) + 1)

        self.dataset_df = pd.DataFrame(self.dataset_df)
        self.prepare_data()

    def prepare_data(self):
        number_of_rows = len(self.dataset_df)
        self.dataset_df["month_name"] = np.arange(0, number_of_rows, 1)

        dataset_train_df = self.dataset_df.iloc[:int(number_of_rows * 0.75)]
        dataset_test_df = self.dataset_df.iloc[int(number_of_rows * 0.75):]

        self.x_train = dataset_train_df.iloc[:, 3:14].values
        #sous dataframe
        self.y_train = dataset_train_df[['Sales']].values

        self.x_test = dataset_test_df.iloc[:, 3:14].values
        #sous dataframe on obtien un array d'array2
        self.y_test = dataset_test_df[['Sales']].values


class Regression:
    def __init__(self, data_preparation_object):
        self.data_preparation_object = data_preparation_object
        self.model = LinearRegression()

        self.model.fit(data_preparation_object.x_train, data_preparation_object.y_train)

        y_train_predicted = self.model.predict(data_preparation_object.x_train)
        mean_train_absolute_error = np.abs(np.mean(y_train_predicted - data_preparation_object.y_train))
        print(f"sur le jeu de train : {mean_train_absolute_error=:.2f}")

        y_test_predicted = self.model.predict(data_preparation_object.x_test)
        mean_test_absolute_error = np.mean(np.abs(y_test_predicted - data_preparation_object.y_test))
        print(f"sur le jeu de test : {mean_test_absolute_error=:.2f}")

        self.show_model_predictions(y_train_predicted, y_test_predicted)

    def show_model_predictions(self, y_train_predicted, y_test_predicted):
        plt.figure(figsize=(15, 6))
        plt.plot(
            self.data_preparation_object.dataset_df['Years'][:len(self.data_preparation_object.x_train)],
            self.data_preparation_object.y_train, "bo-", label='Actual Train Sales')
        plt.plot(
            self.data_preparation_object.dataset_df['Years'][:len(self.data_preparation_object.x_train)],
            y_train_predicted, "b-", label='Predicted Train Sales')

        plt.plot(
            self.data_preparation_object.dataset_df['Years'][len(self.data_preparation_object.x_train):],
            self.data_preparation_object.y_test, "ro-", label='Actual Test Sales')
        plt.plot(
            self.data_preparation_object.dataset_df['Years'][len(self.data_preparation_object.x_train):],
            y_test_predicted, "r-", label='Predicted Test Sales' )

        plt.xlabel('Years')
        plt.ylabel('Sales')
        plt.title('Actual vs Predicted Sales')
        plt.legend()
        plt.show()

# Correct instantiation and usage
dataset_df = pd.read_csv('vente_maillots_de_bain.csv', encoding='ISO-8859-1')
data_preparation_object = DataPreparation(dataset_df)
regression_object = Regression(data_preparation_object)
