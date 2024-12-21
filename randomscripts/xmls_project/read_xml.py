import xml.etree.ElementTree as ET

import os
os.chdir('C:\\Users\\rkrall\\github\\randomscripts\\xmls_project')
file_name = '02.73289 - DENMARK AGRICULTURAL.00582138.0824224932.xml'
#file_name = 'test.xml' #copied file above to pasted in a utf-8 file format
#file_name = 'sample_xml.xml'

tree = ET.parse(file_name)
root = tree.getroot()

#loop through xml to find the node to update
for elem in root:
    for Customer in elem:
        for CustomerInfo in Customer:
            for status in CustomerInfo .iter('Status'):
                if int(status.text) == 5:
                    #print("found 5") #output for debugging
                    #Update value to 0
                    status.text = str(5)
                    status.set('updated','yes')

tree.write('output_xml.xml')
