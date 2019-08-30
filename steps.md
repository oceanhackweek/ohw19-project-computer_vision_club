##  Steps to follow to quickly dip your toes into this CVC project
 
 ### Train your model 
 
Step | Direction |
--- | --- |
 1	| clone project repo (e.g. `git clone`)  |
 2  | clone [Mask_RCNN repo](https://github.com/matterport/Mask_RCNN) into _parent directory_ |
 3  | download training weights [from here](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)  |
 4	| download Massimo's subset of the dataset [here](https://drive.google.com/file/d/1q_FanEMUwS2qT6w9i0sUR_FyYhh4P8IB/view?usp=sharing)  |
 5  | upload training weight to pangeo *"mask_rcnn_coco.h5"*  |
 6  | upload training dataset to pangeo in a zipped file  |
 7  | run setup in the Mask_RCNN directory (e.g. `python setup.py install`)  |
 8  | edit the Mask_RCNN/mrcnn/model.py with a change of `max_queue_size` to 1 (if you do not have a GPU)  |
 9  | unzip data into a data directory (e.g. `unzip sample.zip -d /path/to/directory`)  |
 10 | Run the notebok Jordan wrote `computer_vision_club_script.ipynb` with changes to your unique file paths  |
 11 | gl & hf  |  
   
 ### Test your predictions 
 Step | Direction |
--- | --- |
  1	| copy the file path of the last weight created into the load weights cell | 
  2 | run the last chapter of the computer vision club script notebook  |
 
 
