#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed Feb  1 13:40:01 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'temp'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/Rivendell/Documents/UWA/Psychopy_workshop/Example experiment1/temp.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_slide = visual.ImageStim(win=win, name='welcome_slide',
    image=u'welcome_slide.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "practice_trial"
practice_trialClock = core.Clock()
real_image_practice = visual.ImageStim(win=win, name='real_image_practice',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross_practice = visual.TextStim(win=win, ori=0, name='fixation_cross_practice',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instructions_practice = visual.ImageStim(win=win, name='instructions_practice',
    image=u'instructions.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
real_image = visual.ImageStim(win=win, name='real_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.TextStim(win=win, ori=0, name='fixation_cross',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instructions = visual.ImageStim(win=win, name='instructions',
    image=u'instructions.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "welcome"-------
t = 0
welcomeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
welcome_keypress = event.BuilderKeyResponse()  # create an object of type KeyResponse
welcome_keypress.status = NOT_STARTED
# keep track of which components have finished
welcomeComponents = []
welcomeComponents.append(welcome_slide)
welcomeComponents.append(welcome_keypress)
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "welcome"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_slide* updates
    if t >= 0.0 and welcome_slide.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_slide.tStart = t  # underestimates by a little under one frame
        welcome_slide.frameNStart = frameN  # exact frame index
        welcome_slide.setAutoDraw(True)
    
    # *welcome_keypress* updates
    if t >= 0.0 and welcome_keypress.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_keypress.tStart = t  # underestimates by a little under one frame
        welcome_keypress.frameNStart = frameN  # exact frame index
        welcome_keypress.status = STARTED
        # keyboard checking is just starting
        welcome_keypress.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if welcome_keypress.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            welcome_keypress.keys = theseKeys[-1]  # just the last key pressed
            welcome_keypress.rt = welcome_keypress.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcome_keypress.keys in ['', [], None]:  # No response was made
   welcome_keypress.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('welcome_keypress.keys',welcome_keypress.keys)
if welcome_keypress.keys != None:  # we had a response
    thisExp.addData('welcome_keypress.rt', welcome_keypress.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Users/Rivendell/Documents/UWA/Psychopy_workshop/Example experiment1/temp.psyexp',
    trialList=data.importConditions(u'practice_trials.xlsx'),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop.keys():
        exec(paramName + '= thisPractice_loop.' + paramName)

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop.keys():
            exec(paramName + '= thisPractice_loop.' + paramName)
    
    #------Prepare to start Routine "practice_trial"-------
    t = 0
    practice_trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    real_image_practice.setImage(practice_image)
    keyboard_response_practice = event.BuilderKeyResponse()  # create an object of type KeyResponse
    keyboard_response_practice.status = NOT_STARTED
    # keep track of which components have finished
    practice_trialComponents = []
    practice_trialComponents.append(real_image_practice)
    practice_trialComponents.append(fixation_cross_practice)
    practice_trialComponents.append(keyboard_response_practice)
    practice_trialComponents.append(instructions_practice)
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice_trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practice_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *real_image_practice* updates
        if t >= 0.5 and real_image_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            real_image_practice.tStart = t  # underestimates by a little under one frame
            real_image_practice.frameNStart = frameN  # exact frame index
            real_image_practice.setAutoDraw(True)
        if real_image_practice.status == STARTED and t >= (0.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            real_image_practice.setAutoDraw(False)
        
        # *fixation_cross_practice* updates
        if t >= 0.0 and fixation_cross_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross_practice.tStart = t  # underestimates by a little under one frame
            fixation_cross_practice.frameNStart = frameN  # exact frame index
            fixation_cross_practice.setAutoDraw(True)
        if fixation_cross_practice.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation_cross_practice.setAutoDraw(False)
        
        # *keyboard_response_practice* updates
        if t >= 1.5 and keyboard_response_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyboard_response_practice.tStart = t  # underestimates by a little under one frame
            keyboard_response_practice.frameNStart = frameN  # exact frame index
            keyboard_response_practice.status = STARTED
            # keyboard checking is just starting
            keyboard_response_practice.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if keyboard_response_practice.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                keyboard_response_practice.keys = theseKeys[-1]  # just the last key pressed
                keyboard_response_practice.rt = keyboard_response_practice.clock.getTime()
                # was this 'correct'?
                if (keyboard_response_practice.keys == str(correctAns)) or (keyboard_response_practice.keys == correctAns):
                    keyboard_response_practice.corr = 1
                else:
                    keyboard_response_practice.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *instructions_practice* updates
        if t >= 1.5 and instructions_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_practice.tStart = t  # underestimates by a little under one frame
            instructions_practice.frameNStart = frameN  # exact frame index
            instructions_practice.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practice_trial"-------
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyboard_response_practice.keys in ['', [], None]:  # No response was made
       keyboard_response_practice.keys=None
       # was no response the correct answer?!
       if str(correctAns).lower() == 'none': keyboard_response_practice.corr = 1  # correct non-response
       else: keyboard_response_practice.corr = 0  # failed to respond (incorrectly)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('keyboard_response_practice.keys',keyboard_response_practice.keys)
    thisExp.addData('keyboard_response_practice.corr', keyboard_response_practice.corr)
    if keyboard_response_practice.keys != None:  # we had a response
        thisExp.addData('keyboard_response_practice.rt', keyboard_response_practice.rt)
    thisExp.nextEntry()
    # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_loop'

# get names of stimulus parameters
if practice_loop.trialList in ([], [None], None):  params = []
else:  params = practice_loop.trialList[0].keys()
# save data for this loop
practice_loop.saveAsExcel(filename + '.xlsx', sheetName='practice_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
experiment_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Users/Rivendell/Documents/UWA/Psychopy_workshop/Example experiment1/temp.psyexp',
    trialList=data.importConditions(u'trials.xlsx'),
    seed=None, name='experiment_loop')
thisExp.addLoop(experiment_loop)  # add the loop to the experiment
thisExperiment_loop = experiment_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisExperiment_loop.rgb)
if thisExperiment_loop != None:
    for paramName in thisExperiment_loop.keys():
        exec(paramName + '= thisExperiment_loop.' + paramName)

for thisExperiment_loop in experiment_loop:
    currentLoop = experiment_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExperiment_loop.rgb)
    if thisExperiment_loop != None:
        for paramName in thisExperiment_loop.keys():
            exec(paramName + '= thisExperiment_loop.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    real_image.setImage(image)
    keyboard_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    keyboard_response.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(real_image)
    trialComponents.append(fixation_cross)
    trialComponents.append(keyboard_response)
    trialComponents.append(instructions)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *real_image* updates
        if t >= 0.5 and real_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            real_image.tStart = t  # underestimates by a little under one frame
            real_image.frameNStart = frameN  # exact frame index
            real_image.setAutoDraw(True)
        if real_image.status == STARTED and t >= (0.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            real_image.setAutoDraw(False)
        
        # *fixation_cross* updates
        if t >= 0.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # underestimates by a little under one frame
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation_cross.setAutoDraw(False)
        
        # *keyboard_response* updates
        if t >= 1.5 and keyboard_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyboard_response.tStart = t  # underestimates by a little under one frame
            keyboard_response.frameNStart = frameN  # exact frame index
            keyboard_response.status = STARTED
            # keyboard checking is just starting
            keyboard_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if keyboard_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                keyboard_response.keys = theseKeys[-1]  # just the last key pressed
                keyboard_response.rt = keyboard_response.clock.getTime()
                # was this 'correct'?
                if (keyboard_response.keys == str(correctAns)) or (keyboard_response.keys == correctAns):
                    keyboard_response.corr = 1
                else:
                    keyboard_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *instructions* updates
        if t >= 1.5 and instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions.tStart = t  # underestimates by a little under one frame
            instructions.frameNStart = frameN  # exact frame index
            instructions.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyboard_response.keys in ['', [], None]:  # No response was made
       keyboard_response.keys=None
       # was no response the correct answer?!
       if str(correctAns).lower() == 'none': keyboard_response.corr = 1  # correct non-response
       else: keyboard_response.corr = 0  # failed to respond (incorrectly)
    # store data for experiment_loop (TrialHandler)
    experiment_loop.addData('keyboard_response.keys',keyboard_response.keys)
    experiment_loop.addData('keyboard_response.corr', keyboard_response.corr)
    if keyboard_response.keys != None:  # we had a response
        experiment_loop.addData('keyboard_response.rt', keyboard_response.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'experiment_loop'

# get names of stimulus parameters
if experiment_loop.trialList in ([], [None], None):  params = []
else:  params = experiment_loop.trialList[0].keys()
# save data for this loop
experiment_loop.saveAsExcel(filename + '.xlsx', sheetName='experiment_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
win.close()
core.quit()
