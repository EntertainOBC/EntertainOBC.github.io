  """ EntertainOBC Movies Addon
      Copyright (C) 2014 EntertainOBC Company

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
  """

import urlparse,sys

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')
name = params.get('name')
title = params.get('title')
year = params.get('year')
imdb = params.get('imdb')
tvdb = params.get('tvdb')
season = params.get('season')
episode = params.get('episode')
tvshowtitle = params.get('tvshowtitle')
premiered = params.get('premiered')
url = params.get('url')
image = params.get('image')
meta = params.get('meta')
select = params.get('select')
query = params.get('query')
content = params.get('content')

type = params.get('type')

kids = params.get('kids')
kids = 0 if kids == None or kids == '' else int(kids)

source = params.get('source')
if not source == None:
	from resources.lib.extensions import tools
	source = tools.Converter.dictionary(source)
	if isinstance(source, list):
		source = source[0]

metadata = params.get('metadata')
if not metadata == None:
	from resources.lib.extensions import tools
	metadata = tools.Converter.dictionary(metadata)

# LEAVE THIS HERE. Can be used by downloadsList for updating the directory list automatically in a thread.
# Stops downloader directory Updates
#if not action == 'download' and not (action == 'downloadsList' and not params.get('status') == None):
#	from resources.lib.extensions import downloader
#	downloader.Downloader.itemsStop()

# [BUBBLESCODE]
# Execute on first launch.
if action == None:
	from resources.lib.extensions import tools
	tools.System.launch()
# [/BUBBLESCODE]

if action == None or action == 'home':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).root()

elif action == 'movieNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	lite = tools.Converter.boolean(params.get('lite'))
	navigator.navigator(type = type, kids = kids).movies(lite = lite)

elif action == 'movieFavouritesNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	lite = tools.Converter.boolean(params.get('lite'))
	navigator.navigator(type = type, kids = kids).movieFavourites(lite = lite)

elif action == 'tvNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	lite = tools.Converter.boolean(params.get('lite'))
	navigator.navigator(type = type, kids = kids).tvshows(lite = lite)

elif action == 'tvFavouritesNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	lite = tools.Converter.boolean(params.get('lite'))
	navigator.navigator(type = type, kids = kids).tvFavourites(lite = lite)

elif action == 'toolNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).tools()

elif action == 'searchNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).search()

elif action == 'clearAll':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearAll()

elif action == 'clearProviders':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearProviders()

elif action == 'clearWebcache':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearWebcache()

elif action == 'clearHistory':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearHistory()

elif action == 'clearSearches':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearSearches()

elif action == 'clearDownloads':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearDownloads()

elif action == 'clearTemporary':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearTemporary()

elif action == 'clearViews':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearViews()

elif action == 'person':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).person(params.get('terms'))

elif action == 'movies':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).get(url)

elif action == 'moviePage':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).get(url)

elif action == 'movieArrivals':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).arrivals()

elif action == 'movieSearch':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).search(params.get('terms'))

elif action == 'moviePerson':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).person(params.get('terms'))

elif action == 'movieCollections':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).collections()

elif action == 'movieGenres':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).genres()

elif action == 'movieLanguages':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).languages()

elif action == 'movieCertificates':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).certifications()

elif action == 'movieAge':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).age()

elif action == 'movieYears':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).years()

elif action == 'moviePersons':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).persons(url)

elif action == 'movieUserlists':
	from resources.lib.indexers import movies
	movies.movies(type = type, kids = kids).userlists(mode = params.get('mode'))

elif action == 'channels':
	from resources.lib.indexers import channels
	channels.channels(type = type, kids = kids).get()

elif action == 'tvshows':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).get(url)

elif action == 'tvshowPage':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).get(url)

elif action == 'tvSearch':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).search(params.get('terms'))

elif action == 'tvPerson':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).person(params.get('terms'))

elif action == 'tvGenres':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).genres()

elif action == 'tvNetworks':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).networks()

elif action == 'tvCertificates':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).certifications()

elif action == 'tvAge':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).age()

elif action == 'tvPersons':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).persons(url)

elif action == 'tvUserlists':
	from resources.lib.indexers import tvshows
	tvshows.tvshows(type = type, kids = kids).userlists(mode = params.get('mode'))

elif action == 'seasons':
	from resources.lib.indexers import seasons
	seasons.seasons(type = type, kids = kids).get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
	from resources.lib.indexers import episodes
	episodes.episodes(type = type, kids = kids).get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
	from resources.lib.indexers import episodes
	episodes.episodes(type = type, kids = kids).calendar(url)

elif action == 'tvHome':
	from resources.lib.indexers import episodes
	episodes.episodes(type = type, kids = kids).home()

elif action == 'tvArrivals':
	from resources.lib.indexers import episodes
	episodes.episodes(type = type, kids = kids).arrivals()

elif action == 'tvCalendars':
	from resources.lib.indexers import episodes
	episodes.episodes(type = type, kids = kids).calendars()

elif action == 'episodeUserlists':
	from resources.lib.indexers import episodes
	episodes.episodes(type = type, kids = kids).userlists()

elif action == 'seasonUserlists':
	from resources.lib.indexers import seasons
	seasons.seasons(type = type, kids = kids).userlists()

elif action == 'seasonList':
	from resources.lib.indexers import seasons
	seasons.seasons(type = type, kids = kids).seasonList(url)

elif action == 'refresh':
	from resources.lib.modules import control
	control.refresh()

elif action == 'queueItem':
	from resources.lib.modules import control
	control.queueItem()

elif action == 'openSettings':
	from resources.lib.extensions import tools
	tools.Settings.launch(query)

elif action == 'addView':
	from resources.lib.modules import views
	views.addView(content)

elif action == 'moviePlaycount':
	from resources.lib.modules import playcount
	playcount.movies(imdb, query)

elif action == 'episodePlaycount':
	from resources.lib.modules import playcount
	playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
	from resources.lib.modules import playcount
	playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
	from resources.lib.modules import trailer
	trailer.trailer().play(name, url)

elif action == 'play':
	from resources.lib.sources import sources
	sources(type = type, kids = kids).play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
	from resources.lib.sources import sources
	sources(type = type, kids = kids).addItem()

elif action == 'playItem':
	from resources.lib.extensions import interface
	from resources.lib.sources import sources
	interface.Loader.show() # Immediately show the loader, since slow system will take long to show it in playItem().
	downloadType = params.get('downloadType')
	downloadId = params.get('downloadId')
	handleMode = params.get('handleMode')
	sources(type = type, kids = kids).playItem(source = source, metadata = metadata, downloadType = downloadType, downloadId = downloadId, handleMode = handleMode)

elif action == 'playLocal':
	import json
	from resources.lib.sources import sources
	path = params.get('path')
	downloadType = params.get('downloadType')
	downloadId = params.get('downloadId')
	sources(type = type, kids = kids).playLocal(path = path, source = source, metadata = metadata, downloadType = downloadType, downloadId = downloadId)

elif action == 'alterSources':
	from resources.lib.sources import sources
	sources(type = type, kids = kids).alterSources(url, meta)

# [BUBBLESCODE]

elif action == 'launch':
	from resources.lib.extensions import tools
	if tools.Settings.getBoolean('general.launch.automatic'):
		tools.System.execute('RunAddon(plugin.video.bubbles)')

elif action == 'systemNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).systemNavigator()

elif action == 'systemInformation':
	from resources.lib.extensions import tools
	tools.System.information()

elif action == 'systemManager':
	from resources.lib.extensions import tools
	tools.System.manager()

elif action == 'systemClean':
	from resources.lib.extensions import tools
	tools.System.clean()

elif action == 'informationNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).informationNavigator()

elif action == 'informationDebrid':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).informationDebrid()

elif action == 'informationSplash':
	from resources.lib.extensions import interface
	interface.Splash.popupFull()

elif action == 'informationChangelog':
	from resources.lib.extensions import interface
	interface.Changelog.show()

elif action == 'informationAbout':
	from resources.lib.extensions import interface
	interface.Splash.popupAbout()

elif action == 'informationDonation':
	from resources.lib.extensions import interface
	interface.Splash.popupDonation()

elif action == 'openLink':
	from resources.lib.extensions import tools
	link = params.get('link')
	tools.System.openLink(link)

elif action == 'copyLink':
	from resources.lib.extensions import interface
	from resources.lib.extensions import clipboard
	from resources.lib.extensions import network
	from resources.lib.extensions import tools
	try:
		interface.Loader.show() # Needs some time to load. Show busy.
		if 'link' in params:
			link = params.get('link')
		elif 'source' in params:
			link = source['url']
			if 'resolve' in params and tools.Converter.boolean(params.get('resolve')):
				if 'urlresolved' in source:
					link = source['urlresolved']
				else:
					from resources.lib.extensions import network
					link = network.Networker().resolve(source, clean = True)
			if not link: # Sometimes resolving does not work. Eg: 404 errors.
				link = source['url']
			link = network.Networker(link).link() # Clean link
		clipboard.Clipboard.copyLink(link, True)
	except:
		pass
	interface.Loader.hide()

elif action == 'copyClipboard':
	from resources.lib.extensions import interface
	from resources.lib.extensions import clipboard
	try:
		interface.Loader.show() # Needs some time to load. Show busy.
		clipboard.Clipboard.copy(params.get('value'), True)
	except:
		pass
	interface.Loader.hide()

elif action == 'showDetails':
	from resources.lib.modules import extras
	from resources.lib.extensions import interface
	try:
		interface.Loader.show() # Needs some time to load. Show busy.
		extras.Metadata.showDialog(source = source, metadata = metadata)
	except:
		pass
	interface.Loader.hide()

elif action == 'verificationProviders':
	from resources.lib.modules import extras
	extras.Verification().verifyProviders()

elif action == 'verificationAccounts':
	from resources.lib.modules import extras
	extras.Verification().verifyAccounts()

elif action == 'verificationNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).verificationNavigator()

elif action == 'favouritesNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).favouritesNavigator()

elif action == 'arrivalsNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).arrivalsNavigator()

elif action == 'clearNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).clearNavigator()

elif action == 'traktmoviesNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).traktmovies()

elif action == 'traktmovieslistsNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).traktmovieslists()

elif action == 'imdbmoviesNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).imdbmovies()

elif action == 'trakttvNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).trakttv()

elif action == 'trakttvlistsNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).trakttvlists()

elif action == 'imdbtvNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).imdbtv()

elif action == 'moviesCategories':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).moviesCategories()

elif action == 'moviesLists':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).moviesLists()

elif action == 'moviesPeople':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).moviesPeople()

elif action == 'moviesSearchNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).moviesSearchNavigator()

elif action == 'tvCategories':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).tvCategories()

elif action == 'tvLists':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).tvLists()

elif action == 'tvPeople':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).tvPeople()

elif action == 'tvSearchNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).tvSearchNavigator()

elif action == 'tvYears':
	from resources.lib.indexers import tvshows
	tvshows.tvshows().years()

elif action == 'tvLanguages':
	from resources.lib.indexers import tvshows
	tvshows.tvshows().languages()

elif action == 'searchRecent':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).searchRecent()

elif action == 'searchRecentMovies':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).searchRecentMovies()

elif action == 'searchRecentShows':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).searchRecentShows()

elif action == 'cacheItem':
	from resources.lib.sources import sources
	handleMode = params.get('handleMode')
	sources(type = type, kids = kids).cacheItem(source = source, metadata = metadata, handleMode = handleMode)

####################################################
# PROVIDERS
####################################################

elif action == 'providersNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).providersNavigator()

elif action == 'providersSettings':
	from resources.lib.extensions import tools
	tools.Settings.launch(2)

elif action == 'providersSort':
	from resources.lib.extensions import provider
	mode = params.get('mode')
	slot = params.get('slot')
	provider.Provider.sortDialog(mode = mode, slot = slot)

elif action == 'providersPreset':
	from resources.lib.extensions import provider
	slot = params.get('slot')
	provider.Provider.presetDialog(slot = slot)

####################################################
# ACCOUNTS
####################################################

elif action == 'accountsNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).accountsNavigator()

elif action == 'accountsPremiumize':
	from resources.lib.extensions import debrid
	debrid.PremiumizeInterface().account()

elif action == 'accountsRealDebrid':
	from resources.lib.extensions import debrid
	debrid.RealDebridInterface().account()

elif action == 'accountsSettings':
	from resources.lib.extensions import tools
	tools.Settings.launch(3)

####################################################
# DOWNLOADS
####################################################

elif action == 'download':
	try:
		import json
		from resources.lib.sources import sources
		from resources.lib.extensions import downloader
		from resources.lib.extensions import interface
		from resources.lib.extensions import tools
		interface.Loader.show()
		downloadType = params.get('downloadType')
		downloadId = params.get('downloadId')
		refresh = tools.Converter.boolean(params.get('refresh'))
		downer = downloader.Downloader(downloadType)
		if downloadId == None:
			image = params.get('image')
			handleMode = params.get('handleMode')
			link = sources(type = type, kids = kids).sourcesResolve(source, info = True, internal = False, download = True, handleMode = handleMode)
			if link == None:
				interface.Loader.hide()
			else:
				title = tools.Media.title(type = type, metadata = metadata)
				downer.download(media = type, title = title, link = link, image = image, metadata = metadata, source = source, refresh = refresh)
		else:
			downer.download(id = downloadId, forceAction = True, refresh = refresh)
	except:
		pass

elif action == 'downloadDetails':
	from resources.lib.extensions import downloader
	downloadType = params.get('downloadType')
	downloadId = params.get('downloadId')
	downloader.Downloader(type = downloadType, id = downloadId).details()

elif action == 'downloads':
	from resources.lib.indexers import navigator
	downloadType = params.get('downloadType')
	navigator.navigator(type = type, kids = kids).downloads(downloadType)

elif action == 'downloadsManager':
	from resources.lib.extensions import downloader
	downer = downloader.Downloader(downloader.Downloader.TypeManual)
	downer.items(status = downloader.Downloader.StatusAll, refresh = False)

elif action == 'downloadsBrowse':
	from resources.lib.indexers import navigator
	downloadType = params.get('downloadType')
	downloadError = params.get('downloadError')
	navigator.navigator(type = type, kids = kids).downloadsBrowse(downloadType, downloadError)

elif action == 'downloadsList':
	downloadType = params.get('downloadType')
	downloadStatus = params.get('downloadStatus')
	if downloadStatus == None:
		from resources.lib.indexers import navigator
		navigator.navigator(type = type, kids = kids).downloadsList(downloadType)
	else:
		from resources.lib.extensions import downloader
		downer = downloader.Downloader(downloadType)
		# Do not refresh the list using a thread. Seems like the thread is not always stopped and then it ends with multiple threads updating the list.
		# During the update duration multiple refreshes sometimes happen due to this. Hence, you will see the loader flash multiple times during the 10 secs.
		# Also, with a fresh the front progress dialog also flashes and reset it's focus.
		#downer.items(status = status, refresh = True)
		downer.items(status = downloadStatus, refresh = False)

elif action == 'downloadsClear':
	downloadType = params.get('downloadType')
	downloadStatus = params.get('downloadStatus')
	if downloadStatus == None:
		from resources.lib.indexers import navigator
		navigator.navigator(type = type, kids = kids).downloadsClear(downloadType)
	else:
		from resources.lib.extensions import downloader
		downer = downloader.Downloader(downloadType)
		downer.clear(status = downloadStatus)

elif action == 'downloadsRefresh':
	from resources.lib.extensions import downloader
	downloadType = params.get('downloadType')
	downer = downloader.Downloader(downloadType)
	downer.itemsRefresh()

elif action == 'downloadsSettings':
	from resources.lib.modules import control
	from resources.lib.extensions import tools
	tools.Settings.launch(7)

####################################################
# LIGHTPACK
####################################################

elif action == 'lightpackNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).lightpackNavigator()

elif action == 'lightpackSwitchOn':
	from resources.lib.extensions import tools
	tools.Lightpack().switchOn(message = True)

elif action == 'lightpackSwitchOff':
	from resources.lib.extensions import tools
	tools.Lightpack().switchOff(message = True)

elif action == 'lightpackAnimate':
	from resources.lib.extensions import tools
	force = params.get('force')
	force = True if force == None else tools.Converter.boolean(force)
	tools.Lightpack().animate(force = force, message = True, delay = True)

elif action == 'lightpackSettings':
	from resources.lib.extensions import tools
	tools.Settings.launch(9)

####################################################
# KIDS
####################################################

elif action == 'kidsLock':
	from resources.lib.extensions import tools
	tools.Kids.lock()

elif action == 'kidsUnlock':
	from resources.lib.extensions import tools
	tools.Kids.unlock()

elif action == 'kidsNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).kidsNavigator()

####################################################
# DOCUMENTARIES
####################################################

elif action == 'documentariesNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	navigator.navigator(type = tools.Media.TypeDocumentary, kids = kids).movies()

####################################################
# SHORTS
####################################################

elif action == 'shortsNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	navigator.navigator(type = tools.Media.TypeShort, kids = kids).movies()

####################################################
# SERVICES
####################################################

elif action == 'servicesNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).servicesNavigator()

####################################################
# PREMIUMIZE
####################################################

elif action == 'premiumizeNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).premiumizeNavigator()

elif action == 'premiumizeDownloadsNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	lite = tools.Converter.boolean(params.get('lite'))
	navigator.navigator(type = type, kids = kids).premiumizeDownloadsNavigator(lite = lite)

elif action == 'premiumizeList':
	from resources.lib.extensions import interface
	interface.Dialog.confirm(title = 'Planned Feature', message = 'This feature is planned for a future release. It will allow users to fully utilize Premiumize functionality, such as manually adding downloads, deleting and moving files, and downloading files to local storage.')

elif action == 'premiumizeInformation':
	from resources.lib.extensions import debrid
	debrid.PremiumizeInterface().downloadInformation()

elif action == 'premiumizeAccount':
	from resources.lib.extensions import debrid
	debrid.PremiumizeInterface().account()

elif action == 'premiumizeClear':
	from resources.lib.extensions import debrid
	debrid.PremiumizeInterface().clear()

elif action == 'premiumizeSettings':
	from resources.lib.extensions import tools
	tools.Settings.launch(3)

####################################################
# REALDEBRID
####################################################

elif action == 'realdebridAuthentication':
	from resources.lib.extensions import debrid
	debrid.RealDebridInterface().accountAuthentication()

elif action == 'realdebridNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).realdebridNavigator()

elif action == 'realdebridDownloadsNavigator':
	from resources.lib.indexers import navigator
	from resources.lib.extensions import tools
	lite = tools.Converter.boolean(params.get('lite'))
	navigator.navigator(type = type, kids = kids).realdebridDownloadsNavigator(lite = lite)

elif action == 'realdebridList':
	from resources.lib.extensions import interface
	interface.Dialog.confirm(title = 'Planned Feature', message = 'This feature is planned for a future release. It will allow users to fully utilize RealDebrid functionality, such as manually adding downloads, deleting and moving files, and downloading files to local storage.')

elif action == 'realdebridInformation':
	from resources.lib.extensions import debrid
	debrid.RealDebridInterface().downloadInformation()

elif action == 'realdebridAccount':
	from resources.lib.extensions import debrid
	debrid.RealDebridInterface().account()

elif action == 'realdebridClear':
	from resources.lib.extensions import debrid
	debrid.RealDebridInterface().clear()

elif action == 'realdebridSettings':
	from resources.lib.extensions import tools
	tools.Settings.launch(3)

####################################################
# QUASAR
####################################################

elif action == 'quasarNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).quasarNavigator()

elif action == 'quasarConnect':
	from resources.lib.extensions import tools
	tools.Quasar.connect(confirm = True)

elif action == 'quasarInstall':
	from resources.lib.extensions import tools
	tools.Quasar.install(confirm = True)

elif action == 'quasarLaunch':
	from resources.lib.extensions import tools
	tools.Quasar.launch()

elif action == 'quasarInterface':
	from resources.lib.extensions import tools
	tools.Quasar.interface()

elif action == 'quasarSettings':
	from resources.lib.extensions import tools
	tools.Quasar.settings()

####################################################
# URLRESOLVER
####################################################

elif action == 'urlresolverNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).urlresolverNavigator()

elif action == 'urlresolverSettings':
	try:
		import urlresolver
		urlresolver.display_settings()
	except: pass

####################################################
# SPEEDTEST
####################################################

elif action == 'speedtestNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator().speedtestNavigator()

elif action == 'speedtest':
	from resources.lib.extensions import speedtest
	speedtest.SpeedTester.select(params.get('update'))

elif action == 'speedtestGlobal':
	from resources.lib.extensions import speedtest
	speedtest.SpeedTesterGlobal().show(params.get('update'))

elif action == 'speedtestPremiumize':
	from resources.lib.extensions import speedtest
	speedtest.SpeedTesterPremiumize().show(params.get('update'))

elif action == 'speedtestRealDebrid':
	from resources.lib.extensions import speedtest
	speedtest.SpeedTesterRealDebrid().show(params.get('update'))

####################################################
# VIEWS
####################################################

elif action == 'viewsNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).viewsNavigator()

elif action == 'viewsCategoriesNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).viewsCategoriesNavigator()

elif action == 'views':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).views(content = params.get('content'))

####################################################
# HISTORY
####################################################

elif action == 'historyNavigator':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).historyNavigator()

elif action == 'historyType':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).historyType()

elif action == 'historyStream':
	from resources.lib.indexers import navigator
	navigator.navigator(type = type, kids = kids).historyStream()

####################################################
# TRAKT
####################################################

elif action == 'traktManager':
	from resources.lib.modules import trakt
	from resources.lib.extensions import tools
	refresh = params.get('refresh')
	if refresh == None: refresh = True
	else: refresh = tools.Converter.boolean()
	trakt.manager(imdb = imdb, tvdb = tvdb, season = season, episode = episode, refresh = refresh)

elif action == 'traktAuthorize':
	from resources.lib.modules import trakt
	trakt.authTrakt()

elif action == 'traktListAdd':
	from resources.lib.modules import trakt
	trakt.listAdd()
