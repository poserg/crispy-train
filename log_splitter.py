#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r"^\[.+\] ([0-9a-z]{8}) ")

files = {}
open_file_limit = 500

with open("/tmp/captives/287/trace.log", "r") as f:
    process = 'out'
    for line in f:
        match = pattern.match(line)
        if match is not None:
            process = match.group(1)
        if process not in files:
            filename = '/tmp/captives/287/out/' + process + '.log'
            files[process] = open(filename, 'a')
        output = files[process]
        output.write(line)

        if len(files) >= open_file_limit:
            output.close()
            del (files[process])

for k, v in files.items():
    v.close()