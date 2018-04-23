# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _name = 'salesafe.product'

    name = fields.Char(string="Product Name",required=True)
    price = fields.Float(string="Price of the product",required=True)
    date_arrival = fields.Date(string="Date of arrival of the stock", default=fields.Date.today())
    nb_stock = fields.Integer(string="Number of the stock product",required=True)
    nb_available = fields.Integer(string="Number of available product",readonly=True,compute="_set_nb_available")
    nb_sold = fields.Integer(string="Number of product sold",readonly=True)
    description = fields.Text(string="Product Description")
    sold_poucentage = fields.Float(string="Percentage sold",compute="_set_sold_poucentage",store=True)

    @api.depends('nb_stock','nb_sold')
    def _set_sold_poucentage(self):
        for record in self:
            record.sold_poucentage = float((record.nb_sold*100)/record.nb_stock)

    @api.multi
    @api.depends('nb_stock', 'nb_sold')
    def _set_nb_available(self):
        for record in self:
            record.nb_available = record.nb_stock - record.nb_sold

