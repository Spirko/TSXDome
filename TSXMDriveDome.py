
import TSXSendTry
import MDriveDome
import time

# https://www.bisque.com/wp-content/scriptthesky/classsky6_dome.html

user_input = input("Do I need to home the dome? [y/N]")

if "y" in user_input.lower():
    print("""To save time:
     * Slew so the tab is just to the left of the home tower.""")
    input()
    MDriveSend("AHM 3")
    MDriveSend("AP=-539427")

while True:
    cur_pos = TSXSendTry.TSXGetDome()
    print(cur_pos)
    MDriveDome.MDriveAzGoto(cur_pos)

    time.sleep(1)
