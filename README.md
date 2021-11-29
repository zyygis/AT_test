# Automation of AT commands testing  

## Python libraries  

To be able to use this test we will need to download few libraries with [pip](https://pip.pypa.io/en/stable/):  
  
1.**Paramiko**  
[pip install paramiko](https://www.paramiko.org/installing.html)  
  
2.**Pyserial**  
[python -m pip install pyserial](https://pyserial.readthedocs.io/en/latest/pyserial.html)  

## Example of config file: setting.json

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

## Instructions how to use this test

1. Fill in needed information to config file.
2. 
