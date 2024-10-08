
import TSXSendTry
import MDriveDome
import time

# https://www.bisque.com/wp-content/scriptthesky/classsky6_dome.html

while True:
    cur_pos = TSXSendTry.TSXGetDome()
    print(cur_pos)
    MDriveDome.MDriveAzGoto(cur_pos)

    time.sleep(1)

