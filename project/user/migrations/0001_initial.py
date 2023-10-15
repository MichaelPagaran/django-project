# Generated by Django 4.2.6 on 2023-10-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(blank=True, max_length=150)),
                ('profile_img', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=150)),
                ('lastname', models.CharField(blank=True, max_length=150)),
                ('birthdate', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=255)),
                ('accounts', models.ManyToManyField(to='user.account')),
            ],
        ),
    ]
