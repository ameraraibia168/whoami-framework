import time,requests
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "ip_number",
        "title"       : "Get information about the IP",
        "module"      : "network/info/ip_number",
        "description" : "  Get information about the IP"
}

options ={
  "ip" : [str(var.ip[0]),'{Ip/Url} target']
}

def running():
        try:
                print ('')
                time.sleep(0.01)
                print (light_blue +'[...] Searching for ' + basic_yellow + var.ip[0] )
                print ('')
                request = requests.get('http://ip-api.com/json/'+var.ip[0])
                data = request.json()
                print (green + 'Advanced Information')
                print (basic_green + 'Lat           :      ' + white + str(data['lat']) )
                print (basic_green + 'Lon           :      ' + white + str(data['lon']) )
                print (basic_green + 'Coord         :      ' + white + str(data['lat']) + ',' + str(data['lon']))
                print (basic_green + 'Google Maps   :      ' + white + 'https://www.google.com.br/maps/place/' + str(data['lat']) + ',' + str(data['lon']) )
                print ('')
                print (green + 'Basic Information')
                print (basic_green + 'Country       :      ' + white + data['country'] + '[' + data['countryCode'] + ']' )
                print (basic_green + 'City          :      ' + white + data['city'] + ' - ' + data['region'] + ' - {' + data['regionName'] + '}'  )
                print (basic_green + 'Timezone      :      ' + white + data['timezone'] )
                print (basic_green + 'Zip           :      ' + white + data['zip'] )
                print ('')
                print (green + 'Internet Information')
                print (basic_green + 'ISP           :      ' + white + data['isp'] )
                print (basic_green + 'Org           :      ' + white + data['as'] )
                print ('')
                time.sleep(2)
                print (basic_yellow + '[*] Done ')
                print ('')

        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
