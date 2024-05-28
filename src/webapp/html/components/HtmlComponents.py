#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponents.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# Copyright (C) 2024 Bruno Contreras Moreira and Najla Ksouri
# (terms of use can be found within the distributed LICENSE file).

from HtmlComponentsHelp import HtmlComponentsHelp
from HtmlComponentsAlign import HtmlComponentsAlign
from HtmlComponentsProt import HtmlComponentsProt
from HtmlComponentsFind import HtmlComponentsFind
from HtmlComponentsLocate import HtmlComponentsLocate

class HtmlComponents(object):
    
    @staticmethod
    def help(base_url):
        return HtmlComponentsHelp.help(base_url)
    
    @staticmethod
    def align(base_url, align_form, PREFIX_UI_CTRLS_ALIGN, maps_config):
        return HtmlComponentsAlign.align(base_url, align_form, PREFIX_UI_CTRLS_ALIGN, maps_config)

    @staticmethod
    def prot(base_url, align_form, PREFIX_UI_CTRLS_PROT, maps_config):
        return HtmlComponentsProt.prot(base_url, align_form, PREFIX_UI_CTRLS_PROT, maps_config)
    
    @staticmethod
    def find(base_url, find_form, PREFIX_UI_CTRLS_FIND, maps_config):
        return HtmlComponentsFind.find(base_url, find_form, PREFIX_UI_CTRLS_FIND, maps_config)
    
    @staticmethod
    def locate(base_url, form, PREFIX_UI_CTRLS_LOCATE, maps_config):
        return HtmlComponentsLocate.locate(base_url, form, PREFIX_UI_CTRLS_LOCATE, maps_config)

## END
