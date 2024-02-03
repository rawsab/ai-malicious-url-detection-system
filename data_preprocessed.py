# Gather data to use in pre-processing for training and prediction

import pandas as pd

def main():
    
    url_set = {}
    
    # Define whitelist and blacklist for malicious URLs
    
    url_whitelist = 'url_whitelist.txt'
    
    url_blacklist = 'malicious_url_db.csv'
    url_blacklist = pd.read_csv(url_blacklist)
    
    # Assign values to malicious/non-malicious URLs for supervised learning
    
    for url in url_blacklist['url']:
        # set malicious URLs to 1
        url_set[url] = 1
    
    with open(url_whitelist, 'r') as file:
        lines = file.read().splitlines()
        for url in lines:
            # set non-malicious URLs to 0
            url_set[url] = 0
            
    return url_set


if __name__ == '__main__':
    main()