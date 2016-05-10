import numpy as np
from model.accessdbclient import *
from dateutil.parser import parse
from pitmon.calc import *
from pitmon.viz import *
from sys import exit

def plot():
    dbclient = accessdbclient()
    view = viz()
    print "Enter prism ID:"
    prism_id = raw_input(">>> ")
    print "Plot for: (1)All (2)Year (3)Month (0)Exit program"
    plot_type = int(raw_input(">>> "))
    title = "Prism Monitoring for "
    try:      
        if plot_type == 1: #All
            raw_data = np.array(dbclient.getCD_All(prism_id))
            dates, points_n, points_e, points_z = raw_data[:,0], raw_data[:,-3], raw_data[:,-2], raw_data[:,-1]            
            view.make_plot(dates, points_n, points_e, points_z, title + "All" )
            recy()
        elif plot_type == 2: #Year
            print "Enter the year in this format YYYY:"
            dt = raw_input(">>> ")
            raw_data = np.array(dbclient.getCD_Year(prism_id, parse(dt) ))
            dates, points_n, points_e, points_z = raw_data[:,0], raw_data[:,-3], raw_data[:,-2], raw_data[:,-1]
            view.make_plot(dates, points_n, points_e, points_z, title + dt )
            recy()
        elif plot_type == 3: #Month
            print "Enter the year and month in this format YYYY-MM:"
            dt = raw_input(">>> ")
            raw_data = np.array(dbclient.getCD_Month(prism_id, parse(dt) ))
            dates, points_n, points_e, points_z = raw_data[:,0], raw_data[:,-3], raw_data[:,-2], raw_data[:,-1]
            view.make_plot(dates, points_n, points_e, points_z, title + dt )
            recy()
        elif plot_type == 0:
            exit(0)
        else:
            print "Input incorrect, TRY AGAIN"
            start()
    except Exception as e:
            print e

def recy():
    print "Continue(1) or Exit(any key)"
    reply = int(raw_input(">>> "))
    if reply == 1:
        plot()
    else:
        exit(0)

def start():
    print "Pitmon v1.0 ::: (1)Plot (0)Exit program"
    reply = int(raw_input(">>> "))
    if reply == 1:
        plot()
    elif reply == 0:
        print "Are you sure you want to exit? Retry(1) or Exit(0)"
        reply = int(raw_input(">>> "))
        if reply == 1:
            start()
        else:
            exit(0)
    else:
        print "Input incorrect, TRY AGAIN"
        start()

start()