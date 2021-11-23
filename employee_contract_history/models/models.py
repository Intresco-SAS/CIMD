# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import decimal    

def num2words(num):
    num = decimal.Decimal(num)
    decimal_part = num - int(num)
    num = int(num)

    if decimal_part:
        return num2words(num) + " point " + (" ".join(num2words(i) for i in str(decimal_part)[2:]))

    under_20 = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
    tens = ['TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']
    above_100 = {100: 'HUNDRED', 1000: 'THOUSAND', 100000: 'LAKHS', 10000000: 'CRORES'}

    if num < 20:
        return under_20[num]

    if num < 100:
        return tens[num // 10 - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

    # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
    pivot = max([key for key in above_100.keys() if key <= num])

    return num2words(num // pivot) + ' ' + above_100[pivot] + ('' if num % pivot==0 else ' ' + num2words(num % pivot))


class Employee(models.Model):

    _inherit = 'hr.employee'

    def get_running_contract(self):
        """
        """
        contracts = self.contract_ids.filtered(lambda contract:contract.state == 'open')
        if contracts:
            return contracts[0]
        return self.env['hr.contract']

    def get_other_contract(self):
        """
        """
        contracts = self.contract_ids.filtered(lambda contract:contract.state != 'open')
        return contracts

    def get_num_to_words(self, amount=0.0):
        """
        """
        return num2words(decimal.Decimal(amount, lang='es'))

    def get_current_date(self):
        """
        """
        return datetime.now().strftime("%d %B %Y")