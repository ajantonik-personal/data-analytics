###############################################################################
"""
Utilities for data-analytics repo
Goal: Package commonly used methods by other scripts within this repository
Classes: Utils
Author: @ajantonik-personal (Anthony J Antonik)
Date: 2020-04-25
"""
###############################################################################
## Modules
import hashlib
import logging
import os
import random
import uuid

import pandas as pd
from pandas import json_normalize

###############################################################################
## Logging
LOGNAME = (
    str(os.path.basename(__file__)).replace(".py", "")
    + ".log"
)
file_handler = logging.FileHandler(LOGNAME)
file_handler.mode = "a"
file_handler.setFormatter(
    logging.Formatter(
        fmt="%(asctime)s,%(msecs)d %(name)s" " %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)
file_handler.setLevel(logging.DEBUG)
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


###############################################################################
## Classes & Functions
class Utils:
    """
    Main class containing the following functions:
    text_parse_dict
    text_parse_list
    dict_normalize_df
    uuid_generator
    """

    def __init__(self):
        self.return_dict = {}
        self.return_list = []
        self.dataframe = pd.DataFrame()
        self.uuid_final = ""

    def text_parse_dict(self, filepath, separator):
        """
        Function to parse lines of text from a file into a dictionary
        :param filepath: path to text file to be parsed
        :param separator: string separating keynames from values in text file
        :return return_dict: dictionary of keys, values from text file
        """
        self.return_dict = {}
        with open(os.path.expanduser(filepath), "r") as filetoparse:
            lines = filetoparse.readlines()
            for line in lines:
                line = line.split(separator)
                self.return_dict[line[0].replace(" ", "")] = (
                    line[1].replace("\n", "").replace(" ", "")
                )
        return self.return_dict

    def text_parse_list(self, filepath):
        """
        Function to parse lines of text from a file into a list
        :param filepath: path to text file to be parsed
        :return return_list: list of strings from text file
        """
        with open(os.path.expanduser(filepath), "r") as filetoparse:
            self.return_list = filetoparse.readlines()
            for elem, clean in enumerate(self.return_list):
                self.return_list[elem] = clean.replace("\n", "")
        return self.return_list


    def dict_normalize_df(self, inputdict, index, *args):
        """
        Function to normalize a JSON dictionary and return a dataframe
        :param inputdict: JSON dictionary to be normalized
        :param index: diction def upload_blob(self, bucketname, filedir, filename, foldername):
        """
        logger.info("Normalizing JSON & Generating Dataframe...")
        # NOTE: Need to be able to accept multiple arguments of unknown number
        # because JSON dictionaries to be passed through will have varying
        # layers; thus, we need to determine the number of args passed on the
        # fly and generate a string of args to pass to json_normalize()
        args_len = len(args)
        args_str = ""
        for arg in range(0, args_len):
            if arg == 0:
                args_str = args_str + str(args[arg])
            else:
                args_str = args_str + ", " + str(args[arg])
        self.dataframe = json_normalize(inputdict, args_str, index)
        self.dataframe = self.dataframe[
            [index] + [col for col in self.dataframe.columns if col != index]
        ]
        logger.info(
            "DataframeGenerationStatus: SUCCESS; Dataframe: \n%s",
            self.dataframe,
        )
        return self.dataframe


    def uuid_generator(self, seedvar, bitcount, refstring):
        """
        Function to generate a random hexadecimal UUID for a reference string
        :param seedvar: random positive integer to serve as RNG seed
        :param bitcount: number of bits for hexadecimal function
        :param refstring: reference string for which UUID is generated
        :return uuid_final: random hexadecimal UUID
        """
        logger.info("UUID Generating for %s...", refstring)
        # Generate 32char base UUID with seeded random number
        rd = random.Random()
        rd.seed(seedvar)
        uuid_base = uuid.UUID(int=rd.getrandbits(bitcount)).hex
        # Generate 40char UUID by hashing uuid_base & RefID
        sha = hashlib.sha1()
        sha.update(str(uuid_base + refstring).encode())
        self.uuid_final = sha.hexdigest()
        logger.info(
            "UUIDGenerationStatus: SUCCESS; RefString: %s; UUID: %s",
            refstring,
            self.uuid_final,
        )
        return self.uuid_final

