###############################################################################
"""
Test Cases for utils.py
"""
###############################################################################
## Modules
import json

import pandas as pd

from scripts.utils import Utils


###############################################################################
## Test Cases
def test_text_parse_dict():
    utils = Utils()
    test_filepath = "./utils/tests/test_utils_creds.txt"
    test_dict = utils.text_parse_dict(filepath=test_filepath, separator="=")
    target_dict = {
        "USERNAME": "username@website.com",
        "PASSWORD": "PA$$W0RD",
        "APPID": "MyTestApplication",
    }
    assert test_dict == target_dict


def test_text_parse_list():
    utils = Utils()
    test_filepath = "./utils/tests/test_utils_entities.txt"
    test_list = utils.text_parse_list(filepath=test_filepath)
    target_list = ["ABCD", "1234", "!@#$"]
    assert test_list == target_list


def test_dict_normalize_df():
    # NOTE: This test is a bit circuitous bc storage of a target df requires
    # storing some source from which to generate that df; in this case, we
    # are using test_utils_csv_to_df.csv which represents the desired csv
    # representation of the df with successful execution of the fxn;
    # however, to get our test df in a 1:1 comparable state to the target df
    # generated from this csv, we have to first convert the test df to csv
    # and then convert it back to a df; an annoying nuance, but necessary for
    # true apples-to-apples comparison between dfs generated this way
    utils = Utils()
    INDEX = "ISIN"
    ARGUMENT = "articleList"
    with open("./utils/tests/test_utils_dict_to_df.txt") as dict_file:
        test_dict = json.load(dict_file)
    target_df = pd.read_csv(
        "./utils/tests/test_utils_csv_to_df.csv", keep_default_na=False
    )
    temp_df = utils.dict_normalize_df(test_dict, INDEX, ARGUMENT,)
    temp_df.to_csv(
        "./utils/tests/test_utils_df_to_csv.csv",
        sep=",",
        index=None,
        header=True,
    )
    test_df = pd.read_csv(
        "./utils/tests/test_utils_df_to_csv.csv", keep_default_na=False
    )
    assert test_df.equals(target_df)


def test_uuid_generator():
    utils = Utils()
    test_seedvar = 6
    test_bitcount = 128
    test_refid = "4295905573" # Apple Inc (Organization) RefID
    target_uuid_final = "14fe8b5a6ec8d00eddbfb6bd60c2e82e13a59db3"
    test_uuid_final = utils.uuid_generator(
        seedvar=test_seedvar,
        bitcount=test_bitcount,
        refstring=test_refid,
    )
    assert test_uuid_final == target_uuid_final


###############################################################################
# Test Execution
if __name__ == "__main__":
    test_text_parse_dict()
    test_text_parse_list()
    test_dict_normalize_df()
    test_uuid_generator()