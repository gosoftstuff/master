# -*- coding: utf-8 -*-
from odoo import http

# class /home/darren/softstuff/master/customerNum(http.Controller):
#     @http.route('//home/darren/softstuff/master/customer_num//home/darren/softstuff/master/customer_num/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/darren/softstuff/master/customer_num//home/darren/softstuff/master/customer_num/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/darren/softstuff/master/customer_num.listing', {
#             'root': '//home/darren/softstuff/master/customer_num//home/darren/softstuff/master/customer_num',
#             'objects': http.request.env['/home/darren/softstuff/master/customer_num./home/darren/softstuff/master/customer_num'].search([]),
#         })

#     @http.route('//home/darren/softstuff/master/customer_num//home/darren/softstuff/master/customer_num/objects/<model("/home/darren/softstuff/master/customer_num./home/darren/softstuff/master/customer_num"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/darren/softstuff/master/customer_num.object', {
#             'object': obj
#         })