from dataManagement import SaveData, Entry


# create new data
newData = SaveData()
# add an entry
newData.addEntry(Entry(
	fromAirport="LUK",
	toAirport="LUK",
	aircraft="TB10"
))
# save the data to `save.json` in the current working directory
newData.save()

# load `save.json` from the current working directory
loadedData = SaveData.load()
# print the json version of the loaded data (also used by SaveData.save())
print(loadedData.toJson())
