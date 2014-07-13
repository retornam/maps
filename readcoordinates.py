import csv
import sys


def open_csvfile(filename, newfilename):
    try:
        f = open(filename, 'rb')
        r = open(newfilename, 'wb')
        reader = csv.reader(f)
        for row in reader:
            r.write("%s,%s\n" %(row[2], row[3]))
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    finally:
        f.close()
        r.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    newfilename = sys.argv[2]
    open_csvfile(filename, newfilename)