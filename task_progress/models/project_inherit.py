from odoo import models, fields, api, _


class ProjectProgress(models.Model):
    _inherit = 'project.project'

    development = fields.Float(string=_("Development"), readonly=True, default=0)