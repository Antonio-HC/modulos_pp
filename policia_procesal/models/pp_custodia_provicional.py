# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CustodiaProvicional(models.Model):
    _name = 'pp.custodia'

    fecha_recepcion = fields.Date(
        string='Fecha de recepción'
    )
    procedencia = fields.Char(
        string='Procedencia',
    )
    fecha_hora_entrega = fields.Datetime(
        string='Fecha y hora de entrega',
    )
    pertenencias = fields.Integer(
        string='Pertenencias',
        compute='compute_pertenencias_count'
    )

    #==========Relationship fields==========
    name = fields.Many2one(
        'res.partner',
        string='Nombre del imputado',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string=u'Imputado',
        readonly=True,
        ondelete='set null',
    )
    autoridad_que_solicita_id = fields.Many2one(
        'pp.autoridad',
        string='Autoridad que solicita el traslado'
    )
    vehiculo_id = fields.Many2one(
        'pp.vehiculos',
        string='Vehículo',
    )
    traslado_id = fields.Many2one(
        'pp.traslado',
        string='No. Oficio de traslado',
    )

    #==========METHODS==========
    @api.multi
    def compute_pertenencias_count(self):
        for partner in self:
            partner.pertenencias = self.env['pp.pertenencias'].search_count(
                [('custodia_id', '=', partner.id)])
    