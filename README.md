# Dutch_Address
Finds (Dutch) addresses in strings. 

Examples:

`import address
zoek = address.AddressSearch("PRIO 2 TS223 KRUISPLEIN 26 ROTTERDAM WATEROVERLAST VAK: 5991200")
# address.AddressSearch will automatically download the necessary files and pickle them (= c.a. 250 MB)

zoek.find()
print(zoek.city, zoek.street, zoek.housenumber, zoek.x, zoek.y)

zoek.find('PRIO 2 WATEROVERLAST : : LELIESTRAAT : 44 HENGELO (GLD) 068541') 
print(zoek.city, zoek.street, zoek.housenumber, zoek.x, zoek.y)

# the housenumber 44 is seperated by a colon from the street 'Leliestraat'. AddresSearch only 
# accepts housenumbers adjacent to a given street. In this case it will return an x- and
# y-coordinate in (near) the middle of the street.`
