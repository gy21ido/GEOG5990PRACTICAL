# AGENT BASED MODELLING
This repository is the online portfolio containing all codes and files for Agent Based Model written for the module **GEOG 5990 Programming for Spatial Analysts: Core Skills**, in fulfilment of part of the requirements to achieve a MSc in Geographical Information Systems (GIS) at the University of Leeds.
## Contents list
Files included in the repository include: 
* Agentframework.py (the class code for the Agents)
* Model.py (the code for the agent-based model)
* in.txt / environment.csv (file containing the environment where the agents interact with one another)
* A documentation folder, download all files, and click the **index.html** to read the functions documentations and tests.

## What the Agent Based Model software is
The Agent Based Model (ABM) is an Object-Oriented Programming and iterative model where agents perform various activities among one another and between the environment they occupy. Generally, just as every man has a stop in their day-to-day activities when a limit is reached, so do agents in ABM. The ABM expects three key codes before it can run to expectation:
* ***_The Model code_***, a user interactive code where the model is set up, including information about the agents, iterations given to them, and stopping conditions that ensure model is run efficiently.
* ***_The Agent class code_***, where the agents are built and all information about them is included; for example, behaviours such as how they move, share with their neighbours, eat, and breed to populate themselves.In this model, two agent classes were created (one for the agents proper, and another for wolves (agents predators).
* ***_The Environment code_***, which is the space within which the agents behave as deem fit and interact with themselves. In spatial science,it is mostly a raster grid of data, plotted with matplotlib to include colours.

## Instructions to run the program
**Note:** Refer to **KNOWN ISSUES** below first, so you know what to expect, especially the second point.
1. Download all files stated above into a directory on your local machine (all found on the GitHub page).
2. Run the **Model.py** file using either using any Development Environment, especially Spyder or navigate to the directory with the files and run from command prompt as shown below:
```python
python Model.py
```
3. For user interactivity, the code asks the user to input the: 
- ***_Number of agents_*** as integer between 0 and 100,
- ***_Number of iterations_*** between 0 and 200, 
- ***_Number of wolves_*** between 0 and 50, and
- ***_Number of loops_*** between 1 and 5 for timing.
**Note:** User must enter a value within the boundaries for each variable. Also, user may quit before running the model by hitting **'q or Q'** key on their keyboards.
4. A tkinter window pops up, click the **'Model'** button, then click on **'Run Model'**
**Note:** User runs the model the number of times stated in their chosen loop **(Agents are blue, Wolves are black in colour)**
5. Exit the model using the **'Click and Quit'** button on the model frame or click the cross button at the frame edge

## Expectations upon running the codes
- User is expected to run the model file the number of times given as loop input.
- If user inputs a wrong value apart from the thresholds of required input values, the code will not run, rather, it asks the user to input correct values.
- Agents and Wolves move within the environment at specified paces, upon eating, the environment colour changes. 
- Statistical values will be generated at the end of running the model as follows: 
  * Inline Plot of Agents and Wolves farthest to the East, North, South and West with their location and store.
  * Agents' and Wolves' Population growth rate
  * Agents' birth rate and death rate 
  * Wolves' birth rate (no death rate) since the wolves do not die.
  * Elapsed time for running function.
 Further understanding of how the model runs is included in the GitHub website. To generate the animation video included in the website, use the code below:
 ```python
from matplotlib import animation
# full paths for ffmpeg where gif saves
    plt.rcParams['animation.ffmpeg_path'] = '‪C:\\FFmpeg\bin\ffmpeg.exe'

    animation = matplotlib.animation.FuncAnimation(fig, update, frames = gen_function, repeat = False)
    canvas.draw()
    
    # save animation at exact Agents and Wolves movement
    animation.save('myAnimation.gif', writer = 'Pillow', fps = None)
```
## Known issues
- If the code below is added as import (although commented in the raw code) with the 'tkinter' backend selected within spyder, two plot windows are displayed. User has to close the two windows and interrupt kernel before it works. 
```python
matplotlib.use('TkAgg') 
```
Therefore, the 'Inline' option is best suitable for the model to run effectively.
- To generate the statistics and plot above, user has to input more than a value of 1 for agents, wolves, iterations, and loops; this is to ensure there is opportunity for the agents to move, interact, and breed. If they do not move, there is no breeding, hence, values have to be high. 

## Testings performed
All functions were tested within the Python Console and included in appropriate DocStrings. Other testings were done with the print statements, which were commented out in the files. Detailed tests are placed within the **documentation** folder in this repository. 

## Ideas for further development
Further behavioural characteristics may be added to the agents and wolves.

## Contributions
Contributions are welcome for improvement on the codes.

## License and Copyright
&copy; 201576424, School of Geography, University of Leeds, United Kingdom.  
Licensed under the [MIT License](LICENSE).
