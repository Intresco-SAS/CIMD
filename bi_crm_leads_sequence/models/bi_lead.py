# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Tipoempresa(models.Model):
    _name = "tipo.empresa"
    name = fields.Char('Tipo de empresa', size=64, required=True)
class crm_lead(models.Model):
    _inherit = 'crm.lead'

    tiempo_mercado = fields.Char("Tiempo en el mercado- Año de Constitución")
    solo_empresarios = fields.Char("Sólo para Emprendedores  y Micro empresarios (Esta Generando Ingresos)")
    ingresos_generando = fields.Char("Cuántos Ingresos esta Generando al mes (Emprendedores- Microempresarios)")
    facturacion_mensual = fields.Char("Facturación Mensual- Empresas")
    pais_id = fields.Many2one('res.country',
                              string='Pais', 
                              help='Select Country', 
                              ondelete='restrict', 
                              default=lambda self: self.env['res.country'].browse([(49)])
                              )
    city_id = fields.Many2one('res.country.state.city', 
                              help='Enter City', 
                              string='Ciudad'
                              )
    direccion = fields.Char()
    localidad = fields.Char()
    telefone = fields.Char()
    celular = fields.Char()
    sector_industrial = fields.Char() 
    nombre_contacto = fields.Many2one('res.partner')
    telefono_contacto = fields.Char()
    celular_contacto  = fields.Char()
    mail_contacto = fields.Char()
    cargo_contacto = fields.Char()
    direccion_sociales = fields.Many2one('res.social', 
                                         string='Dirección de Redes Sociales (Face- Instagram- Linked In)'
                                         )
    website_empresa  = fields.Char("Website de la empresa (si tiene)")
    representante_legal = fields.Char("Nombre del Representante Legal ")
    representante_legal_correo = fields.Char("Correo del Representante")
    representante_legal_tel = fields.Char("Telefono del Representante")
    representante_legal_tprod = fields.Char("Productos y/o Servicios de la Empresa")
    clientes_atiende = fields.Char("Clientes que atiende")
    Tipo_empresa_id = fields.Many2many('tipo.empresa')
    tamaño_empresa  = fields.Selection([('micro', '1-10 empleados Micro')])
    necesidad = fields.Text()
    dispo_invertir = fields.Text()
    obser = fields.Text()
    nombre_cargo = fields.Char()