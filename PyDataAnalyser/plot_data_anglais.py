# plot_data.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils import print_colored

def create_plot(data):
    print("To create a plot, please specify the columns to use.")

    while True:
        try:
            x_col = input("Enter the column name for the x-axis: ")
            y_col = input("Enter the column name for the y-axis: ")
            if x_col in data.columns and y_col in data.columns:
                break
            else:
                raise ValueError("Invalid columns, please try again.")
        except ValueError as e:
            print_colored(str(e), 'red')
            print_colored("Please try again.", 'yellow')

    while True:
        print("Choose the type of plot:")
        print("1. Histogram")
        print("2. Boxplot")
        print("3. Scatterplot")
        print("4. Quit")
        
        plot_choice = input("Enter the number of your choice: ")
        
        if plot_choice == '1':
            plt.figure(figsize=(10, 6))
            sns.histplot(data[x_col], kde=True)
            plt.title(f"Histogram of {x_col}")
            plt.xlabel(x_col)
            plt.ylabel("Frequency")
            plt.show()
        elif plot_choice == '2':
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=data[x_col], y=data[y_col])
            plt.title(f"Boxplot of {x_col} and {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        elif plot_choice == '3':
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=data[x_col], y=data[y_col])
            plt.title(f"Scatterplot of {x_col} and {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        elif plot_choice == '4':
            break
        else:
            print_colored("Invalid choice. Please enter a valid number.", 'red')
