===================
django-cas-provider
===================

Updates by AJ:
==============

- Added optional setting to use a field on User instances other than username, like:
   CAS_USER_UNIQUE_FIELD = 'email'
   If a setting is provided, that will be used, otherwise username will be used (so it is compatible with previous code).
   This is the field that is passed to the consumer to identify the logged in user.


Original Readme:
================

---------------------------------
Chris Williams <chris@nitron.org>
---------------------------------

OVERVIEW
=========

django-cas-provider is a provider for the `Central Authentication 
Service <http://jasig.org/cas>`_. It supports CAS version 1.0. It allows 
remote services to authenticate users for the purposes of 
Single Sign-On (SSO). For example, a user logs into a CAS server 
(provided by django-cas-provider) and can then access other services 
(such as email, calendar, etc) without re-entering her password for
each service. For more details, see the `CAS wiki <http://www.ja-sig.org/wiki/display/CAS/Home>`_
and `Single Sign-On on Wikipedia <http://en.wikipedia.org/wiki/Single_Sign_On>`_.

INSTALLATION
=============

To install, run the following command from this directory:

    	``python setup.py install``

Or, put cas_provider somewhere on your Python path.
	
USAGE
======

#. Add ``'cas_provider'`` to your ``INSTALLED_APPS`` tuple in *settings.py*.
#. In *settings.py*, set ``LOGIN_URL`` to ``'/cas/login/'`` and ``LOGOUT_URL`` to ``'/cas/logout/'``
#. In *urls.py*, put the following line: ``(r'^cas/', include('cas_provider.urls')),``
#. Create login/logout templates (or modify the samples)
