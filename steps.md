clone project repo (e.g. `git clone`)  
clone [Mask_RCNN repo](https://github.com/matterport/Mask_RCNN) into _parent directory_  
download training weights [from here](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)  
download Massimo's subset of the dataset [here](https://drive.google.com/file/d/1q_FanEMUwS2qT6w9i0sUR_FyYhh4P8IB/view?usp=sharing)  
upload weights to pangeo  
upload dataset to pangeo  
run setup in the Mask_RCNN directory (e.g. `python setup.py install`)   
go into Mask_RCNN/mrcnn/model.py and change `max_queue_size` to 1 (if you do not have a GPU)    
unzip data into a data directory (e.g. `unzip sample.zip`)  
go through the Jordan's notebook! (e.g. `computer_vision_club_script.ipynb`)  
change paths to weights and data in notebook!  
gl and hf  
