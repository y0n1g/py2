#import logging

from .local_settings import base_d

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '%(asctime)s: %(levelname)s: %(name)s.%(funcName)s()%(lineno)d: %(message)s'
        },
        'trace': {
            #%(processName)s may be alwasys MainProcess, useless
            #%(process)d is the process id we can get by ps aux, useless
            #%(thread)d is a long number like 140041808357120, useless
            #%(threadName)s is like Thread-3 and is created by threading
            'format': '%(asctime)s:%(threadName)s:%(name)s.%(funcName)s()%(lineno)d: %(message)s'
        },
        'info': {
            'format': '%(asctime)s: %(message)s'
        },
        'error': {
            'format': '%(asctime)s: %(name)s.%(funcName)s()%(lineno)d: %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'p.debug': {
            'filters': ['require_debug_true'],
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/p.debug',
            'formatter': 'debug',
        },
        'p.trace': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/p.trace',
            'formatter': 'trace',
        },
        'p.info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/p.info',
            'formatter': 'info',
        },
        'p.error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/p.error',
            'formatter': 'error',
        },
        'p.console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'error',
        },
        'django.debug': {
            'filters': ['require_debug_true'],
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/django.debug',
            'formatter': 'debug',
        },
        'django.info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/django.info',
            'formatter': 'info',
        },
        'django.error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/django.error',
            'formatter': 'error',
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*10,
            'backupCount' : 10,
            'filename': base_d + '/log/django.db.backends',
            'formatter': 'debug',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },

    'loggers': {
        'django': {
            'handlers': ['django.debug', 'django.error',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['django.db.backends', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        #configuration for the p application
        'p': {
            'handlers': ['p.debug', 'p.trace', 'p.info', 'p.error', 'p.console' ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

