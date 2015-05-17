import logging
import os


def post_worker_init(worker):
    from psycogreen.gevent import patch_psycopg

    import django
    from django.core.urlresolvers import resolve

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ogs.settings")

    django.setup()
    resolve('/date')

    patch_psycopg()
    worker.log.info("Made Psycopg Green")

# def post_fork(server, worker):
#
#     from psycogreen.gevent import patch_psycopg
#
#     import django
#     from django.core.urlresolvers import resolve
#
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ogs.settings")
#
#     django.setup()
#     resolve('/date')
#
#     patch_psycopg()
#     worker.log.info("Made Psycopg Green")
