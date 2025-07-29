from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_instruction_options_recipe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pantry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.PositiveIntegerField()),
                ('measurement', models.CharField(choices=[('G', 'gram'), ('ML', 'milliliter')], default='G', max_length=3)),
            ],
        ),
    ]
