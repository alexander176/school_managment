{
    "name": "School Management",
    "version": "16.0.1.0.0",
    "summary": "Manage school students, subjects and teachers",
    "author": "Anthony Simbaña",
    "category": "Other",
    "depends": ["base", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/school_student_view.xml",
        "views/school_subject_view.xml",
        "views/school_teacher_view.xml",
    ],
    "license": "OPL-1",
    "installable": True,
    "application" : True,
}
