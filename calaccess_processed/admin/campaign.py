#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for campaign models.
"""
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_processed import models
from calaccess_raw.admin.base import BaseAdmin

@admin.register(models.Candidate)
class CandidateAdmin(BaseAdmin):
    """
    Custom admin for the Candidate model.
    """
    list_display = (
        "f501_filer_id",
        "last_name",
        "first_name",
        "middle_name",
        "name_suffix",
        "election_year",
        "f501_filing_id",
        "last_f501_amend_id",
        "office",
        "district",
        "agency",
        "party",
    )