# -*- coding: utf-8 -*-
import doctest
import sc.policy.helper.deps


def test_suite():
    return doctest.DocTestSuite(sc.policy.helper.deps)
