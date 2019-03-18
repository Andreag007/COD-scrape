# COD-scrape

For this project, I wanted to successfully scrape The Call of Duty World League official page for the player tags and names. With this, I then wanted to scrape the Call of Duty esports wikipedia page to figure out the achievements of such players. With all of this information, I wanted to make it into a .txt file where you could easily see the Players, their player tags, and their achievements that they have accomplished in competitive Call of Duty. 

For this, I had to use Selenium to scrape the player tags and names because it was not scrapable without it. Second, I had to get the URLs from the Wikipedia page and then dig into each one to get the achievements. These two steps would give me the information that I needed from each pages.

While it seemed like 3 easy steps for me at the time, I was not able to extract more than 5 URLs. Since the information was on a table, it started to give me integers. After various googling, I was able to exctract 5 but not much else. With the Selenium, I tried to make it click the button 'View Roster' but at the end, was not able to find the CSS marker and failed with that too. 
