# -*- coding: utf-8 -*-

from odoo import fields, models

class Traslados(models.Model):
    _name = 'pp.traslado'

    no_oficio = fields.Char(
        string="Número de oficio"
    )
    dependencia = fields.Char(
        string="Dependencia a la que pertenece"
    )
    procedencia_imputado = fields.Char(
        string="Procedencia del imputado"
    )
    descripcion_imputado = fields.Text(
        string="Estado físico y vestimenta del imputado"
    )
    fecha_traslado	 = fields.Date(
        string="Fecha de traslado"
    )
    hora_arribo = fields.Datetime(
        string="Hora de arribo",
        default=fields.Datetime.now
    )
    hora_ingreso = fields.Datetime(
        string="Hora de ingreso",
        default=fields.Datetime.now
    )
    hora_regreso = fields.Datetime(
        string="Hora al regresar la custodia del imputado",
        default=fields.Datetime.now
    )
    dictamen_medico = fields.Boolean(
        string='¿Cuenta con dictamen médico?'
    )

    #==========Relationship fields==========
    name = fields.Many2one(
        'res.partner',
        string='Imputado',
    )
    autoridad_que_ordena_id = fields.Many2one(
        'pp.autoridad',
        string='Autoridad que ordena el traslado'
    )
    autoridad_que_realiza_id = fields.Many2one(
        'pp.autoridad',
        string='Autoridad que realiza el traslado'
    )
    employee_ids = fields.Many2many(
        'hr.employee',
        string='Elementos de apoyo',
    )
    medico_id = fields.Many2one(
        'pp.medico',
        string='Nombre',
    )
    vehiculo_id = fields.Many2one(
        'pp.vehiculos',
        string='Vehículo Oficial',
    )
    

    #==========RELATED==========
    cargo_autoridad_ordena =  fields.Char(
        related='autoridad_que_ordena_id.cargo', 
        string="Cargo",readonly=True
    )
    cargo_autoridad_realiza =  fields.Char(
        related='autoridad_que_realiza_id.cargo', 
        string="Cargo",readonly=True
    )
    no_cedula =  fields.Char(
        related='medico_id.cedula', 
        string="Número de cedula",
        readonly=True
    )
    placas = fields.Char(
        related='vehiculo_id.placas',
        string='Placas',
        readonly=True
    )
    no_economico = fields.Char(
        related='vehiculo_id.no_economico',
        string='Número económico',
        readonly=True
    )