{%- set mod = name|snake -%}
{%- set model = "%s.%s"|format(mod, mod) -%}
{%- set root = "/%s/%s"|format(mod, mod) -%}
# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http

# class {{ mod|pascal }}(http.Controller):
#     @http.route('{{ root }}/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('{{ root }}/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('{{ mod }}.listing', {
#             'root': '{{ root }}',
#             'objects': http.request.env['{{ model }}'].search([]),
#         })

#     @http.route('{{ root }}/objects/<model("{{ model }}"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('{{ mod }}.object', {
#             'object': obj
#         })
