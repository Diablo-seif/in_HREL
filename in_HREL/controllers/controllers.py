# -*- coding: utf-8 -*-
# from odoo import http


# class SeifHr(http.Controller):
#     @http.route('/seif_hr/seif_hr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seif_hr/seif_hr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('seif_hr.listing', {
#             'root': '/seif_hr/seif_hr',
#             'objects': http.request.env['seif_hr.seif_hr'].search([]),
#         })

#     @http.route('/seif_hr/seif_hr/objects/<model("seif_hr.seif_hr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seif_hr.object', {
#             'object': obj
#         })
