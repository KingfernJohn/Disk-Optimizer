import shutil
import os, time
def DISK_OPTIMIZER():
    def storageusage():
        print()
        print("Disk storage usage")
        print()
        what_disk = input("Which disk? - (default -> C):   ")
        print()
        total,used,free = shutil.disk_usage(what_disk +":")
        print("Total:%d GiB" %(total //(2**30)))
        print("Used:%d GiB" %(used //(2**30)))
        print("Free:%d GiB" %(free //(2**30)))
        DISK_OPTIMIZER()
    def cleanup():
        print()
        print("Disk cleaner")
        print()
        clean = os.popen("Cleanmgr.exe").read()
        print("cleaning...")
        print("...")
        print("...")
        print("...")
        print("Finished cleaning the disk!")
        print()
        DISK_OPTIMIZER()
    def defrag():
        print()
        print("Disk defragger")
        print()
        defrag = os.popen("dfrgui.exe C: C/ F/ M")
        print("Press 'Optimize' in the window")
        print()
        time.sleep(5)
        DISK_OPTIMIZER()
    print()
    print("  1  -  Check storage usage")
    print("  2  -  Cleanup disk")
    print("  3  -  Defrag disk")
    print()
    print("  q  -  Quit")
    print()
    tmp_in = input(" --->  ")
    if tmp_in == "1":
        storageusage()
    else:
        if tmp_in == "2":
            cleanup()
        else:
            if tmp_in == "3":
                defrag()
            else:
                if tmp_in == "q":
                    quit()
                else:
                    print()
                    print("ERROR!")
                    print()
                    DISK_OPTIMIZER()
sleep_var = 0.1
print()
print("""  _____ _____  _____ _  __                  ____  _____ _______ _____ __  __ _____ ____________ _____  """)
time.sleep(sleep_var)
print(""" |  __ \_   _|/ ____| |/ /                 / __ \|  __ \__   __|_   _|  \/  |_   _|___  /  ____|  __ \ """)
time.sleep(sleep_var)
print(""" | |  | || | | (___ | ' /      ______     | |  | | |__) | | |    | | | \  / | | |    / /| |__  | |__) |""")
time.sleep(sleep_var)
print(""" | |  | || |  \___ \|  <      |______|    | |  | |  ___/  | |    | | | |\/| | | |   / / |  __| |  _  / """)
time.sleep(sleep_var)
print(""" | |__| || |_ ____) | . \                 | |__| | |      | |   _| |_| |  | |_| |_ / /__| |____| | \ \ """)
time.sleep(sleep_var)
print(""" |_____/_____|_____/|_|\_\                 \____/|_|      |_|  |_____|_|  |_|_____/_____|______|_|  \_\ by KingfernJohn""")
print()
time.sleep(1)
DISK_OPTIMIZER()