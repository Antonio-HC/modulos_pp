# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Pertenencias(models.Model):
    _name = 'pp.pertenencias'

    fecha_registro = fields.Date(
        string='Fecha'
    )
    hora_registro = fields.Datetime(
        string='Hora de registro'
    )
    fecha_devolucion = fields.Date(
        string='Fecha de devolución'
    )
    hora_devolucion = fields.Datetime(
        string='Hora de devolución'
    )

    #==========relationship fields==========

    employee_id = fields.Many2one(
        'hr.employee',
        string='Policía procesal que realizo el regisgtro',
    )
    pertenencias_list_ids = fields.One2many(
        'pp.pertenencia_list',
        'resguardo_id',
        string='Lista de pertenencias',
    )
    custodia_id = fields.Many2one(
        'pp.custodia',
        string='Custodia',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string=u'Imputado ID',
        readonly=True,
        required=True,
        default=lambda self: self.env.context.get('partner_id'),
        ondelete='set null',
    )

class PertenenciasLista(models.Model):
    _name = 'pp.pertenencia_list'
    
    detalle = fields.Char(string='Detalles')
    numero = fields.Integer(string='Número')

    resguardo_id = fields.Many2one(
        'pp.pertenencias',
        string='Resguardo de pertenencias',
    )

    #@api.multi
    #def auto_increment(self):
	#	for record in self:
	#		id_per=record.id
	#		print "*************Id del producto " + str(id_per)
	#		record.numero=id_per
