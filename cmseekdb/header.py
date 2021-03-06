#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 Tuhinshubhra
# This file contains all the methods of detecting cms via http Headers
# Version: 1.0.0
# Return a list with ['1'/'0','ID of CMS'/'na'] 1 = detected 0 = not detected
def check(h):
    if h == "":
        r = ['0', 'na']
        return r
    else:
        hstring = h
        harray = h.split("\n")

        #### START DETECTION FROM HERE

        if '/wp-json/' in hstring:
            ## WordPress
            r = ['1','wp']

        elif 'X-Drupal-' in hstring or '19 Nov 1978 05' in hstring:
            ## Drupal [the date is interesting isn't it? just google for it ;) ]
            r = ['1', 'dru']

        elif 'Expires: Wed, 17 Aug 2005 00:00:00 GMT' in hstring:
            ## This is the only weird but common header i noticed in joomla Sites
            r = ['1', 'joom']

        elif 'X-Wix-' in hstring:
            r = ['1', 'wix']

        elif 'Set-Cookie: ushahidi' in hstring:
            r = ['1', 'ushahidi']

        elif 'X-Generated-By: UMI.CMS' in hstring:
            r = ['1', 'umi']

        elif 'x-generator: Sulu' in hstring:
            r = ['1', 'sulu']

        elif 'X-Powered-CMS: Subrion CMS' in hstring:
            r = ['1', 'subcms']

        elif 'Set-Cookie: SQ_SYSTEM_SESSION' in hstring or 'squizedge.net' in hstring:
            r = ['1', 'sqm']

        elif 'spincms' in hstring:
            r = ['1', 'spin']

        elif 'solodev_session' in hstring:
            r = ['1', 'sdev']

        elif 'SC_ANALYTICS_GLOBAL_COOKIE' in hstring:
            r = ['1', 'score']

        elif 'X-ServedBy: simplebo' in hstring or '_simplebo_tool_session' in hstring:
            r = ['1', 'spb']

        elif 'X-Blog: Serendipity' in hstring or 'Set-Cookie: serendipity[' in hstring or 'Set-Cookie: s9y_' in hstring:
            r = ['1', 'spity']

        elif 'Set-Cookie: SEAMLESS_IDENTIFIER' in hstring:
            r = ['1', 'slcms']

        elif 'X-Powered-By: Roadiz CMS' in hstring:
            r = ['1', 'roadz']

        elif 'X-Powered-By: pimcore' in hstring:
            r = ['1', 'pcore']

        elif 'x-powered-by: PencilBlue' in hstring:
            r = ['1', 'pblue']

        elif 'x-powered-by: Ophal' in hstring:
            r = ['1', 'ophal']

        elif 'Server: OpenCms' in hstring:
            r = ['1', 'ocms']

        elif 'X-Odoo-' in hstring:
            r = ['1', 'odoo']

        elif 'X-SharePointHealthScore' in hstring or 'SPIisLatency' in hstring or 'SPRequestGuid' in hstring or 'MicrosoftSharePointTeamServices' in hstring or 'SPRequestDuration' in hstring:
            r = ['1', 'share']

        elif 'october_session' in hstring:
            r = ['1', 'octcms']

        elif 'Generator: Mura CMS' in hstring:
            r = ['1', 'mura']
            
        else:
            r = ['0', 'na']
        return r
