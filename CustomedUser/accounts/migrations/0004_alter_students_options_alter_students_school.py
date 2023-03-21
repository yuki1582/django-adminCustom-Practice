# Generated by Django 4.1.7 on 2023-03-21 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_schools_options_alter_students_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ('score',), 'verbose_name_plural': '生徒'},
        ),
        migrations.AlterField(
            model_name='students',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.schools', verbose_name='学校名'),
        ),
    ]
