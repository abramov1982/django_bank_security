import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_bank_security.settings')
django.setup()

from datacenter.models import Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    pass
