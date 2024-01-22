#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_huntr import SourceHuntr

if __name__ == "__main__":
    source = SourceHuntr()
    launch(source, sys.argv[1:])
