---
Title: About This Blog
Description: Technical setup and background information about my blog
Date: 2020-07-21 11:00 +0200
Image: /assets/2020/pico/pico.png
Template: single
---

# Some Background Information


## The Past

Previously, I had a German tech blog called  _Go DEV!_ and I posted on it from August 2011 until Juli 2014 with two final posts in April and March 2016.

It ran with WordPress and therefore with PHP and MySQL. First on one of my webspaces, later on one of my vServers.

On _Go DEV!_ I posted regularly at the beginning, but the frequency eventually died down. As I explained in the first post back then, the primary concept was to write about computer science news and software which are rather less common - since full-time bloggers will write about the "big news" better anyway as I could as a project in my spare time - but also about computer science basics and every topic that I currently spending time on.

I tried to write most posts in a formal way, tried to optimize site speed and SEO and spent quite a lot of time on making it more _professional_ (whatever that _actual_ means).
This did cost too much time eventually.

In April 2016, I tried to change the concept of the blog. I wrote my first article in English with the title _That Is Why Video Games Matter_, which was also the first post where I directly wrote about the influence tech can have on a single person and society as a whole.

Shortly after, in March 2016, I gave the blog a new design, added a TLS certificate / HTTPS support via Let's Encrypt (which was much more unstable and harder to do than today) and wrote about it in a final post.

A while after, my MySQL server had a complete database corruption, which I could never recover. Thanks to the lack of a comprehensive automated backup strategy, I did not have any up to date version of my blog I could simply restore.

This was the final blow and my motivation to keep _Go DEV!_ going was gone.



## The Present

Since 2016 I considered several times to start blogging again. Sometimes, there are topics that I would like to write about and share my opinion on. Or I worked on projects, learned a few things and would have loved to share this knowledge with more people.

It never came that far as I spent my entire time in university and at home with projects like the original vision of [Inexor](https://inexor.org), which also brought me to [Conan](https://conan.io) and [Bincrafters](https://github.com/bincrafters). Not to forget my Firefox add-on [Vertical Tabs Reloaded](https://github.com/croydon/vertical-tabs-reloaded) and tons of other bigger and smaller projects. Oh, and I also have a private life.

Starting today, I give it another shot. My posts will be much more informal than what I wrote on _Go DEV!_ and I will have other priorities about the topics.

Writing things down is a great way to reflect and getting to the essential information about an issue, without all the noise going on when actively working on a project.

Which effectively means, that I'm writing for myself too.

And if anyone else likes to read about it and maybe even learns a thing or two - great!


## The Setup

While I still think that WordPress has some great features it is just too much for my needs.

This blog is powered by [Pico](http://picocms.org) - a small, simple, flat file CMS. Meaning it has exactly zero MySQL databases which can go corrupt 😄. I have forked the Pico theme [_Story_](https://github.com/BesrourMS/story) and named it [_Historia_](https://github.com/Croydon/pico-theme-historia) since _Story_ lagged several features that I wanted.

Pico allows me to write all pages in Markdown, which has none of the confusing layout issues, WordPress produced sometimes with their WYSIWYG-HTML editor.

All content of this blog is saved in Git repositories - including [Croydon/blog](https://github.com/Croydon/blog/) and [Croydon/blog-assets](https://github.com/Croydon/blog-assets) - meaning a backup strategy is now automatically included by default.

A GitHub Actions Workflow is installing all parts in their correct places, then it starts an Apache web server and Wget is saving all pages to static HTML files, which are then pushed to GitHub Pages and served with my custom domain _blog.cr0ydon.com_.

Voi­là!
