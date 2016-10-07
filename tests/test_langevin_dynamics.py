#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_langevin_dynamics
----------------------------------

Tests for `langevin_dynamics` module.
"""

import sys, os
import unittest
from contextlib import contextmanager
from click.testing import CliRunner
from langevin_dynamics.langevin_dynamics import *
from langevin_dynamics import cli
from scipy.stats.mstats import normaltest



class TestLangevin_dynamics(unittest.TestCase):

    def setUp(self):
        pass

    def test_read_file(self):
        print('-' * 100)
        print(os.getcwd())
        file = read_file('./tests/sample_data.txt')
        self.assertEqual(len(file), 200) #test that every line is being read
        for i in file:
            self.assertEqual(len(i), 4) #test that lines are being split properly

    def test_no_simulation(self):
        x, v = langevin_dynamics(2,.01, 300, .5, .01, 0, 2, './tests/sample_data.txt')
        self.assertEqual(x, 2)
        self.assertEqual(v, 0.01)

    def test_output_file_created(self):
        langevin_dynamics(0,0, 300, .5, .01, 1.75, 2, './tests/sample_data.txt')
        self.assertTrue(os.path.exists('output.txt'))

    def tearDown(self):
        if(os.path.exists('./output.txt')):
            os.remove('./output.txt')

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'langevin_dynamics.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
