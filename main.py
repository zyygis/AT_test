import modules.config as configModule
import modules.connection as connModule
import modules.data as dataModule
import argparse
import sys
import signal
import threading

def main():
    args = argumentParser()
    device, commands, connType = getConfigData(args)
    dataModule.Data(commands, connType, device, args.ADDRESS, args.USERNAME, args.PASSWORD)

def ctrlc_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, ctrlc_handler)
forever = threading.Event()

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--device',dest = "DEVICE", required = True, help = "Device name")
    parser.add_argument('-a','--address',dest = "ADDRESS", required = True, help = "port/Ip address")
    parser.add_argument('-u','--username',dest = "USERNAME", help = "Username")
    parser.add_argument('-p','--password',dest = "PASSWORD", help = "Password")
    args = parser.parse_args()
    return args
    
def getConfigData(args):
    config = configModule.Config()
    config_data = config.get_device(args.DEVICE.upper())
    if config_data == None:
        exit()
    device = config_data["device"]
    commands = config.get_commands(config_data)
    if commands == None:
        exit()
    connType = config.get_connection(config_data)
    if connType == None:
        exit()
    return device, commands, connType

if __name__ == "__main__":
    main()