import urllib2
import httplib
import json
import serial
#import urllib2


mega = serial.Serial('/dev/ttyACM0')
mega.baudrate = 9600

nano = serial.Serial('/dev/ttyUSB0')
nano.baudrate = 9600
temp = ''

while True:
	ch = nano.read(1)
	if ch =='\n':
	  print 'nilai sensor ='
	  print temp
	  conn = httplib.HTTPConnection('api.thingspeak.com')
	  conn.request("GET", "https://api.thingspeak.com/update?api_key=AJC99AJMLNSZA28C&field1=%s\n"%(temp))
	  conn.close()
	  download = urllib2.urlopen("https://api.thingspeak.com/channels/205467/feeds/last.json?api_key=AJC99AJMLNSZA28")
          response = download.read()
	  #tes=download.getcode()
          data=json.loads(response)
	  print 'data diterima ='
          print data['field1']#,data['created_at']
          mega.write(data['field1'])
          mega.write('\n')
          #mega.write('\n')
	  temp = ''
	else:
	  temp += ch

	
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           #% (CHANNEL_ID,READ_API_KEY))
       
