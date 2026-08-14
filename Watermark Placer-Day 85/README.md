# Day 85 Watermark Placer App

## Overview

This app add a transparent logo to an image. It uses pillow package for transforming the images and tkinter for the user interface of the app.

## Notes

**Approach**

First I googled Pillow and read their docs and also viewed tkinter docs as I had forgotten some of its functions. I wanted to have an app which add an image on top of another image. The pillow dos did't help me much so I asked claude to come up with a plan. As I had each problem ready to be tackled through small sub-steps, I made two the user interface and then wrote specific functions for performing each feature. I kept the design simple image on top of two columns of buttons.

**For Improvement** 
I think the app would be much better if it had the functionality to drag the logo on the image, but I don't know how would I keep track of the coordinates. Moreover, it can also has the ability to resize the logo as per user's demands within the app.

**Biggest Learning**
- I learned that I need to keep revising my concepts because I faced difficulty while writing tkinter objects and it required a lot of googling which wasted time.
- Exploring a completely new package was quite a new experience and it required some thinking to understand how pil images and the tk img being displayed are not the same.
- Coding the paste function was also a hassle and required help. Ultimately, I understood that it is much to create a new image each time logo is shifted through the base image rather than updating the image.  

