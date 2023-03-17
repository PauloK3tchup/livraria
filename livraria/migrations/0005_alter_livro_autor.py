# Generated by Django 4.1.7 on 2023-03-17 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_livro_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='livraria.autor'),
        ),
    ]
