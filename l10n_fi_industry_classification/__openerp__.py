# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jarmo Kortetjärvi
#    Copyright 2015 Oy Tawasta OS Technologies Ltd.
#    Copyright 2015 Vizucom Oy
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Finnish Industry Classification',
    'category': 'CRM',
    'version': '8.0.0.2.15',
    'author': '''
Oy Tawasta OS Technologies Ltd.,
Vizucom Oy
''',
    'license': 'AGPL-3',
    'website': 'http://www.tawasta.fi',
    'depends': [
        'crm'
    ],
    'data': [
        'data/industry_class.xml',
        'data/industry_category.xml',
        'data/industry_industry.xml',

        'view/res_partner.xml',
        'view/business_industry_class.xml',
        'view/business_industry_category.xml',
        'view/business_industry_industry.xml',
        'view/industry_menu.xml',

        'security/ir.model.access.csv',
    ],
}
