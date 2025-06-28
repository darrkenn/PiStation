def getIndividualTemps(Readings):
    individualTemps = []
    for reading in Readings:
        if reading.temperature not in individualTemps:
            individualTemps.append(reading.temperature)
    sortedIndividualTemps = sorted(individualTemps)
    return sortedIndividualTemps

def getIndividualHumidity(Readings):
    individualHumidity = []
    for reading in Readings:
        if reading.humidity not in individualHumidity:
            individualHumidity.append(reading.humidity)
    sortedIndividualHumidity = sorted(individualHumidity)
    return sortedIndividualHumidity

def getIndividualDates(Readings):
    individualDates = []
    for reading in Readings:
        if reading.date not in individualDates:
            individualDates.append(reading.date)
    sortedIndividualDates = list(reversed(individualDates))
    return sortedIndividualDates
def getIndividualPressure(Readings):
    individualPressure = []
    for reading in Readings:
        if reading.pressure not in individualPressure:
            individualPressure.append(reading.pressure)
    sortedIndividualPressure = sorted(individualPressure)
    return sortedIndividualPressure


def getIndividualTimes(Readings):
    individualTimes = []
    for reading in Readings:
        if reading.time not in individualTimes:
            individualTimes.append(reading.time)
    sortedIndividualTimes = sorted(individualTimes)
    return sortedIndividualTimes



