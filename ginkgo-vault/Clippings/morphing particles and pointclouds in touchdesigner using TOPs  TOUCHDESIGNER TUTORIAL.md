---
title: "morphing particles and pointclouds in touchdesigner using TOPs :: [TOUCHDESIGNER TUTORIAL]"
source: "https://www.youtube.com/watch?v=sE716KGZw0w"
author:
  - "[[wxll]]"
published: 2026-07-06
created: 2026-07-20
description: "this pointcloud morphing effect and exact .ply files used in this tutorial are available for download on Patreon. find this and more exclusive projects / tutorials here :: [patreon.com/cw/wxllhx]( htt"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=sE716KGZw0w)

this pointcloud morphing effect and exact .ply files used in this tutorial are available for download on Patreon. find this and more exclusive projects / tutorials here :: \[patreon.com/cw/wxllhx\]( https://www.patreon.com/cw/wxllhx)  
  
patreon :: https://www.patreon.com/cw/wxllhx  
instagram :: https://www.instagram.com/wxll.hx/  
tiktok :: https://www.tiktok.com/@3.27wx  
  
copyright credits for music belong to the original owners.  
  
#touchdesigner #pointclouds #particles #mediapipe #livevisuals #td #download

## Transcript

**0:01** · Hi everyone. Today we'll be going over how I did this effect in TouchDesigner using point clouds and tops.

**0:08** · So here I use MediaPipe to control the morphing, but for the sake of simplicity, we'll just use our keyboard. So if you hold down the one key on your keyboard and release, it will morph in the exact same way as the demo video.

**0:23** · Um we'll also just use two, but you can use as many point clouds as you like and you can use whatever models you like as well.

**0:29** · So for a quick overview of the project, um we are going to learn how to create an \[music\] instancing network using positions and color data.

**0:38** · Um we're going to set up a little system to control the particles exploding and then morphing back into place smoothly.

**0:47** · Um how to make a quick little um cage for the particles and some really simple post-processing to create this really cool effect. So without further ado, um let's get started.

**0:58** · All right. So the first thing we are going to want to do is import our point cloud file. So hit tab and then because we're using tops, um select point file in.

**1:11** · And then this way you can add your point cloud file.

**1:14** · It's important to note that if you hit red, green, and blue, you'll have these options, but not all point cloud files have that.

**1:24** · The general gist is for red, green, and blue, it's probably going to be either XYZ, RGB, \[music\] or red, green, blue.

**1:32** · Um select one of those for these.

**1:35** · But for today, I'm just going to copy and paste mine in cuz I already have them.

**1:41** · So yeah, these don't look like the models, but that's fine.

**1:46** · The first thing we are going to need to figure out \[music\] is the sort of number problem.

**1:53** · What I mean by that is \[music\] if you double click and then press You will see that there are 403 thousand 225 pixels.

**2:04** · For the second model, there are not that many. There are less.

**2:10** · So, why does this matter?

**2:11** · So, for instancing, we can think of it like particle number one, you know, has sort of its position data and eventually its color data.

**2:22** · When we morph them, \[music\] we need to give it an instruction of like, "Hey, particle one, instead of being here, I want to move \[music\] you to some other location with some other color."

**2:33** · And that's fine.

**2:35** · However, as soon as we get to particle 239,122, you know, this this doesn't exist.

**2:45** · So, this particle from the first model will try morphing into something that does not exist.

**2:51** · And then you will not be able to do the effect.

**2:54** · So, the main problem we need to solve is how to make them the same size.

**3:00** · This way, no matter what point cloud file you use, whether it's too big or too small, it will have the exact same amount of points, and we can then do this effect for however many point clouds we want.

**3:11** · So, let's first start with handling the position data.

**3:15** · So, first we are going to want to add a point transform.

**3:20** · This will allow us to, for example, change the scale of all the points later on.

**3:25** · This isn't important now, but we'll get back into it in a bit.

**3:29** · So, one way we can solve the number issue is using two fit tops.

**3:36** · So, if we drag and then hit tab, and then fit, what we can do is go to common, and we can set the output resolution to two times.

**3:48** · What this does is um it increases the resolution by two times. But, what's important is that if you double click, you'll see that there are now over a million particles. Way over a million.

**4:01** · So, we have a lot of particles.

**4:04** · Um, but, you know, if we go to fit again, and we hit common, we can then do output resolution to limit resolution.

**4:14** · And then, I like using 800 by 800, but you might need to do less if your computer can handle it, and you can do more if your computer can.

**4:24** · By doing this, now we have 640,000.

**4:30** · So, this might not seem important, but now if we copy and paste all of these, and do like copy, paste, and make our second point cloud the input, if we look at the fit for, it also has 640,000.

**4:49** · So, this way sort of standardizes standardizes, um, how many points \[music\] there are. So, they are all consistent. So, that's great.

**4:57** · So, the last thing we want to do is for fit one, for input smoothness and viewer smoothness, select nearest pixel.

**5:07** · And we want to do the same \[music\] for the other fit.

**5:10** · And then, we want to do it for these two as well.

**5:15** · Great.

**5:16** · And that just helps with the particles looking really crisp later on when we render it.

**5:21** · So, now we have all of our \[music\] position data sorted out. So, now let's handle color.

**5:28** · So, what we are going to want to do is hit tab, and then do point file select, and drag our point cloud right over it.

**5:37** · So, now it's referencing it.

**5:40** · You can see.

**5:43** · And then, same thing. Um, click, and then do red, green, and blue.

**5:52** · Great. So, now something is going on. They're different.

**5:57** · So, we need to make this into color. And the way you do that is attach a math and then you divide by 127.

**6:09** · And then, if you do it correctly, it should be red.

**6:13** · There you go.

**6:13** · And I can explain why this is in another video, but it has something to do with how color values are stored, and they're not between values zero and one.

**6:25** · So, you can do the same thing with the fit trick.

**6:28** · Select both of these.

**6:31** · Now, command C, command V, or copy and paste.

**6:35** · And then, we should see 640,000 pixels.

**6:42** · And that we do.

**6:43** · So, we do the same thing.

**6:45** · Um so, just copy and paste this entire network.

**6:50** · And then, drag your second point cloud to it.

**6:53** · And then, great. Once again, we should see 640,000.

**6:58** · And that we do.

**7:00** · So, now we can set up for our switch system.

**7:07** · So, go to switch in tops. And then, \[music\] we need to connect the position nodes to switch, and then do one again for color.

**7:19** · So, what you can do, if you're really organized, is say, for example, like position, drag in, and then color, drag in.

**7:29** · And then, sim- similarly, position butterfly, color butterfly.

**7:37** · And these naming conventions are completely arbitrary.

**7:42** · They be whatever you want. So, when people tell you to, you know, type POS COL, it has nothing to do with syntax, at least for now.

**7:52** · Um it's just for your own discretion and whatever helps you understand it.

**7:57** · So, if you wanted \[music\] to, you could say for example, like I don't know, position drag.

**8:04** · That works, too.

**8:05** · But, this is just a really clean and simple way of doing it.

**8:09** · So, now we're going to want to attach both of our position nodes into switch.

**8:14** · Both of our color nodes into color switch.

**8:18** · So, now we can see in the switch one if we press P, that we have two inputs, one for the dragon and one for the butterfly, and for color, same thing.

**8:28** · Important, um for both of them, we want to blend between inputs.

**8:35** · This is because, for example, if you have values between zero and one, um so, you know, let's say you want to morph the dragon, you know, something halfway between \[music\] the dragon and the butterfly, um if you do blend between inputs, it will allow you to have a sort of blend, and that's what gives you that really clean morphing effect, where everything switches at the same time.

**8:56** · Great.

**8:57** · \[music\] And then we can sort of really neatly tie this up by adding a null. When I first used TouchDesigner, \[music\] I didn't really understand why people use nulls, but an analogy is that you can treat them \[music\] like periods in sentences. So, when you're writing an essay, you know, you don't have to use periods, but it allows you to discern when you finish an idea \[music\] and when you're starting the next one.

**9:25** · And that's what we're doing. We have finished creating our system for position data and color data, so we add a null. And we can name it position data and color. So, that way, if we make edits in our sentence or thoughts, then it will remain unaffected. But, at least we know that's where it ends. So, we'll come back to this in a bit.

**9:48** · But, just so we can sort of see what's going on, we can start setting up a really simple render setup. So, hit a tab. Go to comp, geometry. Then we see this torus. Um let's get rid of that. So, double click.

**10:05** · Delete that.

**10:06** · Hit tab. Go to sop, then add and then P, and then add points. So, this will make it such that when we instance, we can add points. And then we need to convert that. Convert and then it should be from from type convert to particles per point. And then particle type render \[music\] has points sprites. And then we want to see it in both the render and the geo comp. So, purple render, blue for display.

**10:45** · Great. So, it looks like nothing has happened, which is expected. So, now let's add a camera. Go to comp, then camera, light, and then a render. So, then go to top, render, and we still see nothing, which is expected. So, now we are going to want to instance our lovely data that we prepared.

**11:12** · So, one way \[music\] we can think of instancing is that, believe it or not, each pixel \[music\] on their color represents a coordinate in this sort of three-dimensional \[music\] space. Um I will get to that in another video. But, you know, each pixel has its own coordinate and geographical position baked into it through the color. Um same thing for the actual color. So, this is the actual color that we'll show.

**11:40** · Instead of me manually telling TouchDesigner, "Hey, I want you to put particle two at, you know, this XYZ coordinate." We can just reference this and reference this um really simply. So, we can do so by going to geo1, go to instance, turn instancing on. And then translate op is sort of like the XYZ positions, so it's sort of like your coordinates. So, we are going to want to take our position top, drag it into translate op.

**12:09** · And then for translate XYZ R G B. Now we can see we have something. And I guess it turns out when I was making these models, \[music\] um I didn't take away the bug one. So, you can enjoy, too. But at least we can see our dragon.

**12:29** · Great.

**12:30** · And then to add color, we go to second tab, instance \[music\] two. Go to the color mode. And drag the color top. And once again, R G and B. And we can see we have a red dragon. Cool. So, now we can adjust the sizes of these points using material.

**12:53** · So, hit tab.

**12:54** · Go to mat.

**12:56** · And then point sprite. And then drag it onto \[music\] the geo. And select the material.

**13:03** · Great.

**13:03** · So, if you go to point sprite, to change the size \[music\] of these particles, we can change it here. So, you want it bigger, you just drag it up. You want it smaller, you just drag it down. And great. I think 0.7 looks pretty cool. So, it gives that, you know, what it is, \[music\] but when it morphs, it's pretty obvious.

**13:26** · So, great.

**13:28** · Now we have that. So, we now \[music\] need to switch between each one really cleanly. So, now we will create \[music\] our chop set up. So, we can do things like switch between them, explode the particles, and all that. So, um here's how we do it. So, the first thing we're going to want to do is use chops. So, go to tab chop and then keyboard in.

**13:59** · So, for keyboard in, if we select it to \[music\] one, we hit the number one key, let go, and it works. We can set this to any number, so five as well works. You can even set it to letters. But for this video, let us stick to one. So, when it's morphing, there are a couple of things going on. So, first the particle explode um while still being a dragon or the first model.

**14:32** · After you release the keyboard, it will switch all the coordinates, get rid of the explosion, and then cleanly morph into the second model. So, we need to sort of account for that delay or sort of those like chain of events. So, the first thing we'll do is set it so that when we hit one, we have some number that will act as how much the particles split. So, to do that, we can first use a map.

**15:06** · So, map, go to range, and then we can set the from range and the \[music\] two range to values we want to use.

**15:15** · So, what this does is for the from range, it says, "Okay, from my input, this is \[music\] the range of values and I want to scale those values to this new range. So, if we hit one, the new max, instead of one, should be Now, the max is 0.37. So, we hit one, we have that.

**15:37** · Um \[music\] and what I mean by scale down is, for example, this part you don't have to follow, but let's say we have it, right? \[music\] So, now when we click it, we get the value 0.5. Instead of the value being half of one, it should now be half of 0.37. Um and if we hold one, we can see that work. So, that's what I mean by it scaled the values down.

**16:04** · Great.

**16:04** · \[music\] So, instead of just it being like, okay, I hold the keyboard, it's immediately that value, we want a sort of gradient, so it \[music\] happens smoothly. So, what we can do is use lag. And if you want smoother animations for anything, this is your go-to. So, now if we hold one, the value changes really smoothly.

**16:28** · So, we'll see here that now there are also two values. So, what do they mean?

**16:32** · The first one means the lag, or how long it takes to get to the value when values increase, and the second one for when it decreases. So, to make this really exaggerated, let's set this to 5 and 1 and 0.1. So, what this means is that it will take 5 seconds for it going from 0 to 0.37.

**16:56** · And to go back down to zero is super quick. So, if I hold one, it'll take a while to get to max value, and when I let go, it's really quick. So, hold one. As you can see, it's taking its sweet time getting to 0.37, but if you let go, it's gone immediately. So, it's subtle, but it's important because for the animation visual, you want a really slow expansion, but a really quick morph.

**17:19** · So, what we can do is play around with it, but I liked 0.7 and 0.2.

**17:28** · Or rather, 0.5.

**17:30** · Great.

**17:31** · And once again, we can sort of like add a period to our plot and add a null. So, now we know that this is the amplitude. And once again, this is a generic naming convention. You can name this whatever you want. You can leave it at null one, but this just makes it such that we know, okay, this value is for the amplitude.

**17:53** · Great.

**17:54** · The second thing we need to do is now add a count. So, we need to know that when you let go of it, it will start morphing into the \[music\] next and blend into the second input. So, we need a way to figure out as this value decreases, it will count up one. So, first we do a lag for a really smooth values. Once again, 0.5 to 0.2.

**18:23** · And to do the count part, we use a count chop.

**18:27** · So, count.

**18:28** · And then, we need it to trigger on decreasing values. So, set to 0.7. So, this means that when the value goes from, you know, one to zero, right, decreasing values, when it gets below 0.7, it will count up. So, we hit one, we release, it counts to one.

**18:53** · Great.

**18:54** · Now, we only have two inputs. So, what happens if we do it again?

**18:59** · Now, we are at zero, one, and two. So, that's not good. So, we need to clamp these values. So, go to count, limit, loop min and max, and then we can do it to one.

**19:12** · or something.

**19:14** · So now, if we hold one, do it again, but it will go back to the first input, zero. And we just change this value for however many point clouds we have. So if we have three point \[music\] point clouds, so if we have three point clouds, it'll be two. So go first input, the second input, the third input, back to the first input.

**19:37** · \[music\] Great.

**19:40** · And then, once again, just to make it a little smoother, we add another lag. Keep at these values, and then we add a null. And then what we can do is we can name this one index, but once again, these can be named whatever you want or however it best helps you keep track and understand what everything is doing.

**20:01** · So now, \[music\] if we wire them up, so go back to the switch, for index, you click on this little star icon, then drag it into index. You'll see it turns blue and is an arrow, which means it's being referenced. Then similarly, we drag it. Great. So now, if we hold one, it should switch really cleanly. Let's see if I got that.

**20:26** · It does.

**20:29** · Great. So now, we need the particles to explode. Um so, here's how we do that. So, we're going to go back to \[music\] our position network, and we're going to add a couple of things. And that's why it's really nice to add this dot, or not dot, this null that acts like a period, because now we can edit it again. And we are going to add noise.

**20:55** · So, from the switch, drag that tab, and then hit noise. And then we see a bunch of things happening. Once again, I can to into it in another video, \[music\] but pretty much whenever these colors are different, it means the geographical \[music\] position of each particle is different. So, if we hook it up, we're going to get something that does not look like a butterfly, which is good. And we control it. So, I'll do that.

**21:27** · And eventually, we are going to add this noise back to our original position. So, we think of it as we are adding distortion to our original position data. So, the first thing we're going to want to do is hit P, pull up the menu, output, set it to only noise. Um great. And then, for these values, we can make it anything we want. So, please experiment, but these are the ones that I used for the project.

**22:02** · Yeah. And then, monochrome off. And then, put the second one as well. And this makes it such that they're more like lines. Um great. So, we can kind of see it's working. But, how do we make it if I hit one, go, you know, so that no noise kind of noise is going on. Um we're going to want to look at amplitude.

**22:24** · So, going back to our chop network, go to amp, make it active, drag it to amplitude chop reference, and great. Now, we see our particle if we hold one, we'll see that the amplitude will change as well. Right. So, it's the first part of the chop setup. And when we release it, it will count the position, so it will switch to the new position, while also the amplitude goes down.

**22:55** · So, okay.

**22:57** · So, great. We hold, let go, it will change index and also get rid of this noise.

**23:06** · Yeah.

**23:07** · So, now we have a really clean morphing effect. So, now we're going to want to sort of change \[music\] the perspective of the dragon. And we can do this by going to our point transform.

**23:24** · Much earlier on.

**23:25** · So, going to go back to this and then we can just click it so we can see in the background. And then one other thing is let us select everything.

**23:37** · Or rather, click render, select everything, go to common, and then we just want everything to look really clean. So, viewer smoothness to nearest pixel kind of helps out there. And then pixel format, this just kind of makes it like higher render or lower render. \[music\] So, make it 32-bit float. Great. So, now we have a sort of like a wider color range. And great. So, we do it again.

**24:01** · Colors are much more vibrant and everything's a lot more crisp and good. So, for this one, you know, we want to kind of like rotate it, right? So, it's like just make use of kind of play around. So, it's like 90, maybe like another 90. And then this one um I don't have like a perfect science to it, but honestly this one's pretty cool.

**24:29** · All right.

**24:34** · Let me go.

**24:35** · Great. And then kind of gives it that great. And then for the dragon, it's also pretty cool, actually. Maybe I should have just do this instead, but um yeah, you you got to just just play around with values until you get something that you like. I'll see you guys with that.

**24:59** · Nice.

**25:00** · And then we are going to want to make it spin. So, \[music\] want the box to have only the lines. So, hit tab, material, and then go \[music\] to wireframe. Then drag it on. So, now we have lines and then we can go to wireframe mode topology.

**25:18** · Another way you can do it is tab, line, and then drag it on here. And this we control things like um how wide it is, how thin it is, and a lot \[music\] more cool things. But, wireframe is easy for now. Okay. And then for the balls, we don't want there to be shading at least for now, so we can use constant.

**25:39** · Drag it on and then now that now they don't have any sort of reflections. And then I kind of want the box to be bigger, so we can go like 1.5. Um and the sphere that I'm going to be using is smaller, so 0.03.

**25:54** · Nice.

**25:55** · And then for the geo, we can make this a bit smaller, so like 0.8. And then yeah, so now it's containing the box. We hit one. Great. So, now our models are inside this rotating box. And to add a background, we can do insert operator, um transform, and then set comp over background color and then the alpha to one. Um and then right.

**26:26** · Great. Another way you can do this is um like you do a constant and then this will sort of be your background. to the resolution of your project. And then use an over make your effect over this background. And then connect it that way. And then you can make this black.

**26:50** · Great.

**26:51** · So, yeah.

**26:54** · So, now we have a morphing particle effect. Um if you want to go more into the post-processing effects, the file will be \[music\] in my Patreon, which is in the bio, but yeah, so with a couple of nodes um and a little bit of chop magic, we have created this really cool effect.

**27:13** · So, you can do a lot of things, too. So, for example, if you want these particles \[music\] to move, you can go to noise, trans noise to a 4D, and then transform like translate 4D abs time.seconds. I'm using like really exaggerated number, but now it will move while that happens. You make it a bit more chill.

**27:36** · Oh.

**27:37** · Maybe more chill.

**27:40** · Nice. Now, it's like moving really subtly. But, yeah. So, I hope you enjoyed this tutorial. I hope it's the first of many. And please enjoy. Thank you so much.