---
title: Where does a photo belong on a GPS track?
summary: How the Sport Activity Animation tool decides where to put a photo on the route when the photo has no position of its own.
date: 2026-10-03
tags:
  - GPS
  - Photos
  - Python
image:
  caption: A generated animation with photo pins and camera badges on the elevation profile.
draft: true  # hidden together with the project page, which it links to; remove this line to show the post again
---

A photo from a race is only useful on a map if the map knows where it was taken. Photos from a phone usually carry a GPS position in their EXIF data. Photos from a professional camera, screenshots and pictures that went through a messenger usually do not. The [Sport Activity Animation](/projects/sport-activity-animation/) tool has to place all of them, so it decides for every photo separately, using the first method that works.

## Four ways to find the place

1. **A manual entry.** A small file next to the photos can say where a picture belongs, either as a distance along the track or as a latitude and longitude. It overrides everything else.
2. **GPS tags in EXIF.** Photos further than 50 metres from the track are skipped, because they were taken somewhere else.
3. **The capture time.** The tool compares it with the timestamps of the track. Cameras often write the time without a time zone, so the tool picks the offset from UTC that fits the most photos inside the activity.
4. **An assumption.** If nothing else is available, the photos are taken to be ten minutes apart, in file name order.

The last two methods are guesses, and the page says so: the popup of such a photo carries a note that its position is approximate.

## The manual file

For photos without any position, the manual file is the simplest fix:

```json
{
  "IMG_0412.jpg": {"km": 12.4},
  "IMG_0431.jpg": [53.7712, 20.4769]
}
```

The first entry puts the photo 12.4 kilometres into the track, the second gives exact coordinates.

## A limitation to know about

Matching by position takes the nearest point of the track. On a route that passes the same place twice, a photo can land on the wrong pass. The capture time does not have this problem, which is one more reason to prefer it when the camera clock is right.

The code and the details are on [GitHub](https://github.com/dtandev/dtandev-running-animation).
