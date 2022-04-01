def totalCost(times, shutdown):
    shutdownArr = shutdown.split(":")
    totalCost = 0
    sDMin = (int(shutdownArr[0]) * 60) + int(shutdownArr[1])
    for time in times:
        splitTime = time.split(":")
        mins = sDMin - (int(splitTime[0]) * 60) + int(splitTime[1]) 
        totalCost += mins
    return totalCost

startupTimes = ["12:30", "14:00", "19:55"]
shutDownTime = "20:00"
print(totalCost(startupTimes, shutDownTime))
#total cost is $1 per minute