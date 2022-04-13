import json

file1 = open('api.txt', 'r', encoding='utf-8', errors='ignore')
lines1 = file1.readlines()

attributes=["id", "apiId","title","summary","rating",
"name", "label", "author", "description", "type", "downloads",
"useCount", "sampleUrl", "downloadUrl", "dateModified",
"remoteFeed", "numComments", "commentsUrl", "Tags", "category",
"protocols", "serviceEndpoint", "version", "wsdl", "data_formats",
"apigroups", "example", "clientInstall", "authentication", "ssl",
"readonly", "VendorApiKits", "CommunityApiKits", "blog", "forum",
"support", "accountReq", "commercial", "provider", "managedBy", 
"nonCommercial", "dataLicensing", "fees", "limits", "terms", "company",
"updated"]

entry=[]
auto_id = 0
for line in lines1:
    tempEntry = {}
    tempEntry["id"] = auto_id
    line_split = (line.strip().split('$#$'))
    index = 1
    for ls in line_split:
        if(attributes[index]=='rating'):
            if(ls == ""):
                tempEntry[attributes[index]]= None
            else:
                tempEntry[attributes[index]]= float(ls)
            index = index+1
            continue
        tempEntry[attributes[index]]= ls
        index = index+1
    auto_id = auto_id+1
    entry.append(tempEntry)

with open("api.json", "w") as output:
    json.dump(entry, output)

output.close()
    


