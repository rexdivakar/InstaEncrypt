import pyAesCrypt
import rsa


class SymmetricDecryption:

    @staticmethod
    def from_aes(aes_key, path):
        aes_decrypted_path = path[:-4]
        pyAesCrypt.decryptFile(path, aes_decrypted_path, aes_key, bufferSize=64*1024)
        return aes_decrypted_path


class AsymmetricDecryption:

    @staticmethod
    def from_rsa(rsa_key):
        # generate symmetric key from rsa_key
        encrypted_key = rsa_key.split(b"||||||\n", maxsplit=1)[0]
        private_key = rsa.PrivateKey.load_pkcs1(rsa_key)
        return rsa.decrypt(encrypted_key, private_key).decode('utf8')


class Decryption(SymmetricDecryption, AsymmetricDecryption):

    symmetric_decryption_mapping = {
        'aes': SymmetricDecryption.from_aes
    }
    asymmetric_decryption_mapping = {
        'rsa': AsymmetricDecryption.from_rsa
    }

    @staticmethod
    def decrypt(path, asymmetric_key_path, symmetric_method, asymmetric_method):

        if symmetric_method not in Decryption.symmetric_decryption_mapping:
            raise ValueError("Specified symmetric method does not exist")
        if asymmetric_method not in Decryption.asymmetric_decryption_mapping:
            raise ValueError("Specified asymmetric method does not exist")

        # read key from asymmetric_key_path
        with open(asymmetric_key_path, mode='rb') as f:
            asymmetric_key = f.read()

        symmetric_key = Decryption.asymmetric_decryption_mapping[asymmetric_method](asymmetric_key)
        decrypted_path = Decryption.symmetric_decryption_mapping[symmetric_method](symmetric_key, path)

        return decrypted_path
