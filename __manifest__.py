{
'name': 'Sample Module',
'version': '18.0.0.0',
'summary': 'This Module is for training purposes.',
'description': """This Module is for training purposes.
""",
'category':'',
'author': ' Jeevan V',
'website': 'www.zbeanztech.com',
"license": "LGPL-3",
'depends': [],
'data': [
    
    'Security/security.xml', # Always keep security fiels @ top
    'Security/ir.model.access.csv', # Always keep security fiels @ top
    'Views/model_one_view.xml',
    'Views/food.xml',
    'Views/menu.xml',
    'Views/car_rental.xml',
    
],
'test': [],
'demo': [],
'installable': True,
'auto_install': False,
'application': False,
}
