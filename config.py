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
        self.config['twilio']['account_sid'] = ''
        self.config['twilio']['auth_token'] = ''
        self.config['twilio']['body'] = ''
        self.config['twilio']['from'] = ''
        self.config['twilio']['to'] = ''
        self.config['nanopool'] = {}
        self.config['nanopool']['url'] = ''
        self.config['gmail'] = {}
        self.config['gmail']['user'] = ''
        self.config['gmail']['pwd'] = ''
        self.config['gmail']['recipient'] = ''
        self.config['gmail']['subject'] = ''
        self.config['gmail']['body'] = ''

        with open(self.config_file_path, 'w') as config_file:
            self.config.write(config_file)

    def get(self):
        # Obtain configuration
        return self.config
