# Generated by Django 3.2.4 on 2021-06-19 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='大学名')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('address', models.TextField(verbose_name='住所')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='氏名')),
                ('grade', models.IntegerField(choices=[('秀', '秀'), ('優', '優'), ('良', '良'), ('可', '可'), ('不', '不')], verbose_name='成績')),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=10, verbose_name='血液型')),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.TextField(verbose_name='住所')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school', verbose_name='大学名')),
            ],
        ),
    ]
