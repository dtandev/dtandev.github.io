---
title: Sport Activity Animation
summary: Turns a GPX track, photos and an event logo into an interactive animation of a sport activity.
date: 2026-10-02
image:
  preview_only: true
tags:
  - Python
  - GPS
  - Sport
  - Visualization
links:
  - name: Code
    url: https://github.com/dtandev/dtandev-running-animation
    icon: brands/github
draft: true  # hidden until InstaRun is ready to be announced; remove this line to show the project again
---

I wanted a better way to show a race or a training than a static map and a screenshot of a watch. The tool works with any activity recorded in a GPX file, whether it is running, cycling or skating. You give it the track, a folder of photos, the event logo and the event name, and it produces one HTML file. A dot moves along the route while time, distance, pace, elevation and heart rate update live. The track can be coloured by pace, heart rate or elevation, and photos pop up as pins when the athlete reaches the place where they were taken.

The animation below is a real skating marathon in Ruciane-Nida. Press Play, change the speed, switch the colouring with the icons on the map, or click a photo pin. The positions of the photos here are illustrative: the pictures carry no GPS data, so I spread them over the route.

{{< iframe src="/demos/mazurski-maraton-rolkowy.html" title="Animation of the Mazurski Maraton Rolkowy" height="720" >}}

It is a single file with no server behind it, so it can be sent by mail or hosted anywhere. The map tiles and the Leaflet library load from the internet. If a photo has no GPS tags the tool falls back to the capture time, and if that is missing too it assumes the photos were taken ten minutes apart.

The code, with the README and an explanation of how it works, is on [GitHub](https://github.com/dtandev/dtandev-running-animation).
