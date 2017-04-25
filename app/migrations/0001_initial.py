# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('a_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('a_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Activity_participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('award_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('award_name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('comp_id', models.CharField(default='00000000000000000000', max_length=20, primary_key=True, serialize=False)),
                ('comp_name', models.CharField(max_length=60)),
                ('comp_tel_no', models.CharField(max_length=10)),
                ('comp_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.CharField(default='0000000', max_length=7, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=1)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Exchange_program',
            fields=[
                ('ex_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('university_name', models.CharField(max_length=45)),
                ('country_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('f_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Get_award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Award')),
            ],
        ),
        migrations.CreateModel(
            name='Get_scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Graduated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Interns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_advisor', models.CharField(max_length=80)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Manage_dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Manage_faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('o_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('o_name', models.CharField(max_length=30)),
                ('o_surname', models.CharField(max_length=50)),
                ('o_password', models.CharField(max_length=16)),
                ('o_picture', models.FileField(upload_to='')),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('p_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=30)),
                ('p_surname', models.CharField(max_length=50)),
                ('p_tel_no', models.CharField(max_length=10)),
                ('p_email', models.CharField(max_length=30)),
                ('p_address', models.CharField(max_length=100)),
                ('p_password', models.CharField(max_length=16)),
                ('p_picture', models.FileField(upload_to='')),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('research_id', models.CharField(default='00000000000000000000', max_length=20, primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('related_field', models.CharField(max_length=100)),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Research_owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Research')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('sch_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('sch_name', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_no', models.CharField(default='0', max_length=2, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=10)),
                ('classroom', models.CharField(max_length=4)),
                ('building', models.CharField(max_length=10)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_year', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_status', models.CharField(max_length=10)),
                ('drop_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=30)),
                ('s_surname', models.CharField(max_length=50)),
                ('s_tel_no', models.CharField(max_length=10)),
                ('s_email', models.CharField(max_length=30)),
                ('s_address', models.CharField(max_length=100)),
                ('s_password', models.CharField(max_length=16)),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Supervise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor')),
                ('s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
                ('s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
                ('section_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Section')),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Take_exchange_program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Exchange_program')),
                ('s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor')),
                ('section_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Section')),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Tuition_fee',
            fields=[
                ('fee', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Undergraduated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='status',
            name='term_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester'),
        ),
        migrations.AddField(
            model_name='research_owner',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='payment',
            name='fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tuition_fee'),
        ),
        migrations.AddField(
            model_name='payment',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='payment',
            name='term_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester'),
        ),
        migrations.AddField(
            model_name='manage_faculty',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor'),
        ),
        migrations.AddField(
            model_name='manage_dept',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor'),
        ),
        migrations.AddField(
            model_name='interns',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='graduated',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='get_scholarship',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='get_scholarship',
            name='sch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Scholarship'),
        ),
        migrations.AddField(
            model_name='get_scholarship',
            name='term_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester'),
        ),
        migrations.AddField(
            model_name='get_award',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='get_award',
            name='term_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='section_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Section'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='term_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Semester'),
        ),
        migrations.AddField(
            model_name='department',
            name='f',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Faculty'),
        ),
        migrations.AddField(
            model_name='activity_participation',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='tuition_fee',
            unique_together=set([('fee', 'd')]),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('c', 'section_no')]),
        ),
    ]