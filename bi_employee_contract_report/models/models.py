# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import decimal    

class Employee(models.Model):

    def get_current_date(self):
        """
        """
        return datetime.now().strftime("%d %B %Y")