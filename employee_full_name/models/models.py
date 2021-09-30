# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from datetime import date

class HrEmployeePrivate(models.Model):
    
    _name = "res.country.state.city"
    _description = "cityes"
    _order = 'code'

    code = fields.Char('City Code', size=5, help='Code DANE - 5 digits-',
                       required=True)
    name = fields.Char('City Name', size=64, required=True)
    state_id = fields.Many2one("res.country.state", help='Enter State', ondelete='restrict', string='Departamento de expedicion')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')

    
class EmployeeFullName(models.Model):
    _inherit = 'hr.employee'

    emp_fname = fields.Char(string='Primer nombre', copy=True)
    emp_mname = fields.Char(string='Segundo nombre', copy=True)
    emp_lname = fields.Char(string='Primer apellido', copy=True)
    emp_slname = fields.Char(string='Segundo apellido', copy=True)
    cargo= fields.Selection([('jefe_desarrollo', 'Jefe desarollo'),('gerente', 'Gerente'),])
    sede= fields.Selection([('planta', 'Planta Hermeco (Calle 7 # 50-96 Poblado-Medellín)'),('antioquia', 'Antioquia (Cra. 43 #31-89-San Diego- Medellín)'),('eje','Eje Cafetero (Km 11 Via Cerritos-Pereira)'),('bogota','Bogotá (Calle 81A # 73A-22 Minuto de Dios-Bogotá)')])
    doctype = fields.Selection([('12', 'Identity Card'),('13', 'Citizenship Card'),('21','Alien Registration Card'),('41','PEP')])
    validity = fields.Date(string='Validity to')
    expedition_date = fields.Date(string='Expedition date')
    country_nacionalidad_id = fields.Many2one('res.country', string='Nacionalidad', help='Select Country', ondelete='restrict')
    state_id = fields.Many2one("res.country.state", help='Enter State', ondelete='restrict', string='Departamento de expedicion')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')    
    city_id = fields.Many2one('res.country.state.city', help='Enter City', string='Municipio de expedicion')
    state_born_id = fields.Many2one("res.country.state",string='Departamento de nacimiento', help='Enter State', ondelete='restrict')
    country_bornid = fields.Many2one('res.country', string='Pais de nacimeinto', help='Select Country', ondelete='restrict')    
    city_born_id = fields.Many2one('res.country.state.city', string='Municipio de nacimiento', help='Enter City')
    city_re_id = fields.Many2one('res.country.state.city', string='Ciudad de residencia', help='Enter City')
    hide = fields.Boolean(string='Hide', compute="_compute_hide")
    sex = fields.Selection([('hombre', 'Hombre'),('mujer', 'Mujer'),('otro','Otro')])
    grupo_sangre = fields.Selection([('a', 'A'),('b', 'B'),('ab','AB'),('o','O')])
    Tipo_pobl_vul= fields.Selection([('1', 'Niños, niñas, adolescentes'),('2', 'Adultos mayores'),('3','Poblaciones en situación de discapacidad'),
                                    ('4','Grupos étnicos'),('5', 'Víctimas'),('6','Víctimas'),('7', 'Enfermedades huérfanas'),
                                    ('8','Enfermedades catastróficas (Cáncer, VIH y renales)')])
    neighborhood = fields.Char(string='Barrio', copy=True)
    estrato = fields.Selection([('1', '1'),('2', '2'),('3','3'),('4','4'),('5','5'),('6','6')])
    tipo_vivienda = fields.Selection([('1', 'Vivienda de Interés Prioritario (VIP)'),('2', 'Vivienda de Interés Social (VIS)'),('3','Vivienda No Vis')])
    movil = fields.Char(string='Celular', copy=True)
    ###########################################################################
    name_f = fields.Char(string='Nombre completo', copy=True)
    r_paren = fields.Selection([('1', 'Hij@'),('2', 'Padre'),('3','Herman@'),('4','4'),('5','5'),('6','6')])
    doctype1 = fields.Selection([('12', 'Identity Card'),('13', 'Citizenship Card'),('21','Alien Registration Card'),('41','PEP')])
    num_iden = fields.Char(string='Numero de identificacion', copy=True)
    sex1 = fields.Selection([('hombre', 'Hombre'),('mujer', 'Mujer'),('otro','Otro')])
    birthday1 = fields.Date(string='Fecha de nacimiento')
    eps = fields.Selection([('1', 'SURA'),('2', 'Nueva')])
    n_edu = fields.Selection([('1', 'Básica primaria'),('2', 'Básica secundaria')])
    ocu = fields.Char(string='Ocupación', copy=True)
    vconcol = fields.Selection([('1', 'Si'),('2', 'No')])
    dep_eco = fields.Selection([('1', 'Si'),('2', 'No')])
    ###########################################################################
    nivel_forma = fields.Selection([('1', 'Nivel Técnico Profesional'),('2', 'Nivel Tecnológico'),('3','Nivel Profesional'),('4','Especializaciones'),('5','Maestrías'),('6','Doctorados')])
    nombre_forma = fields.Char(string='Nombre de formacion', copy=True)
    insti_educ = fields.Char(string='Institución educativa', copy=True)
    date_grade = fields.Date(string='Fecha de Grado')
    estate_study = fields.Selection([('1', '1'),('2', '2'),('3','3'),('4','4'),('5','5'),('6','6')])
    num_horas = fields.Char(string='N° horas', copy=True)
    cargo_exp = fields.Char(string='Cargo', copy=True)
    empresa = fields.Char(string='Empresa', copy=True)
    date_in = fields.Date(string='Fecha de inicio')
    date_out = fields.Date(string='Fecha de fin')
    tipo_contrato = fields.Selection(
        string='Tipo de contrato',
        selection=[('1', 'Término fijo'),
                   ('2', 'Término Indefinido'),
                   ('3', 'Obra o labor'),
                   ('4', 'Aprendizaje'),
                   ('5', 'Temporal, ocasional o accidental'),])
    state_ex_id = fields.Many2one("res.country.state",string='Departamento de nacimiento', help='Enter State', ondelete='restrict')
    country_ex_id = fields.Many2one('res.country', string='Pais de nacimeinto', help='Select Country', ondelete='restrict')    
    city_ex_id = fields.Many2one('res.country.state.city', string='Municipio de nacimiento', help='Enter City')
    retiro = fields.Selection(
        string='Motivo de retiro',
        selection=[('1', 'Renuncia'),
                   ('2', 'Expiración del plazo fijo pactado'),
                   ('3', 'Mutuo consentimiento'),
                   ('5', 'Terminación de la obra o labor contratada'),]
    )
    fun = fields.Char(string='Funciones', copy=True)
    premios = fields.Char(string='Premios o distinciones', copy=True)
    pasatiempos = fields.Char(string='Pasatiempos', copy=True)
    voluntariados_asociaciones = fields.Char(string='Voluntariados o asociaciones', copy=True)
    mascotas = fields.Selection([('1', 'Si'),('2', 'No')])
    job_id = fields.Many2one(help='Enter City')
    otro_cargo = fields.Boolean('Agregar otro cargo',)
    ######################################################
    cargo_exp_1 = fields.Char(string='Cargo', copy=True)
    date_in_1 = fields.Date(string='Fecha de inicio')
    date_out_1 = fields.Date(string='Fecha de fin')
    tipo_contrato_1 = fields.Selection(
        string='Tipo de contrato',
        selection=[('1', 'Término fijo'),
                   ('2', 'Término Indefinido'),
                   ('3', 'Obra o labor'),
                   ('4', 'Aprendizaje'),
                   ('5', 'Temporal, ocasional o accidental'),])
    retiro_1 = fields.Selection(
        string='Motivo de retiro',
        selection=[('1', 'Renuncia'),
                   ('2', 'Expiración del plazo fijo pactado'),
                   ('3', 'Mutuo consentimiento'),
                   ('5', 'Terminación de la obra o labor contratada'),]
    )
    fun_1 = fields.Char(string='Funciones', copy=True)
    empresa_1 = fields.Char(string='Empresa', copy=True)
    state_ex_id_1 = fields.Many2one("res.country.state",string='Departamento de nacimiento', help='Enter State', ondelete='restrict')
    country_ex_id_1 = fields.Many2one('res.country', string='Pais de nacimeinto', help='Select Country', ondelete='restrict')    
    city_ex_id_1 = fields.Many2one('res.country.state.city', string='Municipio de nacimiento', help='Enter City')
    otro_cargo_1 = fields.Boolean('Agregar otro cargo',)
    ######################################################
    cargo_exp_2 = fields.Char(string='Cargo', copy=True)
    date_in_2 = fields.Date(string='Fecha de inicio')
    date_out_2 = fields.Date(string='Fecha de fin')
    tipo_contrato_2 = fields.Selection(
        string='Tipo de contrato',
        selection=[('1', 'Término fijo'),
                   ('2', 'Término Indefinido'),
                   ('3', 'Obra o labor'),
                   ('4', 'Aprendizaje'),
                   ('5', 'Temporal, ocasional o accidental'),])
    retiro_2 = fields.Selection(
        string='Motivo de retiro',
        selection=[('1', 'Renuncia'),
                   ('2', 'Expiración del plazo fijo pactado'),
                   ('3', 'Mutuo consentimiento'),
                   ('5', 'Terminación de la obra o labor contratada'),]
    )
    fun_2 = fields.Char(string='Funciones', copy=True)
    empresa_2 = fields.Char(string='Empresa', copy=True)
    state_ex_id_2 = fields.Many2one("res.country.state",string='Departamento de nacimiento', help='Enter State', ondelete='restrict')
    country_ex_id_2 = fields.Many2one('res.country', string='Pais de nacimeinto', help='Select Country', ondelete='restrict')    
    city_ex_id_2 = fields.Many2one('res.country.state.city', string='Municipio de nacimiento', help='Enter City')
    #############################################################
    otro_estudio = fields.Boolean('Agregar otro titulo',)
    nivel_forma_1 = fields.Selection([('1', 'Nivel Técnico Profesional'),('2', 'Nivel Tecnológico'),('3','Nivel Profesional'),('4','Especializaciones'),('5','Maestrías'),('6','Doctorados')])
    nombre_forma_1= fields.Char(string='Nombre de formacion', copy=True)
    insti_educ_1 = fields.Char(string='Institución educativa', copy=True)
    date_grade_1 = fields.Date(string='Fecha de Grado')
    estate_study_1 = fields.Selection([('1', '1'),('2', '2'),('3','3'),('4','4'),('5','5'),('6','6')])
    num_horas_1 = fields.Char(string='N° horas', copy=True)
    otro_estudio_1 = fields.Boolean('Agregar otro titulo',)
    nivel_forma_2 = fields.Selection([('1', 'Nivel Técnico Profesional'),('2', 'Nivel Tecnológico'),('3','Nivel Profesional'),('4','Especializaciones'),('5','Maestrías'),('6','Doctorados')])
    nombre_forma_2= fields.Char(string='Nombre de formacion', copy=True)
    insti_educ_2 = fields.Char(string='Institución educativa', copy=True)
    date_grade_2 = fields.Date(string='Fecha de Grado')
    estate_study_2 = fields.Selection([('1', '1'),('2', '2'),('3','3'),('4','4'),('5','5'),('6','6')])
    num_horas_2 = fields.Char(string='N° horas', copy=True)
    #################################################################
    otro_fami_dep = fields.Boolean('Agregar otro familiar dependiente')
    name_f_1 = fields.Char(string='Nombre completo', copy=True)
    r_paren_1 = fields.Selection([('1', 'Hij@'),('2', 'Padre'),('3','Herman@'),('4','4'),('5','5'),('6','6')])
    doctype1_1 = fields.Selection([('12', 'Identity Card'),('13', 'Citizenship Card'),('21','Alien Registration Card'),('41','PEP')])
    num_iden_1 = fields.Char(string='Numero de identificacion', copy=True)
    sex1_1 = fields.Selection([('hombre', 'Hombre'),('mujer', 'Mujer'),('otro','Otro')])
    birthday1_1 = fields.Date(string='Fecha de nacimiento')
    eps_1 = fields.Selection([('1', 'SURA'),('2', 'Nueva')])
    n_edu_1 = fields.Selection([('1', 'Básica primaria'),('2', 'Básica secundaria')])
    ocu_1 = fields.Char(string='Ocupación', copy=True)
    vconcol_1 = fields.Selection([('1', 'Si'),('2', 'No')])
    dep_eco_1 = fields.Selection([('1', 'Si'),('2', 'No')])
    ################################################################
    otro_fami_dep_1 = fields.Boolean('Agregar otro familiar dependiente')
    name_f_2 = fields.Char(string='Nombre completo', copy=True)
    r_paren_2 = fields.Selection([('1', 'Hij@'),('2', 'Padre'),('3','Herman@'),('4','4'),('5','5'),('6','6')])
    doctype1_2 = fields.Selection([('12', 'Identity Card'),('13', 'Citizenship Card'),('21','Alien Registration Card'),('41','PEP')])
    num_iden_2 = fields.Char(string='Numero de identificacion', copy=True)
    sex1_2 = fields.Selection([('hombre', 'Hombre'),('mujer', 'Mujer'),('otro','Otro')])
    birthday1_2 = fields.Date(string='Fecha de nacimiento')
    eps_2 = fields.Selection([('1', 'SURA'),('2', 'Nueva')])
    n_edu_2 = fields.Selection([('1', 'Básica primaria'),('2', 'Básica secundaria')])
    ocu_2 = fields.Char(string='Ocupación', copy=True)
    vconcol_2 = fields.Selection([('1', 'Si'),('2', 'No')])
    dep_eco_2 = fields.Selection([('1', 'Si'),('2', 'No')])
    #vegetariano-vegano = fields.Boolean()

    #colombia pordefecto en el campo country_id
    def _colombia(self):
        return self.env['res.country'].search([('code', '=', 'CO')]).id
    '''def _colombia1(self):
        return self.env['res.country'].search([('code', '=', 'CO')]).id'''

    @api.onchange('emp_fname','emp_mname','emp_lname', 'emp_slname')
    def get_employee_name(self):

        for emp_name in self:
            if self.emp_fname:
                fname = self.emp_fname
            else:
                fname = ''
            if self.emp_mname:
                mname = self.emp_mname
            else:
                mname = ''
            if self.emp_slname:
                slname = self.emp_slname
            else:
                slname = ''
            if self.emp_lname:
                lname = self.emp_lname
            else:
                lname = ''
            emp_name.name = (str(fname)+' '+str(mname)+' '+str(lname)+' '+str(slname)).title()

    # Dependent picklist code to show State based on selected Country colombia -> antioquia, cundinamarca,  etc..
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}
 
    # Dependent picklist code to show city based on selected state antioquia -> medellin, copacabana,  etc..
    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            return {'domain': {'city_id': [('state_id', '=', self.state_id.id)]}}
        else:
            return {'domain': {'city_id': []}}

    # Show Hide State selection based on Country
    @api.depends('country_id')
    def _compute_hide(self):
        if self.country_id:
            self.hide = False
        else:
            self.hide = True
    