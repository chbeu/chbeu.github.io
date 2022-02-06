---
id: 3185
title: The Conversation article on our CHIIR 2021 paper
date: 2021-03-30T18:01:13+00:00
author: Christine Bauer
layout: post
guid: https://christinebauer.eu/?p=3185
permalink: /?p=3185
zincy_lite_sidebar_layout:
  - right-sidebar
categories:
  - news
tags:
  - artists
  - bias
  - CHIIR
  - communication to the public
  - fairness
  - gender
  - media
  - publication
  - recommender systems
---
This article is republished from [The Conversation](https://theconversation.com) under a Creative Commons license. Read the [original article](https://theconversation.com/music-recommendation-algorithms-are-unfair-to-female-artists-but-we-can-change-that-158016).

<!--![Logo of The Conversation UK](https://cdn.theconversation.com/static/tc/@theconversation/ui/dist/esm/logos/logo-en-d7023135a67823619bfdbf3322b68dc4.png)  -->

# Music recommendation algorithms are unfair to female artists, but we can change that.

{{< figure src="pixabay_musiclistening_adult-3086302_1920.jpg" alt="Adult, Music, Listening, Sound, Woman, Fun, Enjoyment" title="Algorithms help lots of people discover new music.<br>[Image](https://pixabay.com/photos/adult-music-listening-sound-woman-3086302/)></a> by [Omar Medina Films](https://pixabay.com/users/omarmedinafilms-818453/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3086302) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3086302)" >}}

Article written by: [Christine Bauer](https://theconversation.com/profiles/christine-bauer-1221184), _[Utrecht University](https://theconversation.com/institutions/utrecht-university-1354)_ and [Andrés Ferraro](https://theconversation.com/profiles/andres-ferraro-1221187), _[Universitat Pompeu Fabra](https://theconversation.com/institutions/universitat-pompeu-fabra-2457)_

These days, more and more people listen to music on streaming apps – in early 2020, [400 million people](https://www.statista.com/statistics/669113/number-music-streaming-subscribers/) were subscribed to one. These platforms use algorithms to recommend music based on listening habits. The recommended songs might feature in new playlists or they might start to play automatically when another playlist has ended.

But what the algorithms recommend is not always fair. In [a new study](https://doi.org/10.1145/3406522.3446033) we showed a widely used recommendation algorithm is more likely to pick music by male than female artists. In response, we’ve come up with a simple way to give more exposure to female artists.

The representation of women and gender minorities in the music industry is tremendously low. About [23% of artists](http://assets.uscannenberg.org/docs/aii-inclusion-recording-studio-20200117.pdf) in the 2019 Billboard 100 were women or gender minorities. [Women represent 20% or less](https://www.keychange.eu/what-can-i-do/as-a-music-organisation-representative) of registered composers and songwriters, while 98% of works performed by major orchestras are [by male composers](http://www.drama-musica.com/stories/2018_2019_orchestra_seasons.html).

This bias is also present [in streaming services](https://ec.europa.eu/jrc/en/publication/eur-scientific-and-technical-research-reports/playlisting-favorites-spotify-gender-biased). [A few female “superstars”](https://program.ismir2020.net/static/final_papers/148.pdf) dominate among the most popular artists, but most female and mixed-gender artists are in the [lower levels of popularity](https://program.ismir2020.net/static/final_papers/148.pdf). While the problem stems from beyond the music industry, online music platforms and their algorithms that recommend music – called recommenders – [play a large role](https://arxiv.org/abs/2009.01715).

* * *
Read more:  
[Music streaming: listening to playlists drives down the revenue of smaller artists](https://theconversation.com/music-streaming-listening-to-playlists-drives-down-the-revenue-of-smaller-artists-156926) 
* * *

## Our study

While previous studies have repeatedly asked consumers for their opinion, the music artists, those providing the content, are [rarely in the loop](https://arxiv.org/abs/1911.05395).

We wanted to put the spotlight on artists. We asked musicians to give us their views on what would make online music platforms more fair. When they said gender imbalance was a major problem, we decided to study this in more detail.

Our analysis of around 330,000 users’ listening behaviour over nine years showed a clear picture – only 25% of the artists ever listened to were female. When we tested the algorithm we found, on average, the first recommended track was by a man, along with the next six. Users had to wait until song seven or eight to hear one by a woman.<figure class="align-center ">

{{< figure src="pixabay_xbox_musix_windows-phone-1092785_1920.jpg" alt="Close up of a phone with the Xbox music application on the screen" title="Applications like Spotify use algorithms to find recommendations.<br>[Image](https://pixabay.com/photos/windows-phone-music-mobile-phone-1092785/)></a> by [Štěpán Vraný](https://pixabay.com/users/1767892-1767892/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1092785) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1092785)" >}}


## Breaking the loop

As users listen to the recommended songs, the algorithm learns from these. This creates a feedback loop.

To break this feedback loop, we came up with a simple approach to gradually give more exposure to female artists. We took the recommendations computed by the basic algorithm and re-ranked them – moving male artists a specified number of positions downwards.

In a simulation, we studied how our re-ranked recommendations could affect users’ listening behaviour in the longer term. With the help of our re-ranked algorithm, users would start changing their behaviour. They would listen to more female artists than before.

Eventually, the recommender started to learn from this change in behaviour. It began to place females higher up in the recommended list, even before our re-ranking. In other words, we broke the feedback loop.

This shows how easy it can be. Our simple method can help address the biases in the algorithms that play a large role in the way many people discover new music and artists. Next, we hope to study how real consumers perceive the changes introduced by the re-ranking strategy and how it impacts their listening behaviour in the long term.

Another crucial step would be to collect and use data about the wide scale of gender identities. We’re aware this binary gender classification does not reflect the [multitude of gender identities](https://doi.org/10.1080/15532739.2018.1538841). The unavailability of data beyond the gender binary is a massive obstacle, both for research as well as for taking action and making progress on a societal level.

So far, our simulation could demonstrate the benefits of a simple re-ranking approach. But responsibility is, of course, not with the platform providers alone. Initiatives such as [Keychange](https://www.keychange.eu/) and [Women in Music](https://www.womeninmusic.org/) are working to represent the underrepresented in the music industry. The rest of us need to follow.

As music festivals are being criticised for the [lack of women](https://www.theguardian.com/music/2021/mar/26/music-festivals-return-to-uk-but-lineups-still-lack-women) in their lineups, any step towards representing more women all genders in a more balanced manner is a step in the right direction.<!-- Below is The Conversation's page counter tag. Please DO NOT REMOVE. -->

<img loading="lazy" style="border: none !important; box-shadow: none !important; margin: 0 !important; max-height: 1px !important; max-width: 1px !important; min-height: 1px !important; min-width: 1px !important; opacity: 0 !important; outline: none !important; padding: 0 !important; text-shadow: none !important;" src="https://counter.theconversation.com/content/158016/count.gif?distributor=republish-lightbox-basic" alt="The Conversation" width="1" height="1" /> <!-- End of code. If you don't see any code above, please get new code from the Advanced tab after you click the republish button. The page counter does not collect any personal data. More info: https://theconversation.com/republishing-guidelines -->
<br>
[Christine Bauer](https://theconversation.com/profiles/christine-bauer-1221184), Assistant Professor of Human Centred Computing, _[Utrecht University](https://theconversation.com/institutions/utrecht-university-1354)_ and [Andrés Ferraro](https://theconversation.com/profiles/andres-ferraro-1221187), PhD Candidate, Information and Communication Technologies, _[Universitat Pompeu Fabra](https://theconversation.com/institutions/universitat-pompeu-fabra-2457)_

<br>

{{< cite page="ferraro-2021-break-the-loop" view="4" >}}
