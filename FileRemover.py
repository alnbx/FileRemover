import os
import sys
import time
import argparse

def removeFiles(filesListPath, deleteFileFromDirectory):
    path = str(deleteFileFromDirectory)
    file = str(filesListPath)
    originalPath = path[:]
    #print("path: %s" % path)

    with open(file) as fp:
        line = fp.readline()
        while line:
            fullPath = path + "\\" + line
            if fullPath.find('\n'):
                fullPath = fullPath[:-1]
            line = fp.readline()

            if os.path.isfile(fullPath):
                os.remove(fullPath)
            else:
                print 'file {} does not exists in the directory {}'.format(line, originalPath)
            path = originalPath[:]

def main(filesListPath, deleteFileFromDirectory):
    removeFiles(filesListPath, deleteFileFromDirectory)
  
if __name__ == "__main__":

    desc = '''Please provide 2 argument:
        [1] Path to the file containing a list of files you want to delete
        [2] Path to the directory containing the files you want to delete'''

    parser = argparse.ArgumentParser(description='Program to delete file using a list.\n\n', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("fileList",  type=str, help="Path to the file containing a list of files you want to delete")
    parser.add_argument("Directory", type=str, help="Path to the directory containing the files you want to delete")
    args = parser.parse_args()
    #print (args)

    argLen = len(sys.argv)
    if argLen != 3:
        print("You need to provide two argument. You provided: %d" % len(sys.argv))
        print (desc)
        sys.exit(1)

    else:
        main(sys.argv[1], sys.argv[2])
