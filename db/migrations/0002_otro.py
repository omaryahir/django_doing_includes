# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otrocampo', models.CharField(max_length=50, verbose_name=b'otro campo')),
                ('person', models.ForeignKey(to='db.Person')),
            ],
            options={
                'verbose_name': 'Otro',
                'verbose_name_plural': 'Otros',
            },
            bases=(models.Model,),
        ),
    ]
