# from src.logger import logging

# # logging.debug('This is debug msg')

# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()

# from src.constants import *

# print(MONGODB_URL_KEY)

# import os
# CONNECTION_URL = os.getenv("MONGODB_URL")
# print(CONNECTION_URL)