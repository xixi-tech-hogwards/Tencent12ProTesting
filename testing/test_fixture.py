#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def login():
    print("需要登录")
    username = "tom"
    yield username
    print("teardown ")


class TestDemo:

    # def setup_class(self):
    #     # 第一步，打开浏览器
    #     print("setup_class  第一步，打开浏览器")
    #
    # def setup(self):
    #     print("setup")
    #     # 第二步，输入网址
    #
    # def teardown(self):
    #     print("teardown")
    #
    # def teardown_class(self):
    #
    #     # 第五步，关闭浏览器
    #     print("teardown_class 第五步，关闭浏览器")
    #     # pass

    def test_a(self,login):
        print(f"testa ==== {login}")
        # 第二步，输入网址
        # 第三步，定位
        # 第四步，各种操作
        pass

    def test_b(self):
        print("testb")
        pass

    def test_c(self,login):
        print("testc")
        pass

