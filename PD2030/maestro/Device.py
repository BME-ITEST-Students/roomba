#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:42:38 2017

@author: dieter
"""
from . import Util
from . import Maestro
import gc

from ..roomba import Ports


class BoardDevice:
    def __init__(self, ser_port=False, verbose=False):
        self.id = id(self)
        self.verbose = verbose
        self.device = None
        self.connect(ser_port=ser_port)

    def __del__(self):
        self.verbose = False
        self.disconnect()

    def test_connection(self):
        # This is a minimal test that should be overwritten by the inheriting classes
        return self.device.isInitialized

    def connect(self, ser_port=False, disconnect_all=True):
        if self.verbose: print('\n+ Start Connecting instance', self.id)
        if disconnect_all: self.disconnect_others()
        if not ser_port:
            self.auto_connect()
        else:
            self.manual_connect(ser_port=ser_port)
        success = self.test_connection()
        if success and self.verbose: print('+ Connecting succeeded')
        if not success and self.verbose: print('+ Connecting failed')
        return success

    def manual_connect(self, ser_port):
        self.device = Maestro.Device(con_port=False, ser_port=ser_port)

    def auto_connect(self):
        p = Ports.Ports()
        ser_port = p.get_port('Maestro')
        if ser_port is not None:
            print('+ Port found:', ser_port)
            self.device = Maestro.Device(con_port=False, ser_port=ser_port)
            self.test_connection()
            return
        if ser_port is None:
            print('+ No port found -- is the device connected?')
            return

    def disconnect_others(self):
        signature = str(type(self))
        for other in gc.get_objects():
            signature_other = str(type(other))
            if signature in signature_other:
                if other.id != self.id: other.disconnect()

    def disconnect(self):
        if self.verbose: print('+ Disconnecting Board instance ', self.id)
        try:
            self.device.__del__()
        except Exception as error:
            if self.verbose: print('+ ERROR:', error)