from geojson import Feature, Point,FeatureCollection
import csv
import sys
import json


def open_csvfile(filename, newfilename):
    try:
        f = open(filename, 'rb')
        r = open(newfilename, 'wb')
        reader = csv.reader(f)
        features =[]
        for row in reader:
            #coordinate data is from google maps to mapbox 
            #we need to flip the x and y coordinates
            x  = float(row[2])
            y= float(row[3])
            features.append(Feature(geometry=Point((y, x))))
        json.dump(FeatureCollection(features),r)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    finally:
        f.close()
        r.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    newfilename = sys.argv[2]
    open_csvfile(filename, newfilename)