sc.policy.helper
**************************************************************

.. contents:: Table of Contents
   :depth: 2


Overview
--------

  Helpers to be used with Site Policy packages in Plone.

Requirements
------------

    * Plone >=4.1.x (http://plone.org/products/plone)
    
Installation
------------
    
This package should be declared as a dependency from other packages, so add it
to the install_requires from setup.py
::

      install_requires=[
        'setuptools',
        'sc.policy.helper',
        ],


Or declare it in your dependencies.txt file:
::

	[sc.policy.helper]


And it will become available to your package.


Usage
------------

To use its helper methods, import this package (or one of its modules)
in your code and then use it:
::
	
	import logging
	from sc.policy.helper import setup

	PROJECTNAME = 'sc.customer.portal'
	PROFILE_ID = 'sc.customer.portal:default'

	def run_upgrades(context):
		logger = logging.getLogger('PROJECTNAME')
    	setup.run_upgrades_for_profile(PROFILE_ID, context, logger)
