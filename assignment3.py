#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import re
import urllib2


parser = argparse.ArgumentParser()
parser.add_argument("--url", help = "Please enter a URL linking to a CSV file.")
args = parser.parse_args()


def main():
    if not args.url:
        raise SystemExit
    try:
        csvData = downloadData(args.url)
    except urllib2.URLError:
        print 'The URL that was entered is invalid. Kindly confirm the address and try again.'
    else:
        processData(csvData)


def downloadData(url):
    """
    Downloads content from a supplied URL.
    
    Args:
        url (str): A string value for a URL.

    Returns:
        csv_file (various): A variable linked to content found at the supplied URL, if the URL is valid.

    """
    
    content = urllib2.urlopen(url)
    return content


def processData(content):
    """
    Processes content within a .csv file.

    Args:
        content (file): A .csv file supplied by user or downloaded from a valid URL.

    Returns:
        message1 (str): A string containing the number of total hits.
        message2 (str): A string containing the percentage of hits for image files.
        message3 (str): A string containing the most popular browser and the hits using it.

    """

    csv_file = csv.reader(content)
    line_count = 0
    image_count = 0
    hour_count = 0

    chrome = ['Google Chrome', 0]
    explorer = ['Internet Explorer', 0]
    mozilla = ['Firefox', 0]
    safari = ['Safari', 0]
        
    for line in csv_file:
        line_count += 1
        if re.search("firefox", line[2], re.I):
            mozilla[1] += 1
        elif re.search(r"MSIE", line[2]):
            explorer[1] += 1
        elif re.search(r"Chrome", line[2]):
            chrome[1] += 1
        elif re.search(r"Safari", line[2]):
            safari[1] += 1
        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
            image_count += 1

    image_percentage = (float(image_count) / line_count) * 100

    browser_count = [chrome, explorer, mozilla, safari]

    browser_popularity = 0
    top_browser = ' '
    for b in browser_count:
        if b[1] > browser_popularity:
            browser_popularity = b[1]
            top_browser = b[0]
        else:
            continue

    message1 = ('There were {:,} total page hits today.').format(line_count)
    message2 = ('Hits on images accounted for {}% of all hits.').format(image_percentage)
    message3 = ('{} had the most hits with {:,}.').format(top_browser, browser_popularity)

    print message1
    print message2
    print message3
    

if __name__ == '__main__':
    main()





























#Author: Johnny Zgombic
#Date: September 14, 2019
