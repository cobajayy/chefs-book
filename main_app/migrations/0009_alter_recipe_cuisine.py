from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_recipe_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(choices=[('African', 'African'), ('American', 'American'), ('Asian', 'Asian'), ('Dessert', 'Dessert'), ('European', 'European'), ('Latin', 'Latin'), ('Middle Eastern', 'Middleeastern')], default='African'),
        ),
    ]
