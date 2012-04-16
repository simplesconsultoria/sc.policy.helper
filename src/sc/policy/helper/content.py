# -*- coding:utf-8 -*-


def set_modified_to_effective(brains, logger=None):
    ''' Set modification date to the same value of
        effective date
    '''
    if logger:
        logger.info('Objects to be updated: %d' % len(brains))
    for brain in brain:
        o = brain.getObject()
        date = o.EffectiveDate()
        o.setModificationDate(date)
        o.reindexObject(idxs=['modified'])
