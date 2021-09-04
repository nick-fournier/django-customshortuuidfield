django-shortuuidfield
----------------
Modifies ShortUUIDField to pass a prefix or suffix which will be appended to the string. For Django models which uses the base-57 "Short UUID" package at https://github.com/stochastic-technologies/shortuuid/ .

A form from  benrobster/django-shortuuidfield which was a fork from David Cramer's excellent django-uuidfield.

Installation
============

Install it with pip (or easy_install)::

	pip install django-customshortuuidfield

Usage
=====

First you'll need to attach a ShortUUIDField to your class. This acts as a char(22) to maintain compatibility with SQL versions::

	from shortuuidfield import ShortUUIDField
	
	class MyModel(models.Model):
	    uuid = CustomShortUUIDField(prefix="cust_", suffix="_sys")

Enjoy!

Notes
=====

* ShortUUIDField is a subclass of django.db.models.CharField

* You can pass usual Django CharField parameters on init, although some of them are added/overwritten: 
    + max_length=22 (since we are using base-57 format which is fixed at 22 characters)
    + blank=True, editable=False (set auto=False to remove these fields enforcement)

* Uses shortuuid.uuid() that generates uuid4 random values
