# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    abc_field = fields.Char(string="abc text")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        abc_field = self.env['ir.config_parameter'].sudo().get_param('abc_config.abc_field')
        res.update(
            abc_field=abc_field
        )
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('abc_config.abc_field', self.abc_field)
        super(ResConfigSettings, self).set_values()




class abc_config(models.Model):
     _name = 'abc_config.abc_config'
     _description = 'abc_config.abc_config'

     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
