# False Multiplication Table
from json.encoder import INFINITY
import random
from unicodedata import name

from colorama import Back, Fore, Style
from youtube_dl import main


def falseMultiplication(num):
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
    table = falseMultiplication(number)
    wrongIndex = isCorrrect(table=table, num=number)

    print(f"{Fore.YELLOW}**************************************************\n{Style.BRIGHT}Table Generated by False Multiplication Funciton:- \n{table}{Style.RESET_ALL}{Fore.YELLOW}\n**************************************************{Fore.RESET}")
    print(
        f"{Fore.BLUE}\n************************************************ {Style.BRIGHT}RESULT{Style.RESET_ALL} {Fore.BLUE}********************************************\n{Style.BRIGHT}The number wrong in the table generated by function is {Fore.RED}'{table[wrongIndex]}'{Fore.BLUE}, the correct value should be {Fore.GREEN}'{number*(wrongIndex+1)}'{Fore.RESET}{Fore.BLUE}.{Style.RESET_ALL}{Fore.BLUE} \n****************************************************************************************************\n")
