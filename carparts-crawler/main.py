import hoser
import requests
from bs4 import BeautifulSoup
import sys

@hoser.fn
def query_parts_page(part: str):
    url = 'https://www.car-part.com/cgi-bin/search.cgi'
    with requests.Session() as session:
        session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36"}
        response = session.post(url, data={
            "ref": "",
            "sessionID": "13000000467176161",
            "iKey": "",
            "userModel": "Honda Accord",
            "userPart": part,
            "uID": "",
            "uPass": "",
            "dbPart": "327.1",
            "dbSubPart": "",
            "userLocation": "USA",
            "userPreference": "grade",
            "userPage": "1",
            "confirm_yes": "",
            "confirm_no": "",
            "iCN": "",
            "userClaim": "",
            "userClaimer": "",
            "userLang": "",
            "userZip": "",
            "userLat": "",
            "userLong": "",
            "userCSA": "",
            "userMCO": "",
            "userAdjuster": "",
            "userItem": "",
            "limitYears": "",
            "userVIN": "",
            "userVINModelID": "",
            "userIMS": "",
            "imsFullSpecification": "",
            "userInterchange": "B=@FC}}}327}59718",
            "userSearch": "int",
            "dbModel": "30.3.1.1",
            "vinSearch": "",
            "dummyVar": "B=@FC}}}327}59718", 
            "userDate": "2008",
            "userDate2": "2008",
            "Search+Car+Part+Inventory.x": "9",
            "Search+Car+Part+Inventory.y": "13",
        })

        soup = BeautifulSoup(response.content, "html.parser")
        tables = soup.body.center.findAll("table") # First table is row for labels
        sys.stderr.write(f"number of tables: {len(tables)}\n")
        listings = tables[4]
        rows = listings.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            cols = [str(ele) for ele in cols if ele]
            print(",".join(cols))


hoser.stdout = query_parts_page(part="Exhaust Manifold")
hoser.run()