# livetv.py
import os
from datetime import datetime

def create_playlist():
    try:
        # Get base URL from environment variable or use default
        base_url = os.getenv('LIVETV_BASE_URL', 'http://128.230.54.128:5004/auto')
        # Remove any trailing slashes to prevent double slashes
        base_url = base_url.rstrip('/')
        
        # Complete channel list
        channels = [
            # Local Channels
            ('10.1', 'Local Channel Guide'),
            ('10.2', 'SPECTRUM NEWS'),
            ('11.1', 'WWAY ABC'),
            ('11.6', 'WTYH 5 CBS'),  # Updated from WSFX FOX to match your list
            ('12.1', 'WSFX FOX'),     # Updated from WSFX 2 Court to match your list
            ('12.2', 'WSFX 2 Court'), # Updated from WECT NBC to match your list
            ('12.6', 'WECT NBC'),     # Updated from WECT 2 Bounce to match your list
            ('12.7', 'WECT 2 Bounce'),# Updated from WWAY 3 CW to match your list
            ('13.1', 'WWAY 3 CW'),    # Updated from WUNC PBS to match your list
            ('13.6', 'WUNC PBS'),     # Updated from WUNC 2 PBS Kids to match your list
            ('13.7', 'WUNC 2 PBS Kids'), # Updated from ION to match your list
            ('23.1', 'ION'),          # Updated from WILM 2 Me TV to match your list
            ('23.2', 'WILM 2 Me TV'), # Updated from Telemundo to match your list
            ('24.3', 'Telemundo'),    # Updated from UNIMAS to match your list
            ('25.1', 'UNIMAS'),       # Updated from Univision to match your list
            ('25.2', 'Univision'),    # Updated from Daystar to match your list
            ('25.3', 'Daystar'),      # Updated from TBN to match your list
            ('26.1', 'TBN'),          # Updated from BALLY Sports South to match your list
            ('28.1', 'BALLY Sports South'), # Updated from DELUXE GUIDE to match your list
            # Entertainment
            ('30.1', 'DELUXE GUIDE'), # Updated from USA East Columbia USA to match your list
            ('30.2', 'USA East Columbia USA'), # Updated from AE AETV to match your list
            ('30.3', 'A&E'),          # Updated from TNT to match your list
            ('31.1', 'TNT'),          # Updated from TBS to match your list
            ('31.2', 'TBS'),          # Updated from AMC to match your list
            ('31.3', 'AMC'),          # Updated from DISCOVERY to match your list
            ('32.1', 'DISCOVERY'),    # Updated from HISTORY HIST to match your list
            ('32.2', 'HISTORY'),      # Updated from FX to match your list
            ('32.3', 'FX'),           # Updated from BBC AMERICA to match your list
            ('33.1', 'BBC AMERICA'),  # Updated from SYFY to match your list
            ('33.2', 'SYFY'),         # Updated from TRU TV to match your list
            ('33.3', 'TRU TV'),       # Updated from COMEDY CENTRAL to match your list
            ('34.1', 'COMEDY CENTRAL'), # Updated from PARAMOUNT to match your list
            ('34.2', 'PARAMOUNT'),    # Updated from VH1 to match your list
            ('34.3', 'VH1'),          # Updated from MTV to match your list
            ('35.1', 'MTV'),          # Updated from TV LAND to match your list
            ('35.2', 'TV LAND'),      # Updated from FREEFORM to match your list
            ('35.3', 'FREEFORM'),     # Updated from HALLMARK CHANNEL to match your list
            ('36.1', 'HALLMARK CHANNEL'), # Updated from NATIONAL GEOGRAPHIC to match your list
            ('36.2', 'NATIONAL GEOGRAPHIC'), # Updated from ANIMAL PLANET to match your list
            ('36.3', 'ANIMAL PLANET'), # Updated from SCIENCE to match your list
            ('37.1', 'SCIENCE'),      # Updated from AHC to match your list
            ('37.2', 'AHC'),          # Updated from HGTV to match your list
            ('37.3', 'HGTV'),         # Updated from FOOD NETWORK to match your list
            ('38.1', 'FOOD NETWORK'), # Updated from TRAVEL CHANNEL to match your list
            ('38.2', 'TRAVEL CHANNEL'), # Updated from TLC to match your list
            ('38.3', 'TLC'),          # Updated from BRAVO to match your list
            ('39.1', 'BRAVO'),        # Updated from E! to match your list
            ('39.2', 'E!'),           # Updated from LIFETIME to match your list
            ('39.3', 'LIFETIME'),     # Updated from OWN to match your list
            ('40.1', 'OWN'),          # Updated from BET to match your list
            ('40.2', 'BET'),          # Updated from OVATION to match your list
            ('40.3', 'OVATION'),      # Updated from CNN to match your list
            ('41.1', 'CNN'),          # Updated from FOX NEWS to match your list
            ('41.2', 'FOX NEWS'),     # Updated from MSNBC to match your list
            ('41.3', 'MSNBC'),        # Updated from HLN to match your list
            ('42.1', 'HLN'),          # Updated from CNBC to match your list
            ('42.2', 'CNBC'),         # Updated from FOX BUSINESS to match your list
            ('42.3', 'FOX BUSINESS'), # Updated from BLOOMBERG to match your list
            ('43.1', 'BLOOMBERG'),    # Updated from WEATHER CHANNEL to match your list
            ('43.2', 'WEATHER CHANNEL'), # Updated from C-SPAN to match your list
            ('43.3', 'C-SPAN'),       # Updated from DISNEY CHANNEL to match your list
            ('44.1', 'DISNEY CHANNEL'), # Updated from BOOMERANG to match your list
            ('44.2', 'BOOMERANG'),    # Updated from DISNEY JR to match your list
            ('44.3', 'DISNEY JR'),    # Updated from UNIVERSAL KIDS to match your list
            ('45.1', 'UNIVERSAL KIDS'), # Updated from NICK JR to match your list
            ('45.2', 'NICK JR'),      # Updated from NICKELODEON to match your list
            ('45.3', 'NICKELODEON'),  # Updated from CARTOON NETWORK to match your list
            ('46.1', 'CARTOON NETWORK'), # Updated from DISCOVERY FAMILY to match your list
            ('46.2', 'DISCOVERY FAMILY'), # Updated from CMT to match your list
            ('46.3', 'CMT'),          # Updated from GREAT AMERICAN COUNTRY to match your list
            # Sports
            ('47.1', 'GREAT AMERICAN COUNTRY'), # Updated from ESPN to match your list
            ('47.2', 'ESPN'),         # Updated from ESPN2 to match your list
            ('47.3', 'ESPN2'),        # Updated from DELUXE GUIDE 2 to match your list
            ('48.1', 'DELUXE GUIDE 2'), # Updated from NBC SPORTS NETWORK to match your list
            ('48.2', 'NBC SPORTS'),   # Updated from SEC NETWORK to match your list
            ('48.3', 'SEC NETWORK'),  # Updated from FOX SPORTS 1 to match your list
            ('49.1', 'FOX SPORTS 1'), # Updated from FOX SPORTS 2 to match your list
            ('49.2', 'FOX SPORTS 2'), # Updated from MOTORTREND to match your list
            ('49.3', 'MOTORTREND'),   # Updated from TCM to match your list
            ('50.1', 'TCM'),          # Updated from HSN to match your list
            ('50.2', 'HSN'),          # Updated from EWTN to match your list
            ('50.3', 'EWTN'),         # Updated from SHOP HQ to match your list
            ('51.1', 'SHOP HQ'),      # Updated from QVC to match your list
            ('51.2', 'QVC'),          # Updated from CNN EN ESPANOL to match your list
            ('51.3', 'CNN EN ESPANOL'), # Updated from FXX to match your list
            ('52.1', 'FXX'),          # Updated from MTV2 to match your list
            ('52.2', 'MTV2'),         # Updated from MTV CLASSIC to match your list
            ('52.3', 'MTV CLASSIC'),  # Updated from UP to match your list
            ('53.1', 'UP'),           # Updated from NATIONAL GEO WILD to match your list
            ('53.2', 'NATIONAL GEO WILD'), # Updated from SMITHSONIAN to match your list
            ('53.3', 'SMITHSONIAN'),  # Updated from VICELAND to match your list
            ('54.1', 'VICELAND'),     # Updated from FYI to match your list
            ('54.2', 'FYI'),          # Updated from DESTINATION AMERICA to match your list
            ('54.3', 'DESTINATION AMERICA'), # Updated from INVESTIGATION DISCOVERY to match your list
            ('55.1', 'INVESTIGATION DISCOVERY'), # Updated from ACCU WEATHER to match your list
            ('55.2', 'ACCU WEATHER'), # Updated from COOKING CHANNEL to match your list
            ('55.3', 'COOKING CHANNEL'), # Updated from OXYGEN to match your list
            ('56.1', 'OXYGEN'),       # Updated from WE TV to match your list
            ('56.2', 'WE TV'),        # Updated from POP to match your list
            ('56.3', 'POP'),          # Updated from GAME SHOW NETWORK to match your list
            ('57.1', 'GAME SHOW NETWORK'), # Updated from LOGO to match your list
            ('57.2', 'LOGO'),         # Updated from DISCOVERY LIFE to match your list
            ('57.3', 'DISCOVERY LIFE'), # Updated from BET HER to match your list
            ('58.1', 'BET HER'),      # Updated from TV ONE to match your list
            ('58.2', 'TV ONE'),       # Updated from BBC WORLD NEWS to match your list
            ('58.3', 'BBC WORLD NEWS'), # Updated from NICKTOONS to match your list
            ('59.1', 'NICKTOONS'),    # Updated from TEENNICK to match your list
            ('59.2', 'TEENNICK'),     # Updated from DISNEY XD to match your list
            ('59.3', 'DISNEY XD'),    # Updated from MTV LIVE to match your list
            ('60.1', 'MTV LIVE'),     # Updated from REVOLT to match your list
            ('60.2', 'REVOLT'),       # Updated from FUSE to match your list
            ('60.3', 'FUSE'),         # Updated from INSP to match your list
            ('61.1', 'INSP'),         # Updated from SUNDANCETV to match your list
            ('61.2', 'SUNDANCETV'),   # Updated from LMN to match your list
            ('61.3', 'LMN'),          # Updated from IFC to match your list
            ('62.1', 'IFC'),          # Updated from HALLMARK MOVIES to match your list
            ('62.2', 'HALLMARK MOVIES'), # Updated from BET SOUL to match your list
            ('62.3', 'BET SOUL'),     # Updated from PAC-12 NETWORK to match your list
            ('63.1', 'PAC-12 NETWORK'), # Updated from BYU TV to match your list
            ('63.2', 'BYU TV'),       # Updated from FX MOVIE CHANNEL to match your list
            ('63.3', 'FX MOVIE CHANNEL'), # Updated from IMPACT NETWORK to match your list
            ('64.1', 'IMPACT NETWORK'), # Updated from DIY NETWORK to match your list
            ('64.2', 'DIY NETWORK'),  # Updated from MTVU to match your list
            ('64.3', 'MTVU'),         # Updated from NEWSMAX to match your list
            # Sports Pass
            ('65.1', 'NEWSMAX'),      # Updated from BIG TEN to match your list
            ('65.2', 'BIG TEN'),      # Updated from ACC NETWORK to match your list
            ('65.3', 'ACC NETWORK'),  # Updated from BEIN SPORTS to match your list
            ('66.1', 'SPORTS PASS GUIDE'), # Updated from CBS SPORTS to match your list
            ('66.2', 'BEIN SPORTS'),  # Updated from ESPN DEPORTES to match your list
            ('69.1', 'CBS SPORTS'),   # Updated from SPORTS PASS GUIDE to match your list
            ('69.2', 'ESPN DEPORTES'), # Updated from BEIN SPORTS to match your list
            ('70.1', 'ESPN NEWS'),    # Updated from CBS SPORTS to match your list
            ('73.2', 'ESPNU'),        # Updated from ESPN DEPORTES to match your list
            ('74.1', 'FOX DEPORTES'), # Updated from ESPN NEWS to match your list
            ('74.2', 'GOLF CHANNEL'), # Updated from ESPNU to match your list
            ('74.3', 'MLB NETWORK'),  # Updated from FOX DEPORTES to match your list
            ('76.2', 'MLB STRIKE ZONE'), # Updated from GOLF CHANNEL to match your list
            ('76.3', 'NBA TV'),       # Updated from MLB NETWORK to match your list
            ('77.1', 'NFL NETWORK'),  # Updated from MLB STRIKE ZONE to match your list
            ('77.2', 'NFL REDZONE'),  # Updated from NBA TV to match your list
            ('77.3', 'NHL NETWORK'),  # Updated from NFL NETWORK to match your list
            ('78.1', 'OLYMPIC CHANNEL'), # Updated from NFL REDZONE to match your list
            ('78.2', 'OUTDOOR CHANNEL'), # Updated from NHL NETWORK to match your list
            ('78.3', 'PAC-12 ARIZONA'), # Updated from OLYMPIC CHANNEL to match your list
            ('79.1', 'PAC-12 BAY AREA'), # Updated from OUTDOOR CHANNEL to match your list
            ('79.2', 'PAC-12 LOS ANGELES'), # Updated from PAC-12 ARIZONA to match your list
            ('79.3', 'PAC-12 MOUNTAIN'), # Updated from PAC-12 BAY AREA to match your list
            ('80.1', 'PAC-12 OREGON'), # Updated from PAC-12 LOS ANGELES to match your list
            ('80.2', 'PAC-12 WASHINGTON'), # Updated from PAC-12 MOUNTAIN to match your list
            ('80.3', 'SEC ALTERNATE'), # Updated from PAC-12 OREGON to match your list
            ('81.1', 'TENNIS CHANNEL'), # Updated from PAC-12 WASHINGTON to match your list
            ('81.2', 'TVG'),          # Updated from SEC ALTERNATE to match your list
            ('81.3', 'TUDN'),         # Updated from TENNIS CHANNEL to match your list
            ('82.1', 'WILLOW CRICKET'), # Updated from TVG to match your list
            ('82.2', 'HBO GUIDE'),    # Updated from TUDN to match your list
            ('82.3', 'HBO'),          # Updated from WILLOW CRICKET to match your list
            # HBO Channels
            ('98.1', 'HBO 2'),        # Updated from HBO GUIDE to match your list
            ('98.2', 'HBO SIGNATURE'), # Updated from HBO to match your list
            ('98.3', 'HBO COMEDY'),   # Updated from HBO 2 to match your list
            ('98.4', 'HBO FAMILY'),   # Updated from HBO SIGNATURE to match your list
            ('99.1', 'HBO LATINO'),   # Updated from HBO COMEDY to match your list
            ('99.2', 'HBO ZONE'),     # Updated from HBO FAMILY to match your list
            ('99.3', 'HBO'),          # Updated from HBO LATINO to match your list
            ('99.4', 'HBO 2')         # Updated from HBO ZONE to match your list
        ]
        
        # Generate TiviMate compatible M3U
        output_file = 'tivimate_playlist.m3u'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # M3U Header
            f.write('#EXTM3U x-tvg-url=""\n')
            f.write(f'#PLAYLIST:{datetime.utcnow().strftime("%Y-%m-%d")}\n\n')
            
            # Process channels
            for channel in channels:
                # Write channel entry
                # Format the channel name as 'FULL_NAME vCHANNEL.NUM' (e.g., 'WWAY 2 CBS v11.6')
                channel_name = f"{channel[1]} v{channel[0]}"
                f.write(f'#EXTINF:-1 tvg-id="{channel[0]}" tvg-name="{channel_name}",{channel_name}\n')
                f.write(f'#EXTVLCOPT:http-referer={base_url}/\n')
                f.write(f'#EXTVLCOPT:http-user-agent=Mozilla/5.0\n')
                f.write(f'{base_url}/v{channel[0]}\n\n')

        print(f"TiviMate playlist generated: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == '__main__':
    create_playlist()
