#!/usr/bin/env python3
import sys
import os
import json
import xml.etree.ElementTree as ET

def extract_feeds(opml_content):
    try:
        root = ET.fromstring(opml_content)
        feeds = []
        for outline in root.findall(".//outline[@type='rss']"):
            xml_url = outline.get('xmlUrl')
            if xml_url:
                feeds.append(xml_url)
        return feeds
    except Exception as e:
        print(f"Error parsing OPML: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_opml.py <opml_file>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        content = f.read()
    
    feeds = extract_feeds(content)
    print(json.dumps(feeds, indent=2))
