# ohw19-project-computer_vision_club
Computer vision club project for ocean hackweek 2019

Welcome to the computer vision club at OHW 2019. Please join us in the slack channel #computervisionclub-2   


## Rule
RULE 1: have fun and don't freak out.  


## Important scripts  
`data_preparation.ipynb`  
`computer_vision_club_script.ipynb`  
`utility.py`  
`robot_overlord.gif`  


#### Project title

*Underwater Currency Counter- a Semi Supervised Annotation Tool: Kickass AI to count sand dollars*

#### Discussion Participants

[Jordan Pierce](https://www.jordanmakesmaps.com/)    

[Dimitris Politikos](https://www.linkedin.com/in/dimitris-politikos-74b754160/)   

[Massimo Di Stefano](https://ccom.unh.edu/user/distefano)  

[Ágata Piffer Braga](https://www.linkedin.com/in/%C3%A1gata-piffer-braga-42724873/?originalSubdomain=br)  

[Ivan Rodriguez-Pinto](https://boswelllab.wixsite.com/boswelllab/people)  

[Emilio](https://github.com/EmilioTesin100) 

[Coral Moreno](https://ccom.unh.edu/user/cmoreno)   


#### The Problem

Annotating imagery data by hand is time consuming, mundane and costly which is only exacerbated with larger datasets. What if you could use AI to help you with the brunt of the workload, leaving you with the simple task of going over its predictions and ensuring it is correct?

This project aims to use benthic habitat imagery data collected from ROVs to train a deep object recognition algorithm. With a learned model, its task will then be used to make predictions on non-annotated data. Predictions with high enough confidences will be retained as per the users discretion.

### Workflow at a glance:

1.) Parsing/cleaning existing annotation data  
2.) Extracting and organizing training data   
3.) Preprocessing and augmenting training data    
4.) Train object recognition/image classification network   
5.) Apply trained model to new data, take *good* predictions and add to training data   

Rendered version of the [computer_vision_club_script notebook](https://nbviewer.jupyter.org/github/oceanhackweek/ohw19-project-computer_vision_club/blob/master/computer_vision_club_script.ipynb)

##  Steps to follow to quickly dip your toes into this CVC project
 
 ### Train your model 
 
Step | Direction |
--- | --- |
 1	| clone this project repo (e.g. `git clone`)  |
 2  | clone [Mask_RCNN repo](https://github.com/matterport/Mask_RCNN) into _parent directory_ |
 3  | download training weights [from here](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)  |
 4	| download Massimo's subset of the dataset [here](https://drive.google.com/file/d/1q_FanEMUwS2qT6w9i0sUR_FyYhh4P8IB/view?usp=sharing)  |
 5  | upload training weight to pangeo or wherever you're working *"mask_rcnn_coco.h5"*  |
 6  | upload training dataset to pangeo or wherever you're working in a zipped file  |
 7  | run setup in the Mask_RCNN directory to install the repo's code (e.g. `python setup.py install`)  |
 8  | edit `model.py` with a change of `max_queue_size` to 1 and `multi_threading` to False (if you do not have a GPU)  |
 9  | unzip data into a data directory (e.g. `unzip sample.zip -d /path/to/directory`)  |
 10 | run the notebook `computer_vision_club_script.ipynb`; make changes to your unique file paths  |
 11 | have fun and good luck  |  
   
 ### Test your predictions 
 Step | Direction |
--- | --- |
  1	| copy the file path of the last weight created into the load weights cell | 
  2 | run the last chapter of the computer vision club script notebook  |
 

#### Proposed methods/tools

Tensorflow - for building and training the network   
Keras - for building and training the network   
OpenCv - image processing and augmentation  
Scikit image - image processing and augmentation  
Pandas - for data science  
Numpy and/or Cupy - for data science  
labelImg - for annotating data  

#### Background reading/watching

[Mask RCNN with Keras tutorial](https://www.pyimagesearch.com/2019/06/10/keras-mask-r-cnn/)  
[YOLO TED Talk](https://www.youtube.com/watch?v=Cgxsv1riJhI)  
[Rare Puppers](https://i.redd.it/keszh72c3io01.jpg)  

### Longterm project objective 
  
Help our robot overlords achieve world domination

![All hail the robot overlords!](robot_overlord.gif)



