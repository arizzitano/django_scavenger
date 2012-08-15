# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Clue'
        db.create_table('main_app_clue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('code_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hint', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('url_slug', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True, null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=32, null=True, blank=True)),
            ('next_clue', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='prev_clue', unique=True, null=True, to=orm['main_app.Clue'])),
        ))
        db.send_create_signal('main_app', ['Clue'])


    def backwards(self, orm):
        # Deleting model 'Clue'
        db.delete_table('main_app_clue')


    models = {
        'main_app.clue': {
            'Meta': {'object_name': 'Clue'},
            'code_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hint': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'next_clue': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'prev_clue'", 'unique': 'True', 'null': 'True', 'to': "orm['main_app.Clue']"}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'url_slug': ('django.db.models.fields.CharField', [], {'max_length': '32', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_app']