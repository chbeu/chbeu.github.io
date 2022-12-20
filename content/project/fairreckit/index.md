---
title: "FairRecKit"
summary: "*FairRecKit* is a web-based analysis software that supports researchers in performing, analyzing, and understanding recommendation computations. The idea behind *FairRecKit* is to facilitate the in-depth analysis of recommendation outcomes considering fairness aspects. With (nested) filters on user or item attributes, metrics can easily be compared across user and item subgroups."
tags:
tags: [FairRecKit, resource, toolkit, analysis software, web-based, evaluation, analysis, recommender systems, music, movies]
date: "2022-03-01T00:00:00Z"
profile: false

# Optional external URL for project (replaces project detail page).
#external_link: ""

image:
  focal_point: Smart

url_video: https://www.youtube.com/watch?v=6C1cRpy4b44
links:
- icon: github
  icon_pack: fab
  name: Code FairRecKitApp
  url: https://github.com/FairRecKit/FairRecKitApp
- icon: github
  icon_pack: fab
  name: Code FairRecKitLib
  url: https://github.com/FairRecKit/FairRecKitLib
---

*FairRecKit* is a web-based analysis software that supports researchers in performing, analyzing, and understanding recommendation computations. The idea behind *FairRecKit* is to facilitate the in-depth analysis of recommendation outcomes considering fairness aspects. With (nested) filters on user or item attributes, metrics can easily be compared across user and item subgroups. Further, (nested) filters can also be used on dataset level; this way, recommendation outcomes can be compared across several sub-datasets to analyze for differences considering fairness aspects. The software currently features 5 datasets, 11 metrics, and 21 recommendation algorithms to be used in computational experimentation. It is open source and developed in a modular manner to facilitate extension. 
The analysis software consists of two components: A software package (*FairRecKitLib*) that is used to run recommendation algorithms on the available datasets and a web-based user interface (*FairRecKitApp*) to start experiments, retrieve results of previous experiments, and analyze details. The application also comes with an extensive documentation and options for result customization, which makes for a flexible tool that supports in-depth analysis.