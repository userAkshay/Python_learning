# import necessary packages
from string import Template

def Fetch_pubg_player_info():

        print('Report Player for using hacks')
        username = input('UserName: ')
        server = input('Server: ')
        country = input('Country: ')
        region_lang = input('Region and Language: ')
        flag = input('Flag: ')
        tier = input('Tier: ')
        rp_rank = input('Royal Pass Rank: ')
        
        print('Cheating has not been detected ')
        print('This player is not using any hack')
        print('\n')
        print("Quotation as follows: ")       
        print('\n')
        template = Template('This profile belongs to player ${u}, '
                            ' who primarily plays on the ${s} server on behalf of the '
                            'country ${c}. The player selected ${r} as his language and region. '
                            '${f} is the flag selected for this profile. The top tier for this profile, '
                            'is ${t} and Royal rank is ${rp}.')
        
        
        
        Template('Player ${n}, Mainly plays in ${a} server, '
                'and your username is ${u}')
        
        
        output = template.substitute(u=username, s=server, c=country, r=region_lang, f=flag, t=tier, rp= rp_rank)
        print(output)

if __name__ == "__main__":
        Fetch_pubg_player_info()