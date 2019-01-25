import logging
import os
import time

from configuration.configuration import Configuration
from conversion.conversion_service import ConversionService
from database.conversion_database import ConversionDatabase
from storage.storage_service import StorageService

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    configuration = Configuration()

    conversion = ConversionService(configuration)
    input_file = os.path.join('input.avi')
    output_file = os.path.join('output.mkv')
    t0 = time.time()
    conversion.convert_video(input_file, output_file)
    t1 = time.time()
    storage = StorageService(configuration)
    t2 = time.time()
    storage.upload_blob(output_file, 'movie.mkv')
    t3 = time.time()
    database = ConversionDatabase(configuration)
    database.insert_stats(output_file, t1 - t0, t3 - t2)
