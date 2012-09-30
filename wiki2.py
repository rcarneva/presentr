from urllib2 import urlopen
from json import load,dumps
from splitpgraph import splitpgraph
import re

#def getFacts(subject):
subject = 'tiger'

for section in xrange(1,5):

  url = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=%d&titles='+subject+'&format=json'
	article = load(urlopen(url % section))

	articleID = article['query']['pages'].keys()
	articleText = article['query']['pages'][articleID[0]]['revisions'][0]['*']

	#print articleText
	unwiki = re.compile(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]')
	newText = unwiki.sub(r'\1', articleText)
	newText = re.sub('<ref.*/ref>','',newText)
	newText = re.sub('\{\{.*\}\}','',newText)
	newText = re.sub('\n',' ',newText)

	sentences = splitpgraph(newText)

	print sentences[2]

