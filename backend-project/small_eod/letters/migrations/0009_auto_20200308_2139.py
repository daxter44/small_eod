# Generated by Django 3.0.3 on 2020-03-08 21:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0006_auto_20200221_1956'),
        ('letters', '0008_letter_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='channels.Channel', verbose_name='Channel'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='comment',
            field=models.CharField(blank=True, help_text='Comment for letter.', max_length=256, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Date of sending or receiving.', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='excerpt',
            field=models.CharField(blank=True, help_text='Excerpt of letter.', max_length=256, verbose_name='Excerpt'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='final',
            field=models.BooleanField(default=True, help_text='Indicates whether the document has final content or is, for example, a draft', verbose_name='Final version'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='identifier',
            field=models.CharField(blank=True, help_text='Identifier of letter.', max_length=256, verbose_name='Identifier'),
        ),
    ]
