# -*- coding:utf-8 -*-
from sc.policy.helper import deps
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.upgrade import listUpgradeSteps


def _order_packages(packages, dependencies):
    ''' Given an ordered list of packages to be installed,
        return a list of ordered dependencies
    '''
    dict_depts = dict([(d['package'], d) for d in dependencies])
    return [dict_depts[p] for p in packages if p in dict_depts]


def install_packages(packages, dependencies, context, logger=None):
    ''' Install packages from, '''
    qi = getToolByName(context, 'portal_quickinstaller')
    ordered = _order_packages(packages, dependencies)
    for dep in ordered:
        name = deps.get_package_name(dep['package'])
        qi.installProduct(name,
                          locked=dep['locked'],
                          hidden=dep['hidden'],
                          profile=dep['profile'])
        if logger:
            logger.info('Installed %s' % name)


def uninstall_packages(packages, context, logger=None):
    ''' Uninstall packages '''
    qi = getToolByName(context, 'portal_quickinstaller')
    for package in packages:
        name = deps.get_package_name(package)
        if qi.isProductInstalled(name):
            # We could pass a list in here, but debugging
            # would be harder
            qi.uninstallProducts(products=[name])
            if logger:
                logger.info('Uninstalled %s' % name)


def run_upgrades_for_profile(profile_id, context, logger=None):
    """ Run all upgrade steps for given profile_id
    """
    site = context.getSite()
    setup_tool = getToolByName(site, 'portal_setup')
    version = setup_tool.getLastVersionForProfile(profile_id)
    upgradeSteps = listUpgradeSteps(setup_tool, profile_id, version)
    sorted(upgradeSteps, key=lambda step: step['sortkey'])

    for step in upgradeSteps:
        oStep = step.get('step')
        if oStep is not None:
            oStep.doStep(setup_tool)
            setup_tool.setLastVersionForProfile(profile_id, oStep.dest)
            if logger:
                msg = "Ran upgrade step %s for profile %s" % (oStep.title,
                                                              profile_id)
                logger.info(msg)


def remove_default_content(context, logger=None):
    """ Clean up default content types
    """
    portal = getToolByName(context, 'portal_url').getPortalObject()
    content_ids = ['front-page', 'news', 'Members', 'events']
    portal_ids = portal.objectIds()
    for cId in content_ids:
        if cId in portal_ids:
            portal.manage_delObjects([cId])
            if logger:
                logger.info('Deleted object with id %s' % cId)

    if logger:
        logger.info('Cleaned up portal contents')
