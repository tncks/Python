'''
Created on 2017. 7. 23.

@author: duddn
'''

import os

for(path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s%s" % (path, filename))