from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.CharField(default='caravan', max_length=20),
            preserve_default=False,
        ),
    ]
