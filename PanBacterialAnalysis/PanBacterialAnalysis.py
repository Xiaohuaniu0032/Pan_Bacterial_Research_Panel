#!/usr/bin/python
# Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved
import sys
import os
import subprocess
import json
import time
import traceback
from glob import glob
from optparse import OptionParser
from subprocess import *
import simplejson
import re
from ion.utils import compress
from ion.plugin import *

class PanBacterialAnalysis(IonPlugin):
  '''Run the Pan Bacterial Analysis pipeline.'''
  version = "1.0.0.0"
  major_block = True
  runtypes = [ RunType.FULLCHIP, RunType.THUMB, RunType.COMPOSITE ]
  runlevels = [ RunLevel.DEFAULT ]
  
  def launch(self,data=None):
    plugin = Popen([
        '%s/PanBacterialAnalysis_plugin.py' % os.environ['DIRNAME'], '-V', self.version, '-d',
        '-B', os.environ['TSP_FILEPATH_BAM'], '-P', os.environ['TSP_FILEPATH_OUTPUT_STEM'],
        '-R', os.environ['TSP_FILEPATH_GENOME_FASTA'],
        '-U', os.environ['TSP_URLPATH_PLUGIN_DIR'], '%s/startplugin.json' % os.environ['TSP_FILEPATH_PLUGIN_DIR']
      ], stdout=PIPE, shell=False )
    plugin.communicate()
    sys.stderr.write("here")
    sys.stderr.write('\n')
    sys.stderr.flush()
    sys.exit(plugin.poll())


if __name__ == "__main__":
  PluginCLI()

