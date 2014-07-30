# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImagrUser'
        db.create_table(u'imagr_user_imagruser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'imagr_user', ['ImagrUser'])

        # Adding M2M table for field groups on 'ImagrUser'
        m2m_table_name = db.shorten_name(u'imagr_user_imagruser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagruser', models.ForeignKey(orm[u'imagr_user.imagruser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagruser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'ImagrUser'
        m2m_table_name = db.shorten_name(u'imagr_user_imagruser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagruser', models.ForeignKey(orm[u'imagr_user.imagruser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagruser_id', 'permission_id'])

        # Adding model 'Relationships'
        db.create_table(u'imagr_user_relationships', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_one', self.gf('django.db.models.fields.related.ForeignKey')(related_name='relationship_from', to=orm['imagr_user.ImagrUser'])),
            ('user_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='relationship_to', to=orm['imagr_user.ImagrUser'])),
            ('follower_status', self.gf('django.db.models.fields.IntegerField')()),
            ('friendship', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'imagr_user', ['Relationships'])


    def backwards(self, orm):
        # Deleting model 'ImagrUser'
        db.delete_table(u'imagr_user_imagruser')

        # Removing M2M table for field groups on 'ImagrUser'
        db.delete_table(db.shorten_name(u'imagr_user_imagruser_groups'))

        # Removing M2M table for field user_permissions on 'ImagrUser'
        db.delete_table(db.shorten_name(u'imagr_user_imagruser_user_permissions'))

        # Deleting model 'Relationships'
        db.delete_table(u'imagr_user_relationships')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imagr_user.imagruser': {
            'Meta': {'object_name': 'ImagrUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagr_user.ImagrUser']", 'symmetrical': 'False', 'through': u"orm['imagr_user.Relationships']", 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'imagr_user.relationships': {
            'Meta': {'object_name': 'Relationships'},
            'follower_status': ('django.db.models.fields.IntegerField', [], {}),
            'friendship': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_one': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relationship_from'", 'to': u"orm['imagr_user.ImagrUser']"}),
            'user_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relationship_to'", 'to': u"orm['imagr_user.ImagrUser']"})
        }
    }

    complete_apps = ['imagr_user']