#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
'''
function: the default scope, the fixture is destroyed at the end of the test.
class: the fixture is destroyed during teardown of the last test in the class.
module: the fixture is destroyed during teardown of the last test in the module.
package: the fixture is destroyed during teardown of the last test in the package.
session: the fixture is destroyed at the end of the test session.
'''
import smtplib
import pytest


@pytest.fixture(scope='module')
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes
