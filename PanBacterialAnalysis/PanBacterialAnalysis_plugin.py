#!/usr/bin/env python
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

# set up for Django rendering with TSS installed apps
from django.conf import settings
from django.template.loader import render_to_string
from django.conf import global_settings
global_settings.LOGGING_CONFIG=None

#
# ----------- custom tag additions -------------
# Use template.base.add_to_builtins("django_tags") to add from django_tags.py (in cwd)
#
from django import template
register = template.Library()

@register.filter 
def toMega(value):
  return float(value) / 1000000

template.builtins.append(register) 

# global data collecters common to functions
pluginParams = {}
pluginResult = {}
pluginReport = {}
barcodeData = []
countsData = {}
offTargetData = {}
idData = {}
genesData = {}
output16sData = {}
outputERCCData = {}
barcodeReport = {}
numPass =""
totalSamples=""
numAvgCov=""
numUniformity=""
variantCallerName=""
coverageAnalysisName=""
hotspotsFile=""
#
# -------------------- customize code for this plugin here ----------------
#

def parseCmdArgs():
  '''Process standard command arguments. Customized for additional debug and other run options.'''
  # standard run options here - do not remove
  parser = OptionParser()
  parser.add_option('-B', '--bam', help='Filepath to root alignment BAM file. Default: rawlib.bam', dest='bamfile', default='')
  parser.add_option('-P', '--prefix', help='Output file name prefix for output files. Default: '' => Use analysis folder name or "output".', dest='prefix', default='')
  parser.add_option('-R', '--reference_fasta', help='Path to fasta file for the whole reference', dest='reference', default='')
  parser.add_option('-U', '--results_url', help='URL for access to files in the output directory', dest='results_url', default='')
  parser.add_option('-V', '--version', help='Version string for tracking in output', dest='version', default='')
  parser.add_option('-X', '--min_bc_bam_size', help='Minimum file size required for barcode BAM processing', type="int", dest='minbamsize', default=0)
  parser.add_option('-d', '--scraper', help='Create a scraper folder of links to output files using name prefix (-P).', action="store_true", dest='scraper')
  parser.add_option('-k', '--keep_temp', help='Keep intermediate files. By default these are deleted after a successful run.', action="store_true", dest='keep_temp')
  parser.add_option('-l', '--log', help='Output extra progress Log information to STDERR during a run.', action="store_true", dest='logopt')
  parser.add_option('-s', '--skip_analysis', help='Skip re-generation of existing files but make new report.', action="store_true", dest='skip_analysis')
  parser.add_option('-x', '--stop_on_error', help='Stop processing barcodes after one fails. Otherwise continue to the next.', action="store_true", dest='stop_on_error')

  # add other run options here (these should override or account for things not in the json parameters file)

  (cmdOptions, args) = parser.parse_args()
  if( len(args) != 1 ):
    printerr('Takes only one argument (parameters.json file)')
    raise TypeError(os.path.basename(__file__)+" takes exactly one argument (%d given)."%len(args))
  with open(args[0]) as jsonFile:
    jsonParams = json.load(jsonFile)
  global pluginParams
  pluginParams['cmdOptions'] = cmdOptions
  pluginParams['jsonInput'] = args[0]
  pluginParams['jsonParams'] = jsonParams
  pluginParams['config'] = jsonParams['pluginconfig'].copy() if 'pluginconfig' in jsonParams else {}
  if not 'runWholeGenomeMapping' in pluginParams['config']: pluginParams['config']['runWholeGenomeMapping'] = 'No'
  if not 'lowStringency16s' in pluginParams['config']: pluginParams['config']['lowStringency16s'] = 'No'

def addAutorunParams(plan=None):
  '''Additional parameter set up for automated runs, e.g. to add defaults for option only in the GUI.'''
  pass

def RunCommand( command , errorExit=1):
        global progName, haveBed, noerrWarn, noerrWarnFile
        command = command.strip()
        #WriteLog( " $ %s\n" % command )
        stat = os.system( command )
        printlog("stat is %d" %stat)
        if( stat ) != 0:
                if errorExit != 0:
                        sys.stderr.write( "ERROR: resource failed with status %d:\n" % stat )
                else:
                        sys.stderr.write( "INFO: return status %d:\n" % stat)
                        errorExit = 1
                sys.stderr.write( "$ %s\n" % command )
                sys.exit(errorExit)


def furbishPluginParams():
  '''Complete/rename/validate user parameters.'''
  # For example, HTML form posts do not add unchecked option values
  pass


def printStartupMessage():
  '''Output the standard start-up message. Customized for additional plugin input and options.'''
  printlog('')
  printtime('%s plugin running...' % pluginParams['plugin_name'])

  printlog('Alignment plugin run options:')
  if pluginParams['cmdOptions'].version != "":
    printlog('  Plugin version    : %s' % pluginParams['cmdOptions'].version)
  printlog('  Plugin start mode : %s' % pluginParams['start_mode'])
  printlog('  Run is barcoded   : %s' % ('Yes' if pluginParams['barcoded'] else 'No'))

  printlog('Data files used:')
  if pluginParams['cmdOptions'].logopt:
    printlog('  Parameters file   : %s' % pluginParams['jsonInput'])
  printlog('  Alignment file    : %s' % pluginParams['bamroot'])
  if 'runWholeGenomeMapping' in pluginParams['config']:
  	printlog(' Run whole genome mapping at the end : %s' % pluginParams['config']['runWholeGenomeMapping'])
  if 'lowStringency16s' in pluginParams['config']:
  	printlog(' Low Stringency for 16s : %s' % pluginParams['config']['lowStringency16s'])
  printlog('')


def updateBarcodeSummaryReport(autoRefresh=False):
  '''Create barcode summary (progress) report. Called before, during and after barcodes are being analysed.'''
  global barcodeData, numPass, numAvgCov, numUniformity, totalSamples, variantCallerName,coverageAnalysisName, countsData, offTargetData, idData, genesData, output16sData, outputERCCData
  render_context = {
    "autorefresh" : autoRefresh,
    "run_name" : pluginParams['prefix'],
    "library_type" : "ID Targets + 16s",
    "genome_name" : "gg_13_5_with_taxonomy8fasta_with_truefalsefalse.fasta",
    "targets_name" : "PanBacterial_ID_Genes_Reference.fasta",
    "hotspots_name" : "PanBacterial_ID_Genes_designed.bed",
    "run_name" : pluginParams['prefix'],
    "barcodeData" : barcodeData,
    "countsData" : countsData,
    "offTargetData" : offTargetData,
    "idData" : idData,
    "genesData" : genesData,
    "output16sData" : output16sData,
    "outputERCCData" : outputERCCData,
  }
  # extra report items, e.g. file links from barcodes summary page
  if barcodeReport:
    render_context.update(barcodeReport)
  
  if 'runWholeGenomeMapping' in pluginParams['config']:
  	createReport( os.path.join(pluginParams['results_dir'],pluginParams['report_name']), 'barcode_summary.html', render_context )
  else:
  	createReport( os.path.join(pluginParams['results_dir'],pluginParams['report_name']), 'barcode_summary_all.html', render_context )
  #createReport( os.path.join(pluginParams['results_dir'],pluginParams['block_report']), 'barcode_block.html', render_context)	


def createIncompleteReport(errorMsg=""):
  '''Called to create an incomplete or error report page for non-barcoded runs.'''
  sample = pluginParams['sample_names'] if isinstance(pluginParams['sample_names'],basestring) else ''
  render_context = {
    "autorefresh" : (errorMsg == ""),
    "run_name": pluginParams['prefix'],
    "Sample_Name": sample,
    "Error": errorMsg }
  createReport( os.path.join(pluginParams['results_dir'],pluginParams['report_name']), 'incomplete.html', render_context )


def createDetailReport(resultData,reportData):
  '''Called to create the main report (for un-barcoded run or for each barcode).'''
  render_context = resultData.copy()
  render_context.update(reportData)
  createReport( os.path.join(pluginParams['output_dir'],pluginParams['report_name']), 'report.html', render_context )


def createBlockReport():
  '''Called at the end of run to create a block.html report. Use 'pass' if not wanted.'''
  printtime("Creating block report...")
  if pluginParams['barcoded']:
    render_context = { "barcode_results" : simplejson.dumps(barcodeSummary) }
    tplate = 'barcode_block.html'
  else:
    render_context = pluginResult.copy()
    render_context.update(pluginReport)
    tplate = 'report_block.html'
  createReport( pluginParams['block_report'], tplate, render_context )


#
# --------------- Base code for standard plugin runs -------------
#

def emptyResultsFolder():
  '''Purge everything in output folder except for specifically named files.'''
  # Dangerous - replace with something safer if it becomes obvious (e.g. putting output in subfolder?)
  logopt = pluginParams['cmdOptions'].logopt
  results_dir = pluginParams['results_dir']
  if results_dir == '/': return
  printlog("Purging old results...")
  for root,dirs,files in os.walk(results_dir,topdown=False):
    for name in files:
      # these are the exceptions - partial names and in the to level results
      if root == results_dir:
        start = os.path.basename(name)[:10]
        if start == "drmaa_stdo" or start == "ion_plugin" or start == "startplugi":
          continue
      fname = os.path.join(root,name)
      if logopt and root == results_dir:
        printlog("Removing file %s"%fname)
      os.system('rm -f "%s"'%fname)
    for name in dirs:
      fname = os.path.join(root,name)
      if logopt:
        printlog("Removing directory %s"%fname)
      os.system('rm -rf "%s"'%fname)
  if logopt: printlog("")

def parseForNames(filein, sep=None):
  ret = []
  if os.path.exists(filein):
    with open(filein) as fin:
	printlog(filein)
	for line in fin:
		line = line.strip()
		if not line == "":
			if line.startswith("#ID"):
				kvp = line.split(sep)
				for i in range(1, len(kvp)):
					s = kvp[i].strip()
					if not s == "":
						ret.append(kvp[i]) 
  return ret

def parseForCounts(filein, sep=None):
  ret = []
  if os.path.exists(filein):
    with open(filein) as fin:
   	printlog(filein)
	for line in fin:
		line = line.strip()
		if line == "" or not line[0].isalnum():
			continue
		if "total" in line:
			continue
		if "numInvalid" in line:
			continue
		kvp = line.split(sep)
		ret.append([])
		for i in range(0, len(kvp)):
			ret[-1].append(kvp[i])
  return ret

def parseToDict(filein,sep=None):
  ret = {}
  if os.path.exists(filein):
    with open(filein) as fin:
      printlog(filein)
      for line in fin:
	printlog(line)
        line = line.strip()
        # ignore lines being with non-alphanum (for comments, etc)
        if line == "" or not line[0].isalnum():
          continue
        kvp = line.split(sep,1)
        key = kvp[0].strip().replace(' ','_')
        ret[key] = line
  else:
    printerr("parseToDict() could not open "+filein)
  return ret

def printerr(msg):
  cmd = os.path.basename(__file__)
  sys.stderr.write( '%s: ERROR: %s\n' % (cmd,msg) )
  sys.stderr.flush()

def printlog(msg):
  sys.stderr.write(msg)
  sys.stderr.write('\n')
  sys.stderr.flush()

def printtime(msg):
  printlog( '(%s) %s'%(time.strftime('%X'),msg) )

def createlink(srcPath,destPath,srcFile=None,destFile=None ):
  # os.symlink to be performed using 2, 3 or 4 args (to track and avoid code repetition)
  if srcFile:
    srcPath = os.path.join(srcPath,srcFile)
  if destFile:
    destPath = os.path.join(destPath,destFile)
  elif srcFile:
    destPath = os.path.join(destPath,srcFile)
  if os.path.exists(destPath):
    os.unlink(destPath)
  if os.path.exists(srcPath):
    os.symlink(srcPath,destPath)
    if pluginParams['cmdOptions'].logopt:
      printlog("\nCreated symlink %s -> %s"%(destPath,srcPath))
    return True
  elif pluginParams['cmdOptions'].logopt:
    printlog("\nFailed to create symlink %s -> %s (source file does not exist)"%(destPath,srcPath))
  return False
  
def deleteTempFiles(tmpFiles):
  if tmpFiles == None or pluginParams['cmdOptions'].keep_temp:
    return
  output_dir = pluginParams['output_dir']
  for filename in tmpFiles:
    flist = glob( os.path.join(output_dir,filename) )
    for f in flist:
      if pluginParams['cmdOptions'].logopt:
        printlog("Deleting file %s"%f)
      os.unlink(f)

def createReport(reportName,reportTemplate,reportData):
  with open(reportName,'w') as bcsum:
    bcsum.write( render_to_string(reportTemplate,reportData) )

def sampleNames():
  try:
    if pluginParams['barcoded']:
      samplenames = {}
      bcsamps = pluginParams['jsonParams']['plan']['barcodedSamples']
      if isinstance(bcsamps,basestring):
        bcsamps = json.loads(bcsamps)
      for bcname in bcsamps:
        for bc in bcsamps[bcname]['barcodes']:
          samplenames[bc] = bcname
    else:
      samplenames = jsonParams['expmeta']['sample']
  except:
    return ""
  return samplenames

def loadPluginParams():
  '''Process default command args and json parameters file to extract TSS plugin environment.'''
  global pluginParams
  parseCmdArgs()

  # copy typical environment data needed for analysis
  jsonParams = pluginParams['jsonParams']
  pluginParams['plugin_name'] = jsonParams['runinfo'].get('plugin_name','')
  pluginParams['plugin_dir'] = jsonParams['runinfo'].get('plugin_dir','.')
  pluginParams['genome_id'] = jsonParams['runinfo'].get('library','')
  pluginParams['run_name'] = jsonParams['expmeta'].get('run_name','')
  pluginParams['analysis_name'] = jsonParams['expmeta'].get('results_name',pluginParams['plugin_name'])
  pluginParams['analysis_dir'] = jsonParams['runinfo'].get('analysis_dir','.')
  pluginParams['results_dir'] = jsonParams['runinfo'].get('results_dir','.')
  #pluginParams['hotspots_file'] = jsonParams['plan'].get('regionfile', '.') 
  #pluginParams['regions_file'] = jsonParams['plan'].get('bedfile', '.') 
  
  # some things not yet in startplugin.json are provided or over-writen by cmd args
  copts = pluginParams['cmdOptions']
  pluginParams['reference'] = copts.reference if copts.reference != "" else jsonParams['runinfo'].get('reference','')
  pluginParams['bamroot']   = copts.bamfile   if copts.bamfile != "" else '%s/rawlib.bam' % pluginParams['analysis_dir']
  pluginParams['prefix']    = copts.prefix    if copts.prefix != "" else pluginParams['analysis_name']
  pluginParams['results_url'] = copts.results_url if copts.results_url != "" else os.path.join(
  jsonParams['runinfo'].get('url_root','.'),'plugin_out',pluginParams['plugin_name']+'_out' )

  # set up for barcoded vs. non-barcodedruns
  pluginParams['bamfile'] = pluginParams['bamroot']
  pluginParams['output_dir'] = pluginParams['results_dir']
  pluginParams['output_url'] = pluginParams['results_url']
  pluginParams['output_prefix'] = pluginParams['prefix']
  pluginParams['bamname'] = os.path.basename(pluginParams['bamfile'])
  pluginParams['barcoded'] = os.path.exists(pluginParams['analysis_dir']+'/barcodeList.txt')
  pluginParams['sample_names'] = sampleNames()

  # disable run skip if no report exists => plugin has not been run before
  pluginParams['report_name'] = pluginParams['plugin_name']+'.html'
  pluginParams['block_report'] = os.path.join(pluginParams['results_dir'],pluginParams['plugin_name']+'_block.html')
  if not os.path.exists( os.path.join(pluginParams['results_dir'],pluginParams['report_name']) ):
    if pluginParams['cmdOptions'].skip_analysis:
      printlog("Warning: Skip analysis option ignorred as previous output appears to be missing.")
      pluginParams['cmdOptions'].skip_analysis = False

  # set up plugin specific options depending on auto-run vs. plan vs. GUI
  config = pluginParams['config'] = jsonParams['pluginconfig'].copy() if 'pluginconfig' in jsonParams else {}
  if 'launch_mode' in config:
    pluginParams['start_mode'] = 'Manual start'
  elif 'plan' in jsonParams:
    pluginParams['start_mode'] = 'Autostart with plan configuration'
    addAutorunParams(jsonParams['plan'])
  else:
    pluginParams['start_mode'] = 'Autostart with default configuration'
    addAutorunParams()

  # plugin configuration becomes basis of results.json file
  global pluginResult, pluginReport
  pluginResult = pluginParams['config'].copy()
  pluginResult['barcoded'] = pluginParams['barcoded']
  if pluginParams['barcoded']:
    pluginResult['barcodes'] = {}
    pluginReport['barcodes'] = {}

  # configure django to use the templates folder and various installed apps
  if not settings.configured:
    settings.configure( DEBUG=False, TEMPLATE_DEBUG=False,
      INSTALLED_APPS=('django.contrib.humanize',),
      TEMPLATE_DIRS=(os.path.join(pluginParams['plugin_dir'],'templates'),) )


def writeDictToJsonFile(data,filename):
  with open(filename,'w') as outfile:
    json.dump(data,outfile)

def testRun(outdir,prefix):
  # default for testing framework
  testout = os.path.join(outdir,prefix+"_test.out")
  with open(testout,'w') as f:
    f.write("This is a test file.\n")
  printlog('Created %s'%testout)

def runForBarcodes():
  global pluginParams, pluginResult, pluginReport
  # read barcode ids
  barcodes = []
  try:
    bcfileName = pluginParams['analysis_dir']+'/barcodeList.txt'
    with open(bcfileName) as bcfile:
      for line in bcfile:
        if line.startswith('barcode '):
          barcodes.append(line.split(',')[1])
  except:
    printerr("Reading barcode list file '%s'" % bcfileName)
    raise
  numGoodBams = 0
  numUnalBams = 0
  minFileSize = pluginParams['cmdOptions'].minbamsize
  (bcBamPath,bcBamRoot) = os.path.split(pluginParams['bamroot'])
  validBarcodes = []
  for barcode in barcodes:
    # use unmapped BAM if there else mapped BAM (unmapped may not be present on Proton)
    bcbam = os.path.join( bcBamPath, "%s_%s"%(barcode,bcBamRoot) )
    if not os.path.exists(bcbam):
      bcbam = os.path.join( pluginParams['analysis_dir'], "%s_rawlib.bam"%barcode )
      numUnalBams += 1
    if not os.path.exists(bcbam):
      bcbam = ": BAM file not found"
      numUnalBams -= 1
    elif os.stat(bcbam).st_size < minFileSize:
      bcbam = ": BAM file too small"
    else:
      numGoodBams += 1
      validBarcodes.append(barcode)

  printlog("Processing %d barcodes...\n" % numGoodBams)
  if numUnalBams > 0:
    printlog("Warning: %d barcodes will be processed using mapped BAM files. (Unmapped BAMs were not available.)\n" % numUnalBams)
  pluginReport['num_barcodes_processed'] = numGoodBams
  pluginReport['num_barcodes_failed'] = 0

  # iterate over all barcodes and process the valid ones
  skip_analysis = pluginParams['cmdOptions'].skip_analysis
  stop_on_error = pluginParams['cmdOptions'].stop_on_error
  create_scraper = pluginParams['cmdOptions'].scraper
  sample_names = pluginParams['sample_names']
  postout = False; # just for logfile prettiness
  sampleNamesFile = ("%s/sampleNames.txt" % pluginParams['results_dir'])
  sampleNamesFW = open(sampleNamesFile, 'w')
  for barcode in barcodes:
    sample = sample_names[barcode] if barcode in sample_names else ''
    sampleNamesFW.write("%s:%s\n" %(barcode, sample))
  sampleNamesFW.close()
  binDir = os.path.join(pluginParams['plugin_dir'], 'bin')
  outDir = pluginParams['results_dir']
  analysisDir = pluginParams['analysis_dir']
  inputsDir = os.path.join(pluginParams['plugin_dir'], 'inputs')

  runWGMapping = 0
  lowStringency16s = 0
  if 'lowStringency16s' in pluginParams['config']:
	lowStringency16s = 1
  if 'runWholeGenomeMapping' in pluginParams['config']:
	runWGMapping = 1
  #printlog("runWG is %d" % runWGMapping)
  #printlog("low16sStringency is %d" % lowStringency16s)
  minIdPercent = "0.1"
  minGenePercent = "0.1"
  minFamilyPercent = "1.0"
  minWGContigPercent = "0.1" # this argument is not really used in the pipeline.
  minReadLength = "60"
  minLocalAlignmentScore = "60" 
  idEnforceEndToEnd = "1"
  minValuePerCell = "1"
  minPercentSignatureMatch = "0.75"
  if 'minIdPercentage' in pluginParams['config']:
	minIdPercent = pluginParams['config']['minIdPercentage']
	printlog("minIdPercentage is %s" %pluginParams['config']['minIdPercentage'])
  if 'minGenePercentage' in pluginParams['config']:
	minGenePercent = pluginParams['config']['minGenePercentage']
	printlog("minGenePercentage is %s" %pluginParams['config']['minGenePercentage'])  
  if 'minFamilyPercentage' in pluginParams['config']:
	minFamilyPercent = pluginParams['config']['minFamilyPercentage']
	printlog("minFamilyPercentage is %s" %pluginParams['config']['minFamilyPercentage'])  
  if 'minReadLength' in pluginParams['config']:
	minReadLength = pluginParams['config']['minReadLength']
	printlog("minReadLength is %s" %pluginParams['config']['minReadLength'])  
  if 'minLocalAlignmentScore' in pluginParams['config']:
	minLocalAlignmentScore = pluginParams['config']['minLocalAlignmentScore']
	printlog("minLocalAlignmentScore is %s" %pluginParams['config']['minLocalAlignmentScore'])  
  #if 'idEnforceEndToEnd' in pluginParams['config']:
  # 	idEnforceEndToEnd = pluginParams['config']['idEnforceEndToEnd']
  #	printlog("idEnforceEndToEnd is %s" %pluginParams['config']['idEnforceEndToEnd'])  
  #if 'minPercentSignatureMatch' in pluginParams['config']:
  #	minPercentSignatureMatch = pluginParams['config']['minPercentSignatureMatch']
  #	printlog("minPercentSignatureMatch is %s" %pluginParams['config']['minPercentSignatureMatch'])  
  #if 'minValuePerCell' in pluginParams['config']:
  #	minValuePerCell = pluginParams['config']['minValuePerCell']
  #	printlog("minValuePerCell is %s" %pluginParams['config']['minValuePerCell'])  
  if 'analysisSensitivity' in pluginParams['config']:
	analysisSensitivity = pluginParams['config']['analysisSensitivity']
	printlog('16s Analysis sensitivity is %s' %analysisSensitivity)
	if analysisSensitivity == "Low":
		minValuePerCell="2"
		minPercentSignatureMatch="0.8"
	elif analysisSensitivity == "Medium":
		minValuePerCell="1"
		minPercentSignatureMatch="0.8"
	elif analysisSensitivity == "High":
		minValuePerCell="1"
		minPercentSignatureMatch="0.7"
			
  #cmd = ("%s/jdk1.8.0_45/bin/java -jar %s/PathogenDetectionModule.jar %s/IonXpress_026_rawlib.bam %s/sepsis_microbial_panel_reference.fasta %s/sepsis_microbial_panel_designed.bed %s %s %s/gg_13_5_with_taxonomy8fasta_with_truefalsefalse.fasta both" %( binDir, binDir, analysisDir, inputsDir, inputsDir, outDir, binDir, inputsDir))
  cmd = ("java -jar %s/PathogenDetectionModule.jar null %s/panBacterial_ID_Genes_Reference.fasta %s/panBacterial_ID_Genes_Designed.bed %s %s %s/panBacterial_16s_Reference.fasta All %s/sepsis_whole_genomes_final.fasta %s/gg_13_5_with_taxonomy8fasta_with_truefalsefalse.fasta %s %d %s %s %s %s %s %s %s %s %s 8" %( binDir, inputsDir, inputsDir, outDir, binDir, inputsDir, inputsDir, inputsDir, analysisDir, runWGMapping, minIdPercent, minGenePercent, minFamilyPercent, minWGContigPercent, minReadLength, minLocalAlignmentScore, idEnforceEndToEnd, minPercentSignatureMatch, minValuePerCell ))

  printlog(cmd) 
  RunCommand(cmd);
  # parse out data in results text file to dict AND coverts spaces to underscores in keys to avoid Django issues
  statsfile = 'summary.xls'
  analysisData = parseToDict( os.path.join(outDir,statsfile), "\t")
  global barcodeData
  summaryFile = ("%s/barcodeSummary.xls" % pluginParams['results_dir'])
  summaryFileFW = open(summaryFile, 'w')
  summaryFileFW.write("Barcode\tSample Name\tTotal Reads\tReads mapped to ID and Genes targets\tReads mapped to 16s Reference\tUnmapped Reads\tInvalid Reads\n") 
  for barcode in validBarcodes:
	printlog(barcode)
        barcode_entry = {}
        sample = sample_names[barcode] if barcode in sample_names else ''
        barcode_entry['name'] = barcode
	barcodeKey = "%s" %barcode
        if barcodeKey in analysisData:
		barcodeLine = analysisData[barcodeKey]
                printlog("%s\t%s\n" %(barcode, barcodeLine))
                kvp = barcodeLine.split("\t")
                #key = kvp[0].strip()
		if(len(kvp) == 10):
                	barcode_entry['sample_name'] = sample
                	barcode_entry['reads_total'] = kvp[1].strip()
                	barcode_entry['targetsMapped_total'] = kvp[2].strip()
                	barcode_entry['numInvalid'] = kvp[3].strip()
                	barcode_entry['mapped16s_total'] = kvp[6].strip()
                	barcode_entry['offTarget_mapping']=kvp[7].strip()
			barcode_entry['unmapped_total'] = kvp[9].strip()
                elif(len(kvp) == 8):
                	barcode_entry['sample_name'] = sample
                	barcode_entry['reads_total'] = kvp[1].strip()
                	barcode_entry['targetsMapped_total'] = kvp[2].strip()
                	barcode_entry['numInvalid'] = kvp[3].strip()
                	barcode_entry['offTarget_mapping']=kvp[6].strip()
			barcode_entry['unmapped_total'] = kvp[7].strip()
                elif(len(kvp) == 7):
                	barcode_entry['sample_name'] = sample
                	barcode_entry['reads_total'] = kvp[1].strip()
                	barcode_entry['targetsMapped_total'] = kvp[2].strip()
                	barcode_entry['numInvalid'] = kvp[3].strip()
                	barcode_entry['mapped16s_total'] = kvp[6].strip()
                	barcode_entry['offTarget_mapping']="0"
			barcode_entry['unmapped_total'] = int(kvp[1].strip()) - int(kvp[2].strip()) - int(kvp[3].strip()) - int(kvp[6].strip())

		barcodeData.append(barcode_entry)
		summaryFileFW.write(barcodeKey+"\t"+sample+"\t"+str(barcode_entry['reads_total'])+"\t"+str(barcode_entry['targetsMapped_total'])+"\t"+str(barcode_entry['mapped16s_total'])+"\t"+str(barcode_entry['unmapped_total'])+"\t"+str(barcode_entry['numInvalid'])+"\n")
  
  summaryFileFW.close()
  countsfile = 'outputSummary.txt'
  barcodeNames = parseForNames(os.path.join(outDir, countsfile), "\t")
  barcodeCounts = parseForCounts(os.path.join(outDir, countsfile), "\t")
  
  global countsData 
  countsData['barcodeNames'] = barcodeNames
  countsData['barcodeCounts'] = barcodeCounts

  countsfile1 = 'outputOffTargetSummary.txt'
  barcodeNames1 = parseForNames(os.path.join(outDir, countsfile1), "\t")
  barcodeCounts1 = parseForCounts(os.path.join(outDir, countsfile1), "\t")
  
  global offTargetData
  offTargetData['barcodeNames'] = barcodeNames1
  offTargetData['barcodeCounts'] = barcodeCounts1

  countsfile2 = 'idSummary.xls'
  barcodeNames2 = parseForNames(os.path.join(outDir, countsfile2), "\t")
  barcodeCounts2 = parseForCounts(os.path.join(outDir, countsfile2), "\t")
  global idData
  idData['barcodeNames'] = barcodeNames2
  idData['barcodeCounts'] = barcodeCounts2
  
  countsfile3 = 'geneSummary.xls'
  barcodeNames3 = parseForNames(os.path.join(outDir, countsfile3), "\t")
  barcodeCounts3 = parseForCounts(os.path.join(outDir, countsfile3), "\t")
  
  global genesData
  genesData['barcodeNames'] = barcodeNames3
  genesData['barcodeCounts'] = barcodeCounts3

  countsfile4 = 'output16sSummary.xls'
  barcodeNames4 = parseForNames(os.path.join(outDir, countsfile4), "\t")
  barcodeCounts4 = parseForCounts(os.path.join(outDir, countsfile4), "\t")
  
  global output16sData
  output16sData['barcodeNames'] = barcodeNames4
  output16sData['barcodeCounts'] = barcodeCounts4
  
  countsfile5 = 'erccSummary.txt'
  barcodeNames5 = parseForNames(os.path.join(outDir, countsfile5), "\t")
  barcodeCounts5 = parseForCounts(os.path.join(outDir, countsfile5), "\t")
  
  global outputERCCData
  outputERCCData['barcodeNames'] = barcodeNames5
  outputERCCData['barcodeCounts'] = barcodeCounts5
  
  updateBarcodeSummaryReport()
  #Call the R scripts to generate formatted summaries and charts.
  #Rcmd=("%s/sepsisFilterLowAS_count.sh %s" %( binDir, outDir))
  #printlog(Rcmd)
  #RunCommand(Rcmd);

  if create_scraper:
    createScraperLinksFolder( pluginParams['results_dir'], pluginParams['prefix'] )
  #createReport( os.path.join(pluginParams['results_dir'],pluginParams['report_name']), 'block_barcodes.html', render_context )

def runNonBarcoded():
  printerr('Analysis not supported for non-barcoded runs')
  pluginResult.update({ 'Error': 'Analysis not supported for non-barcoded runs' })
  createIncompleteReport('Analysis not supported for non-barcoded runs')
  if pluginParams['cmdOptions'].scraper:
    createScraperLinksFolder( pluginParams['output_dir'], pluginParams['output_prefix'] )

def createScraperLinksFolder(outdir,rootname):
  '''Make links to all files matching <outdir>/<rootname>.* to <outdir>/scraper/link.*'''
  # rootname is a file path relative to outdir and should not contain globbing characters
  scrapeDir = os.path.join(outdir,'scraper')
  if pluginParams['cmdOptions'].logopt:
    printlog("Creating scraper folder %s"%scrapeDir)
  if not os.path.exists(scrapeDir):
    os.makedirs(scrapeDir)
  subroot =  os.path.basename(rootname)+'.'
  flist = glob( os.path.join(outdir,rootname)+'.*' )
  for f in flist:
    lname = os.path.basename(f).replace(subroot,'link.')
    createlink( f, os.path.join(scrapeDir,lname) )

def wrapup():
  '''Called at very end of run for final data dump and clean up.'''
  #if not 'Error' in pluginResult: createBlockReport()
  printtime("Writing results.json...")
  writeDictToJsonFile(pluginResult,os.path.join(pluginParams['results_dir'],"results.json"))

def plugin_main():
  '''Main entry point for script. Returns unix-like 0/1 for success/failure.'''
  try:
    loadPluginParams()
    printStartupMessage()
  except Exception, e:
    printerr("Failed to set up run parameters.")
    traceback.print_exc()
    return 1
  try:
    if not pluginParams['cmdOptions'].skip_analysis:
      emptyResultsFolder()
    if pluginParams['barcoded']:
      runForBarcodes()
      if pluginReport['num_barcodes_processed'] == 0:
      	printlog("WARNING: No barcode alignment files were found for this barcoded run.")
      elif pluginReport['num_barcodes_processed'] == pluginReport['num_barcodes_failed']:
      	printlog("ERROR: Analysis failed for all barcode alignments.")
      	return 1
    else:
      runNonBarcoded()
    wrapup()
  except Exception, e:
    traceback.print_exc()
    wrapup()  # call only if suitable partial results are available, including some error status
    return 1
  return 0

if __name__ == "__main__":
  x = plugin_main()
  exit(x)
