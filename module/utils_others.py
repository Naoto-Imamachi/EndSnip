#!/usr/bin/env python3

import re
def Input_config_file(config_file):
    config_dict = {}
    for line in open(config_file, 'r'):
        if line == '\n' or re.match(r'^#',line):
            continue
        line = line.rstrip()
        line = line.replace(' ','')
        fields = line.split('=')
        key_name = fields[0]
        infor = fields[1]
        config_dict[key_name] = infor
    return config_dict

from datetime import datetime
#Print out comment with now time
def now_time(comment):
    now = datetime.now()
    nowtime = "{0:%Y-%m-%d %H:%M:%S}".format(now)
    print ('[' + nowtime + ']' + ' ' + comment)

