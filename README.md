# Ao3-Scraper - Archivist
In progress application for webscraping Archive of Our Own Data.
#### Dependencies:
 * pandas
 * bs4
 * requests
 * time
 * Tkinter
## Current Functionality: 
  * can optionally return the following data, given an Ao3 search page URL (for every fic, on as many pages as specified)
    * ID
    * Title
    * Author
    * Date
    * fandom
    * required archive tags
    * optional tags (categorized as: warnings, relationships, characters, and tags)
    * work stats (language, word count, chapters, etc.)
  * returns a list WorkText of First Chapter texts for each ID with WorkTextScraper(WorkIds)
  * can export collected data as a CSV with proper column headers
  * Functionality Example:
    * Say you want to collect data on every She-Ra fic from the past year, but only the ones featuring catradora. at current functionality you would have to use the Ao3 search to specifiy that. then you can take the URL from the first page of results, and enter it in Archivist, while specifying which data you want (kudos, title, comments etc.) and how many pages of fics you want to scrape. then the Archivist can scrape all of that data for you, and you can have Archivist load it all into a nice CSV that you can open up in excel or whatever data tools you enjoy for your analysis.
## Future Plans:
  * Enable Scraping ALL metadata, including the name/ids of user who bookmarked or gave kudos to a work
  * Enable Scraping full fics (not just first chapter, as it does now)
  * Finish the GUI interface, currently very primitive and only a quarter-way functional
