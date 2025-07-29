from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_pantry_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(choices=[('African', 'African'), ('American', 'American'), ('Asian', 'Asian'), ('European', 'European'), ('Latin', 'Latin'), ('Middle Eastern', 'Middleeastern')], default='African'),
        ),
    ]
