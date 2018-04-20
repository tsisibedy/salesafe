# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _name = 'salesafe.sale_service'

    name = fields.Many2one('salesafe.product', string="Product name to buy",domain=[('nb_available','!=',0)])
    nb_buy = fields.Integer(string="Number to buy", required=True)
    total_price = fields.Float(string="Total price of product")
    sale_id = fields.Many2one('salesafe.sale',string="Sale du service")

    @api.onchange('name', 'nb_buy')
    def check_total_price(self):
        for record in self:
            if not record.name:
                pass
            else:
                if record.nb_buy != 0:
                    record.total_price = float(record.name.price*record.nb_buy)
