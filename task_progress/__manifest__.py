{
    'name': "Project Task Progress",
    'summary': """
        Track progress of project based on task and task based on subtask using weight and completion status""",
    'author': "Ardent Sharma",
    'category': 'Project',
    'version': '16.0',
    'depends': ['base', 'project'],
    'images': ['static/description/banner.png'],
    'data': [
        'views/project_view_inherit.xml',
        'views/project_task_view_inherit.xml',
    ],
}
