# Copyright (c) 2013 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This is a common boiler-plate module that is used to set up autotest_lib into
# the PYTHONPATH. It should be copied into every deps directory.

import os, sys
dirname = os.path.dirname(sys.modules[__name__].__file__)
client_dir = os.path.abspath(os.path.join(dirname, "..", ".."))
sys.path.insert(0, client_dir)
import setup_modules
sys.path.pop(0)
setup_modules.setup(base_path=client_dir,
                    root_module_name="autotest_lib.client")