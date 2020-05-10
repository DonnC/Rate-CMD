'''
   @author:    Donald C
   @github:    @DonnC
   @project:   Get ZW rates
   @created:   10 May 2020
   @updated:   10 May 2020

   @source:    Data source from https://www.marketwatch.co.zw/
'''
from bs4 import BeautifulSoup as bs
import requests as req
from pprint import pprint

url = "https://www.marketwatch.co.zw/"

#print(f"[INFO] Getting data from {url}..")

def scrapeRates():
   # TODO: Add a try..except block
   resp = req.get(url)

   content = resp.content

   resp.close()

   # scrape rates and return dict of rates
   soup        = bs(content, features='html.parser')

   tb          = soup.find('div', class_='elementor-widget-wrap')

   updated     = tb.find('div', class_='elementor-shortcode')
   updatedOn   = updated.text

   # get table with rates
   table       = tb.find('table', id='tablepress-4')
   rows        = table.findAll('tr')

   data            = dict()
   data['source']  = "MARKET WATCH ZW"
   data['updated'] = updatedOn

   # source-rates repository
   rates = []

   for row in rows:
      # take each rate and its source and add to our rates repository
      data_rate   = {}
      dataSource  = row.findAll('td')
      source      = dataSource[0].text
      rate        = dataSource[1].text

      data_rate['source'] = source
      data_rate['rate']   = rate

      rates.append(data_rate)

   data['rates'] = rates

   return data

#ratesInfo = scrapeRates()

#pprint(ratesInfo)

#print("[INFO] Done")