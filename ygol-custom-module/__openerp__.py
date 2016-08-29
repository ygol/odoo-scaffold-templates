#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Ygol InterNetwork - Yves Goldberg
#    ----------------------------------------------------
#     
#    ----------------------------------------------------
#    langage : Python 2.7
#    creation date : 02/08/16
#    modification date: 02/08/16
#    author  : Yves Goldberg <admin@ygol.com>
#
##############################################################################

{
    'name': "{{ name }}",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        """,

    # 'description': put the module description in README.rst

    'author': 'Ygol InterNetwork',
    'website': "http://www.ygol.com",

    # Categories can be used to filter modules in modules listing
    # Check http://goo.gl/0TfwzD for the full list
    'category': 'Ygol',
    'version': '9.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

