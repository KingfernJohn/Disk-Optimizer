import shutil, os, time
def DISK_OPTIMIZER():
    def storageusage():
        print("\nDisk storage usage\n")
        what_disk = input("Disk >>> ")
        print()
        total,used,free = shutil.disk_usage(what_disk +":")
        print("Total:%d GiB" %(total //(2**30)))
        print("Used:%d GiB" %(used //(2**30)))
        print("Free:%d GiB" %(free //(2**30)))
        DISK_OPTIMIZER()
    def cleanup():
        print("\nDisk cleaner\n")
        clean = os.popen("Cleanmgr.exe").read()
        print("cleaning...")
        print("Finished cleaning the disk!\n")
        DISK_OPTIMIZER()
    def defrag():
        print("\nDisk defragger\n")
        defrag = os.popen("dfrgui.exe C: C/ F/ M")
        print("Press 'Optimize' in the window\n")
        time.sleep(5)
        DISK_OPTIMIZER()
    print("\n  1  -  Check storage usage")
    print("  2  -  Cleanup disk")
    print("  3  -  Defrag disk")
    print("  q  -  Quit\n")
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
                    print("\nERROR\n")
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
