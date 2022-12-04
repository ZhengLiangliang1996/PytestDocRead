#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# content of test_sample.py
import pytest 

def func(x):
    return x + 1

def systemexit():
    raise SystemExit(1)

def test_func():
    assert func(3) == 4

def test_systemexit():
    with pytest.raises(SystemExit):
        systemexit()
