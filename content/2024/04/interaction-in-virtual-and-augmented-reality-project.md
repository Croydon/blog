---
Title: Interaction in Virtual and Augmented Reality
Description: My project for the university course Interaction in Virtual and Augmented Reality.
Date: 2024-04-02 00:01 +0200
Image: /assets/2024/ivar/thumbnail.jpg
Template: single
---

This is my report for my university project for the course Interaction in Virtual and Augmented Reality.


## Motivation

We have been given an [existing VR project](https://github.com/wenjietseng/VR-locomotion-parkour). In this virtual environment exists a race track through a city. Along the way are collectable coins. The race track is structured in three different areas. Shortly before a new area, a task has to be done, at which a T-shaped object has to be selected, rotated and moved in the second T-shaped object. Ideally, those two T-objects are then exactly at the same position with the same rotation, so that you can't distingish them anymore.

We had the following tasks:
  * Implement a locomotion method
  * Implement a method that allows selection, moving and rotation of the T-objects
  * Implement something that reduces cyber-sickness
  * Design and execute a study to evalute the results


## Initial Implementation Idea

My initial idea was to implement some flying. Either some Ironman-like flying locomotion where you put your open hands down horizontally and it applies some upwards force and some force in the direction of where you are looking. Or some Superman-like flying where you have some power-pose that let you fly in the direction of your strechted arm, both horizontal and vertical.

For the interaction task, I wanted to stay in this superhero-themed setting and either use some Ironman-like energy beams that attach to the T-object on the first hit and then rotates and moves with your hand. Or effectively the same thing with some Spiderman webs.

For the cyper-sickness reduction, I planned to implement a tunnling vignette.


## Technical Details and Actual Implementation

### General

The implementation is build with Unity and requires a Meta Quest 2 headset to run. 

The original implementation used Unity 2021.3.10f1 and the Oculus Integration 46.0 package. Over the timespan of my development, I first updated to the latest Unity patch version and later performed an upgrade to Unity 2022.3.19f1. First of all, I wanted to be able to use all currently existing engine features and packages, that only work with newer Unity versions, and secondly, even more important, I also had another university project at the same time, that was also implemented in this Unity version. I did not want to learn and work with two different Unity version simultaneously, particular as I keep getting the impression, that Unity is changing things regularly in a backwards incompatible way.

Upgrading Unity to the 2022.3 LTS version also forced me to migrate from the now legacy Oculus integration, that was directly available from the Unity package registry, to the new Meta SDKs, that are either available from the Unity Asset Store or directly via Meta's npm registry. (Side node: The Unity package manager builds upon npm. Therefore other npm registries can be added and then directly used inside the Unity Editor's package manger.) I first went with the Asset Store version as I was already used to this workflow as I am also using other assets from there, but I had to switch to Meta's npm registry later on, when I added continuous integration (CI) and continuous delivery (CD) to my git repository, since the Asset Store always requires authentication with an Unity account, even for free assets, and my CI system does not support this for the Asset Store at the moment.

Unity itself has several official packages for XR development. I experimented around with several of them, but ultimately do not use them in my final state of the project. Those XR packages do not seem to be compatible with Meta SDKs, therefore would have required me to re-implement everything and re-learn a lot. For this, the time was to limited. However, I have the impression that Unity's XR packages are probably a solid choice for any new project, for several reason:

  * They work with a wider range of XR hardware, not just Meta hardware.
  * They come with a lot of ready-to-use functionality for interactions, locomotions and cyber-sickness reduction methods I would have been interested in, that in part do not exist at all or in that specific way in the Meta SDKs.
  * My subjective, perhabs misleading, impression is also, that there seems to be an overall trend towards those Unity packages. I oftentimes found more up-to-date information how to do X, Y, Z with those integrations, but had a much harder time to find the same information for the Meta SDKs.


At the end, I also enabled Meta Quest 3 as a build target, however, this is completely untested and my project might not work at all with Quest 3 hardware.


### Locomotion 

### Cyber-Sickness Reduction

### Interaction



## Unity Quirks (rename, remove?)

This was also a major pain point while working with Unity in general...

Incompatibility between Unity versions, Unity package versions, different implementation methods to accomplish very similar things etc. make it really, really hard to find information and resources that are actually working for my specific use case. Several scripts and packages did not work with my version etc.

## CI / CD


## Study


### Study Design



<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/WJ9H1r-tjjA?si=LRXK7RNcCNR2oxgA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Study Results

#### Pre-Study


#### Study


#### Discussions


## Future Work


## Conclusion


## Resources

  * [Implementation Repository](https://github.com/Croydon/tuda-vr-parkour)
    * [APK Downloads for Meta Quest 2](https://github.com/Croydon/tuda-vr-parkour/releases)
  * [Study Data Repository](https://github.com/Croydon/tuda-vr-parkour-study)
  * [Study Task Walkthrough](https://www.youtube.com/watch?v=WJ9H1r-tjjA)
