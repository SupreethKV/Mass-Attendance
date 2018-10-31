# -*- coding: utf-8 -*-
{
    'name': "Mass Attendance",
    'summary': """
        Mass Attendance for employees""",
    'description': """
        Takes Mass Attendance for all Employess listed in HR Module. 
        Once validated, present employess will be listed in Attendance menu and Absent 
        Employees will be listed in HR Leaves.
    """,
    'author': "Supreeth",
    'website': "http://www.autochip.in",
    'category': 'Attendance',
    'version': '0.1',
    'depends': ['hr', 'hr_attendance', 'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'views/mass_attendance_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}