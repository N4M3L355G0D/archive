SORT='priceasc'
AVAILABILITY_MODE='0'
#mode 0 - immediately
#mode 1 - available in 30 days
#mode 2 - available beyond 30 days
MIN_COST='600'
ZIPCODE='93933'

URL="https://monterey.craigslist.org/search/roo?sort=""$SORT""&availabilityMode=""$AVAILABILITY_MODE""&min_price=""$MIN_COST""&postal=""$ZIPCODE"

CMD="firefox $URL"

$CMD 
