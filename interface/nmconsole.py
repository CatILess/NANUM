# Program : nmconsole.py
# Developer : Cat|less
# Python 3.7.3

# Import Modules
import os
from ui_tools.ui_basic import strStyle

# Basic UI Functions
def banner():
    banner_context = """
███╗   ██╗ █████╗ ███╗   ██╗██╗   ██╗███╗   ███╗
████╗  ██║██╔══██╗████╗  ██║██║   ██║████╗ ████║
██╔██╗ ██║███████║██╔██╗ ██║██║   ██║██╔████╔██║
██║╚██╗██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║    
██║ ╚████║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║        
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝  
      ┌┐ ┬ ┬  ┌─┐┌─┐┌┬┐ │ ┬  ┌─┐┌─┐┌─┐
      ├┴┐└┬┘  │  ├─┤ │  │ │  ├┤ └─┐└─┐
      └─┘ ┴   └─┘┴ ┴ ┴  │ ┴─┘└─┘└─┘└─┘
                                     version 0.4
    """
    return banner_context
def help():
    help_context = """
Basic Commands
===============

Command\t\t\tDescription
-------\t\t\t-----------
?      \t\t\tHelp Menu
banner \t\t\tDisplay a NANUM Main Banner
sample \t\t\tUse Sample Modules

    """
    return help_context

# Module Control Functions
def status():
    stat_context = """
 [*] NANUM STATUS SCREEN
   [+] ACTIVE
""" + "      Modules" + """
   [-] INACTIVE 
""" + "      Modules\n"
    return stat_context[1:]

# Sub Funstions
def getStat():
    pass

#################
# Main Function #
#################

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\','/') + "/../"

    # Printing Banner
    print(banner())

    # Command Control
    cmd = ""
    while cmd not in ["q","quit","exit"]:
        cmd = raw_input(strStyle("nmconsole > ",["CYAN"]))
        cmd = cmd.lower().strip()

        if cmd in ["?","help","h"]:
	    print(help())
        elif cmd in ["banner"]:
	    print(banner())
        elif cmd in ["status","stat"]:
	    print(status())	
        elif cmd in ["control"]:
	    pass	
        elif "sample" in cmd:
            argv = cmd.split(" ")
            if len(argv) != 3:
                os.system("bash "+ROOT_PATH+"sample/start_end.sh")
            else:
                os.system("bash "+ROOT_PATH+"sample/start_end.sh "+argv[1]+" "+argv[2])
            # elif cmd in [""]:
	    #     pass	
	    # elif cmd in [""]:
	    #     pass
