from encoder_variable_anglais import *
from load_data_anglais import *
from plot_data_anglais import *
from prepare_data_anglais import *
from save_data_anglais import *
from test_anglais import *
from utils_anglais import *

def main():
    data, filename = load_data_a()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Display dataset information")
        print("2. Prepare dataset (Remove NaNs, duplicates, and rename columns)")
        print("3. Rename columns")
        print("4. Remove duplicates")
        print("5. Group columns")
        print("6. Create a time index column")
        print("7. Create a plot")
        print("8. Remove columns")
        print("9. Encode variables")
        print("10. Handle outliers")
        print("11. Save modifications")
        print("12. Quit")

        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            show_info(data)
        elif choice == '2':
            data = prepare_data(data)
        elif choice == '3':
            rename_column(data)
        elif choice == '4':
            remove_duplicates(data)
        elif choice == '5':
            merge_columns(data)
        elif choice == '6':
            create_time_index(data)
        elif choice == '7':
            create_plot(data)
        elif choice == '8':
            data = remove_columns(data)
        elif choice == '9':
            encoder_variables(data)
        elif choice == '10':
            data = handle_outliers(data)
        elif choice == '11':
            save_data(data, filename)
        elif choice == '12':
            print("Thank you for using the tool.")
            break
        else:
            print_colored("Invalid choice. Please enter a valid number.", 'red')

if __name__ == "__main__":
    main()
