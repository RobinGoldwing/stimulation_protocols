# Xscape Project – Stimulus Presentation Code

This repository contains the code used for presenting stimuli in the **Xscape Project**.

It supports integration with:
- **EyeLink** eye-tracking systems  
- **Pupil/Core** with Neon glasses  
- **EmotiBit** FitBands for physiological data synchronization  

Each folder includes specific documentation and scripts related to its functionality.

## Status

🛠️ **Under Development**  
This code is currently a work in progress. The code for running experiments synchronizing eye trakcin/emotibit is already up and working.
For contributions, feedback, and suggestions are very welcome, contact the corresponding author:
arturo-jose.valino@incipit.csic.es

Project (CSIC-INCIPIT) 02/03/2023


# Set up

1. Prepare the picture
	- Put in the OBJECTS folder all the tif images you want to show
	- If surprise images needed in a fixe position add a pseudorandom folder with the tif images and order.txt file with the order

2. Verify main screen -> main screen must be the one where the experiment will be displayed

3. Connect and run pupil capture
	- Make sure that calibration is on screen set up
	- put correct participant name in the record window
	- check the camera red light on eyes

# Run the experiment

1. Open "Anaconda Prompt (miniconda3)"

2. Type in:

	cd C:\Users\LScholtus\Archeo\XSCAPE\Automatic_EXP\screen_stimulus_presentation

3. activate the environment:

	conda activate pupil_labs

4: run the experiment:

	python stim_emotibit_cal_before.py C:\Users\LScholtus\Archeo\XSCAPE\Automatic_EXP\screen_stimulus_presentation\EXP

5. follow instruction on the screen

6. Copy Pupil capture console into a txt file


To stop the experiment if something is wrong ctr + c



If problems with step 4 you can also follow this procedure

	- type in:

	python stim_emotibit_window_min_calibration.py C:\Users\LScholtus\Archeo\XSCAPE\Automatic_EXP\screen_stimulus_presentation\EXP

		- press enter to start calibration
		- type ok even if no calibration started
		- launch calibration from Pupil Capture
		- if calibration ok type start in Miniconda
	
## Stim protocol for pupil labs

Code for presentation of stimulus for the Xscape proyect.
The code automatically executes the stimulation protocol for a 
pupil labs experiment in a display monitor. It automatically connects through
the pupil lab and API, starts the recording and shows the stimulus.
It also sends events to pupil core to record the timstamp in which each event 
was presented.  

To install the environment just execute:

conda env create -f pupil_labs.yml

Once with the environment installed drop the fotos in .tif format you want
for the screen stimulation in OBJECTS. The stimuly from OBJECTS will be randomized,
and the files in OBJECTS/PSEUDORANDOM will be presented in a fixed place but radonmized order
as determined by the order.txt. Where the order is determined by a sequence of numbers seperated by ','.
(0,2,4,5)----order is pythonic where 0 is the first order of appearance.

** If you want an experiment wit all images completely random just delete the pseudorandom folder.

It might be necesary to play with the parameter screen=(0,1) and to change the main screen in iondows configurations
depending on the computer set up. Dependeding on the computer it may be necesarry to configure the stimulation monitor
as the main screen of the computer, to show the calibration in the stimulation monitor.

With pupil capture executed type
python stim_emotibit.py <dir>

Where dir is the directory to save the stimulation images and a .txt with the order of appearance.
Each .tif will be saved with the following format <image_name>_<order_of_appearance(int)>.tif 


For help type

python stim_emotibit.py -h

Run the program and follow the instruction in the console.


## De code is under development. Any contributions and suggestions are welcome. To 
commit a pull request refer to the Xscape proyect corresponding author: 
arturo-jose.valino@incipit.csic.es

                                            Xscape Project (CSIC-INCIPIT) 02/03/2023
                                            


