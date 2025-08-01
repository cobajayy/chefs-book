from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_pantry'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pantry',
            field=models.ManyToManyField(to='main_app.pantry'),
        ),
        migrations.AlterField(
            model_name='pantry',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
