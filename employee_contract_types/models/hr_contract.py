# -*- coding: utf-8 -*-
from odoo import models, fields

class HrContract(models.Model):
    _inherit = "hr.contract"

    contract_type_id = fields.Many2one("hr.contract.type", string="Contract Type")
    nivel_del_cargo = fields.Selection([('a', 'A')])
    resource_calendar_id = fields.Many2one("resource.calendar", string="Jornada laboral")
    project = fields.Many2one("project.project", string="proyecto")
    honorarios = fields.Float(string="Hononarios")
    grado_salarial = fields.Selection([('a', 'A')])
    tipo_gasto = fields.Selection([('a', 'Costo directo'),
                                   ('2', 'Costo indirecto'),
                                   ('3', 'Gasto administrativo'),
                                   ('4', 'Gasto ventas')
                                   ])
    fin_periodo_prueba = fields.Date(string="Fin del periodo de prueba")
    
    #Perfil_cargo no se usa, se cambia por perfil_cargo1
    perfil_cargo = fields.Char(string="Perfil del cargo") 
    perfil_cargo1 = fields.Binary(string="Perfil del cargo")

    antiguedad = fields.Integer(string="Antigüedad")
    bank_id = fields.Integer(string="Número de cuenta")
    metodo_pago = fields.Selection([('a', 'Transferencia bancaria (predterminado)')])
    pais = fields.Many2one('res.country', string='Pais', help='Select Country', ondelete='restrict') 
    banco =  fields.Many2one('res.partner.bank', string='Banco', help='Select bank', ondelete='restrict') 
    tipo_decuenta = fields.Selection([('ahorros', 'Ahorros'),
                                      ('2', 'Corriente')
                                      ])
    arl = fields.Selection(string='ARL',selection=[('sura', 'SURA')], default='sura')
    clase_riesgo = fields.Selection(string='Clase de riesgo',selection=[('1', 'Tipo I'),
                                                                        ('2', 'Tipo II'),
                                                                        ('3', 'Tipo III'),
                                                                        ('4', 'Tipo IV'),
                                                                        ('5', 'Tipo V')
                                                                        ]
                                    )
    cs = fields.Selection(string='Caja de compensacion',
                        selection=[('comfamiliarRisaralda', 'Comfamiliar Risaralda'),
                        ('compensar', 'Compensar'),
                        ('comfama', 'Comfama'),
                        ]
    )
    afp = fields.Selection(string='AFP',
                        selection=[('olpensiones', 'Colpensiones'),
                        ('olfondos', 'Colfondos'),
                        ('orvenir', 'Porvenir'),
                        ('rotecci', 'Protección'),
                        ('skandia', 'Old Mutual (skandia)'),
                        ('ensionado', 'Pensionado'),
                        ('oaplica', 'No aplica'),
                        ]
    )
    afc = fields.Selection(string='AFC',
                        selection=[('ondoacionalAhorro', 'Fondo Nacional del Ahorro'),
                        ('olfondos', 'Colfondos'),
                        ('orvenir', 'Porvenir'),
                        ('rotección', 'Protección'),
                        ('skandia', 'Old Mutual (skandia)'),
                        ('oaplica', 'No aplica'),
                        ]
    )
    eps = fields.Selection(string='EPS',
                        selection=[('Ambuq', 'Ambuq'),
                        ('Asmet_Salud', 'Asmet Salud'),
                        ('Cafesalud', 'Cafesalud'),
                        ('CajacopiAtlantico', 'Cajacopi Atlántico'),
                        ('CapitalSalud', 'Capital Salud'),
                        ('Capresoca', 'Capresoca'),
                        ('Colmedica', 'Colmedica'),
                        ('Colpatria', 'Colpatria'),
                        ('Comfachoc', 'Comfachocó'),
                        ('Comfacor', 'Comfacor'),
                        ('Comfacundi', 'Comfacundi'),
                        ('Comfamiliar', 'Comfamiliar'),
                        ('ComfamiliarNariño', 'Comfamiliar Nariño'),
                        ('ComfenalcoAntioquia', 'Comfenalco Antioquia'),
                        ('ComfenalcoValle', 'Comfenalco Valle'),
                        ('Comparta', 'Comparta'),
                        ('Compensar', 'Compensar'),
                        ('Convidia', 'Convidia'),
                        ('Coomeva', 'Coomeva'),
                        ('Coosalud', 'Coosalud'),
                        ('CruzBlanca', 'Cruz Blanca'),
                        ('Ecoopsops', 'Ecoopsops'),
                        ('Empresamutual', 'Empresa mutual'),
                        ('Empresamutual', 'Empresa mutual'),
                        ('EmssanarESS', 'Emssanar ESS'),
                        ('EpsasociacinIND', 'Eps asociación IND'),
                        ('Famisanar', 'Famisanar'),
                        ('Fosyga', 'Fosyga'),
                        ('GoldenGroup', 'GoldenGroup'),
                        ('HumanaVivir', 'Comfenalco Antioquia'),
                        ('Medimas', 'Medimas'),
                        ('MutualSer', 'Mutual Ser'),
                        ('Nuevaeps', 'Nueva eps'),
                        ]
    )

class HrEmployeePrivate(models.Model):
    
    _name = "res.country.state.city"
    _description = "cityes"
    _order = 'code'

    code = fields.Char('City Code', size=5, help='Code DANE - 5 digits-',
                       required=True)
    name = fields.Char('City Name', size=64, required=True)
    state_id = fields.Many2one("res.country.state", help='Enter State', ondelete='restrict', string='Departamento de expedicion')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict', default='_colombia')