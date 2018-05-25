# Export Todoist tasks To Text Files
# Read a CSV file of Project Template from Todoist
# and generate one file per task.
#
# File details:
#   file name - Task description without special characteres
#   file content - Task description + task notes
#
# This is util to import Todoist tasks to Evernote
# using the Import Folder funcionality of that
#
# Author: Ricidleiv Tondatto
# Date: 25.May.2018

import os
import re
import csv

path_to_csv = '/home/tondatto/Workspace/Python/todoist/csv/'
path_to_txt = '/home/tondatto/Workspace/Python/todoist/txt/'

TODOIST_RECORD_SEP = ',,,,,,,,'

# iter each file in directory
for filename in sorted(os.listdir(path_to_csv)):
    
    # directory to save the project tasks
    d = re.sub(r'\.\w+$', '', filename) 
    d = re.sub(r'\W', '', d)

    # create directory if not exists
    dir_name = path_to_txt + d
    
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    
    with open(path_to_csv + filename, 'r') as f:

        # get the tasks records
        records = f.read().split(TODOIST_RECORD_SEP)

        # iter each task record
        for r in records:
            note_title = ''
            note_content = ''

            # core logic
            for line in csv.reader(r.split('\n'),
                                   quotechar='"',
                                   delimiter=',',
                                   quoting=csv.QUOTE_ALL,
                                   skipinitialspace=True):
                if len(line) > 0:
                    if line[0] == 'task':
                        note_title = line[1]
                        note_content = note_title + '\n\n'
                    elif line[0] == 'note':
                        note_content = note_content + line[1] + '\n'

            # prepare file to save the task

            # remove mentions to 'filter' 
            file_title = re.sub(r'@\w+', '', note_title)

            # remove special characters
            file_title = re.sub(r'[^\s\w]', '', file_title).strip()
            
            if file_title != '':

                # write the file
                with open(dir_name + '/' + file_title, 'w') as text_file:
                    print(note_content, file=text_file)
