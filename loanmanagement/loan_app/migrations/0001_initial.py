# Generated by Django 3.0 on 2019-12-09 09:01

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import loan_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('loanamount', models.IntegerField()),
                ('status', models.CharField(choices=[('DRAFTS', 'drafts'), ('STAGE ONE PENDING', 'stage_one_pending'), ('STAGE ONE VERIFIED', 'stage_one_verified'), ('STAGE TWO PENDING', 'stage_two_pending'), ('STAGE TWO VERIFIED', 'stage_two_verified'), ('ARCHIVED', 'archived')], default='DRAFTS', max_length=25)),
                ('employee_id', models.IntegerField()),
                ('permanent_address', models.CharField(max_length=100)),
                ('temporary_address', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('recruitdate', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('submission_form', models.ImageField(null=True, upload_to='')),
                ('lalpurja', models.ImageField(null=True, upload_to=loan_app.models.folder)),
                ('malpot_receipt_1', models.ImageField(null=True, upload_to='')),
                ('malpot_receipt_2', models.ImageField(null=True, upload_to='')),
                ('verified_map', models.ImageField(null=True, upload_to='')),
                ('blue_print', models.ImageField(null=True, upload_to='')),
                ('committee_sifaris', models.ImageField(null=True, upload_to='')),
                ('marriage_certificate', models.ImageField(null=True, upload_to='')),
                ('mun_vdc_sifaris', models.ImageField(null=True, upload_to='')),
                ('dristibandha', models.ImageField(null=True, upload_to='')),
                ('close_house_photo', models.ImageField(null=True, upload_to='')),
                ('inspection_report', models.ImageField(null=True, upload_to='')),
                ('anusuchi_six_form', models.ImageField(null=True, upload_to='')),
                ('tippani', models.ImageField(null=True, upload_to='')),
                ('voucher', models.ImageField(null=True, upload_to='')),
                ('debit_credit', models.ImageField(null=True, upload_to='')),
                ('quotation', models.ImageField(null=True, upload_to='')),
                ('memo', models.ImageField(null=True, upload_to='')),
                ('credit_note', models.ImageField(null=True, upload_to='')),
                ('approved_letter', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Loantype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loantype', models.CharField(max_length=100)),
                ('interest', models.FloatField(default=0)),
                ('period_years', models.FloatField(default=0.0)),
                ('num_payments_per_year', models.FloatField(default=0.0)),
                ('start_date', models.DateField(default=0.0)),
                ('created_on', models.CharField(default='2076-08-23', max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_app.Loan')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='loanname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_app.Loantype'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
