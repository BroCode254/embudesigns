# Generated by Django 5.1 on 2024-09-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Items_remaining',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('A', 'Accessories'), ('M', 'Menwear'), ('W', 'womenwear'), ('S', 'shoes')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('A', 'Nike'), ('B', 'Gucci'), ('E', 'Addidas'), ('R', 'Embu designs'), ('T', 'Mwivitoni'), ('Y', 'Bata shoes'), ('U', 'Bama'), ('I', 'Denim')], max_length=200, null=True),
        ),
    ]
