#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
from unittest.mock import patch 

class Car():
    def drive(self, speed):
        return "GO" + speed

def create_drive():
    car = Car()
    speed = 'a'
    return car.drive(speed)

# autospec=True: Functions or methods being mocked will have their arguments checked to check that they are called with the correct signature.

@patch("mock_patch_spec.Car", autospec=True)
def test_create_drive_success(Car_mock):
    car = Car_mock.return_value
    car.drive.return_value = "GO"
    noise = create_drive()
    assert noise == "GO"
