import modules.connection as connModule
import modules.printToTerminal as printToTerminalModule
import modules.writeToFile as writeToFileModule
import time
class Data:

    __conn = None
    __toFile = None
    __device = None

    def __init__(self, commands, connType, device, address, username, password):
        self.__conn = connModule.Connection(connType, address, username, password, device)
        modem = self.getModem()
        self.__toFile = writeToFileModule.Write(device, modem)
        self.__device = device
        self.processData(commands)

    def processData(self, commands):
        total_commands = len(commands)
        count_pass = 0
        count_fail = 0

        try:
            for index in range(total_commands):
                command = commands[index]["command"]
                expected_result = commands[index]["result"]
                param = commands[index]["param"]

                printToTerminalModule.Terminal.toTerminal(self.__device, command, total_commands, count_pass, count_fail)
                response = self.__conn.sendCommand(command, param)
                command_result = self.checkResponse(response, command, param)
                count_pass, count_fail, test_result = self.checkResult(response, commands, index, count_pass, count_fail)

                printToTerminalModule.Terminal.toTerminal(self.__device, command, total_commands, count_pass, count_fail)
                self.__toFile.writeToFile(command, expected_result, command_result, test_result)

        except Exception as e:
            print("Error: ", e)

    def checkResponse(self,response ,command, param):
        attempts = 0
        command_result = "None"
        response = []
        while attempts < 2:
            response = self.__conn.sendCommand(command, param)
            if 'OK' in response:
                command_result = "OK"
                break;
            elif 'ERROR' in response:
                command_result = "ERROR"
                break;
            else:
                attempts += 1
        return command_result

    def checkResult(self, response, commands, index, count_pass, count_fail):
        if commands[index]["result"] in response:
            test_result = "Passed"
            count_pass += 1
        else:
            count_fail += 1
            test_result = "Failed"
        return count_pass, count_fail, test_result

    def getModem(self):
        response = self.__conn.sendCommand(command = "ATI", param = "")
        modem = []
        for value in response:
            if value == "ATI":
                response.remove(value)
                break
        for index, value in enumerate(response):
            if index == 2:
                break
            modem.append(value)
        return modem

    