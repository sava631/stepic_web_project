CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/',
    'python3': '/usr/bin/python3',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        #'app.module',
        'hello:app',
    ),
}
