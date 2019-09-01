# Generated by Django 2.2.4 on 2019-09-01 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webcasename', models.CharField(max_length=200, verbose_name='用例名称')),
                ('webtestresult', models.BooleanField(verbose_name='测试结果')),
                ('webtester', models.CharField(max_length=16, verbose_name='测试负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'web 测试用例',
                'verbose_name_plural': 'web 测试用例',
            },
        ),
        migrations.CreateModel(
            name='WebCaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webcasename', models.CharField(max_length=200, verbose_name='测试用例标题')),
                ('webteststep', models.CharField(max_length=200, verbose_name='测试步骤')),
                ('webtestobjname', models.CharField(max_length=200, verbose_name='测试对象名称描述')),
                ('webfindmethod', models.CharField(max_length=200, verbose_name='定位方式')),
                ('webevelement', models.CharField(max_length=800, verbose_name='控件元素')),
                ('weboptmethod', models.CharField(max_length=200, verbose_name='操作方法')),
                ('webtestdata', models.CharField(max_length=200, null=True, verbose_name='测试数据')),
                ('webassertdata', models.CharField(max_length=200, verbose_name='验证数据')),
                ('webtestresult', models.BooleanField(verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('WebCase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webtest.WebCase')),
            ],
        ),
    ]
