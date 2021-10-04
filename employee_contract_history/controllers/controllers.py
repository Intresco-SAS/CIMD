# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeContractHistory(http.Controller):
#     @http.route('/employee_contract_history/employee_contract_history/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_contract_history/employee_contract_history/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_contract_history.listing', {
#             'root': '/employee_contract_history/employee_contract_history',
#             'objects': http.request.env['employee_contract_history.employee_contract_history'].search([]),
#         })

#     @http.route('/employee_contract_history/employee_contract_history/objects/<model("employee_contract_history.employee_contract_history"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_contract_history.object', {
#             'object': obj
#         })
