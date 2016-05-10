import numpy as np
from model.accessdbclient import accessdbclient

class calc(object):
    """Methods for calculating average and displacements"""
    def __init__(self):
        self.client = accessdbclient()

    def average(self, pid, get_date):        
        rw_dat = np.array(self.client.getRawData_Day(pid, get_date))
        date = rw_dat[:,0]
        avg_n = rw_dat[:,[1,4,7]].mean(axis=0)
        avg_e = rw_dat[:,[2,5,8]].mean(axis=0)
        avg_z = rw_dat[:,[3,6,9]].mean(axis=0)
        return avg_n, avg_e, avg_z

    def disp(self, pid, get_date):
        try:
            bm_dat = np.array(self.client.getBenchmark())
            avgs = np.array(calc().average(pid, get_date))
            disp = avgs - bm_dat
            for row in avgs:
                disp = bm_dat - row
            return disp
        except Exception as e:
            print e