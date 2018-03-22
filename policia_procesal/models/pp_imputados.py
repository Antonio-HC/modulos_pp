# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Imputados(models.Model):
    #_name = 'pp.imputado'
    _inherit = 'res.partner'

    #=====Ver numero de registro de traslados=====
    traslados_count = fields.Integer(
        compute='compute_traslados_count'
    )

    @api.multi
    def compute_traslados_count(self):
        for imputado in self:
            imputado.traslados_count = self.env['pp.traslado'].search_count(
                [('imputado_id', '=', imputado.id)])
