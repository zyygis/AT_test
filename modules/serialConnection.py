import time
import serial

class Connect:

    __ser = None

    def __init__(self, address, username, password, device):
        self.connect(address, username, password)

    def connect(self, address, username, password):
        port = address
        try:
            total_attempts = 3
            for attempt in range(total_attempts):
                ser = serial.Serial(port, baudrate = 115200, timeout = 5)
                self.__ser = ser
        except Exception as e:
            print("Connection error (serial): ", e)
            exit()

    def sendCommand(self, command, param):
        try:
            self.__ser.write(str.encode(command + "\r"))
            time.sleep(0.2)
            self.__ser.write(str.encode(param + "\r"))
            time.sleep(0.2)
            self.__ser.write(str.encode(chr(26)))

            attempts = 0
            while attempts < 30:
                data = self.getResponse()
                if len(data) < 2:
                    time.sleep(5)
                    attempts += 1
                else:
                    break
            return data
        except Exception as e:
            print("Error occured sending command (serial): ", e)
            exit()

    def getResponse(self):
        try:

            terminal_data = self.__ser.readlines()
            String = [x.decode('utf-8') for x in terminal_data]
            String = [x.rstrip('\r\n') for x in String]
            data = []
            for value in String:
                if value:
                    data.append(value)
            return data
        except Exception as e:
            print("Error getting response (serial): ", e)

    def __del__(self):
        if self.__ser:
            self.__ser.close()