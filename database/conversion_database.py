import datetime
import logging
import os

from google.cloud import bigquery


class ConversionDatabase(object):

    def __init__(self, _config_):
        self.client = bigquery.Client()
        dataset_id = _config_.get_bigquery_dataset()
        table_id = _config_.get_bigquery_table()
        table_ref = self.client.dataset(dataset_id).table(table_id)
        self.table = self.client.get_table(table_ref)

    def insert_stats(self, file, conversion_duration, upload_duration):
        size = os.path.getsize(file)
        row_to_insert = [
            (size, conversion_duration, upload_duration, datetime.datetime.utcnow())
        ]
        errors = self.client.insert_rows(self.table, row_to_insert)
        assert errors == []
        logging.info('Insert stats to database.')
