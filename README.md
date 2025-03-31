# Wikipedia Poets Analysis

## Overview
This project aims to analyze French poets by retrieving data from Wikidata and Wikipedia. It gathers information about their works, literary movements, and popularity based on Wikipedia page views. Additionally, it builds a network graph showing connections between poets based on Wikipedia page links.

## Features
- **Wikipedia Page Views:** Uses the Wikimedia API to get the number of views for each poet's Wikipedia page.
- **Wikidata Query:** Fetches poets' names, birth/death dates, works, and literary movements.
- **Data Filtering:** Identifies poets who primarily wrote in French.
- **Data Visualization:** 
  - Pie charts for literary movement distribution.
  - Bar charts for poet deaths by decade.
- **Network Graph:** 
  - Extracts links between poets from Wikipedia.
  - Saves relationships as a CSV file.
  - Visualizes the graph using NetworkX and PyVis.

## Technologies Used
- **Python Libraries:** 
  - `requests` for API calls
  - `SPARQLWrapper` for Wikidata queries
  - `pandas` for data manipulation
  - `matplotlib` and `plotly` for visualization
  - `networkx` and `pyvis` for graph visualization
  - `wikipedia-api` for extracting links
- **Data Sources:**
  - Wikimedia API for page views
  - Wikidata SPARQL endpoint for poet metadata
  - Wikipedia API for page links

## How It Works
1. **Retrieve Data:** 
   - Query Wikidata for French poets.
   - Fetch their Wikipedia page views.
   - Filter by popularity (views > 10,000).
2. **Process Data:** 
   - Normalize names.
   - Identify poets primarily writing in French.
   - Extract relationships from Wikipedia page links.
3. **Generate Outputs:** 
   - Save poet data as `data_frenchpoet.json`.
   - Save poet relationships as `links.csv`.
   - Visualize movement distribution and poet connections.

## Usage
1. Install dependencies:
   ```sh
   pip install requests SPARQLWrapper pandas matplotlib plotly networkx pyvis wikipedia-api
   ```
2. Run the main script:
   ```sh
   python main.py
   ```
3. View outputs:
   - JSON files containing poet data.
   - CSV file of poet connections.
   - Graphs showing literary movements and poet networks.

## Future Improvements
- Enhance poet classification with a more robust NLP model.
- Expand the network analysis by incorporating citation data.
- Add an interactive web-based visualization for better exploration.

## Contributors
- Nafru

