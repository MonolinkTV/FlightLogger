from typing import List
from datetime import datetime
import json
import os


class InvalidJson(Exception):
	def __init__(self, path: str, _type: str, entry: str):
		self.path = path
		self.type = _type
		self.entry = entry

	def __str__(self):
		return f"InvalidJson: {self.type} at '{self.path}' for '{self.entry}'"


class Entry:
	def __init__(self, fromAirport: str, toAirport: str, aircraft: str, date=datetime.now()):
		self.fromAirport = fromAirport
		self.toAirport = toAirport
		self.aircraft = aircraft
		self.date = date

	def __str__(self):
		return f"<Entry: from={self.fromAirport}, to={self.toAirport}, in={self.aircraft}>"

	def toJson(self):
		return {
			"dateOrdinal": self.date.toordinal(),
			"fromAirport": self.fromAirport,
			"toAirport": self.toAirport,
			"aircraft": self.aircraft
		}

	@classmethod
	def fromJson(cls, data: dict, path="<Entry>"):
		date = datetime.now()
		if "dateOrdinal" in data:
			date = datetime.fromordinal(data["dateOrdinal"])
		if "fromAirport" in data:
			fromAirport = data["fromAirport"]
		else:
			raise InvalidJson(path, "MISSING", "fromAirport")
		if "toAirport" in data:
			toAirport = data["toAirport"]
		else:
			raise InvalidJson(path, "MISSING", "toAirport")
		if "aircraft" in data:
			aircraft = data["aircraft"]
		else:
			raise InvalidJson(path, "MISSING", "aircraft")
		return cls(fromAirport, toAirport, aircraft, date=date)


class SaveData:
	def __init__(self, **kwargs):
		self.entries: List[Entry] = kwargs.get("entries", [])

	def __str__(self):
		return f"<SaveData: entryCount={len(self.entries)}>"

	def addEntry(self, entry: Entry):
		self.entries.append(entry)

	def toJson(self):
		return {
			"entries": [entry.toJson() for entry in self.entries]
		}

	@classmethod
	def fromJson(cls, data: dict, path="<SaveData>"):
		entries = []
		if "entries" in data:
			for entry in data["entries"]:
				entries.append(Entry.fromJson(entry, path))
		return cls(entries=entries)

	def save(self):
		# we use `dataStr` to not have the file open when processing data
		dataStr = json.dumps(self.toJson())
		with open("save.json", "w") as f:
			f.write(dataStr)

	@classmethod
	def load(cls):
		if os.path.isfile("save.json"):
			with open("save.json", "r") as f:
				# we use `dataStr` to not have the file open when processing data
				dataStr = f.read()
			data = json.loads(dataStr)
			return cls.fromJson(data)
		return cls()
