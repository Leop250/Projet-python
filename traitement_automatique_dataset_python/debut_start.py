from utils import print_colored
from main_anglais import main as main_anglais
from main_version import main_f

def print_bold(text):
    print_colored(f"\033[1m{text}\033[0m", 'white')

while True:
    language = input("Choisir votre langage / choose your language: français / english ").lower()

    if language == "french" or language == "français":
        print_bold("\n\nBienvenue sur le programme qui traite vos données\n")
        main_f()
        break
    elif language == "english":
        print_bold("\n\nWelcome to the program that treats your data\n")
        main_anglais()
        break
    else:
        print_colored("\n\nLanguage not recognized. Please choose either 'french' or 'english'.\n", 'red')
