# -*- coding: utf-8 -*-

import unittest2 as unittest

from sc.policy.helper.testing import INTEGRATION_TESTING
from sc.policy.helper import deps
from sc.policy.helper import setup
from sc.policy.helper import tests

DEPENDENCIES =  deps.get_package_dependencies(tests)

class TestInstall(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

#    def test_install_packages(self):
#
#    def test_uninstall_packages(self):
#
#    def test_run_upgrades(self):

    def test_remove_default_content(self):
        setup.remove_default_content(self.portal)
        portal_ids = self.portal.objectIds()
        for content_ids in ['front-page', 'news', 'Members', 'events']:
            self.failIf(content_ids in portal_ids)

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)