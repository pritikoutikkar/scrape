import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, "html.parser")

# Find the "Search Postings" heading
postings_heading = soup.find("h2", text="Search Postings")

# Find the table containing the postings
table = postings_heading.find_next("table")

# Find all the rows in the table
rows = table.find_all("tr")

# Iterate over the rows and extract the desired fields for the first 5 postings
postings = []
for row in rows[1:6]:  # Exclude the header row
    columns = row.find_all("td")
    est_value_notes = columns[0].text.strip()
    description = columns[1].text.strip()
    closing_date = columns[2].text.strip()
    postings.append({
        "Est. Value Notes": est_value_notes,
        "Description": description,
        "Closing Date": closing_date
    })

# Print the list of postings
for posting in postings:
    print(posting)
