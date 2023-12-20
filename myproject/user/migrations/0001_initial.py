# Generated by Django 3.2.4 on 2022-03-17 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('cpic', models.ImageField(default='', upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('confirmPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndes', models.TextField(max_length=5000)),
                ('ndate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('Dob', models.DateField()),
                ('Password', models.CharField(max_length=30)),
                ('ConfirmPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stitle', models.CharField(max_length=200)),
                ('sdes', models.CharField(max_length=500)),
                ('spic', models.ImageField(default='', upload_to='static/slider/')),
                ('sdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vtitle', models.CharField(max_length=200)),
                ('vdes', models.TextField(max_length=600)),
                ('thumb', models.ImageField(default='', upload_to='static/thumbnail/')),
                ('vlink', models.CharField(max_length=500)),
                ('vdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('headlines', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=800)),
                ('newsdetail', models.TextField(max_length=8000)),
                ('newspic', models.ImageField(default='', upload_to='static/news/')),
                ('ndate', models.DateField()),
                ('ncategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
    ]