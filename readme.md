
<div  id="top"></div>


  

<!-- PROJECT SHIELDS -->

<!--

*** I'm using markdown "reference style" links for readability.

*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).

*** See the bottom of this document for the declaration of the reference variables

*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.

*** https://www.markdownguide.org/basic-syntax/#reference-style-links

-->


[![LinkedIn][linkedin-shield]][linkedin-url]

  
  
  

<!-- PROJECT LOGO -->

<br />

<div  align="center">

<a  href="https://github.com/github_username/instant-playlist">


</a>

  

<h3  align="center">INSTANT PLAYLIST</h3>

  

<p  align="center">

An open source playlist recommender system for spotify based on the user input of one song. 

<br />

<br />

<br />

<a  href="https://hzloto-instant-playlist-visual-interface-sn7nag.streamlitapp.com/">View Demo</a>
Note: Server is live but stateless. To use the app, please run streamlit on your local machine

·

<a  href="https://github.com/HZloto/instant-playlist/issues">Report Bug</a>

·


</p>

</div>

  
  
  

<!-- TABLE OF CONTENTS -->

<details>

<h3>Table of Contents</h3>

<ol>

<li>

<a  href="#about-the-project">About The Project</a>

<ul>

<li><a  href="#built-with">Built With</a></li>

</ul>

</li>

<li>

<a  href="#getting-started">Getting Started</a>

<ul>

<li><a  href="#prerequisites">Prerequisites</a></li>

<li><a  href="#installation">Installation</a></li>

</ul>

</li>

<li><a  href="#usage">Usage</a></li>

<li><a  href="#roadmap">Roadmap</a></li>

<li><a  href="#contributing">Contributing</a></li>

<li><a  href="#license">License</a></li>

<li><a  href="#contact">Contact</a></li>

<li><a  href="#acknowledgments">Acknowledgments</a></li>

</ol>

</details>

  
  
  

<!-- ABOUT THE PROJECT -->

##  About The Project

  


  

Instant playlist replicates the way most music recommender systems work at a simpler scale. The app uses a mix of **Collaborative filtering** and **Feature analysis** to recommend a playlist based on a given song input. We first use user similarities to find groups of artist like the one we picked, then leverage the Spotify feature analysis to find the tracks that are most similar.
  
  


  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- GETTING STARTED -->

##  Getting Started

  

To get a local copy up and running follow these simple steps.

  

###  Prerequisites

  

Any version of Python 3 will work with the project, but some libraries need to be downloaded. They are listed below: 

* Pandas
* html_to_json
* spotipy
* scipy
* streamlit


```sh
#Run the below code in your terminal 

pip install pandas
pip install html_to_json==2.0.0
pip install spotipy==2.20.0
pip install scipy==1.8.1
pip install streamlit


```

  

###  Installation

  

1. Get a free API Key at [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/)

2. Clone the repo

```sh

git clone https://github.com/HZloto/instant-playlist.git

```

3. Input your Spotify API keys

Change all references to `client_id` and `client_secret` to your credentials in `main.py`, `database.py` and `playlist_API.py`
  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- USAGE EXAMPLES -->

##  Usage

  

To use the app, type in your terminal:

```sh
streamlit run visual_interface.py
```
  You will be redirected to the in-browser app. Enter an artist, pick a song, and wait for the Spotify URL of your playlist to be returned! 

_Our teacher is a fan of Muse. Find the playlist created for him [HERE](https://open.spotify.com/playlist/2QX5ZbJYT4GBIwHrtjBDwo)_

  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- ROADMAP -->

##  Framework

  The flowchart below shows the relation between the scripts. 
  ![alt-text](https://raw.githubusercontent.com/HZloto/instant-playlist/main/app_flow.jpeg)

- [ ] Visual Interface
- Using open source app framework streamlit, generate a dynamic page for the user

- [ ] Scrapper
- Crawl a website that offers similar artists to an input using requests and json

- [ ] Input API
- Using spotify API the ID of the artist is retrieved and passed to the next steps

- [ ] Database
- Using API endpoints to get top 5 songs of all similar artists and their features.

- [ ] Recommender
- Using spatial distance between user-picked song and each of the selected artist’s songs. Powered by scipy.

- [ ] Playlist API
- This script creates a public playlist and afterwards adds the 50 recommended songs to it.



  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- CONTRIBUTING -->

##  Contributing

  

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

  

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

  

1. Fork the Project

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- LICENSE -->

##  License

  

Distributed under the MIT License. See `LICENSE.txt` for more information.

  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- CONTACT -->

##  Contact

  

Hugo Zlotowski - zlotowski.hugo@esade.edu

  


  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- ACKNOWLEDGMENTS -->

##  Acknowledgments

This app was developed for educational purposes with the following team:

*  []() Demi Vinke

*  []() Chris Cauchi

*  []() Martin Garica
* Juan Esteban Perez Isaza

  

<p  align="right">(<a  href="#top">back to top</a>)</p>

  
  
  

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]:  https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge

[contributors-url]:  https://github.com/github_username/repo_name/graphs/contributors

[forks-shield]:  https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge

[forks-url]:  https://github.com/github_username/repo_name/network/members

[stars-shield]:  https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge

[stars-url]:  https://github.com/github_username/repo_name/stargazers

[issues-shield]:  https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge

[issues-url]:  https://github.com/github_username/repo_name/issues

[license-shield]:  https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge

[license-url]:  https://github.com/github_username/repo_name/blob/master/LICENSE.txt

[linkedin-shield]:  https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]:  https://www.linkedin.com/in/hugo-zlotowski-770974135/

[product-screenshot]:  images/screenshot.png

[Next.js]:  https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white

[Next-url]:  https://nextjs.org/

[React.js]:  https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB

[React-url]:  https://reactjs.org/

[Vue.js]:  https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D

[Vue-url]:  https://vuejs.org/

[Angular.io]:  https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white

[Angular-url]:  https://angular.io/

[Svelte.dev]:  https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00

[Svelte-url]:  https://svelte.dev/

[Laravel.com]:  https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white

[Laravel-url]:  https://laravel.com

[Bootstrap.com]:  https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white

[Bootstrap-url]:  https://getbootstrap.com

[JQuery.com]:  https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white

[JQuery-url]:  https://jquery.com