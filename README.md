# ohw19-project-computer_vision_club
computer vision club project for ocean hackweek 2019

Welcome to the computer vision club at OHW 2019. Please join us in the slack channel #computervisionclub-2

## Rules
RULE 1: name notebooks and files with lower case letters and _ for spaces.  
RULE 2: have fun and don't freak out.

## Structuring the repo

Improve the `README.md` by filling individual sections from the project guidelines:

[https://oceanhackweek.github.io/wiki/project_guidelines.html](https://oceanhackweek.github.io/wiki/project_guidelines.html)

#### Project title

*Underwater currency counter: Kickass AI to count sandollars*

#### Discussion Participants

Jordan Pierce  

Dimitris Politikos  

Massimo Di Stefano

Ágata Piffer Braga

Ivan Rodriguez-Pinto

Emilio

Coral Moreno
...  
...  

#### The Problem

Annotating imagery data by hand is time consuming, mundane and costly which is only exacerbated with larger datasets. What if you could use AI to help you with the brunt of the workload, leaving you with the simple task of going over its predictions and ensuring it is correct?

This project aims to use benthic habitat imagery data collected from ROVs to train a deep object recognition algorithm. With a learned model, its task will then be used to make predictions on non-annotated data. Predictions with high enough confidences will be retained as per the users discretion.

### Workflow at a glance:

1.) Parsing/cleaning existing annotation data   __complete__
2.) Extracting and organizing training data   __complete__
3.) Preprocessing and augmenting training data   
4.) Train object recognition/image classification network  
5.) Apply trained model to new data, take *good* predictions and add to training data  

#### Application example

#### Specific tasks

The current task:  

Everyone should have access to the most updated version of 'jordan_scrap_notebook' and the results/sample/... data that Massimo organized. With these you can now start your own training process! :)

What you need to do is change the configure file which in the script, is a class titled `TrainConfig()`

[Here](https://github.com/matterport/Mask_RCNN) is the link to the repo that we're using, if you need help, find what you need in the tutorials under the section __Getting Started__

[Here](https://machinelearningmastery.com/how-to-train-an-object-detection-model-with-keras/) is the link to the Kangaroo tutorial. Jordan's script is almost the same exact code. If you don't understand why Jordan did what he did, read this!  

Last but not least, download Massimo's [data!](https://drive.google.com/file/d/1q_FanEMUwS2qT6w9i0sUR_FyYhh4P8IB/view?usp=sharing).

[This](https://gist.github.com/21c99f12f286cb84f6abd025d299a800) is how the data was prepared!

__Make sure to put the data in your local machine, unzip it, and edit Jordan's script to work with it (change the source variable)__

#### Existing methods

#### Proposed methods/tools

Keras - for building and training the network   
OpenCv - image processing and augmentation  
Scikit image - image processing and augmentation  
Pandas - data science  
Numpy and/or Cupy - data science  
Numba - SPEED  
labelImg -- has to be installed in your cloud environment. Use pip to install labelImg in your terminal. 

#### Background reading/watching

YOLO: https://www.youtube.com/watch?v=Cgxsv1riJhI   

### Project Organization

Name : Task

### Longterm project objective 
  
Help our robot overlords achieve world domination

![](robot_overlord.gif)


