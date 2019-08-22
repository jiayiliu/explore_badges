Explore of Badges
=================

|Build Status| |codecov|

Python package
--------------

Here is a simple
`tutorial <https://docs.python-guide.org/writing/structure/>`__.

Travis-ci
---------

1. Link to Github and add the repository.
2. Follow the
   `instructions <https://docs.travis-ci.com/user/tutorial/>`__

CodeCov
-------

1. From Github.com install
   `CodeCov <https://github.com/marketplace/codecov>`__. It is free for
   open-source repository.
2. Add the repo in codecov.
3. update ``.travis.yml``

Note: because ``codecov`` is in ``after_success``, it won't give a
failing error if it fails.

Sphinx-doc for gh-pages
-----------------------

1. Make sure sphinx generate doc you want
2. Follow instructions
   `here <https://gist.github.com/brenns10/f48e1021e8befd2221a2>`__

   a. put ORG,REPO,EMAIL var in travis-ci repo setting
   b. add publish.sh

.. |Build Status| image:: https://travis-ci.org/jiayiliu/explore_badges.svg?branch=master
   :target: https://travis-ci.org/jiayiliu/explore_badges
.. |codecov| image:: https://codecov.io/gh/jiayiliu/explore_badges/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jiayiliu/explore_badges
