# coding=utf-8
#-----------------------------------------------------------------------------
# Copyright (c) 2024, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------
from PyInstaller.utils.hooks.qt import exclude_extraneous_qt_bindings

# This module conditionally imports all Qt bindings. Prevent all available bindings from being pulled in by trying to
# select the most applicable one.
#
# The preference order for this module appears to be: PyQt5, PySide2, PyQt6, PySide6. See:
# https://github.com/Usama01TN/ManyQt
#
# We, however, use the default preference order of the helper function, in order to keep it consistent across multiple
# hooks that use the same helper.
excludedimports = exclude_extraneous_qt_bindings(hook_name="hook-ManyQt", qt_bindings_order=None)
