========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.com/ionelmc/pytest-benchmark-elasticsearch.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/ionelmc/pytest-benchmark-elasticsearch

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/pytest-benchmark-elasticsearch?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/pytest-benchmark-elasticsearch

.. |requires| image:: https://requires.io/github/ionelmc/pytest-benchmark-elasticsearch/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/pytest-benchmark-elasticsearch/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/pytest-benchmark-elasticsearch/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/pytest-benchmark-elasticsearch

.. |codecov| image:: https://codecov.io/gh/ionelmc/pytest-benchmark-elasticsearch/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/pytest-benchmark-elasticsearch

.. |version| image:: https://img.shields.io/pypi/v/pytest-benchmark-elasticsearch.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pytest-benchmark-elasticsearch

.. |wheel| image:: https://img.shields.io/pypi/wheel/pytest-benchmark-elasticsearch.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pytest-benchmark-elasticsearch

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pytest-benchmark-elasticsearch.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pytest-benchmark-elasticsearch

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pytest-benchmark-elasticsearch.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pytest-benchmark-elasticsearch

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/pytest-benchmark-elasticsearch/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/pytest-benchmark-elasticsearch/compare/v0.0.0...master



.. end-badges

Elasticseach storage backend for pytest-benchmark.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pytest-benchmark-elasticsearch

You can also install the in-development version with::

    pip install https://github.com/ionelmc/pytest-benchmark-elasticsearch/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import pytest_benchmark_elasticsearch
    pytest_benchmark_elasticsearch.longest()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
