# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IdentityPlugin'
        db.create_table(u'cmsplugin_identityplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'resume', ['IdentityPlugin'])

        # Adding model 'SocialPlugin'
        db.create_table(u'cmsplugin_socialplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('github', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'resume', ['SocialPlugin'])

        # Adding model 'JobPlugin'
        db.create_table(u'cmsplugin_jobplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')(null=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('job_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company_website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'resume', ['JobPlugin'])

        # Adding model 'ProjectPlugin'
        db.create_table(u'cmsplugin_projectplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_plugins', null=True, to=orm['resume.JobPlugin'])),
        ))
        db.send_create_signal(u'resume', ['ProjectPlugin'])

        # Adding model 'EducationPlugin'
        db.create_table(u'cmsplugin_educationplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')(null=True)),
            ('diploma_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('diploma_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'resume', ['EducationPlugin'])

        # Adding model 'TitlePlugin'
        db.create_table(u'cmsplugin_titleplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'resume', ['TitlePlugin'])

        # Adding model 'FreeTextPlugin'
        db.create_table(u'cmsplugin_freetextplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'resume', ['FreeTextPlugin'])


    def backwards(self, orm):
        # Deleting model 'IdentityPlugin'
        db.delete_table(u'cmsplugin_identityplugin')

        # Deleting model 'SocialPlugin'
        db.delete_table(u'cmsplugin_socialplugin')

        # Deleting model 'JobPlugin'
        db.delete_table(u'cmsplugin_jobplugin')

        # Deleting model 'ProjectPlugin'
        db.delete_table(u'cmsplugin_projectplugin')

        # Deleting model 'EducationPlugin'
        db.delete_table(u'cmsplugin_educationplugin')

        # Deleting model 'TitlePlugin'
        db.delete_table(u'cmsplugin_titleplugin')

        # Deleting model 'FreeTextPlugin'
        db.delete_table(u'cmsplugin_freetextplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'resume.educationplugin': {
            'Meta': {'object_name': 'EducationPlugin', 'db_table': "u'cmsplugin_educationplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'diploma_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'diploma_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'resume.freetextplugin': {
            'Meta': {'object_name': 'FreeTextPlugin', 'db_table': "u'cmsplugin_freetextplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'resume.identityplugin': {
            'Meta': {'object_name': 'IdentityPlugin', 'db_table': "u'cmsplugin_identityplugin'", '_ormbases': ['cms.CMSPlugin']},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'resume.jobplugin': {
            'Meta': {'object_name': 'JobPlugin', 'db_table': "u'cmsplugin_jobplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'job_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'resume.projectplugin': {
            'Meta': {'object_name': 'ProjectPlugin', 'db_table': "u'cmsplugin_projectplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_plugins'", 'null': 'True', 'to': u"orm['resume.JobPlugin']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'resume.socialplugin': {
            'Meta': {'object_name': 'SocialPlugin', 'db_table': "u'cmsplugin_socialplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'resume.titleplugin': {
            'Meta': {'object_name': 'TitlePlugin', 'db_table': "u'cmsplugin_titleplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['resume']