# Generated by Django 3.0 on 2019-12-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='empoyee_id',
            new_name='empoyeeid',
        ),
    ]
