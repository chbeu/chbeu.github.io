---
title: Featured Publications
subtitle: ""
widget: collection
show_date: false

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 80


content:
  filters:
    folders:
      - publications
    featured_only: true
    tag: ''
    category: ''
    publication_type: ''
    author: ''
    exclude_featured: false
    exclude_future: false
    exclude_past: false
  # Choose how many pages you would like to display (0 = all pages)
  count: 5
  # Choose how many pages you would like to offset by
  # Useful if you wish to show the first item in the Featured widget
  offset: 0
  # Field to sort by, such as Date or Title
  sort_by: 'Date'
  sort_ascending: false

  archive:
    enable: true
    text: See all publications
    link: publications/

design:
  # Choose a listing view
  view: citation
  # Choose how many columns the section has. Valid values: '1' or '2'.
  columns: '2'
---
