# Program : ui_basic.py
# Developer : Cat|less
# Python 3.7.3

# Import Modules

# Basic Variables
C_END = "\033[0m"
C_UNDER = "\033[4m"
C_CYAN = "\033[36m"
C_RED = "\033[31m"
C_GREEN  = "\033[32m"
C_PURPLE = "\033[35m"
C_YELLOW = "\033[33m"

# UI Functions
def strStyle(string, style_lst):
    if style_lst == []:
        return "? Style: UNDER,CYAN,RED,GREEN,PURPLE,YELLOW"

    for style in style_lst:
        style = style.upper()
        if style == "UNDER":
            string = C_UNDER + string
        elif style == "CYAN":
            string = C_CYAN + string
        elif style == "RED":
            string = C_RED + string
        elif style == "GREEN":
            string = C_GREEN + string
        elif style == "PURPLE":
            string = C_PURPLE + string
        elif style == "YELLOW":
            string = C_YELLOW + string
    string = string + C_END

    return string

# Test Main Function
if __name__ == "__main__":
    print(strStyle("TEST",["RED"]))
