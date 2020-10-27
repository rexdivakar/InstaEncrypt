import pyAesCrypt
import rsa


def from_rsa(rsa_key):
    """
    decrypts given rsa_key with rsa
    Args:
        rsa_key (bytes): rsa key
    Returns:
        (str): decrypted symmetric key
    """
    # generate symmetric key from rsa_key
    encrypted_key = rsa_key.split(b"||||||\n", maxsplit=1)[0]
    private_key = rsa.PrivateKey.load_pkcs1(rsa_key)
    return rsa.decrypt(encrypted_key, private_key).decode('utf8')


def from_aes(aes_key, path):
    """
    decrypts path with aes_key
    Args:
        aes_key (str): aes key for decryption
        path (str): path to decrypt
    Returns:
        aes_decrypted_path (str): decrypted aes path
    """
    aes_decrypted_path = path[:-4]
    pyAesCrypt.decryptFile(path, aes_decrypted_path, aes_key, bufferSize=64*1024)
    return aes_decrypted_path


def decrypt(path, asymmetric_key_path, symmetric_method, asymmetric_method):
    """
    Decrypt file/folder using the given method
    Args:
        path (str): path to file/folder to decrypt
        asymmetric_key_path (str): asymmetric key path
        symmetric_method (str): symmetric method to use for decryption
        asymmetric_method (str): asymmetric method to use for decryption
    Returns:
        isSuccessful (bool): whether decryption is successful or not
        decrypted_path (str, None): file/folder path after decryption
    """

    decrypted_path = None
    is_successful = True

    try:

        symmetric_decryption_mapping = {
            'aes': from_aes
        }
        asymmetric_decryption_mapping = {
            'rsa': from_rsa
        }

        if symmetric_method not in symmetric_decryption_mapping:
            raise ValueError("Specified symmetric method does not exist")
        if asymmetric_method not in asymmetric_decryption_mapping:
            raise ValueError("Specified asymmetric method does not exist")

        # read key from asymmetric_key_path
        with open(asymmetric_key_path, mode='rb') as f:
            asymmetric_key = f.read()

        symmetric_key = asymmetric_decryption_mapping[asymmetric_method](asymmetric_key)
        decrypted_path = symmetric_decryption_mapping[symmetric_method](symmetric_key, path)

        print('Decryption Done')

    except Exception as e:
        print(f"ERROR:{e}")
        is_successful = False

    return is_successful, decrypted_path
