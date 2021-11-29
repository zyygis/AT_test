from datetime import datetime
import csv

class Write:

    __csvFile = None
    __file = None

    def __init__(self, device, modem):
        self.openFile(device, modem)

    def openFile(self,device, modem):
        filename = device + f" {datetime.now():%Y-%m-%d_%H:%M:%S}.csv"
        fieldnames = ['Command', 'Expected result', 'Result', 'Test result']
        self.__file = open(r"/PATH/WHERE/TO/WRITE/CSV/FILE " + filename, 'x')
        try:
            self.writeModem(modem)
            self.__csvFile = csv.DictWriter(self.__file, fieldnames = fieldnames)
            self.__csvFile.writeheader()
        except Exception as e:
            print("Could not write to .csv file:", e )
            exit()

    def writeToFile(self, command, expected_result, result, test_PF):
        try:
            self.__csvFile.writerow({'Command': command, 'Expected result': expected_result, 'Result': result, 'Test result': test_PF})
        except Exception as e:
            print("Error writing to file: ", e)
            exit()

    def writeModem(self, modem):
        field = ['Manufacturer', 'Model']
        write = csv.writer(self.__file)
        write.writerow(field)
        write.writerow(modem)
        write.writerow([' '])

    def __del__(self):
        self.__file.close()