import urllib.request as libreq
import xml.etree.ElementTree as ET
import json

OAI = "{http://www.openarchives.org/OAI/2.0/}"
arXiv = "{http://arxiv.org/OAI/arXiv/}"

def main():
    path = input("Enter the path(example --> D:/MachineLearning/) --> ")
    choosing_variable = input("which one?\n1.title\n2.Author\n3.Abstract\n4.Comment\n5.Journal Reference\n6.Subject Category\n7.Report Number\n8.Id\n9.All of the above\n10.Time\n(example --> 1+2+7)\n --> ")
    if choosing_variable.find('10') != -1:
        time_from = input("10.Time\nform(example --> 2015-04-01) --> ")
        time_until = input("until --> ")
        time_extracting(time_from, time_until, path)
    return

def time_extracting(time_from, time_until, path):
    metadata_dict = {"identifier":[], "datestamp":[], "setSpec":[], "id":[], "created":[], "updated":[], "authors":[], "title":[], "categories":[], "comments":[], "journal-ref":[], "doi":[], "abstract":[]}
    
    with libreq.urlopen('http://export.arxiv.org/oai2?verb=ListRecords&set=physics&from=%s&until=%s&metadataPrefix=arXiv' %(time_from, time_until)) as url:
        r = url.read()
        
    with open(path+"from"+time_from+"until"+time_until+".xml",'w') as f:
        f.write(r.decode())
        
    with open(path+"from"+time_from+"until"+time_until+".xml") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        count = 0
        if root.find(OAI+'ListRecords') == None:
            print("there is no article in this time :( ")
            print("you can see it by your eyes here --> %sfrom%suntil%s.xml" %(path, time_from, time_until))
            return
        if root.find(OAI+'ListRecords') != None:
            for element in root.find(OAI+'ListRecords').findall(OAI+'record'):
                count += 1
                if element.find(OAI+"header").find(OAI+"identifier") != None:
                    metadata_dict["identifier"].append(element.find(OAI+"header").find(OAI+"identifier").text)
                if element.find(OAI+"header").find(OAI+"identifier") == None:
                    metadata_dict["identifier"].append("None")
                if element.find(OAI+"header").find(OAI+"datestamp") != None:
                    metadata_dict["datestamp"].append(element.find(OAI+"header").find(OAI+"datestamp").text)
                if element.find(OAI+"header").find(OAI+"datestamp") == None:
                    metadata_dict["datestamp"].append("None")
                if element.find(OAI+"header").find(OAI+"setSpec") != None:
                    metadata_dict["setSpec"].append(element.find(OAI+"header").find(OAI+"setSpec").text)
                if element.find(OAI+"header").find(OAI+"setSpec") == None:
                    metadata_dict["setSpec"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"id") != None:
                    metadata_dict["id"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"id").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"id") == None:
                    metadata_dict["id"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"created") != None:
                    metadata_dict["created"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"created").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"created") == None:
                    metadata_dict["created"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"updated") != None:
                    metadata_dict["updated"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"updated").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"updated") == None:
                    metadata_dict["updated"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"authors").findall(arXiv+"author") != None:
                    authors_dict = {"keyname":[], "forenames":[]}
                    for author in element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"authors").findall(arXiv+"author"):
                        if author.find(arXiv+"keyname") != None:
                            authors_dict["keyname"].append(author.find(arXiv+"keyname").text)
                        if author.find(arXiv+"keyname") == None:
                            authors_dict["keyname"].append("None")
                        if author.find(arXiv+"forenames") != None:
                            authors_dict["forenames"].append(author.find(arXiv+"forenames").text)
                        if author.find(arXiv+"forenames") == None:
                            authors_dict["forenames"].append("None")
                    metadata_dict["authors"].append(authors_dict)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"authors").findall(arXiv+"author") == None:
                    metadata_dict["authors"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"title") != None:
                    metadata_dict["title"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"title").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"title") == None:
                    metadata_dict["title"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"categories") != None:
                    metadata_dict["categories"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"categories").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"categories") == None:
                    metadata_dict["categories"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"comments") != None:
                    metadata_dict["comments"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"comments").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"comments") == None:
                    metadata_dict["comments"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"journal-ref") != None:
                    metadata_dict["journal-ref"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"journal-ref").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"journal-ref") == None:
                    metadata_dict["journal-ref"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"doi") != None:
                    metadata_dict["doi"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"doi").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"doi") == None:
                    metadata_dict["doi"].append("None")
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"abstract") != None:
                    metadata_dict["abstract"].append(element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"abstract").text)
                if element.find(OAI+"metadata").find(arXiv+"arXiv").find(arXiv+"abstract") == None:
                    metadata_dict["abstract"].append("None")
            
    with open(path+"from"+time_from+"until"+time_until+"count"+str(count)+".json", 'w') as f:
        json.dump(metadata_dict, f)
    print("metadata of %i articles from arxiv is in %s as xml file,from%suntil%s.xml, and its datas saved in a dictionary,{"'id'":list of all articles id,...(and other informations like this how)}, as a json file in %sfrom%suntil%scount%i.json" %(count, path, time_from, time_until,path, time_from, time_until, count))
    return

main()
    
            