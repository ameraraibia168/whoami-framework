import shodan
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "Shodan_search",
        "title"       : "Shodan search",
        "module"      : "auxiliary/gather/shodan_search",
        "description" : """
  This module uses the Shodan API to search Shodan. Accounts are free
  and an API key is required to use this module. Output from the
  module is displayed to the screen and can be saved to a file or the
  MSF database. NOTE: SHODAN filters (i.e. port, hostname, os, geo,
  city) can be used in queries, but there are limitations when used
  with a free API key. Please see the Shodan site for more
  information. Shodan website: https://www.shodan.io/ API:
  https://developer.shodan.io/api
"""
}

options ={
  "APIKEY" : [str(var.all_var['apikey']),'The SHODAN API key'],
  "SEARCH" : [str(var.all_var['search']),'Keywords you want to search for']
}

def shodan_search(search, apikey):
                                if apikey:
                                        API_KEY = apikey
                                else:
                                        API_KEY = red+'[-]'+default+'REPLACE WITH API KEY AND KEEP QUOTES'

                                api = shodan.Shodan(API_KEY)
                                ips_and_ports = []

                                # Get IPs from Shodan search results
                                try:
                                        results = api.search(search, page=1)
                                        total_results = results['total']
                                        print (blue+'[*]'+default+'Total results: {0}'.format(total_results))
                                        print (blue+'[*]'+default+'First page:')
                                        for r in results['matches']:
                                                ip = r['ip_str']
                                                port = r['port']
                                                ip_port = '{0}:{1}'.format(ip, port)
                                                print (green+' [+]'+default, ip_port)

                                except Exception as e:
                                        print (red+'[-]'+default+'Shodan search error:', e)
def running():
        try:
                search = str(var.all_var['search'])
                apikey = str(var.all_var['apikey'])
                shodan_search(search, apikey)

        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
