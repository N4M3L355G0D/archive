import os


def main():
    if os.path.exists("./receipt.py"):
        import receipt
    else:
        print("the required file, receipt.py, does not exist, so quitting!")
        return 2
    
    receipt.cmdline()

main()
