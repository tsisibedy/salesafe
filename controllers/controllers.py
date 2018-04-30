# -*- coding: utf-8 -*-
from odoo import http

class Salesafe(http.Controller):
    @http.route('/salesafe/product_list',auth="public",website=True)
    def product_list(self,**kw):
        product = http.request.env['salesafe.product'].search([])
        return http.request.render('salesafe.product_list',{
            'products':product
        })

    @http.route('/salesafe/product_create',auth="public",website=True,methods=['POST'],type="http")
    def create(self,**paramse):
        print(paramse)
        products = http.request.env['salesafe.product']
        products.create({
            'name':paramse.get('name'),
            'price':paramse.get('price'),
            'date_arrival':paramse.get('date_arrival'),
            'nb_stock':paramse.get('nb_stock'),
            'nb_sold':paramse.get('nb_sold'),
            'description':paramse.get('description'),
            'sold_poucentage':paramse.get('sold_poucentage'),
        })

        return http.request.redirect('/salesafe/product_list')