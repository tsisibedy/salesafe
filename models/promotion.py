# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Promotion(models.Model):
    _name = 'salesafe.promotion'

    name = fields.Char(string="Slogan of the promotion", required=True)
    reduction = fields.Integer(string="Percentage of the promotion", required=True)
    date_reduction = fields.Date(string="Date of the reduction", required=True,readonly=True,default=fields.Date.today())
    type_promotion = fields.Selection([
        ('reduction', 'Réduction'),
        ('augmentation','Augmentation'),
    ],string="Promotion type",default='reduction')
    activeState = fields.Boolean(string="Activation of the promation",default=True)

    @api.constrains('activeState')
    def check_the_promotion(self):
        statePromotion = self.env['salesafe.promotion'].search([('id','!=',self.id)])
        for stateP in statePromotion:
            if stateP.activeState == True:
                raise ValueError('Une promotion est en cours de lancement vous devez la stopé avant de lancé une autre!')


    @api.model
    def create(self, vals):
        promotion = self.env['salesafe.product'].search([])
        for promo in promotion:
            priceCalcul = (promo.price * vals['reduction']) / 100
            pricePromotion = 0.0
            if vals['type_promotion'] == 'reduction':
                pricePromotion = promo.price - priceCalcul

            if vals['type_promotion'] == 'augmentation':
                pricePromotion = promo.price + priceCalcul

            history = self.env['salesafe.history']

            history.create({
                'name':vals['name'],
                'name_product':promo.name,
                'price_init':promo.price,
                'price_current':pricePromotion,
                'reduction':float(vals['reduction']),
                'date_reduction':fields.Date.today(),
                'activeState':vals['activeState'],
            })


            if vals['activeState'] == True:
                promo.update({
                    'price': pricePromotion
                })

        return super(Promotion, self).create(vals)


    @api.multi
    def write(self, vals):
        promotion_product = self.env['salesafe.product'].search([])
        promotion_history = self.env['salesafe.history'].search([])
        for record in self:
            for promoH in promotion_history:
                pricePromotion = 0.0
                if record.name == promoH.name:
                    if 'activeState' in vals:
                        promoH.update({
                            'activeState':vals['activeState']
                        })
                    else:
                        promoH.update({
                            'activeState': record.activeState
                        })
                    if 'reduction' in vals:
                        promoH.update({
                            'reduction':vals['reduction']
                        })
                        priceCalcul = (promoH.price_init * vals['reduction']) / 100
                    else:
                        promoH.update({
                            'reduction': record.reduction
                        })
                        priceCalcul = (promoH.price_init * record.reduction) / 100
                    if 'type_promotion' in vals:
                        if vals['type_promotion'] == 'reduction':
                            pricePromotion = promoH.price_init - priceCalcul

                        if vals['type_promotion'] == 'augmentation':
                            pricePromotion = promoH.price_init + priceCalcul
                    else:
                        if record.type_promotion == 'reduction':
                            pricePromotion = promoH.price_init - priceCalcul

                        if record.type_promotion == 'augmentation':
                            pricePromotion = promoH.price_init + priceCalcul

                    promoH.update({
                        'price_current':pricePromotion
                    })
                    for promoP in promotion_product:
                        if promoH.name_product == promoP.name:
                            if 'activeState' in vals:
                                if vals['activeState'] == True:
                                    promoP.update({
                                        'price':pricePromotion
                                    })
                            else:
                                if record.activeState == True:
                                    promoP.update({
                                        'price':pricePromotion
                                    })


        return super(Promotion, self).write(vals)

    @api.multi
    def unlink(self):
        remove = self.env['salesafe.history']
        for unlinkSelf in self:
            executeUnlink = remove.search([])
            for liste in executeUnlink:
                if unlinkSelf.name == liste.name:
                    liste.unlink()

        return super(Promotion, self).unlink()
