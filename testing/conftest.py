#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def pytest_collection_modifyitems(session, config, items:list):
    # print(items)
    # print(type(items))
    # for item in items:
    #     if 'add' in item.nodeid:
    #         item.add_marker(pytest.mark.add)
    #
    #     elif 'div' in item.nodeid:
    #         item.add_marker(pytest.mark.div)

    items.reverse()