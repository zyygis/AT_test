
class Connection:

    __connectionFile = None

    def __init__(self, connType, address, username, password, device):
        self.__connectionFile = self.__connection(connType, address, username, password, device)
        if not self.__connectionFile:
            exit("Unable to load connection file")

    def __connection(self, connType, address, username, password, device):
        module = None
        try:
            module = __import__('modules.{type}'.format(type = connType), fromlist=['modules'])
            return module.Connect(address, username, password, device)
        except Exception as e:
            print("Error loading connection module:", e)
            exit()

    def sendCommand(self, command, param):
        return self.__connectionFile.sendCommand(command, param)

    # def getResponse(self,command, param):
    #     return self.__connectionFile.getResponse(command, param)

    # def getModem(self):
    #     return self.__connectionFile.getModem()