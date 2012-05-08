****************
sc.policy.helper
****************

.. contents:: Table of Contents
   :depth: 2

Overview
--------

Helpers to be used with Site Policy packages in Plone.

Usage
-----

To use its helper methods, import this package (or one of its modules)
in your code and then use it::
	
	import logging
	from sc.policy.helper import setup

	PROJECTNAME = 'sc.customer.portal'
	PROFILE_ID = 'sc.customer.portal:default'

	def run_upgrades(context):
		logger = logging.getLogger('PROJECTNAME')
    	setup.run_upgrades_for_profile(PROFILE_ID, context, logger)

