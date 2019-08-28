import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from jinja2 import Template


def xml2df(xml_files, basedir="results/samples/"):
    xml_list = []
    for xml_file in xml_files:
        xml_file = basedir+xml_file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
    
    
def df2xml(dfgroup, output_dir='samples/newxml'):
    object_tpl = '''<object>
    <name>{{label}}</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
	    <xmin>{{xmin}}</xmin>
	    <ymin>{{ymin}}</ymin>
	    <xmax>{{xmax}}</xmax>
	    <ymax>{{ymax}}</ymax>
    </bndbox>
    </object>'''
    annotation_tpl = '''<annotation>
    <folder></folder>
    <filename>{{filename}}</filename>
    <path>{{filename}}</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>1360</width>
        <height>1024</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    {{objects}}
    </annotation>'''
    ti = Template(object_tpl)
    t = Template(annotation_tpl)

    for name, group in dfgroup:
        out_xml = name.replace('.jpg','.xml')
        out_xml = output_dir+'/'+out_xml
        print(out_xml)
        with open(out_xml, "w") as xml_file:
            obj = ''
            for index, row in group.iterrows():
                obj += ti.render(label=row['class'], 
                                 xmin=row['xmin'], 
                                 xmax=row['xmax'], 
                                 ymin=row['ymin'], 
                                 ymax=row['ymax'])
            body = t.render(filename=name, objects=obj)
            print(name, '\n', '########################','\n')
            xml_file.write(body)