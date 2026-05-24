from .base import *  # noqa: F403

DEBUG = True
SECRET_KEY = "unsafe-local-development-key"  # noqa: S105
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]  # noqa: S104
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

INSTALLED_APPS += ["debug_toolbar", "django_extensions", "django_browser_reload"]  # noqa: F405
MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
