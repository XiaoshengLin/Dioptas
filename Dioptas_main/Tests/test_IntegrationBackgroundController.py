# -*- coding: utf8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray data
# Copyright (C) 2014  Clemens Prescher (clemens.prescher@gmail.com)
# GSECARS, University of Chicago
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Clemens Prescher'

import unittest
import os
import sys

import numpy as np
from PyQt4 import QtGui, QtCore
from PyQt4.QtTest import QTest

from Views.IntegrationView import IntegrationView
from Data.SpectrumData import SpectrumData
from Data.ImgData import ImgData
from Controller.IntegrationBackgroundController import IntegrationBackgroundController

class IntegrationBackgroundControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        self.view = IntegrationView()
        self.spectrum_data = SpectrumData()
        self.img_data = ImgData()
        self.controller = IntegrationBackgroundController({}, self.view, self.img_data, self.spectrum_data)
        self.overlay_tw = self.view.overlay_tw

    def tearDown(self):
        del self.app

    def test_spectrum_bkg_toggle_inspect_button(self):
        self.spectrum_data.load_spectrum(os.path.join('Data', 'FoG_D3_001.xy'))
        self.view.bkg_spectrum_gb.setChecked(True)

        self.view.bkg_spectrum_inspect_btn.toggle()

        x_bkg, y_bkg = self.view.spectrum_view.bkg_item.getData()
        self.assertGreater(len(x_bkg), 0)
