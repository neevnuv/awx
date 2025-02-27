# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-08 14:51
from __future__ import unicode_literals

from django.db import migrations, models
from awx.main.migrations._create_system_jobs import create_clearsessions_jt


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0077_v360_add_default_orderings'),
    ]

    operations = [
        # Schedule Analytics System Job Template
        migrations.RunPython(create_clearsessions_jt, migrations.RunPython.noop),
        # previously ran create_cleartokens_jt, logic for this has been removed
        migrations.AlterField(
            model_name='systemjob',
            name='job_type',
            field=models.CharField(
                blank=True,
                choices=[
                    ('cleanup_jobs', 'Remove jobs older than a certain number of days'),
                    ('cleanup_activitystream', 'Remove activity stream entries older than a certain number of days'),
                    ('cleanup_sessions', 'Removes expired browser sessions from the database'),
                    ('cleanup_tokens', 'Removes expired OAuth 2 access tokens and refresh tokens'),
                ],
                default='',
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name='systemjobtemplate',
            name='job_type',
            field=models.CharField(
                blank=True,
                choices=[
                    ('cleanup_jobs', 'Remove jobs older than a certain number of days'),
                    ('cleanup_activitystream', 'Remove activity stream entries older than a certain number of days'),
                    ('cleanup_sessions', 'Removes expired browser sessions from the database'),
                    ('cleanup_tokens', 'Removes expired OAuth 2 access tokens and refresh tokens'),
                ],
                default='',
                max_length=32,
            ),
        ),
    ]
