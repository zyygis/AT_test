import paramiko
import time

class Connect:

    __sshConn = None
    __transport = None
    __session = None

    def __init__(self, address, username, password, device):
        self.connect(address, username, password,)
        self.checkDevice(device)
        self.connectToSocat()

    def connect(self, address, username, password):
        host = address
        user = username
        passw = password

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            total_attempts = 3
            for attempt in range(total_attempts):
                ssh.connect(hostname = host, username = user, password = passw)
                self.__sshConn = ssh
                self.__transport = ssh.get_transport()
                self.__session = self.__transport.open_session()
                self.__session.setblocking(0)
                self.__session.get_pty()
                self.__session.invoke_shell()
                self.waitForTerminal()
                self.__session.recv(9999)
                return
        except Exception as e:
            print("Connection error (ssh): ", e)
            exit()

    def connectToSocat(self):
        self.sendCommand("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane", "")

    def checkDevice(self, device):
        response = self.sendCommand("uci get system.system.routername", "")
        device_name  = response[1]
        if device != device_name[:6]:
            print("Connected device:", device_name)
            exit()

    def waitForTerminal(self):
        attempts=0 
        while not self.__session.recv_ready():
            time.sleep(1)
            attempts += 1
            if attempts > 185:
                break

    def sendCommand(self, command, param):
        try:
            self.__session.send(command + "\r")
            time.sleep(0.2)
            self.__session.send(param + "\r")
            time.sleep(0.2)
            self.__session.send(chr(26))
            time.sleep(0.2)
            data = self.getResponse()
            return data
        except Exception as e:
            print("Error occured sending command (ssh): ",e)

    def getResponse(self):
        time.sleep(0.2)
        try:
            self.waitForTerminal()
            terminal_data = self.__session.recv(9999).decode('utf-8').rstrip('\r').split('\n')
            decoded_data = []
            for value in terminal_data:
                if value:
                    decoded_data.append(value)
            return decoded_data
        except Exception as e:
            print("Couldn't get response from device (ssh): ", e)
            decoded_data = None
        return decoded_data

    def __del__(self):
        if self.__sshConn:
            self.__sshConn.close()
        if self.__transport:
            self.__transport.close()