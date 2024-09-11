from odoo import models, fields, api 
from datetime import datetime

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                today = datetime.today()
                birth_date = student.birth_date
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                student.age = age
            else:
                student.age = 0
