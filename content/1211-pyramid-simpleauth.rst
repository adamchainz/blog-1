Password cases and test fixes on pyramid_simpleauth
###################################################

:date: 2012-11-30 12:00:00
:tags: topic:pyramid
:category: GitHub Contributions
:summary: Updates to pyramid_simpleauth to allow for uppercase passwords and some bug fixes.

At Quibly we're using Pyramid at the centre of a Python framework. Providing user functionality is the `pyramid_simpleauth <https://github.com/thruflo/pyramid_simpleauth>`_ library.

While writing integration tests before we put the site live, I found that my test users we not able to authenticate with their testing passwords (usually just a simple string like 'Password'). Digging inside the simpleauth library, I found some fixes necessary to how cases are handled by the lib - plus also fixed some doctests while I was at it.

These `changes <https://github.com/thruflo/pyramid_simpleauth/pull/7>`_ all
been merged now and the library rolled up a version.
