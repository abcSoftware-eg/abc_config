# -*- coding: utf-8 -*-
# from odoo import http


# class AbcConfig(http.Controller):
#     @http.route('/abc_config/abc_config/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_config/abc_config/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_config.listing', {
#             'root': '/abc_config/abc_config',
#             'objects': http.request.env['abc_config.abc_config'].search([]),
#         })

#     @http.route('/abc_config/abc_config/objects/<model("abc_config.abc_config"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_config.object', {
#             'object': obj
#         })
