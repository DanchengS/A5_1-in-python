import fire
import os

SAMPLEKEY = '4B6150645367566B'
SAMPLEKEYBI = '0100101101100001010100000110010001010011011001110101011001101011'

class A5_1(object):

	def help(self):
		print('print something')


	def generate(self, KeyStreamLen, Key = SAMPLEKEYBI):
		output = ''
		X_reg = Key[0:19]
		Y_reg = Key[19:41]
		Z_reg = Key[41:]
		while(KeyStreamLen>0):
			newKey = self.core(X_reg, Y_reg, Z_reg, KeyStreamLen)
			output = output+ newKey[0]
			X_reg = newKey[1:20]
			Y_reg = newKey[20:42]
			Z_reg = newKey[42:]
			KeyStreamLen = KeyStreamLen-1
		return output
	
	def core(self, X_reg, Y_reg, Z_reg, KeyStreamLen):
		if (int(X_reg[8])+int(Y_reg[10])+int(Z_reg[10])) > 1:
			M = '1'
		else:
			M = '0'
		if X_reg[8] == M:
			X_reg = self.shift(X_reg, 'X')
		if Y_reg[10] == M:
			Y_reg = self.shift(Y_reg, 'Y')
		if Z_reg[10] == M:
			Z_reg = self.shift(Z_reg, 'Z')
		#use option 1,2,3 to represent step X, Y, Z

		key = str(int(X_reg[18])^int(Y_reg[21])^int(Z_reg[22]))
		'''
		#for debug purpose
		print('X: '+ X_reg[18])
		print('Y: '+ Y_reg[21])
		print('Z: '+ Z_reg[22])		
		print("There is the key: " + key)
		'''
		return key+X_reg+Y_reg+Z_reg 	#send back the package with first bit as key. 

	def shift(self, stream, option):
		t=''
		if option == 'X': #for x_reg
			t = str(int(stream[13])^int(stream[16])^int(stream[17])^int(stream[18]))
		elif option == 'Y': #for y_reg
			t = str(int(stream[20])^int(stream[21]))
		else:		# for z_reg
			t = str(int(stream[7])^int(stream[20])^int(stream[21])^int(stream[22]))
		output = t+stream[:-1]
		return output





if __name__ == '__main__':
    fire.Fire(A5_1)
