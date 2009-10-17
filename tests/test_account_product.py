#!/usr/bin/env python
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import sys, os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import RPCProxy, CONTEXT, SOCK, test_view


class AccountProductTestCase(unittest.TestCase):
    '''
    Test AccountProduct module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_product')

    def test0005views(self):
        '''
        Test views.
        '''
        self.assertRaises(Exception, test_view('account_product'))

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(AccountProductTestCase)

if __name__ == '__main__':
    suiteTrytond = trytond.tests.test_tryton.suite()
    suiteAccountProduct = suite()
    alltests = unittest.TestSuite([suiteTrytond, suiteAccountProduct])
    unittest.TextTestRunner(verbosity=2).run(alltests)
    SOCK.disconnect()