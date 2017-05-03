# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : cleanup_old_files.py
## Author : Denny <denny@dennyzhang.com>
## Description :
##    Remove old files in a safe and organized way
## Sample:
##    # Remove files: Check /opt/app and remove files naming "app-.*-SNAPSHOT.jar". But keep latest 2 copies
##    python cleanup_old_files.py --working_dir "/opt/app" --filename_pattern "app-.*-SNAPSHOT.jar" \
##               --cleanup_type file --min_copies 3
##
##    # Remove files: Only cleanup files over 100MB
##    python cleanup_old_files.py --working_dir "/opt/app" --filename_pattern "app-.*-SNAPSHOT.jar" \
##               --cleanup_type file --min_size_mb 100
##
##    # Remove folders: Cleanup subdirectories, keeping latest 2 directories
##    python cleanup_old_files.py --working_dir "/opt/app" --filename_pattern ".*" --cleanup_type directory
##
## --
## Created : <2017-05-03>
## Updated: Time-stamp: <2017-05-03 16:15:17>
##-------------------------------------------------------------------
import argparse
import re

if __name__ == '__main__':
    # get parameters from users
    parser = argparse.ArgumentParser()
    parser.add_argument('--working_dir', required=True, \
                        help="Perform cleanup under which directory", type=str)

    parser.add_argument('--filename_pattern', required=False, default=".*", \
                        help="Filter files/directories by filename, before cleanup", type=str)
    parser.add_argument('--cleanup_type', required=False, default='file', \
                        help="Whether to perform the cleanup for files or directories", type=str)
    parser.add_argument('--min_copies', default=3, required=False, \
                        help='minimal shards each elasticsearch index should have', type=int)
    parser.add_argument('--min_size_mb', default='100', required=False, \
                        help='When remove files, skip files too small', type=str)
    l = parser.parse_args()

    working_dir = l.working_dir
    filename_pattern = l.filename_pattern
    cleanup_type = l.cleanup_type
    min_copies = l.min_copies
    min_size_mb = l.min_size_mb

## File : cleanup_old_files.py ends
