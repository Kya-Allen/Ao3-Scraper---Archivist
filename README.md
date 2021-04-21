# Ao3-Scraper - Archivist
In progress module for webscraping Archive of Our Own Data.
#### Dependencies:
 * pandas
 * bs4
 * requests
 * time
## Current Functionality: 
  * returns a list WorkIds given a URL and page=[number of pages] as arguments to PageScraperID()
  * returns a list WorkText of First Chapter texts for each ID with WorkTextScraper(WorkIds)
## Future Plans:
  * Enable Scraping All metadata from a given fic (Kudos, tags, etc.)
  * Enable Scraping full fics (not just first chapter, as it does not)
  * Productionize a browser extension with a simple UI to allow non less technical users to set parameters, scrape, and download a csv in browser
