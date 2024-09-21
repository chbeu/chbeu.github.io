---
title: "{{ replace .Name "-" " " | title }}"
cms_exclude: true
type: talk

draft: false
reading_time: false  # Show estimated reading time?
share: true  # Show social sharing links?
profile: false  # Show author profile?
commentable: false  # Allow visitors to comment? Supported by the Page, Post, and Docs content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Docs content types.

event:
event_url:
location:
address:
#  street:
  city:
#  region:
#  postcode:
  country:
summary:
abstract:

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: {{ .Date }}
date_end: {{ .Date }}
all_day: true

# Schedule page publish date (NOT event date).
publishDate: {{ .Date }}

#authors: ["Christine Bauer"]
tags: [talk]

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
#image:
#  caption: ""
#  focal_point: ""
#  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your event's folder or a URL.
#url_slides:

#url_code: ""
#url_pdf:  ""
#url_slides:  ""
#url_video: ""

# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
