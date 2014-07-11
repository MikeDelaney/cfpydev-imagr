# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'imagr_images_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo_owner', to=orm['imagr_user.ImagrUser'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('date_uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('privacy_option', self.gf('django.db.models.fields.IntegerField')()),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('size_range', self.gf('django.db.models.fields.CharField')(max_length=27)),
        ))
        db.send_create_signal(u'imagr_images', ['Photo'])

        # Adding model 'Album'
        db.create_table(u'imagr_images_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Album_owner', to=orm['imagr_user.ImagrUser'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('date_uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('privacy_option', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'imagr_images', ['Album'])

        # Adding M2M table for field photos on 'Album'
        m2m_table_name = db.shorten_name(u'imagr_images_album_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'imagr_images.album'], null=False)),
            ('photo', models.ForeignKey(orm[u'imagr_images.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'photo_id'])

        # Adding M2M table for field cover_photo on 'Album'
        m2m_table_name = db.shorten_name(u'imagr_images_album_cover_photo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'imagr_images.album'], null=False)),
            ('photo', models.ForeignKey(orm[u'imagr_images.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'photo_id'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'imagr_images_photo')

        # Deleting model 'Album'
        db.delete_table(u'imagr_images_album')

        # Removing M2M table for field photos on 'Album'
        db.delete_table(db.shorten_name(u'imagr_images_album_photos'))

        # Removing M2M table for field cover_photo on 'Album'
        db.delete_table(db.shorten_name(u'imagr_images_album_cover_photo'))


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
        u'imagr_images.album': {
            'Meta': {'ordering': "['title', 'description']", 'object_name': 'Album'},
            'cover_photo': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cover_photo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['imagr_images.Photo']"}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Album_owner'", 'to': u"orm['imagr_user.ImagrUser']"}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'album_photo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['imagr_images.Photo']"}),
            'privacy_option': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'imagr_images.photo': {
            'Meta': {'ordering': "['title', 'description']", 'object_name': 'Photo'},
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo_owner'", 'to': u"orm['imagr_user.ImagrUser']"}),
            'privacy_option': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'size_range': ('django.db.models.fields.CharField', [], {'max_length': '27'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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

    complete_apps = ['imagr_images']