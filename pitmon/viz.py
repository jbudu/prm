import matplotlib.pyplot as plt

class viz(object):
    """Preparing plots and visualizing"""
    def __init__(self, *args, **kwargs):
        return super(viz, self).__init__(*args, **kwargs)

    def make_plot(self, dates, pt1, pt2, pt3, title):
        fig = plt.figure()
        nor = plt.plot_date(dates, pt1, "bo")
        eas = plt.plot_date(dates, pt2, "go")
        ele = plt.plot_date(dates, pt3, "ro")
        fig.autofmt_xdate()
        #plt.legend((nor, eas, ele), ('Northing', 'Easting', 'Reduced Level'), loc='upper right')
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Differential displacement")
        return plt.show()