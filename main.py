# Written by Henry Graham for the purpose of analyzing the contents of my .mbox files.
# Feel free to use the below code in any way possible without the need to release the end product.

import mailbox
import sys
import re


def get_from(mboxfile, fileout):
    locallist = [] # List in which from lines will be held.

    mbox = mailbox.mbox(mboxfile)

    # For each message in the mailbox look at the from line and put into the list.
    for message in mbox:
        frm = message['From']
        locallist.append(frm)
    
    for x in locallist:

        # This try/except is to catch errors pertaining to spam. Some spammers do weird stuff with addresses and names which results in an error
        # being thrown here. I'll review it if it is encountered more
        try:
            match = re.findall(r'[\w\.-]+@[\w\.-]+', x) # 90% sure this regex catches everything, in my test data it caught every email
        except:
            print(x)

        # Yes this is not the ideal way of doing this, I'll fix it if it creates issues later on.
        # The try except is also a result of spam. Similar reason with outputs. Can be resolved by fixing the Header issue encountered in DS1.
        try:
            fileout.writelines(match)
            fileout.write("\n")
        except:
            print(x)

if __name__ == "__main__":
    
    # Getting the path to the .mbox file and creating the .txt file in the same dir as the mbox file
    frmfile = open(sys.argv[1]+ ".fromlist.txt", "w")
    get_from(sys.argv[1], frmfile)

    frmfile.close()

