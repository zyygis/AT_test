import json
from json.decoder import JSONDecodeError

class Config:

  __configName = "settings.json"
  __config = None

  def __init__(self):
      pass

  def __open_config(self):
    try:
      configFile = open(self.__configName, "r")
      self.__config = configFile
    except:
      print("Could not open ", self.__configName ,"file")
      exit(1)

  def __close_config(self):
    if self.__config:
      self.__config.close() 

  def get_device(self, deviceName):
    self.__open_config()
    try:
      config = json.loads(self.__config.read())
    except JSONDecodeError:
      print("Error loading json file")
      return None

    for dev in config["devices"]:
      if dev["device"] == deviceName:
        device = dev
        self.__close_config()
        return device
    print("Device not found")
    return None

  def get_commands(self, device):
    commands = device["commands"]
    if commands != []:
      # print(commands)
      return commands
    print("No commands found")
    return None

  def get_connection(self, device):
    connection = device["connection"]
    if connection.upper() != "SERIAL" and connection != "SSH":
      print("Connection not found")
      return None
    if connection.upper() == "SERIAL":
      connection = "serialConnection"
    else:
      connection = "sshConnection"
    # print(connection)
    return connection

  def __del__(self):
    # print("Closing config file")
    self.__close_config()
      
      
    


