import os
from ..func_API import *

USER = os.environ.get("ONISEP_USER")
PASS = os.environ.get("ONISEP_PASS")
dataset_code = "5fa5816ac6a6e"


def main():
    token = login(USER, PASS)


if __name__ == "__main__":
    main()
