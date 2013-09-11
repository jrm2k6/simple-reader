# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'simplereader_client_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'simplereader_client', ['Feed'])

        # Adding model 'ReaderUser'
        db.create_table(u'simplereader_client_readeruser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=300)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=300)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'simplereader_client', ['ReaderUser'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table(u'simplereader_client_feed')

        # Deleting model 'ReaderUser'
        db.delete_table(u'simplereader_client_readeruser')


    models = {
        u'simplereader_client.feed': {
            'Meta': {'object_name': 'Feed'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'simplereader_client.readeruser': {
            'Meta': {'object_name': 'ReaderUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '300'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['simplereader_client']