# In command window, pip install requests, then pip install bs4, and then pip install matplotlib
import requests
from bs4 import BeautifulSoup

def print_unicode_grid_from_html(doc_url: str) -> None:
    """
    Fetches a published Google Doc as HTML, extracts a table whose rows contain:
        x-coordinate | character | y-coordinate
    Builds and prints a 2D grid with uppercase characters placed at (x, y).
    """

    # Fetch the HTML content of the published Google Doc
    response = requests.get(doc_url)
    response.raise_for_status()
    html = response.text

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find all table rows
    rows = soup.find_all("tr")
    if not rows:
        raise ValueError("No table found in the Google Doc HTML.")

    entries = []

    # Parse each row of the table
    for row in rows:
        cells = row.find_all("td")
        if len(cells) != 3:
            continue  # skip malformed rows

        try:
            x = int(cells[0].get_text(strip=True))
            char = cells[1].get_text(strip=True).upper()
            y = int(cells[2].get_text(strip=True))
            entries.append((x, char, y))
        except ValueError:
            # Skip rows that don't contain valid numeric coordinates
            continue

    if not entries:
        raise ValueError("No valid (x, char, y) rows found in the table.")

    # Determine grid size
    max_x = max(x for x, _, _ in entries)
    max_y = max(y for _, _, y in entries)

    # Create empty grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters
    for x, char, y in entries:
        grid[y][x] = char

    # Print the final graphic
    for row in grid:
        print("".join(row))

print_unicode_grid_from_html("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")