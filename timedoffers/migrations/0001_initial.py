# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimedOffer'
        db.create_table(u'timedoffers_timedoffer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(default='Offer of the week', max_length=50)),
            ('offer_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 3, 22, 0, 0))),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 3, 29, 0, 0))),
        ))
        db.send_create_signal(u'timedoffers', ['TimedOffer'])


    def backwards(self, orm):
        # Deleting model 'TimedOffer'
        db.delete_table(u'timedoffers_timedoffer')


    models = {
        u'timedoffers.timedoffer': {
            'Meta': {'object_name': 'TimedOffer'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 3, 29, 0, 0)'}),
            'heading': ('django.db.models.fields.CharField', [], {'default': "'Offer of the week'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 3, 22, 0, 0)'})
        }
    }

    complete_apps = ['timedoffers']