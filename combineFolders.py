import os
import shutil

def extractor5000(rootDir, copyDir, prefix=None):

    count = 1
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            srcFile = os.path.join(dirName, fname)
            dstFile = os.path.join(copyDir, fname)
            if prefix!=None:
                dstFile = os.path.join(copyDir, prefix+"_"+fname)
            print str(count)+". Copying File "+srcFile+" as "+dstFile+" ..."
            shutil.copy2(srcFile, dstFile)
            count += 1

if __name__ == '__main__':
    extractor5000('./bbc/business','./corpus', 'biz')
    extractor5000('./bbc/entertainment','./corpus', 'ent')
    extractor5000('./bbc/politics','./corpus', 'pol')
    extractor5000('./bbc/sport','./corpus', 'sport')
    extractor5000('./bbc/tech','./corpus', 'tech')