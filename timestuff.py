import time


def countdown():        # T-10; 9; 8; 7; 6; (Engine Ignition); 5; 4; 3; 2; 1. Lift Off!!!
    print("Welcome to timer!")

    def countdown(t):

        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        print('Yeet!')

    t = input("Enter the time in seconds: ")

    countdown(int(t))
