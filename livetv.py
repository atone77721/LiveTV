# livetv.py
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from datetime import datetime

def encrypt_url(url, key, iv):
    """Encrypt URL using AES-256-CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(url.encode(), AES.block_size))
    return base64.b64encode(ct_bytes).decode('utf-8')

def create_playlist():
    try:
        # Get configuration from environment variables
        base_url = os.getenv('LIVETV_BASE_URL')
        if not base_url:
            raise ValueError("LIVETV_BASE_URL environment variable is not set")
        
        encryption_key = os.getenv('ENCRYPTION_KEY').encode()
        encryption_iv = os.getenv('ENCRYPTION_IV').encode()
        
        # Complete channel list
        channels = [
            # Local Channels
            ('10.1', 'SPECTRUM NEWS'),
            ('10.2', 'WWAY ABC'),
            ('11.1', 'WWAY 2 CBS'),
            ('11.6', 'WSFX FOX'),
            ('12.1', 'WSFX 2 Court'),
            ('12.2', 'WECT NBC'),
            ('12.6', 'WECT 2 Bounce'),
            ('12.7', 'WWAY 3 CW'),
            ('13.1', 'WUNC PBS'),
            ('13.6', 'WUNC 2 PBS Kids'),
            ('13.7', 'ION'),
            ('23.1', 'WILM 2 Me TV'),
            ('23.2', 'Telemundo'),
            ('24.3', 'UNIMAS'),
            ('25.1', 'Univision'),
            ('25.2', 'Daystar'),
            ('25.3', 'TBN'),
            ('26.1', 'BALLY Sports South'),
            ('28.1', 'DELUXE GUIDE'),
            # Entertainment
            ('30.1', 'USA East Columbia USA'),
            ('30.2', 'AE AETV'),
            ('30.3', 'TNT'),
            ('31.1', 'TBS'),
            ('31.2', 'AMC'),
            ('31.3', 'DISCOVERY'),
            ('32.1', 'HISTORY HIST'),
            ('32.2', 'FX'),
            ('32.3', 'BBC AMERICA'),
            ('33.1', 'SYFY'),
            ('33.2', 'TRU TV'),
            ('33.3', 'COMEDY CENTRAL'),
            ('34.1', 'PARAMOUNT PAR'),
            ('34.2', 'VH1'),
            ('34.3', 'MTV'),
            ('35.1', 'TV LAND'),
            ('35.2', 'FREEFORM'),
            ('35.3', 'HALLMARK CHANNEL'),
            ('36.1', 'NATIONAL GEOGRAPHIC'),
            ('36.2', 'ANIMAL PLANET'),
            ('36.3', 'SCIENCE'),
            ('37.1', 'AHC'),
            ('37.2', 'HGTV'),
            ('37.3', 'FOOD NETWORK FOOD'),
            ('38.1', 'TRAVEL CHANNEL'),
            ('38.2', 'TLC'),
            ('38.3', 'BRAVO'),
            ('39.1', 'E! E!'),
            ('39.2', 'LIFETIME LIFE'),
            ('39.3', 'OWN'),
            ('40.1', 'BET'),
            ('40.2', 'OVATION TV OVATION'),
            ('40.3', 'CNN'),
            ('41.1', 'FOX NEWS'),
            ('41.2', 'MSNBC'),
            ('41.3', 'HLN'),
            ('42.1', 'CNBC'),
            ('42.2', 'FOX BUSINESS NETWORK'),
            ('42.3', 'BLOOMBERG'),
            ('43.1', 'WEATHER CHANNEL WEATH'),
            ('43.2', 'C-SPAN CSPAN'),
            ('43.3', 'DISNEY CHANNEL DISN'),
            ('44.1', 'BOOMERANG BOOM'),
            ('44.2', 'DISNEY JR DJCH'),
            ('44.3', 'UNIVERSAL KIDS UKIDS'),
            ('45.1', 'NICK JR NICKJR'),
            ('45.2', 'NICKELODEON NICK'),
            ('45.3', 'CARTOON NETWORK TOON'),
            ('46.1', 'DISCOVERY FAMILY DFC'),
            ('46.2', 'CMT'),
            ('46.3', 'GREAT AMERICAN COUNTRY GAC'),
            # Sports
            ('47.1', 'ESPN'),
            ('47.2', 'ESPN2'),
            ('47.3', 'DELUXE GUIDE 2'),
            ('48.1', 'NBC SPORTS NETWORK NBCSN'),
            ('48.2', 'SEC NETWORK SEC'),
            ('48.3', 'FOX SPORTS 1 FS1'),
            ('49.1', 'FOX SPORTS 2 FS2'),
            ('49.2', 'MOTORTREND MT'),
            ('49.3', 'TCM'),
            ('50.1', 'HSN'),
            ('50.2', 'EWTN'),
            ('50.3', 'SHOP HQ'),
            ('51.1', 'QVC'),
            ('51.2', 'CNN EN ESPANOL CNNE'),
            ('51.3', 'FXX'),
            ('52.1', 'MTV2'),
            ('52.2', 'MTV CLASSIC ROCK'),
            ('52.3', 'UP'),
            ('53.1', 'NATIONAL GEO WILD'),
            ('53.2', 'SMITHSONIAN CHANNEL'),
            ('53.3', 'VICELAND VICE'),
            ('54.1', 'FYI'),
            ('54.2', 'DESTINATION AMERICA'),
            ('54.3', 'INVESTIGATION DISCOVERY'),
            ('55.1', 'ACCU WEATHER'),
            ('55.2', 'COOKING CHANNEL COOK'),
            ('55.3', 'OXYGEN'),
            ('56.1', 'WE TV'),
            ('56.2', 'POP'),
            ('56.3', 'GAME SHOW NETWORK'),
            ('57.1', 'LOGO'),
            ('57.2', 'DISCOVERY LIFE'),
            ('57.3', 'BET HER'),
            ('58.1', 'TV ONE'),
            ('58.2', 'BBC WORLD NEWS'),
            ('58.3', 'NICKTOONS'),
            ('59.1', 'TEENNICK'),
            ('59.2', 'DISNEY XD'),
            ('59.3', 'MTV LIVE'),
            ('60.1', 'REVOLT RVLT'),
            ('60.2', 'FUSE'),
            ('60.3', 'INSP'),
            ('61.1', 'SUNDANCETV SUNDANC'),
            ('61.2', 'LMN'),
            ('61.3', 'IFC'),
            ('62.1', 'HALLMARK MOVIES HMM'),
            ('62.2', 'BET SOUL BETSOUL'),
            ('62.3', 'PAC-12 NETWORK PAC12'),
            ('63.1', 'BYU TV BYUTV'),
            ('63.2', 'FX MOVIE CHANNEL FXM'),
            ('63.3', 'IMPACT NETWORK IMPCNET'),
            ('64.1', 'DIY NETWORK DIY'),
            ('64.2', 'MTVU'),
            ('64.3', 'NEWSMAX TV NEWSMX'),
            # Sports Pass
            ('65.1', 'BIG TEN BIGTEN'),
            ('65.2', 'ACC NETWORK ACC'),
            ('65.3', 'BEIN SPORTS BEIN'),
            ('66.1', 'CBS SPORTS NETWORK'),
            ('66.2', 'ESPN DEPORTES ESPND'),
            ('69.1', 'SPORTS PASS GUIDE'),
            ('69.2', 'BEIN SPORTS BEIN'),
            ('70.1', 'CBS SPORTS NETWORK'),
            ('73.2', 'ESPN DEPORTES ESPND'),
            ('74.1', 'ESPN NEWS'),
            ('74.2', 'ESPNU'),
            ('74.3', 'FOX DEPORTES FXDEP'),
            ('76.2', 'GOLF CHANNEL GOLF'),
            ('76.3', 'MLB NETWORK MLBN'),
            ('77.1', 'MLB STRIKE ZONE MLBNSZ'),
            ('77.2', 'NBA TV NBATV'),
            ('77.3', 'NFL NETWORK NFLNET'),
            ('78.1', 'NFL REDZONE NFLNRZ'),
            ('78.2', 'NHL NETWORK NHLNET'),
            ('78.3', 'THE OLYMPIC CHANNEL OLY'),
            ('79.1', 'OUTDOOR CHANNEL OUTD'),
            ('79.2', 'PAC-12 ARIZONA PAC12AZ'),
            ('79.3', 'PAC-12 BAY AREA PAC12BA'),
            ('80.1', 'PAC-12 LOS ANGELES PAC12LA'),
            ('80.2', 'PAC-12 MOUNTAIN PAC12MT'),
            ('80.3', 'PAC-12 OREGON PAC12OR'),
            ('81.1', 'PAC-12 WASHINGTON PAC12WA'),
            ('81.2', 'SEC ALTERNATE SEC2'),
            ('81.3', 'TENNIS CHANNEL TENNIS'),
            ('82.1', 'TVG'),
            ('82.2', 'TUDN'),
            ('82.3', 'WILLOW CRICKET WILLOW'),
            # HBO Channels
            ('98.1', 'HBO GUIDE'),
            ('98.2', 'HBO'),
            ('98.3', 'HBO 2 HBO2'),
            ('98.4', 'HBO SIGNATURE HBOSIG'),
            ('99.1', 'HBO COMEDY HBOC'),
            ('99.2', 'HBO FAMILY HBOF'),
            ('99.3', 'HBO LATINO HBOLAT'),
            ('99.4', 'HBO ZONE HBOZ')
        ]
        
        # Generate TiviMate compatible M3U
        output_file = 'tivimate_playlist.m3u'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # M3U Header
            f.write('#EXTM3U x-tvg-url=""\n')
            f.write(f'#PLAYLIST:{datetime.utcnow().strftime("%Y-%m-%d")}\n\n')
            
            # Process channels
            for channel_num, channel_name in channels:
                # Encrypt the URL
                channel_url = f'v{channel_num.replace(".", "")}'
                full_url = f'{base_url}{channel_url}'
                encrypted_url = encrypt_url(full_url, encryption_key, encryption_iv)
                
                # Write channel entry
                f.write(f'#EXTINF:-1 tvg-id="{channel_num}" tvg-name="{channel_name}",{channel_name}\n')
                f.write(f'#EXTVLCOPT:http-referer={base_url}\n')
                f.write(f'#EXTVLCOPT:http-user-agent=Mozilla/5.0\n')
                f.write(f'{encrypted_url}\n\n')

        print(f"TiviMate playlist generated: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == '__main__':
    create_playlist()
