import requests  
import json
import sys
from time import sleep 
json_data=[]
index=-1
profile=sys.argv[1]
uid=int(sys.argv[2])
while True:
    data = requests.post("https://www.quora.com/graphql/gql_para_POST?q=UserProfileAnswersMostRecent_RecentAnswers_Query", headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "priority": "u=1, i",
        "quora-broadcast-id": "main-w-chan56-8888-react_rhvancsuygqfyuyr-cDpr",
        "quora-canary-revision": "false",
        "quora-formkey": "c09446b6a4353625785caf758a343b55",
        "quora-page-creation-time": "1729078602586577",
        "quora-revision": "1c813001f1e3aaf70900b68e3048d997952573f5",
        "quora-window-id": "react_rhvancsuygqfyuyr",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "__stripe_mid=f6594168-c7f0-420b-82a8-7fe6b763193f62f4f7; m-b=i_igAWrJFmbh5MG8asajZQ==; m-b_lax=i_igAWrJFmbh5MG8asajZQ==; m-b_strict=i_igAWrJFmbh5MG8asajZQ==; m-s=Gxt5aGv550G90VnJghQ0fA==; m-theme=light; m-dynamicFontSize=regular; m-themeStrategy=auto; m-ql10n_ar=https%3A%2F%2Fqsbr.cf2.quoracdn.net%2F-4-l10n_main-30-ar-693686341370417f.translation.json; m-login=1; m-lat=BEwiRHlPCIVnpumlNW9YGfZo5PEZramsOqzoT9NdRA==; m-uid=2563106278; m-sa=1; __stripe_sid=56dea236-280f-42cc-a104-46a2fad728823aea18; __gads=ID=0fb3d626f75bb9e2:T=1729017358:RT=1729078447:S=ALNI_MYNK02o06NmmwgKSL-omaV80WcHjw; __gpi=UID=00000f3f02cef187:T=1729017358:RT=1729078447:S=ALNI_MY_mO-nrpi_D-xp4vgkNAb3bX36tA; __eoi=ID=b1ee6cd216f5e02c:T=1729017358:RT=1729078447:S=AA-AfjaWHALk6KDK3V7WejdvXFxs",
        "Referer": f"https://www.quora.com/profile/{profile}/answers",
        "Referrer-Policy": "strict-origin-when-cross-origin"
        },json={"queryName":"UserProfileAnswersMostRecent_RecentAnswers_Query","variables":{"uid":uid,"first":3,"after":str(index),"answerFilterTid": None},"extensions":{"hash":"87c0ab1d94902029565e396a4a0483108998ce98c4f1cce6ccf4f7c7a3fc4e03"}})
    answer=json.loads(data.text)
    try :
        url=answer["data"]["user"]["recentPublicAndPinnedAnswersConnection"]["edges"][0]["node"]["url"]
    except:
        break
    if not( url.startswith("https")):
        
        url="https://www.quora.com"+url
    json_data.append({"Link":url})
    sleep(8)
    index+=1
print(index)
with open("test.json","w") as f:
    y = json.dumps(json_data)
    f.write(y)