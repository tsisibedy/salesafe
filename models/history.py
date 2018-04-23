# -*- coding: utf-8 -*-

from odoo import models, fields, api


class History(models.Model):
    _name = 'salesafe.history'

    name = fields.Char(string="Slogan of the promotion", required=True,readonly=True)
    name_product = fields.Char(string="Product Name", required=True,readonly=True)
    price_init = fields.Float(string="Initial price", required=True,readonly=True)
    price_current = fields.Float(string="Current price", required=True,readonly=True)
    reduction = fields.Float(string="Percentage of reduction", required=True,readonly=True)
    date_reduction = fields.Date(string="Date of the reduction", readonly=True,
                                 default=fields.Date.today())
    activeState = fields.Boolean(string="Activation of the promation", default=False,readonly=True)
