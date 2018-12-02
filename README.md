# A5_1-in-python
realize A5/1 in python


### Usage: 
```sh
$ python ./A5_1.py help
$ python ./A5_1.py generate KEYSTREAMLENGTH BITSKEY
```
KEYSTREAMLENGTH is the length of the keystream that will be generated. 
BITSKEY is the BITSKEY for the initialization of three registers. Can only be 0s and 1s. 

### For Example:
```sh
$ python ./A5_1.py generate 64
```
This command will generate a keystream with length of 64 bits using the defauly bitskey. 