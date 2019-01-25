import logging

from google.cloud import storage


class StorageService(object):

    def __init__(self, _config_):
        self.bucket_name = _config_.get_gcloud_bucket_name()

    def upload_blob(self, source_file_name, destination_blob_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        logging.info('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))
