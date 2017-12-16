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

log_dir = os.path.join(os.getcwd(), "error_logs")
#add log directory
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)

work_normally = np.random.randint(0, 10)

if(work_normally < 7):
    print("work normally")

else:
    print("encounter some error")
    print("working on some checking and recovering...")
    
    time.sleep(30)
    
    # log the error message
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(os.path.join(log_dir, "error_log_"+current_time+".txt"), "w") as fp:

        print(os.path.join(log_dir, "error_log_"+current_time+".txt"))
        fp.write("error: "+current_time )
