# Generated by Django 4.2.7 on 2023-12-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_homeyonalishlardivs_svg'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemavjudyonalishlar',
            name='cap_color',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]