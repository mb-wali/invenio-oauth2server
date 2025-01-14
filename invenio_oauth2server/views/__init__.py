# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Blueprint instances."""

from __future__ import absolute_import, print_function

from .server import blueprint as server_blueprint
from .settings import blueprint as settings_blueprint

__all__ = (
    "server_blueprint",
    "settings_blueprint",
)
