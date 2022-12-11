#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
from unittest.mock import Mock, patch

class Production:
    def method(self):
        self.something(1, 2, 3)
    
    def somthing(self, a, b, c):
        pass 

class Production2:
    def method(self, close):
        close.something()
    
def some_function():
    instance = Production()
    return instance.method()

def test_mock_method():
    real = Production()
    real.something = Mock()
    real.method()
    real.something.assert_called_once_with(1, 2, 3)

def test_mock_objects():
    real = Production2()
    mock = Mock()
    real.method(mock)
    mock.something.assert_called_with()

# !!! need to provide full path
def test_production_mock_classes():
    with patch('mock_patching_methods.Production') as mock:
        instance = mock() 
        instance.method.return_value = "result"
        result = some_function()
        assert result == "result"

@patch('mock_patching_methods.Production')
def test_production_mock_classes_decorator(mock_production):
    # get the instance of mock class 
    instance = mock_production()
    instance.method.return_value = "result"
    result = some_function()
    assert result == "result"


