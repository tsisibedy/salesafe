# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import *

class Product(models.Model):
    _name = 'salesafe.sale'

    def _sales_serial_number(self):
        return str(randint(0,999999999999))+''+'SaleSafe'

    name = fields.Char(string="Sales serial number",readonly=True,store=True,default=_sales_serial_number)
    date_purchase = fields.Date(string="date of purchase",readonly=True,default=fields.Date.today())
    product_list = fields.One2many('salesafe.sale_service','sale_id',string="List of pruduit to buy")
    total_price = fields.Float(string="Total price of purchases",store=True)

    @api.constrains('product_list')
    def check_total_price_test(self):
        count_price = 0.0
        for record in self:
            if not record.product_list:
                pass
            else:
                for prix in record.product_list:
                    verify_stock = prix.name.nb_stock - prix.name.nb_sold
                    name_product = prix.name.name
                    if verify_stock < prix.nb_buy:
                        raise ValueError(
                            'Il n\'y a pas plus de stock pour satisfaire votre demande, vous devez contacte votre fornisseur. Il vous reste: %s de %s' % (
                            verify_stock,name_product))

                    sold = prix.name.nb_sold + prix.nb_buy
                    prix.mapped('name').write({'nb_sold': sold})
                    nb_count_available = prix.name.nb_stock - prix.name.nb_sold
                    prix.mapped('name').write({'nb_available': nb_count_available})
                    count_price = count_price + prix.total_price
                record.total_price = count_price





