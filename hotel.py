class Room(object):

	def __init__(self, roomNumber, beds, price, smoking, pets, handicapped):

		self.roomNumber = roomNumber
		self.beds = beds
		self.price = price
		self.smoking = smoking
		self.pets = pets
		self.handicapped = handicapped

	def getRoomNumber(self):
		return self.roomNumber

	def getBeds(self):
		return self.beds

	def getPrice(self):
		return self.price

	def getSmoking(self):
		return self.smoking

	def getHandicapped(self):
		return self.handicapped

	def __str__(self):
		return "Room Number: %s \nNumber of beds: %s \nPrice per night: $%.2f \nSmoking allowed: %s \nPets allowed: %s \nHandicapped accessible: %s" % (self.roomNumber, self.beds, self.price, self.smoking, self.pets, self.handicapped)

room3 = Room(3, 2, 199.99, False, False, True)

print(room3)