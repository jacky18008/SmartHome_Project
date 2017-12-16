import datetime
import argparse
import numpy as np
import time
import os

parser = argparse.ArgumentParser(description='path')
parser.add_argument('path', type=str)
args = parser.parse_args()
path = args.path
#change current directories
os.chdir(path)

work_normally = np.random.randint(0, 10)

if(work_normally < 7):
    print("work normally")

else:
    print("encounter some error")
    print("working on some checking and recovering...")
    
    time.sleep(10)
    
    # log the error message
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("error_log_"+current_time+".txt", "w") as fp:
        
        fp.write("error: "+current_time )
