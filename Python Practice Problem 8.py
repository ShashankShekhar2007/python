# False Multiplication Table
import random
from unicodedata import name
from colorama import Fore, Back, Style
from youtube_dl import main


def rohanMultiplication(num):
    wrong = random.randint(0, 9)
    table = [i*num for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(1, 5)
    return table


def isCorrrect(table, num):
    for i in range(0, 10):
        if table[i] != num*(i+1):
            return i
    return None


if __name__ == "__main__":

    number = int(input(
        f"\n{Fore.BLUE}********************************************* {Style.BRIGHT}\nEnter A Number: {Style.RESET_ALL}"))
    print(f"{Fore.BLUE}*********************************************\n")
    table = rohanMultiplication(number)
    wrongIndex = isCorrrect(table=table, num=number)

    print(f"{Fore.YELLOW}*********************************************\n{Style.BRIGHT}Table of Rohan Das's Funciton:- \n{table}{Style.RESET_ALL}{Fore.YELLOW}\n*********************************************{Fore.RESET}")
    print(
        f"{Fore.BLUE}\n******************************************* {Style.BRIGHT}RESULT{Style.RESET_ALL} {Fore.BLUE}***************************************\n{Style.BRIGHT}The number wrong in the table of Rohan Das is {Fore.RED}'{table[wrongIndex]}'{Fore.BLUE}, the correct value should be {Fore.GREEN}'{number*(wrongIndex+1)}'{Fore.RESET}{Fore.BLUE}.{Style.RESET_ALL}{Fore.BLUE} \n******************************************************************************************\n")
