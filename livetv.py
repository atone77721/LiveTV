# save as livetv.py
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from datetime import datetime
import json

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
        
        # Channel groups and logos mapping
        groups = {
            'News': ['10.1', '10.2', '11.1', '12.2', '12.6'],
            'Sports': ['26.1', '47.1', '47.2', '47.3', '48.1', '48.2', '48.3'],
            'Entertainment': ['30.2', '30.3', '31.1', '31.2', '32.1', '32.2'],
            # Add more groups as needed
        }
        
        # Generate TiviMate compatible M3U
        output_file = 'tivimate_playlist.m3u'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # M3U Header
            f.write('#EXTM3U x-tvg-url=""\n')
            f.write(f'#PLAYLIST:{datetime.utcnow().strftime("%Y-%m-%d")}\n\n')
            
            # Process channels
            for channel_num, channel_name in channels:
                # Find group for this channel
                group = next((g for g, nums in groups.items() if channel_num in nums), 'Other')
                
                # Encrypt the URL
                channel_url = f'v{channel_num.replace(".", "")}'
                full_url = f'{base_url}{channel_url}'
                encrypted_url = encrypt_url(full_url, encryption_key, encryption_iv)
                
                # Write channel entry
                f.write(f'#EXTINF:-1 tvg-id="{channel_num}" tvg-name="{channel_name}" group-title="{group}" tvg-logo="https://your-logo-url.com/{channel_num}.png",{channel_name}\n')
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