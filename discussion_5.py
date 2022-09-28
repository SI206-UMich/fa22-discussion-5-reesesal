import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for letter in sentence:
		if letter == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		if len(self.items) == 0:
			return None
		maxItem = None
		maxQuantity = 0
		for item in self.items:
			currentQuantity = self.items.count(item)
			if currentQuantity > maxQuantity:
				maxQuantity = currentQuantity
				maxItem = item
		return maxItem
		pass
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("pizza"), 1, "Pizza")
		self.assertEqual(count_a("zazazazaa"), 5, "zazazazaa")
		self.assertEqual(count_a(""), 0, "empty string")
		self.assertEqual(count_a("nothing"), 0, "nothing")
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse1 = Warehouse()
		self.warehouse1.add_item(self.item3)
		self.assertEqual(self.item3 in self.warehouse1.items, True, "item 3 in warehouse 1")
		self.assertEqual(self.item4 in self.warehouse1.items, False, "item 4 in warehouse 1")

		self.warehouse2 = Warehouse()
		self.assertEqual(self.item1 in self.warehouse2.items, False, "item 1 in warehouse 2")
		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.warehouse1 = Warehouse()
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item1)

		self.warehouse1.add_item(self.item2)
		self.warehouse1.add_item(self.item2)
		self.assertEqual(self.warehouse1.get_max_stock(), self.item1, "item 1 is max")

		self.warehouse2 = Warehouse()
		self.assertEqual(self.warehouse2.get_max_stock(), None, "empty warehouse")
		self.warehouse2.add_item(self.item3)
		self.assertEqual(self.warehouse2.get_max_stock(), self.item3, "item 3 is max")
		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()