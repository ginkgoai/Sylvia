---
title: "live cyanotype effect in touchdesigner using TOPs :: [BEGINNER-FRIENDLY TOUCHDESIGNER TUTORIAL]"
source: "https://www.youtube.com/watch?v=5ozEu9vtoPQ"
author:
  - "[[wxll]]"
published: 2026-07-11
created: 2026-07-20
description: "this beginner-friendly cyanotype effect and exact textures used in this tutorial are available for download on Patreon. find this and more exclusive projects / tutorials here :: [patreon.com/cw/wxllhx"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=5ozEu9vtoPQ)

this beginner-friendly cyanotype effect and exact textures used in this tutorial are available for download on Patreon. find this and more exclusive projects / tutorials here :: \[patreon.com/cw/wxllhx\](https://www.patreon.com/wxllhx/posts/live-cyanotype-161961375)  
  
patreon :: https://www.patreon.com/cw/wxllhx  
instagram :: https://www.instagram.com/wxll.hx/  
tiktok :: https://www.tiktok.com/@3.27wx  
  
copyright credits for music belong to the original owners.  
:: shoutout https://www.instagram.com/jakobdkr/ for the music!  
  
#touchdesigner #cyanotype #printed #visualeffects #livevisuals #td #download

## Transcript

**0:01** · Hey everyone, today we are going to learn how to do this cyanotype effect in TouchDesigner using tops.

**0:07** · It's the same effect I used in this video that I posted online that did pretty well.

**0:12** · So, what's nice about this effect is that it can be used both on static photos and live video feed.

**0:19** · Um before we get started, I kind of want to give some intuition or a framework or a way to think about this project.

**0:27** · So, you can kind of get a sense for the logic behind it.

**0:32** · I think when people use TouchDesigner online, you can do a lot of things like blob tracking or particle work that you can't really do in other softwares, but TouchDesigner is just as much of a creative tool as any other platform \[music\] or app like Photoshop or Illustrator.

**0:53** · And what this means is that the thinking can be taken from places like Photoshop and applied to TouchDesigner.

**1:00** · And more specifically, I think the logic of applying textures um is something I don't really see a lot on TouchDesigner tutorials.

**1:10** · So, imagine using Photoshop for those who know, and you \[music\] have, you know, some kind of image, and you have a texture you want to apply.

**1:20** · You know, you have all these operations, same as Photoshop, like pin light, reflect, screen, multiply, difference, and all that logic is still the same. \[music\] So, when you apply that logic to projects like TouchDesigner, you can get really fun live video input as opposed to only having to do a static one.

**1:41** · So, that's sort of the thinking that went behind it. For a quick project tour, we are going to take our input, whether it's photo or video, extract its resolution data.

**1:53** · We are going to use a lot \[music\] of sort of leveling to play around with things like brightness, contrast, gamma.

**1:59** · Then apply a bunch of texture. And then lastly, we are going to use a lookup so we can apply color. And that's it. So, it's a very simple network, but I think it's sort of the way of thinking about it that's important. So, without further ado, let's get started.

**2:15** · All right. So, the first thing we are going to want to do is hit tab. And then click movie file in. And this will allow us to bring \[music\] in any image from our desktop. So, how we do that is we hit the plus and then you you can just choose from \[music\] your desktop.

**2:31** · But, I already have my inputs. So, I'm going to paste them in.

**2:36** · So, now we have our photo. As you can see, we're using movie file in.

**2:40** · Alternatively, if you want to use a live video feed from your, you know, webcam or laptop camera, you can use video device in. And then more likely than not, it will be flipped on the x-axis. So, you want to hit flip.

**3:00** · And then choose flip X, and then you'll have your video input.

**3:06** · So, the first thing we want to do is put a null, and we are going to name it input.

**3:13** · So, this can be named whatever, but the reason why we are doing this is because later on when we reference a bunch of nodes, we want it to be very clean. We want it to point to sort of just one standardized node.

**3:32** · Because let's say later on we have a photo that's vertical, and we don't want to use this horizontal photo anymore.

**3:37** · Instead of changing all the reference names or having to re-drag um the input to it, if we just from the get make it standardized and reference only this node that's called input, we can have a dynamic um changing project.

**3:55** · And it'll make \[music\] more sense later on.

**3:57** · So, for the first thing is we want to extract this resolution data. So, if you right-click and go to info, it will tell \[music\] you the size.

**4:07** · But, another way we can do this dynamically, so, you know, if we switch inputs, we already have the resolution immediately, is we can \[music\] drag, hit tab, and then go to chop, and select info.

**4:21** · From with info, we have a lot of really useful information.

**4:25** · But, the ones that we care about today are res X and res Y.

**4:29** · So, to select them, just so it looks a little cleaner, um drag out from the end, hit tab, and then choose select.

**4:38** · So, from channel names, if you hit the drop-down, you can now choose, so choose res X, do it again, res Y.

**4:45** · So, now we have our resolution.

**4:47** · Once again, just so it's a little cleaner, you can use a null, and just name it something like res, or resolution. And once again, for these naming conventions, they can be anything. So, whatever helps you understand it, please name it that.

**5:05** · Great.

**5:06** · So, now anytime we, you know, import a photo, like textures, we can use this to always crop it, so everything's the same size, which is really useful. So, you don't have to do it, but just so you kind of get the idea, drag from input, hit tab, we click on fit, go to common, and we hit the little star on res to make it active.

**5:29** · If we drag res X into the X resolution and Y into the res, sorry, the res Y into the Y resolution, reference them, now we can see it's always going to be that size.

**5:44** · So, that's sort of the first part. All right. So, for the next step, I think it's important to understand what you are working towards. So, you have sort of many tasks to complete before you get to the final picture.

**5:59** · So, we know that the final product we want something that's pretty decently contrasted, is only blue and white, and something that looks like there's a paper texture on it.

**6:12** · So, to translate sort of those ideas, we can use a level top.

**6:17** · So, drag from the end, hit tab, choose level.

**6:22** · And then, whatever we just described, we can pretty much translate here. So, let's set something slightly more contrasted.

**6:30** · Maybe a little opaque, so we can see a texture really nicely.

**6:36** · Um yeah, to sort of emphasize on the contrast, we can do black level here, and then turn down the gamma bit.

**6:45** · So, for the next part, what we want to do is apply our paper texture.

**6:53** · And eventually, we will combine it with this input. So, the link to the textures are in my bio, and also on Patreon, but same thing, you use \[music\] your file in. So, I'm just going to copy it in cuz I already have it.

**7:11** · And you might get something like this.

**7:14** · That's fine. If you have a free version, it just means it's limiting the resolution, which is expected.

**7:19** · So, great. So, now that we have our texture in here, if you right click and go to info, we can see that this isn't the same resolution as our base photo, which is 1280 and I think 1080. \[music\] So, that's where we can use this system.

**7:38** · So, after it, hit tab, choose fit.

**7:41** · And then, hit P, common, and then we want to drag and drop this resolution into here, so it's the same size.

**7:51** · So, now um it works.

**7:57** · So, now it's cropped to match the size.

**8:00** · It might be kind of hard to tell, but if you right click and hit info, now we can see that it's 1080 by 720, which I guess is the original size of photo.

**8:10** · Great.

**8:10** · After that, we want to make it slightly opaque, so we can sort of combine \[music\] the two, and it will look layered on really nicely.

**8:18** · So, go to level, and then post, and then lower the opacity.

**8:24** · And bring it to comp.

**8:27** · And then, great. It looks like nothing happened, but we just have to choose the operation. So, one way you can do it, um cool trick I learned is that if you hit preview grid, and you make it active, these are every single operation that they look like.

**8:41** · So, just a little trick, but to save us the time, go to operation, and we choose pin light.

**8:48** · Great.

**8:49** · So, now we need to make this black and white, but we can start seeing things like, you know, there's a slight texture over the figure have all this color, so we know we are on the right track.

**9:02** · So, to make this black and white, drag, hit tab, choose monochrome.

**9:10** · Great.

**9:11** · And then, let's choose levels, so we can make some more adjustments.

**9:18** · And then, I think we can make this even more contrasted, so let's do something like 1.95.

**9:25** · Great. So, that already looks a lot better.

**9:28** · And then, you can do this now or later on, but if you, for example, want it to be like the blue is on the darker and the white's on the lighter part or vice versa, you can invert it. So, just for the sake of demonstration, um if you do level again, go to invert and set it to one.

**9:51** · So, now we can see it's perfectly inverted.

**9:55** · And maybe we want to apply even more contrast.

**10:00** · Why not?

**10:01** · So, set it to 1.7 and gamma Great. So, this looks pretty good.

**10:18** · So, yeah. The next step, we are going to apply even \[music\] more texture.

**10:24** · So, but if we see what we have so far, it already looks pretty good. And this was just from applying a texture and playing around with the level of it. For the next part, we want to sort of apply a texture where it looks like it's been printed or misprinted and there is smudge. So, the type of texture we can use is called a dirty scan.

**10:46** · So, this will be available on my Patreon, but if you go online and just search up like high quality, high resolution dirty scan texture image, you should get a bunch. And you can go to Texture Labs or Unsplash, there's a bunch of websites. But, the first thing we need to do is make sure that this is the same resolution, which it's not.

**11:08** · So, after it drag, hit tab, and then go to fit.

**11:15** · And once again, hit P, and then go to common, and then drag and drop from earlier um the resolution.

**11:26** · So, now it will probably, yeah, it will bleed on the side. That's because of the type of fit. So, for the fit, you want \[music\] to select fit outside.

**11:36** · So, now it fits fully into that resolution.

**11:41** · So, now if you want to make more edits like have it be more contrasted or you want to bump up the highlights more so they are more apparent, you can add a level after.

**11:51** · But actually for this one, we don't need to, which is really nice.

**11:55** · And then once again after it, use a null so it just cleanly ends this segment of the project. So, null and then we can just name it something like dirty scan.

**12:06** · And once again, this is just arbitrary.

**12:07** · \[music\] It just helps me understand what it is.

**12:10** · So, now we need to combine it onto the level. So, hit tab composite drag both of them into the composite.

**12:19** · And then the operation we want to select is difference.

**12:25** · So nice. Now it looks really good.

**12:30** · Another thing we can do is select everything and then go to common.

**12:34** · And then for viewer smoothness, hit nearest pixel.

**12:37** · It just helps it look \[music\] really like crisp.

**12:42** · So great. Now we just need to make this blue and white.

**12:49** · So let's add a null.

**12:52** · And then maybe we can name this like base. So, it's for like the base image before we add color.

**13:01** · And yeah, I'm actually going to change the display. So sometimes if you work like this, um it's nice cuz you can see what's going on, but it's not nice because it sort of just muddles everything.

**13:13** · So, another way you can display it is um right click like sort of anywhere, hit display and then go to backdrops, turn it off.

**13:21** · And then select the sort of like split in half rectangle.

**13:26** · And then in this top left menu hit top viewer.

**13:31** · Now we can see everything on the side.

**13:34** · So it's a good way to just sort of like clean up the work space and see what you need to see.

**13:39** · So now what we want to use is a look up.

**13:43** · So go to look up and you'll get an error sign and it says second input required and that's because we need to assign what the colors will be based on this. And because this is only black and white, we hit tab, go to ramp and then yeah. So if we plug this in and then maybe I'll just do this just so I don't have to keep changing the display.

**14:09** · Nothing has changed.

**14:11** · But let's say we flip it and then this part I'm just showing to demonstrate.

**14:18** · It becomes inverted.

**14:19** · And that's because it's looking up the new color from the second input. So it's saying that from the darkest part it should be white and the lightest part should be black.

**14:32** · So if we look at the original one, it doesn't change because yes, the darkest is dark and the brightest part is white. If we flip it though, it's saying the darkest part now is white and the brightest part now is blue.

**14:43** · So what we want here is that the dark parts are blue and the \[music\] white light parts are white.

**14:50** · So click on the black portion of the ramp and then we are just going to play around until we get the blue we want.

**15:00** · So um yeah. So you can see now we have blue.

**15:05** · Which is great. So you can just play around with these. It's not a um a formal science.

**15:13** · But you just kind of do it until you find a color that you really like.

**15:16** · Honestly, this one's pretty good.

**15:18** · So yeah. Now we have this really great textured effect with color. And if you want to invert it, there's a lot of ways you can do it.

**15:29** · You can, you know, once again, go to here before and change \[music\] the actual like image input and then invert it there.

**15:37** · Another way you can do it is invert the ramp, so right click on the node, insert operator, go to flip, flip X, and then it flips on the X axis.

**15:47** · Um but yeah, so that's actually it.

**15:54** · So we have this really nice sort of printed effect.

**16:04** · Um and with just a couple of nodes we were able to achieve this.

**16:10** · But once again, I think the main thing is that the way to think about it is important and just understanding that you can apply logic from Photoshop into TouchDesigner, you can make really cool visuals like this that can be reactive or take live video input. So your webcam can be that effect.

**16:30** · So I hope you enjoyed this tutorial. If you want the full file, it will be available on my Patreon.

**16:38** · And yeah, consider subscribing to my Patreon. So thank you so much and have a lovely day.