from distutils.command.upload import upload
from odoo import models, fields

class UpLoadImg(models.Model):
    _inherit = "hr.contract.type"

    upload_img = fields.Binary(String="Imagenes para firma")

    def get_logo(self,id_no): 
        logo = (self.env["hr.contract.type"].search([("upload_img","=",id_no)])).inv_logo
        return logo