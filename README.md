# ohw19-project-computer_vision_club
computer vision club project for ocean hackweek 2019

Welcome to the computer vision club at OHW 2019. Please join us in the slack channel #computervisionclub-2

RULE 1: name notebooks and files with lower case letters and _ for spaces. Thank you.
RULE 2: have fun.

Group Members:
Jordan Pierce

Location of LabelImg --> https://github.com/tzutalin/labelImg (recommend using PyPi to install)


## Structuring the repo

Improve the `README.md` by filling individual sections from the project guidelines:

[https://oceanhackweek.github.io/wiki/project_guidelines.html](https://oceanhackweek.github.io/wiki/project_guidelines.html)

#### Project title

#### Discussion Participants

#### The problem

#### Application example

#### Specific tasks

- Go through all XML annotations and record all of the different number of organisms annotated
(e.g. scallop, starfish, ray) and find the distribution. The goal here is to find the majority 
class. That is the class we care about.

- Now that we know majority class, we need to parse the XML files. That is, go through every single
XML file and find the annotations that correspond to the majority class and save those annotations 
to a new annotation file. This new annotation file will only contain the annotations for the majority 
class.

- With all these new XML files, we then need to convert the annotation data in them into another
data structure (maybe a Pandas dataframe?)... This dataframe will be something like:
___________________________________________________________________
Annotation ID | Original Image | xmin | ymin | xmax | ymax | area |
-------------------------------------------------------------------

With this format, we can setup a function that will take in each row (individual annotation instances) and crop
the sub-image from the original image and save it as it's own. We will have a folder containing many many patches; 
these will act as our training data.

Further down the road:

Data augmentation
Choosing the cnn network and object detection framework (two seperate pieces that go together)
THE TRAINING
Predictions

#### Existing methods

#### Proposed methods/tools

#### Background reading

### Project Organization
