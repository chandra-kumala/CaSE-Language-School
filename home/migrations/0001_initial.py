# Generated by Django 2.2.9 on 2020-07-10 12:34

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_tag', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Facebook site code',
                'verbose_name_plural': 'Facebook site code',
            },
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_tag', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Google site code',
                'verbose_name_plural': 'Google site code',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css', models.CharField(blank=True, max_length=255, null=True, verbose_name='List CSS Classes (eg. text-primary py-0)')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Desc on hover (eg. December Bulletin)')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link to resource (eg tel:+62-061-661-6765)')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='FA Icon (eg. fas fa-newspaper fa-fw fa-2x)')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Visible text (eg. Latest School Bulletin)')),
            ],
            options={
                'verbose_name': 'Social Media link and icon',
                'verbose_name_plural': 'Social Media links and icons',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('google_ad_code', models.CharField(blank=True, max_length=50, null=True)),
                ('my_stream', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(blank=True, classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(blank=True)), ('embed', wagtail.embeds.blocks.EmbedBlock(blank=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('mapurl', wagtail.core.blocks.CharBlock('Google Map URL', blank=True, max_length=500, null=True)), ('calendarurl', wagtail.core.blocks.URLBlock('URL for calendar', blank=True, null=True)), ('buttonLink', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(blank=True)), ('link', wagtail.core.blocks.URLBlock(blank=True, label='external URL'))])), ('jumbotron', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(blank=True, classname='full title')), ('text', wagtail.core.blocks.TextBlock(blank=True, required=False)), ('classes', wagtail.core.blocks.CharBlock(blank=True, label='CSS classes from BS (text-light or text-dark)', required=False)), ('background', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('buttonLabel', wagtail.core.blocks.CharBlock(blank=True, label='Text on button', required=False)), ('buttonUrl', wagtail.core.blocks.URLBlock(blank=True, required=False))])), ('testimonial', wagtail.core.blocks.StructBlock([('test_name', wagtail.core.blocks.TextBlock(blank=True)), ('test_quote', wagtail.core.blocks.TextBlock(blank=True)), ('test_reversed', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('test_pic', wagtail.images.blocks.ImageChooserBlock(blank=True))])), ('carousel', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock('Title ...', blank=True, max_length=250)), ('caption', wagtail.core.blocks.TextBlock(blank=True, required=False)), ('button', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]), blank=True, icon='image', null=True))], blank=True, null=True)),
                ('seo_image', models.ForeignKey(blank=True, help_text='Optional social media image 300x300px image < 300kb.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=250)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_items', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
