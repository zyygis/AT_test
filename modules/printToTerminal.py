import sys
import time
import os

class Terminal:

    def toTerminal(device, command, totalCommands, passed_comm, failed_comm):
        progress_1 = 'Device: {}'
        progress_2 = 'Command: {}'
        progress_3 = 'Successful Commands: {}'
        progress_4 = 'Failed Commands: {}'
        progress_5 = 'Total Commands: {}'

        os.system('cls' if os.name == 'nt' else 'clear') #clears terminal
        sys.stdout.write('\033[F' * 10)
        print(progress_1.format(device))
        print(progress_2.format(command))
        sys.stdout.write("\033[92m") #green color
        print(progress_3.format(passed_comm))
        sys.stdout.write("\033[0;0m") #reset color
        sys.stdout.write("\033[1;31m") #red color
        print(progress_4.format(failed_comm))
        sys.stdout.write("\033[0;0m") #reset color
        print(progress_5.format(totalCommands))
        time.sleep(0.02)
