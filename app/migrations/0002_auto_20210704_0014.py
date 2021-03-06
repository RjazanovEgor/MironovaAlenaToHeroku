# Generated by Django 3.2.5 on 2021-07-03 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcompany',
            options={'ordering': ('name',), 'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.CreateModel(
            name='AboutCompanyPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='app.aboutcompany')),
            ],
            options={
                'verbose_name': 'Пункты',
                'verbose_name_plural': 'Пункт',
                'ordering': ('description',),
            },
        ),
    ]
