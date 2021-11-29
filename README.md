# Automation of AT commands testing  

## Python libraries  

To be able to use this test download these libraries with [pip](https://pip.pypa.io/en/stable/):  
(If you dont have python [click here](https://realpython.com/installing-python/))  
  
1.**Paramiko**  
[pip install paramiko](https://www.paramiko.org/installing.html)  
  
2.**Pyserial**  
[python -m pip install pyserial](https://pyserial.readthedocs.io/en/latest/pyserial.html)  

## Example of config file: settings.json

```json
{
  "devices" : 
  [
    { 
      "device": "DEVICE NAME", Device name on which AT commands will be tested.
      "connection" : "CONNECTION TYPE", Connection type SSH or SERIAL.
      "commands": 
      [
        {
          "command": "COMMAND", AT command.
          "param": "PARAMETER", Command parameter if there is none leave "".
          "result": "EXPECTED RESULT" What result you expect to be OK or ERROR.
        },
        {
          "command": "ATI",
          "param": "",
          "result": "OK"
        }
      ]
    }
    {
      "device": "RUTX11",
      "connection" : "SSH",
      "commands": 
      [
        {
          "command": "ATE1",
          "param": "",
          "result": "OK"
        },
        {
          "command": "AT+CMGS=\"+37060000000\"",
          "param": "Sample text",
          "result": "ERROR"
        }
      ]
    }
  ]
}
```

## Instructions how to use

1. Fill in needed information to config file as shown above.
2. Go to modules folder open writeToFile.py Module, in 15 line write path where .csv files will be created.
3. Open terminal go to AT_test folder example( user@computer123:~/Documents/python/AT_test$ )
4. Command line arguments:  
  -d / --device Device name  
  -a / --address port/Ip address  
  -u / --username Username  
  -p , --password Password  
  
  -d(device name) and -a(port or ip address) is required arguments to start test.  
5. In terminal type:  
  python3 main.py -a /dev/ttyUSB3 -d trm240      ---this is example for SERIAL connection type.   
  python3 main.py -a 192.168.1.1 -d rutx11 -u admin -p admin      ---this is example for SSH connection type.  
