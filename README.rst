===============================
langevin-dynamics
===============================

.. image:: https://img.shields.io/travis/arosenstein/langevin_dynamics.svg
        :target: https://travis-ci.org/arosenstein/langevin_dynamics

.. image:: https://readthedocs.org/projects/langevin-dynamics/badge/?version=latest
        :target: https://langevin-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/arosenstein/langevin_dynamics/shield.svg
     :target: https://pyup.io/repos/github/arosenstein/langevin_dynamics/
     :alt: Updates

.. image:: https://coveralls.io/repos/github/arosenstein/langevin_dynamics/badge.svg?branch=master
	:target: https://coveralls.io/github/arosenstein/langevin_dynamics?branch=master


Features
--------

This is a 1-Dimensional Langevin Dynamics Simulator implemented in python for CHE 477 at the University of Rochester.
Unit tests, 100% Code Coverage, and continuous integration are all included. Additionally, it uses the Euler integration method.

Running the Simulation
--------

An input file is required for the simulation to be run. It has to be of the form: 

+-------------+------------+------------------+-----------+ 
|    INDEX    |    TIME    | POTENTIAL ENERGY |   FORCE   |
+=============+============+==================+===========+


Running Tests
-------- 

In order to run the complete test, go into the main directory of the repo and run :code:`python setup.py test`


Credits & License
---------

* Free software: MIT license
* Documentation: https://langevin-dynamics.readthedocs.io.
* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

