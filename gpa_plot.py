"""Plotting BUAA GPA Algorithm"""

import numpy
import matplotlib.pyplot

xlist = numpy.arange(0, 100, 0.01)
ylist = [4-(3*((100-x)**2)/1600) if x >= 60 else 0 for x in xlist]

matplotlib.pyplot.title(r"BUAA's GPA Algorithm")
matplotlib.pyplot.xlabel(r"Subject Percentile Score")
matplotlib.pyplot.ylabel(r"Subject Grade Point")
matplotlib.pyplot.plot(xlist, ylist)

matplotlib.pyplot.savefig('./gpa.png')
