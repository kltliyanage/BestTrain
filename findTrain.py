import pathFind
def findTrain(startStation, endStation):
    path=findPath(startStation,endStation)
    express=findExpree(path);
    
    
    for i in express:
       findQuickestTrainTo