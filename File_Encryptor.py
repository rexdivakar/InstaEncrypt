import hashlib
import pyAesCrypt
import random
import time,os

buffer=64*1024

print('*********************************Fi1e EncRypt0R********************************')
print('''This tool is an Open Source AES Standard encrytion tool, Always make sure to 
backup the encryption key if not the files cannot be reverted back 
for contacts: rexdivakar@gmail.com''')
print('*******************************************************************************')
print('\n1.Encrypt \n2.Decrypt\n')
ip=int(input(('Enter options: ')))
if ip==1:
	fname=input(str('Enter file path (without quotes): '))
	try:
		sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"
		enc_key =  "".join(random.sample(sub_key,30))
		pyAesCrypt.encryptFile(fname,fname+'.aes',enc_key,buffer)
		print('''----------Encryption Sucessfull----------\n \nUser Warning: Make sure to notedown the encryption key,
failure to do so the data cannot be reverted back ever again.''')
		print('\nEncryption Key: ',enc_key)
		now=time.strftime("%H:%M")
		with open('C:\\Intel\\'+'temp_key.txt','a+') as f:
			f.write(fname+'|||'+now+'||||'+enc_key+'\n')
	except:
		print('Invalid File')
	time.sleep(10)

elif ip==2:
	try:
		fname=input(str('Enter file path: '))
		if fname[-4:]=='.aes':
			key=input(str('Enter ur decryption key: '))
			pyAesCrypt.decryptFile(fname,'Op_'+fname[:-4],key,buffer)
			print('Decyrption Succesfull...')
		else:
			print('Invalid Crypto-File')
	except:
		print('Decryption Failed...')

	time.sleep(5)
elif ip==000:
	os.startfile('C:\\Intel\\temp_key.txt')
elif ip==3:
	print('Thanks for using Fi1e EncRypt0R')
	time.sleep(5)
else:
	print('Invalid Input ')
	time.sleep(1)
	