from odoo import  models ,fields

class HREmployeeInherit(models.Model):
        _inherit = 'hr.employee'
        military_certificate = fields.Binary(string="Military Certificate",  )


