---
widget: pages

# This file represents a page section.
headless: true
draft: false

# Order that this section appears on the page.
weight: 75

title: Recent and Upcoming Events
subtitle:

content:
  # Page type to display. E.g. post, talk, publication...
  #page_type: talks
  # Choose how many pages you would like to display (0 = all pages)
  count: 3
  # Filter on criteria
  filters:
    folders: 
      - events
    author: ""
    #category: "event"
    #tag: "event"
    exclude_featured: false
    exclude_future: false
    exclude_past: false
    publication_type: ""
  # Choose how many pages you would like to offset by
  offset: 0
  # Field to sort by, such as Date or Title
  sort_by: 'Date'
  sort_ascending: false
  archive:
    enable: true
    text: See all events
    link: events/

design:
  # Choose a view for the listings:
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view: 2
---
