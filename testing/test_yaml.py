#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

with open("datas/add1.yml") as f:
    print(yaml.safe_load(f))