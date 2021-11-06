import zipfile
import re 
import os
import random
import string
import shutil
import sys
#from urlextract import URLExtract

print("-----------------------------------------------------------------------------------")
print("File name: "+sys.argv[1])
print("-----------------------------------------------------------------------------------")
print("")
print("")
print("")


common_domains=["schemas.openxmlformats.org", "www.w3.org", "schemas.microsoft.com"]
suspicious_keywords=['ole']


letters = string.ascii_lowercase
random_string=''.join(random.choice(letters) for i in range(10))
 
fantasy_zip = zipfile.ZipFile(sys.argv[1])
fantasy_zip.extractall('extract_temp\\'+random_string+"\\")
fantasy_zip.close()


path = 'extract_temp\\'+random_string+"\\"


files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
	for file in f:
		files.append(os.path.join(r, file))

domains=[]

unusual_urls=[]
suspicious_urls=[]
for f in files:
	current_urls=[]
	fp=open(f, "rb")
	content=fp.read()
	content=content.decode('latin1')


	#m = re.findall('"(http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"', content)
	
	m = re.findall('([a-zA-Z]+://[^"<\'\s]+)', content)
	
	#m = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", content)
	#'''
	#extractor=URLExtract()
	#m=extractor.find_urls(content)


	print("======= "+f.split(random_string)[1]+" =======")
	for url in m:
		url=url.encode('latin1')
		url=url.decode('utf-8')
		if url not in current_urls:
			current_urls.append(url)
			print(url)
			try:
				domain=url.split("//")[1].split("/")[0]
			except:
				domain=url
			if domain not in domains:
				domains.append(domain)
			if domain not in common_domains:
				unusual_urls.append((f, url))
			for word in suspicious_keywords:
				if word in url:
					suspicious_urls.append((f, url))
					unusual_urls.append((f, url))
			
		

	print("")
	fp.close()

print("delete temporary files.")
print(os.path.abspath(path))
shutil.rmtree(path)

print("++++++++++++++++++++++ found domains ++++++++++++++++++++++")
for domain in domains:
	print(domain)
print("++++++++++++++++++++++ found domains ++++++++++++++++++++++")



if len(unusual_urls) != 0:
	print("\n\n\n")
	print("++++++++++++++++++++++ unusual urls ++++++++++++++++++++++\n")
	for url in unusual_urls:
		print(url[0].split(random_string)[1]+":\t"+url[1])
	print("\n++++++++++++++++++++++ unusual urls ++++++++++++++++++++++")

	
if len(suspicious_urls) != 0:
	print("\n\n\n")
	print("++++++++++++++++++++++ suspicious urls ++++++++++++++++++++++\n")
	for url in suspicious_urls:
		print(url[0].split(random_string)[1]+":\t"+url[1])
	print("\n++++++++++++++++++++++ suspicious urls ++++++++++++++++++++++")

print("\n\n\n")
print("-----------------------------------------------------------------------------------")
print("File name: "+sys.argv[1])
print("-----------------------------------------------------------------------------------")
