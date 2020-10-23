import os
import shutil
import secrets
import pyAesCrypt
import rsa


class SymmetricEncryption:

    @staticmethod
    def to_aes(path):
        """
        encrypts given path with AES Encryption
        Args:
            path (str): path of file
        Returns:
            aes_key (str): aes key
            aes_path (str) aes encrypted file path
        """
        aes_key = secrets.token_hex(30)


        aes_path = path + '.aes'
        pyAesCrypt.encryptFile(path, aes_path, aes_key, bufferSize=64*1024)
        return aes_key, aes_path


class AsymmetricEncryption:

    @staticmethod
    def to_rsa(symmetric_key):
        """
        encrypts given symmetric key with rsa
        Args:
            symmetric_key (str): symmetric key to encrypt
        Returns:
            rsa_key (bytes): rsa asymmetric key
        """
        # generate public and private key for rsa
        public_key, private_key = rsa.newkeys(1024)

        # encrypt using encryption key with public key
        encrypted_symmetric_key = rsa.encrypt(symmetric_key.encode('utf8'), public_key)



        #generate private key
        private_key = private_key.save_pkcs1()

        # concat encrypted_key and private_key
        rsa_key = encrypted_symmetric_key + b"||||||\n" + private_key

        return rsa_key


class Encryption(SymmetricEncryption, AsymmetricEncryption):

    # we can add more as we progress
    symmetric_encryption_mapping = {
        'aes': SymmetricEncryption.to_aes
    }
    asymmetric_encryption_mapping = {
        'rsa': AsymmetricEncryption.to_rsa
    }

    @staticmethod
    def encrypt(path, symmetric_method, asymmetric_method):
        """
        Encrypt file/folder using the specified symmetric method
        Args:
            path (str): file/folder path to encrypt
            symmetric_method (str): symmetric method to use for encryption
            asymmetric_method (str): asymmetric method to use for encrypting symmetric key
        Returns:
            encrypted_path (str): encrypted file/folder path
            encrypted_key_path (str): encrypted key path
        """

        if symmetric_method not in Encryption.symmetric_encryption_mapping:
            raise ValueError("Specified symmetric method does not exist")
        if asymmetric_method not in Encryption.asymmetric_encryption_mapping:
            raise ValueError("Specified asymmetric method does not exist")

        is_folder = os.path.isdir(path)

        if is_folder:
            path = shutil.make_archive(path, 'zip', path)

        symmetric_key, encrypted_path = Encryption.symmetric_encryption_mapping[symmetric_method](path)
        asymmetric_key = Encryption.asymmetric_encryption_mapping[asymmetric_method](symmetric_key)

        # remove asymmetric key if already existed
        asymmetric_key_path = os.path.join(os.path.dirname(os.path.abspath(path)), 'key.pem')
        if os.path.exists(asymmetric_key_path):
            os.remove(asymmetric_key_path)

        with open(asymmetric_key_path, 'wb') as f:
            f.write(asymmetric_key)

        # remove zip folder created for encryption
        if is_folder:
            os.remove(path)

        return encrypted_path, asymmetric_key_path
