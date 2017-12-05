import numpy as np
import time

work_normally = np.random.randint(0, 10)

if(work_normally < 7):
    print("work normally")

else:
    print("encounter some error")
    print("working on some checking and recovering....")

    with open("log.txt", "w") as fp:
        fp.write("error: "+time.time() )
