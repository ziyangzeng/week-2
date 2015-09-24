import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "48B629DB7396C3550DCFFEB77E0472CCE71181EC00CE34322A8A8B9631632594")
db_name = "soufun"
db_username = "admin"
db_password = "admin"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit()

lat1 = 23.116176
lat2 = 23.122395

lng1 = 113.276047
lng2 = 113.286487

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'

# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.

for record in records:
    print record.price
    
sumPrice = 0
for record in records:
    sumPrice += record.price

avgPrice=str(sumPrice/numListings)

minPrice = 100000
for record in records:
    if record.price < minPrice:
        minPrice = record.price
        
maxPrice = 0
for record in records:
    if record.price > maxPrice:
        maxPrice = record.price

        
# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: '+ str(minPrice)
print 'max price: '+ str(maxPrice) 
print 'average price: '+ str(avgPrice)

client.db_close()