import requests

def dict_get(x,key,here=None): #Stolen from stackoverflow: https://stackoverflow.com/a/51789386
    x = x.copy()
    if here is None: here = []
    if x.get(key):  
        here.append(x.get(key))
        x.pop(key)
    else:
        for i,j in x.items():
          if  isinstance(x[i],list): dict_get(x[i][0],key,here)
          if  isinstance(x[i],dict): dict_get(x[i],key,here)
    return here

class API():
    def __init__(self, platform, username):
        self.p = platform
        self.u = username

    def verify(self):
        r = requests.get(f'https://r6.apitab.com/search/{self.p}/{self.u}')
        data = r.json()
        try:
            if dict_get(data, 'p_user')[0]:
                return True
        except:
            return False

    def getInfo(self):
        ranks = ['Copper IV',
                'Copper III',
                'Copper II',
                'Copper I',
                'Bronze IV',
                'Bronze III',
                'Bronze II',
                'Bronze I',
                'Silver IV', 
                'Silver III',
                'Silver II',
                'Silver I',
                'Gold IV',
                'Gold III',
                'Gold II',
                'Gold I',
                'Platinum III',
                'Platinum II',
                'Platinum I',
                'Diamond',
                'Champion']

        info_list = ['p_name',
                    'level',
                    'rank',
                    'mmr',
                    'kd']

        r = requests.get(f'https://r6.apitab.com/search/{self.p}/{self.u}')
        data = r.json()

        uid = dict_get(data, 'p_user')[0]
        pfp = f'https://ubisoft-avatars.akamaized.net/{uid}/default_256_256.png'

        stats = {'pfp': pfp}

        for info in info_list:
            try:
                if info == 'rank':
                    stats[info] = ranks[dict_get(data, info)[0]-1]
                else:
                    stats[info] = dict_get(data, info)[0]
            except:
                pass

        return stats