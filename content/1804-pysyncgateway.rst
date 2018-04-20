The benefits of extracting Python packages from projects
========================================================

:date: 2018-04-20 22:00
:tags: language:python
:category: Code
:summary: Thoughts on extracting service code into libraries and the benefits
          that it can bring.
:scm_path: content/1804-pysyncgateway.rst


Last week we released version 1 of `pysyncgateway
<https://pypi.org/project/pysyncgateway/>`_ - a Python package for
communicating with `Couchbase's Sync Gateway
<https://github.com/couchbase/sync_gateway>`_ via its REST API.

But this library was not created from scratch - it consists mainly of code
extracted from my employer's Django-DRF-powered server repository. I've thought
that this process has been really helpful and so I thought I'd put together
this list of some of the benefits that I've found so far.


Better separation of concerns
-----------------------------

The boundary between the new library and the server code makes it much easier
to reason about where responsibilities start and end.

Originally the Sync Gateway code was tightly knitted with our Django API
server:

* It used Django settings for establishing URLs of the Sync Gateway instance in
  test and production.

* It provided test cases to our server's old ``Unittest`` test suite, Those
  test cases created test Databases, Users and Documents on the Sync Gateway
  for each test - tearing them down afterwards.

* It manipulated the statistical data retrieved from Sync Gateway and posted it
  to our ``statsd`` instance. Again Django's settings were used for
  configuration.

In extracting the library, these responsibilities have been cleaned out and
clarified:

* Communication with Sync Gateway's API from Python - Responsibility of
  ``pysyncgateway`` library. All calls made to Sync Gateway are the
  responsibility of the library.

* Testing and mitigating any strange behaviours of the Sync Gateway API -
  Responsibility of ``pysyncgateway``. The library's code is the place to pin
  and mitigate any strange behaviours that are found.

* Integration of Sync Gateway's objects (User, Document, Database) into
  the API server and Django - Responsibility of API server code. The server
  code remains responsible for managing its own tests conditions.

* Synchronisation of Django's User object with Sync Gateway's User objects -
  Responsibility of API server. The library is naive to the application that is
  using it - in the same way that the `requests libary
  <http://docs.python-requests.org/en/master/>`_ is naive to the fact that is
  it being used by ``pysyncgateway`` to communicate with Sync Gateway.


Improved efficiency of development and test
-------------------------------------------

While working on the library code, I've found that testing has been much more
efficient.

In terms of time, a build on `Circle CI
<https://circleci.com/gh/constructpm/pysyncgateway/tree/master>`_ takes around
10s whereas in our API server test suite it was taking 40s and was mixed in
with a much longer (~20 minute) long test suite.

The dedicated library code repository now means that when I've had questions
about how Sync Gateway behaves in certain situations, then the library code is
the place to explore that behaviour and ensure that the library code is
fulfilling its main responsibility - communicating as best it can with any Sync
Gateway instance.


Document all the things
-----------------------

In general, the built documentation is great. Many of the docstrings were in
place in much of the code, but reading them on the `Read The Docs site
<https://pysyncgateway.readthedocs.io/>`_ or from a local HTML render is really
helpful - I've found it much better than reading docs via a code editor or
``ipython``.


Still a monolith, but with packaging benefits
---------------------------------------------

Our server code remains a single monolith - it's one installed blob of code on
one server. The Sync Gateway code was extracted into a library, not a service.

However, now that the Sync Gateway code is installed from PyPi via
``pip-sync``, there is an additional abstraction that we can select the version
of the library that will be installed.

This means that we have more flexibility to move the library forward to work
with the latest version of Sync Gateway 2 (it's currently only tested with 1.5)
and also Python 3. We can upgrade the library and bump versions without
touching the server monolith at all.

Finally
-------

The extraction of ``pysyncgateway`` has worked out well for us and so I'm
preparing to extract our next library - a simple object orientated layer that
we use to communicate with Nextcloud.

There will be quite a bit of time invested to extract the code, but my
expectation is that the test benefits will be great. Not only we will get to
remove library code from our API repository that takes around 6 minutes to
test, but also we will gain the library's tests suite as a dedicated area to
test nuanced edges of Nextcloud's API.

Happy code extraction!
