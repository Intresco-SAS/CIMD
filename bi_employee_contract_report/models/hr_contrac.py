from odoo import _, api, fields, models, tools
import locale
import datetime

TRANS_MONTH = {'january' : 'Enero',
               'november' : 'Noviembre'}

class HrContract(models.Model):

    _inherit = 'hr.contract'

    

    def print_date(self):
        month = datetime.datetime.today().strftime('%B')
        print(month)
        return TRANS_MONTH.get(month,month)