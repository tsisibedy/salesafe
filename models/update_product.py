# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UpdateProduct(models.Model):
    _name = 'salesafe.update_product'

    name = fields.Many2one('salesafe.product',string="Product Name",required=True)
    number_update = fields.Integer(string="Price of the product",required=True)
    date_arrival = fields.Date(string="Date of arrival of the stock", default=fields.Date.today())

    @api.model
    def create(self, vals):
        updateProduct = self.env['salesafe.product'].browse(vals['name'])
        calculNewStock = updateProduct.nb_stock + vals['number_update']
        updateProduct.update({
            'nb_stock':calculNewStock
        })

        return super(UpdateProduct, self).create(vals)

