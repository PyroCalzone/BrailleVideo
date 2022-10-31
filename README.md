<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--  <a href="https://github.com/PyroCalzone/BrailleVideo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

<h3 align="center">BrailleVideo</h3>

  <p align="center">
    Represent videos with braille characters.
    <br />
    <a href="https://github.com/PyroCalzone/BrailleVideo/issues">Report Bug</a>
    ·
    <a href="https://github.com/PyroCalzone/BrailleVideo/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* [ffmpeg](https://ffmpeg.org/) installed in Python/Scripts.
* [sk-video](http://www.scikit-video.org/stable/)
* [pygame](www.pygame.org)

### Installation

1. Clone the repo
 ```sh
 git clone https://github.com/PyroCalzone/BrailleVideo.git
 ```
2. Download the Prerequisites


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* `convertVideo(file)` converts mp4 file to braille frames. Compression skips frames E.G. `fps, frames = convertVideo(videoFile, compression=2)`
* `playVideo(fps, frames)` plays braille video using pygame, more accurate than terminal. E.G. `playVideo(fps, frames, audioFile=audioFile)`
* `playVideoTerminal(fps, frames)` plays braille video using terminal. E.G. `playVideoTerminal(fps, frames)`
* `audioFromVideo(file)` converts video file into mp3 for use with `playVideo(audioFile=)`. E.G. `audioFile = audioFromFile('BadApple.mp4')`
* `convertToBraille(code)` converts braille code into braille characters. Left column top to bottom: 1, 2, 3, 7. Right column top to bottom: 4, 5, 6, 8. so code `123568` is `⢷`


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Braille dictionary
- [x] Convert pixels to braille data
- [x] Terminal video player
- [x] Non-Terminal video player
- [x] Audio with video player


See the [open issues](https://github.com/PyroCalzone/BrailleVideo/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pyro - [Discord Server](https://discord.gg/udf9HJpGKP) - pyrocalzoneemail@gmail.com

Project Link: [https://github.com/PyroCalzone/BrailleVideo](https://github.com/PyroCalzone/BrailleVideo)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PyroCalzone/BrailleVideo.svg?style=for-the-badge
[contributors-url]: https://github.com/PyroCalzone/BrailleVideo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PyroCalzone/BrailleVideo.svg?style=for-the-badge
[forks-url]: https://github.com/PyroCalzone/BrailleVideo/network/members
[stars-shield]: https://img.shields.io/github/stars/PyroCalzone/BrailleVideo.svg?style=for-the-badge
[stars-url]: https://github.com/PyroCalzone/BrailleVideo/stargazers
[issues-shield]: https://img.shields.io/github/issues/PyroCalzone/BrailleVideo.svg?style=for-the-badge
[issues-url]: https://github.com/PyroCalzone/BrailleVideo/issues
[license-shield]: https://img.shields.io/github/license/PyroCalzone/BrailleVideo.svg?style=for-the-badge
[license-url]: https://github.com/PyroCalzone/BrailleVideo/blob/master/LICENSE.md
