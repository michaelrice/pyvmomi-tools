# Copyright (c) 2014 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module implements simple extensions for vim.VirtualMachine

methods
=======

power_on
--------

code::
    vm.power_on()

A blocking power on method. Relies on the task extensions.

power_off
---------

code::
    vm.power_off()

A blocking power off method. Relies on the task extensions.

soft_reboot
-----------

code::
    vm.soft_reboot()

A non-blocking call to guest reboot API. Causes the guest OS to reboot.

hard_reboot
-----------

A blocking call to the ResetVM_Task method. Relies on the task extensions.

clone
-----

code::
    vm.clone(xxx, yyy)

A CloneVM_Task is created. Depending on options it may or may not wait for
that task to complete, and will return either a VirtualMachine or a Task.

"""
__author__ = ["VMware, Inc.", "Michael Rice"]

from pyVmomi import vim


def clone(name, *args, **kwargs):
    """
    This method needs to support the pysphere clone options so it can be used
    in projects like SaltCloud where they originally used pysphere.

    name, sync_run=True, folder=None, resourcepool=None, datastore=None,
    host=None, power_on=True, template=False, snapshot=None, linked=False

    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    sync_run = True
    if "sync_run" in kwargs:
        sync_run = kwargs.get("sync_run")
    pass

vim.VirtualMachine.power_on = lambda self: self.PowerOn().wait()
vim.VirtualMachine.power_off = lambda self: self.PowerOff().wait()
vim.VirtualMachine.soft_reboot = lambda self: self.RebootGuest()
vim.VirtualMachine.hard_reboot = lambda self: self.ResetVM().wait()
vim.VirtualMachine.clone = clone