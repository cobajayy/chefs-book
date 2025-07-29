from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_recipe_pantry_alter_pantry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantry',
            name='measurement',
            field=models.CharField(choices=[('g', 'Gram'), ('ml', 'Milliliter'), ('lbs', 'Pounds'), ('oz', 'Ounces'), ('tsp', 'Teaspoon'), ('tbsp', 'Tablespoon'), ('cup', 'Cup')], default='g', max_length=4),
        ),
    ]
