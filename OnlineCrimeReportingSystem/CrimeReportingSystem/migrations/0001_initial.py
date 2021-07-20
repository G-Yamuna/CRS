# Generated by Django 3.0 on 2021-07-02 08:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCrime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_type', models.CharField(choices=[('Rape', 'Rape'), ('Dowry', 'Dowry'), ('Petty Crime', 'Petty Crime'), ('Taxi Scam', 'Taxi Scam'), ('Arms Trafficking', 'Arms Trafficking'), ('Domestic Violence', 'Domestic Violence'), ('Illegal Drug Trade', 'Illegal Drug Trade'), ('s', '----Select----')], default='s', max_length=50)),
                ('crime_date', models.DateField(blank=True)),
                ('law', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AddCriminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_name', models.CharField(max_length=30)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('S', 'Select Gender')], default='S', max_length=15)),
                ('dob', models.DateField(null=True)),
                ('height', models.IntegerField(default=5)),
                ('weight', models.IntegerField(default=35)),
                ('identification', models.CharField(max_length=200)),
                ('full_details', models.CharField(blank=True, max_length=300)),
                ('criminal_photo', models.ImageField(blank=True, upload_to='')),
                ('criminal_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=100)),
                ('p_complaint', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
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
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('SelectGender', '---Select Gender---')], default='SelectGender', max_length=30)),
                ('age', models.IntegerField(default=18)),
                ('mobile_no', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
                ('pid_no', models.CharField(blank=True, max_length=10)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('profile', models.ImageField(default='default.png', upload_to='profiles/')),
                ('role', models.IntegerField(choices=[(0, 'guest'), (1, 'user'), (2, 'police')], default=0)),
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
        migrations.CreateModel(
            name='RoleRqst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('roletype', models.PositiveIntegerField(choices=[(1, 'user'), (2, 'police')])),
                ('proof', models.ImageField(blank=True, upload_to='proof/')),
                ('is_checked', models.BooleanField(default=0)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(max_length=20)),
                ('case_date', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('crime_proof', models.ImageField(blank=True, upload_to='')),
                ('update_status', models.IntegerField(choices=[(1, 'In Progress'), (2, 'Solved'), (3, 'Pending'), (4, 'Closed'), (5, 'Applied')], default=5)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]