import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin

__addon__ = xbmcaddon.Addon()


line0 = "Boba TV"
line1 = "Please Remeber That We Are Trying To Make The Best Iptv Provider"
line2 = "Join Our Group On Facebook To B3Connected"
line3 = "https://www.facebook.com/groups/bobatvgroup/"
line4 = "Please Click On Okay To Close This Menu!"
 
xbmcgui.Dialog().ok(line0, line1, line2, line3, line4)

def CATEGORIES():
   addDir3('Live Tv','https://entertainobc.github.io/Customers/USA.txt',3,'http://original.livestream.com/filestore/logos/6a941358-6c7f-2ebf-e8ac-b05f4f338270-banner.png','','')
   addDir3('Movies','https://entertainobc.github.io/Customers/MOVIES.txt',4,'https://www.offerpop.com/wp-content/uploads/2014/08/Movies.jpg','','')

def channel():
   r = requests.get('https://entertainobc.github.io/Customers/USA.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
def Movies():
   r = requests.get('https://entertainobc.github.io/Customers/MOVIES.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
def addLink(name,url,image,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       
#################################################################################################################

#                               NEED BELOW CHANGED

  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
     
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
elif mode==3:
        channel()
elif mode==4:
        Movies()

        


xbmcplugin.endOfDirectory(int(sys.argv[1]))
