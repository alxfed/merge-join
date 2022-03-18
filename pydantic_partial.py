# -*- coding: utf-8 -*-
"""...
"""
from typing import Optional, Dict, List
from pydantic import BaseModel, validator

# s3 persistence
bucket_name     = 'aws-data-science'
oraculum_glob   = 'oraculum/'
experiments_dir = 'experiments/'
generation_dir  = 'generation/'
data_dir        = 'data/'
plots_dir       = 'plots/'
tables_dir      = 'tables/'
archive_dir     = 'archive/'


class DataFiles(BaseModel):
    groups_file         : Optional[str] = f"groups_file.json",
    all_logins_file     : Optional[str] = "all_logins_file.json",
    all_progress_file   : Optional[str] = "all_progress_file.json",
    all_payments_file   : Optional[str] = "all_payments_file.json",
    all_ads_file        : Optional[str] = "all_ads_file.json",
    raw_installs_file   : Optional[str] = "raw_installs.json",
    raw_retention_file  : Optional[str] = "raw_retention.json",
    raw_playtime_file   : Optional[str] = "raw_playtime.json",
    raw_conversion_file : Optional[str] = "raw_conversion.json",
    raw_cumversion_file : Optional[str] = "raw_cumversion.json",
    raw_arpu_file       : Optional[str] = "raw_arpu_file,json",
    extra: Optional[str] = {}


if __name__ == '__main__':
    df = DataFiles()
    print('ok')