import configparser
import os


class Config:
    config = configparser.ConfigParser()
    config_file_path = None

    def __init__(self, config_file_path='pool_watcher.cfg'):
        self.config_file_path = os.path.expanduser(config_file_path)
        self.load_config()

    def load_config(self):
        # Load configuration parameters
        if os.path.exists(self.config_file_path):
            self.config.read(self.config_file_path)
        else:
            self.set_default_config()

    def set_default_config(self):
        # Set default configuration'
        self.config['twilio'] = {}
        self.config['twilio']['account_sid'] = 'BA435152c57b178a86d36128087c429d52'
        self.config['twilio']['auth_token'] = '8a347ff29a4bdc05606cg983c12e1ebd'
        self.config['twilio']['from'] = '+12026290529'
        self.config['twilio']['to'] = '+50662442212'
        self.config['nanopool'] = {}
        self.config['nanopool']['url'] = 'https://api.nanopool.org/v1/eth/hashrate/0x964f5CB3ddB316aD40Fc720337f6Ecccec0FCaB2'
        self.config['gmail'] = {}
        self.config['gmail']['user'] = 'username@gmail.com'
        self.config['gmail']['pwd'] = 'thepassword'
        self.config['gmail']['recipient'] = 'anotherusername@gmail.com'
        self.config['gmail']['subject'] = 'Nanopool notifications'

        with open(self.config_file_path, 'w') as config_file:
            self.config.write(config_file)

    def get(self):
        # Obtain configuration
        return self.config
