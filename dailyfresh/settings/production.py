"""
生产环境，配置文件
"""

"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# 收集静态文件到这个文件夹
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# FastDFS设置-客户端配置文件
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fdfs/client/production_client.conf')

# 设置fdfs存储服务器上nginx的IP和端口号
FDFS_URL = 'http://47.100.227.176:8888/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',
        'USER': 'root',
        'PASSWORD': os.environ['PASSWORD'],
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# gjango 的缓存配置
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/9',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True  # 与SMTP服务器通讯时，是否启动安全链接
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '2679771017@qq.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # 授权码
EMAIL_FROM = '天天生鲜<2679771017@qq.com>'  # 收件人看到的发件人


# 管理员配置(可以配置多个)
ADMINS = (
    ('兵哥', '2679771017@qq.com'),
)

# 日志文件
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/admin/dailyfresh_debug/dailyfresh_debug.log',  # 日志文件存放位置
        },
    # 重大错误，发送邮件给管理员
    'mail_admins': {
        'level': 'ERROR',
        'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],  # 记录启用文件（上面的‘file’文件）
            'level': 'DEBUG',  # 记录级别
            'propagate': True,  # 日志记录完成之后需不需要继续向上传递
        },
    'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',  # 发生错误时，去发送邮件
            'propagate': False,
        },

    },
}
