# -*- coding:utf-8 -*-
import os
import ConfigParser


def _format_profile_id(package_name, profile):
    ''' Format profile id to be
        package_name:profile_name

        >>> _format_profile_id('sc.policy.helper',
        ...                    'sc.policy.helper:default')
        'sc.policy.helper:default'

        >>> _format_profile_id('sc.policy.helper', 'default')
        'sc.policy.helper:default'

        >>> _format_profile_id('sc.policy.helper', '')
        ''

    '''
    profile_id = profile.split(':')
    if len(profile_id) == 2:
        if not (profile_id[0] == package_name):
            profile_id = ''
        else:
            profile_id = profile
    elif profile_id[0]:
        # Profile name was informed
        profile_id = '%s:%s' % (package_name, profile[0])
    else:
        profile_id = ''

    return profile_id


def get_package_dependencies(pkg=None):
    ''' Handle dependencies.txt file for a package

        >>> import sc.policy.helper.tests
        >>> deps = get_package_dependencies(sc.policy.helper.tests)
        >>> len(deps)
        3
        >>> deps[0].get('package')
        'collective.grok'

        >>> deps[1].get('package')
        'experimental.btree'

        >>> deps[3].get('package')
        'plone.app.theming'

    '''
    dependencies = []
    if not (pkg and hasattr(pkg, '__file__')):
        return dependencies
    path = os.path.join(os.path.dirname(pkg.__file__),
                        'dependencies.txt')
    defaults = dict(hidden='False',
                    install='False',
                    profile='')
    config = ConfigParser.ConfigParser(defaults)
    config.read([path])
    for p in config.sections():
        hidden = config.getboolean(p, 'hidden')
        install = config.getboolean(p, 'install')
        profile = config.get(p, 'profile')
        # profile_id is package_name:profile_name
        profile_id = _format_profile_id(p, profile)
        if install:
            package = dict(package=p,
                           locked=False,
                           hidden=hidden,
                           install=install,
                           profile=profile_id)
            dependencies.append(package)
    return dependencies


def get_package_name(name):
    ''' Remove the Products namespace from package names
        This is used when dealing with portal_quickinstaller

        >>> get_package_name('Products.PloneFormGen')
        PloneFormGen

        >>> get_package_name('collective.person')
        collective.person
    '''
    return name[9:] if name.startswith('Products') else name
