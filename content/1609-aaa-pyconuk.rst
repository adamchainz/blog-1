Cleaner unit testing with the Arrange Act Assert pattern
========================================================

:date: 2016-09-18 20:00
:tags: language:python, topic:testing
:category: Talk
:summary: My PyConUK 2016 talk about the AAA pattern for unit tests and how
          using it can help us all make our tests cleaner, easier to read
          and as Pythonic as possible.
:scm_path: content/1609-aaa-pyconuk.rst

At `PyConUK 2016
<http://2016.pyconuk.org/talks/cleaner-unit-testing-with-the-arrange-act-assert-pattern/>`_
I spoke about the Arrange Act Assert pattern and how it can help clean up unit
tests. I plan to write a short guide to AAA for Python developers and will
link to that from here when done - meanwhile, below are my slides and links
to some of the resources that have helped me.

Original proposal
-----------------

PyConUK ask that we provide an explanation of why we think that attendees
will be interested in our talk. This was my original proposal's reasoning.

    This talk focuses on developers that practise TDD, or want to use it
    more in their coding.

    My assumption is that our community feels a lot of pain from testing.
    I've heard fellow developers talk about the difficulty with managing
    complicated test suites; issues with reading and understanding others'
    tests; and struggles when updating others' tests. I hope that the
    PyConUK attendees will have felt some of this pain be interested in a
    talk that demonstrates the use of a pattern that can (hopefully)
    mitigate some of it and help us all to be "cleaner" testers.

    Although I've marked "moderately experienced" I think that my talk
    would have a broad appeal: Those who are new to testing and would like
    a "template" to follow. And those who are expert because of the
    discussion about when to DRY out tests and how to assert that our test
    refactors are safe.

Slides
------

.. raw:: html

    <script async class="speakerdeck-embed" data-id="d25e0e15acef4ccc8fe70abba5adce03" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

Resources
---------

* `PEP08 <https://www.python.org/dev/peps/pep-0008/>`_ and `PEP20
  <https://www.python.org/dev/peps/pep-0020/>`_.

* `Kent Beck: Test Driven Development: By Example
  <http://www.goodreads.com/book/show/387190.Test_Driven_Development>`_ - a
  great book which references the AAA pattern (page 97).

* `Google-style docstrings
  <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_:
  In addition to using this style in my AAA tests, I've started to add a
  ``Trusts`` section to indicate which other tests are trusted by any
  particular test and why.

* `Bill Wake's post about AAA
  <http://xp123.com/articles/3a-arrange-act-assert/>`_: Bill Wake is cited by
  Kent Beck as having coined the term ``3A``.

* `Extract Method <http://refactoring.com/catalog/extractMethod.html>`_: I've
  used extract method as defined by Martin Fowler. See also `Extract Variable
  <http://refactoring.com/catalog/extractVariable.html>`_.

Finally
-------

Thanks again to `Carles <https://github.com/txels>`_ for introducing me to the
AAA pattern. Check out his `data driven tests library
<https://github.com/txels/ddt>`_.