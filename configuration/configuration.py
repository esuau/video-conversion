import yaml
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)


class Configuration(object):

    def __init__(self):
        self.configuration_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'application.yml')
        self.configuration_data = None

        f = open(self.configuration_file, 'r')
        self.configuration_data = yaml.load(f.read())
        f.close()

    def get_gcloud_bucket_name(self):
        return self.configuration_data['gcloud']['bucket']['name']

    def get_bigquery_dataset(self):
        return self.configuration_data['gcloud']['bigquery']['dataset']

    def get_bigquery_table(self):
        return self.configuration_data['gcloud']['bigquery']['table']
