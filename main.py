import mailbox
import sys
import re


def get_from(mboxfile, fileout):
    locallist = []
    mbox = mailbox.mbox(mboxfile)
    for message in mbox:
        frm = message['from']
        locallist.append(frm)
    
    for x in locallist:
        match = re.findall(r'[\w\.-]+@[\w\.-]+', x) # 90% sure this regex catches everything, in my test data it caught every email

        # Yes this is not the ideal way of doing this, I'll fix it if it creates issues later on.
        try:
            fileout.writelines(match)
            fileout.write("\n")
        except:
            print(x)


if __name__ == "__main__":

    frmfile = open(sys.argv[1]+ "frmlist.txt", "w")

    get_from(sys.argv[1], frmfile)

    frmfile.close()

