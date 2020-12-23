from datetime import datetime

def gcLogSplit(sourceFile,outPath,fileLines):
    lineCount = 0
    validCount = 0
    fileIndex = 0
    title = {}
    filePrefix = sourceFile.split("/")[-1]
    f = open(sourceFile,'r')
    lines = f.readlines()
    f.close()

    # 1.找出表头
    for line in lines:
        if line.startswith("2020-"):
            break
        title[lineCount] = line
        lineCount += 1

    f = open(outPath + filePrefix + "_" + str(fileIndex) + ".txt", "w")
    for line in lines:
        if line.startswith("2020-"):
            validCount += 1
            # 2.填充title
            if validCount % fileLines == 1:
                # 换文件
                f = open(outPath + filePrefix + "_" + str(fileIndex) + ".txt", "w")
                for s in title:
                    f.write(title[s])
                fileIndex += 1

            f.write(line)
        else:
            f.write(line)


#大文本拆分为小文本
def textSplit(sourceFile,outPath,fileLines):
    lineCount = 0
    validCount = 0
    filePrefix = sourceFile.split("/")[-1]
    fileIndex = 0

    f = open(sourceFile,"r")
    lines = f.readlines()
    f.close()

    f = open(outPath + filePrefix + "_" + str(fileIndex) + ".txt", "w")
    for line in lines:
        lineCount += 1
        if len(line) > 5:
            validCount += 1
            if validCount % fileLines == 1:
                # 换文件
                f = open(outPath + filePrefix + "_" + str(fileIndex) + ".txt", "w")
                fileIndex += 1
            f.write(line)
    print("lineCount:", lineCount, ",validCount:", validCount)


if __name__ == "__main__":
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # 拆分gcLog，原文件路径、结果文件夹、有效gc日志数量是10w(非文档行数)：
    sourceFile = 'C:/Users/xiongxiaoyu/Desktop/gcopt/23_stock_c4.log'
    outPath = 'C:/Users/xiongxiaoyu/Desktop/gcopt/stock/'
    fileLines = 100000
    gcLogSplit(sourceFile,outPath,fileLines)


    # txt大文件按照行数拆小，原文件路径、结果文件夹、每个文件行数：
    # sourceFile = 'C:/Users/xiongxiaoyu/Desktop/c3c4 gclog 11.5-11.11/666test.txt'
    # outPath = 'C:/Users/xiongxiaoyu/Desktop/c3c4 gclog 11.5-11.11/sss/'
    # fileLines = 5
    # textSplit(sourceFile,outPath,fileLines)


    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


