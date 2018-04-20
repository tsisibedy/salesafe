# -*- coding: utf-8 -*-
from odoo import http

# class Salesafe(http.Controller):
#     @http.route('/salesafe/salesafe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salesafe/salesafe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('salesafe.listing', {
#             'root': '/salesafe/salesafe',
#             'objects': http.request.env['salesafe.salesafe'].search([]),
#         })

#     @http.route('/salesafe/salesafe/objects/<model("salesafe.salesafe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salesafe.object', {
#             'object': obj
#         })