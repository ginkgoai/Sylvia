---
title: "We Made Claude Code Build Lovable in 75 Minutes (With No Code)"
source: "https://www.youtube.com/watch?v=_GMtx9EsIKU"
author:
  - "[[Riley Brown]]"
published: 2025-07-08
created: 2026-07-02
description: "Want to build your version? Download VibeCode here: https://vibecode.go.link/86IboCan Claude Code actually beat Cursor?In this video, I sit down with AI engineer Kehan Zhang to test if Claude Code"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=_GMtx9EsIKU)

Want to build your version? Download VibeCode here: https://vibecode.go.link/86Ibo  
  
Can Claude Code actually beat Cursor?  
  
In this video, I sit down with AI engineer Kehan Zhang to test if Claude Code can build a real app — fast. The goal? A Lovable clone. Built in one session that was less than 90 minutes. No shortcuts.  
  
We cover:  
\-How Claude Code SDK actually works  
\-Building in isolated sandboxes with Daytona  
\-Real time app generation with Claude  
\-Fixing permissions, logs, and memory issues  
  
Where you can find more of us:  
Follow me on X: https://x.com/rileybrown\_ai  
Follow Kehan on X: https://x.com/kehanisvibing  
  
Link to the GitHub Repo we used in this video: https://github.com/kehanzhang/lovable-clone  
  
As always, thank you very much for supporting my channel by watching this video. If you liked this video, please subscribe to my channel and check out our other videos - and if there's any specific tutorials or ideas you have for future videos, please let me know below in the comments.  
\-Riley  
  
TIME STAMPS:  
00:00 Introduction & Setup  
00:31 Explaining Claude Code and SDK  
02:11 Starting the Lovable Clone Build  
04:04 Memory and Configuration Setup  
05:51 Using Plan Mode and SDK Docs  
07:00 Generating a Simple Function  
09:00 Executing with Claude Code  
11:00 Building a Tic Tac Toe Game  
16:33 Front-End UI Build for Lovable Clone  
21:24 Connecting Front-End with Backend Function  
26:01 Scaling & Issues with Local Code Writes  
30:04 Creating Isolated Bubbles with Daytona  
34:24 Debugging & Testing Bubbles  
42:48 Test Execution in Daytona Sandbox  
52:32 All Components Working Together  
54:17 The Big Reveal & Testing  
  
Listen to the audio-only version of this podcast: https://rss.com/podcasts/a-new-vibe/

## Transcript

### Introduction & Setup

**0:00** · Many people think that claude code is better than cursor. So I brought on an AI coding legend, Khan Zang, to see if Claude code can actually vibe code full application. And so to test this in one sitting, Khan is going to try and build lovable with Claude Code. In this video, we show you how to set up Claude Code.

**0:19** · We talk about how you can build Claude Code wrappers with their SDK. And by the end of the video, you will see if we're successful in building lovable with Claude Code. And this thing also just finished generating a website. Bro, ours looks better. So cool. I'm super excited.

### Explaining Claude Code and SDK

**0:36** · This was a fun one. Let's dive in. So, Khan, what are we doing today?

**0:42** · Today, we're going to be building a website that builds websites with Claude Code SDK using Cloud Code.

**0:51** · So, it's tough to wrap my head around this.

**0:54** · Do you want to like maybe break that down just a little bit for those who are like vibe coder native?

**1:00** · Yeah, sure. So, claude code is a tool that lives in your command line interface also known as CLI. It's this big scary black box normally near the bottom of cursor and it also exists separately as like a terminal. It's the same thing and it lives in the terminal basically. And so this is a software that Anthropic has released that uses cloud to help you develop software like kind of like cursor like cursor and wind surf except it lives in your terminal which makes it different.

**1:27** · Yeah, it's a little more technical but I also think it's a little more powerful and the cool thing about it right like anthropic released it for you to use as a tool as a general consumer but they also used it for you to use as a developer. So I can develop tools that use it as well. So like similar to the way people are making money with chat GBT rappers or like replicate rappers, you can create a claude code wrapper with something called an SDK.

**1:54** · Yeah. And so the way that kind of works is like chat GPT is a very generalist LLM like it can answer and do a variety of things. Cloud code is definitely like he's the nerd in the class. He's like, "Oh, I'm only good at coding. I don't care about anything else." but he does coding really well you know and so you can definitely build rappers around cloud code but you'll definitely be in the industry of like vibe code lovable

### Starting the Lovable Clone Build

**2:15** · bault replet like you're going to be building a codegen tool so if you wrap cloud code it has great capabilities of writing code but just know that the products that you can make are kind of limited in the scope that you're probably going to be using it to write code right right I mean it is called cloud code yeah yeah so today what you're saying is we are going to use this new tool cloud code to use the SDK of cloud code which will power the app that we create called Lovable. We're going to create a Lovable clone powered by the SDK.

**2:42** · Yeah. Yeah. Yeah. A really a really basic one. Yeah.

**2:45** · Let's do it. How do we get started? In our last episode that I did with Mickey where he broke down cloud code, he says he uses it in cursor and so you do the same usually, right?

**2:53** · Yeah. So, here's my experiment actually, but we can just create straight up a new one.

**2:58** · So, we're starting a new fresh project in cursor.

**3:01** · We're going to go ahead and create a folder called lovable clone. Amazing.

**3:06** · Yeah, we're just going to go ahead and open it. So now this is by the books a very standard, you know, cursor code development environment. I can create a terminal by either doing this or using the shortcut. And so I have a terminal now and I can go ahead and run cloud code like I did before in the terminal.

**3:26** · And it's asking to like read your stuff.

**3:29** · Sure, go ahead. And we can actually configure this to do a lot of things without asking. Normally you'll see that. Oh, okay. No, I actually don't want you to do anything. So, it's already like trying to start coding. I can tell it to stop.

**3:42** · It's eager.

**3:43** · Yeah, it found out that I wanted to make a lovable clone because I named the It just looked at the name of your file.

**3:49** · That's and it started like telling you like, "Oh, I'm going to set up a next.js project with TypeScript. I'm going to create a landing page. I'm going to implement."

**3:56** · Cloud's like, "I don't need you."

**3:57** · Just gonna go through everything.

**3:58** · Honestly, it would be a super fun experience to kind of see if it can do it just right off the bat by itself. But we have some custom demands. We want to use cloud code SDK to go ahead and build this whole thing. So there are a few things that I guess I could show you first. So like a shortcut that you can do is you can actually do looking for it on the keyboard.

### Memory and Configuration Setup

**4:22** · This pound sign allows you to kind of create like cloud MD files which access persistent memory for your cla code session. So I can say like I am building a lovable clone but I want to use the claude code SDK and I can create that and it'll ask me okay do I want it in my user memory or my project memory. Well, user memory would mean for every single instance I use cloud code, it will try to think that I'm building lovable, which is not like the right thing.

**4:54** · Yeah, that would probably be more something like my name is Khan, I could save that forever as my user memory.

**5:00** · Project memory, this is where it belongs because I am building a vibe coding a lovable clone right now. So, I'll go ahead and So, I guess I guess if for those of who have used cursor one, the bottom one would have been like your cursor rules and then the top one would be like a readme file in that project.

**5:15** · Yeah. And as you can see, it's actually very similar. Like Claude literally just spun up a readme. Basically, an MD file is a markdown file and it's basically an upgraded txt file. So this is basically a readme. And so it's it noted down. I'm building a lovable clone. And so that's really cool. Another quick feature I wanted to showcase before we dive into using it is you can shift tab to kind of show autoedits on. So this is really cool. And I can also shift tab again to show plan mode.

**5:42** · So, I guess I would actually begin by saying I like do some research on it because that's what I'm going to do. And one really interesting trick about Enthropics Cloud Code is that it uses the web and it does a lot of research, but you kind of have to push it in the right direction. So, here I have the Cloud Code SDK documentation.

### Using Plan Mode and SDK Docs

**6:02** · I found it by saying Cloud Code SDK and then if you go to Google, it's the first link. So, I'm going to go ahead and grab this link and I'm going just give it to Claude on plan mode and be like, "Okay, look." So, it has the memory that I'm building a lovable clone, but I want to use the cloud SDK. Let's just tell it like, let's focus on using the Claude code SDK to power my code gen agent capabilities, codegen features for my lovable clone.

**6:36** · Lovable clone. For now, let's scope things down.

**6:43** · So, Lovable is a website that builds websites. For now, I'm going to build My background is mainly in backend engineering, right?

**6:49** · I'm definitely more on the infrastructure and backend side of things. So, we're going to stick to that since this project is pretty orientated around that. And we're just going to go ahead and ask it, you know, I want a function that builds something for me.

### Generating a Simple Function

**7:02** · And that something is going to be what should translate. function that you need to execute. For those of you who aren't as technical, you want to create a place that you can type your app idea and it will execute it or do it and create the code for that project.

**7:15** · Exactly.

**7:16** · Exactly. So, we're going to go ahead and tell that we just want the raw piece of code that you can execute that will build something for me. And so, I'm going to translate that a little bit more tech lingo. Let's scope things down. I want a function that lets me input a prompt and uses claude code to build it. Let's just see what it does, you know. Amazing. And so I have it on plan mode. I don't need to tell it specifically like, hey, I don't want you to edit code. I just want you to come up with a plan.

**7:47** · It's currently asking, can I read this?

**7:50** · Yes, you can. And the cool thing about this now I can take this time to explain to you that cloud code will generate this directory called cloud. Inside of it it has settings and it just keeps track of things that you allow and disallow. And so we have to configure this when we build software that uses cloud code to make sure that the SDK cloud code must also have the correct permissions so that it can write and read and do things that you know we kind of wanted to do.

**8:16** · Let's pause there for a sec. So the same way that cloud code asks you permission, right? We are building an app that uses cloud code. So we need to basically enable the app that we create to do the same thing to have the same permissions that we're granting as we build. Okay.

**8:30** · Exactly. Exactly.

**8:32** · And so it's giving me a lot of things.

**8:34** · Once again, it's giving me like build simple UI build with next project implement service class. Like all of this, you know, we're trying to scope down. This is probably a good engineering practice. We should be having service classes. We should have simple UI. Pretty simple. But yeah, like we're going to just say no.

**8:52** · Yeah. Yeah. I like it. I like it.

**8:53** · I just want a simple TypeScript function that takes in a prompt and tries to build it with Claude code. Don't worry about the website yet. We want to prove to ourselves that we can accomplish the main functionality first.

### Executing with Claude Code

**9:21** · And so, show me pseudo code make sure that the clawed code SDK is configured to have the right permissions to read and write automatically. So, yeah. And what's cool is we're using the SDK of the tool we're using. So it probably has good knowledge of the SDK.

**9:48** · You'd think so, but I don't think it actually does. See, once again, it's going ahead to like go read about itself, which is really interesting because I think the way that this works is that cloud releases. I think cloud code came out before four, but four might have some documentation on cloud code, but obviously they're probably they might have even trained cloud 4 on the implementation of cloud code, but they definitely don't they're keeping that closed source.

**10:13** · So its knowledge isn't that great.

**10:15** · It's also like a needle in the haststack one part of its training data and it's not going to like know exactly how it's implemented and be able to remember that from its training set and just know about instantly. And also this way it kind of has a better control of like what is released to the public and so whatever it finds online it can know that like okay I can like definitely use this. So that's probably all baked into like the model that they trained itself.

**10:36** · But let's see it kind of has us given me some pseudo code about you know looks this looks like okay it's giving itself tools to use max turns 10. I'll get more into that later but it kind of looks like you know it's looping through some messages and it's looks like a function to extract code from messages. That's interesting. It seems like this could work. So, I'm just going to go ahead get off of plan mode and get on auto accept edits mode and say, "Okay, implement this feature and I want you to test it.

### Building a Tic Tac Toe Game

**11:07** · Try and make a simple ticktactoe game using the function that calls Claude code SDK.

**11:18** · Let's go, baby.

**11:20** · Make this in HTML for now." And so HTML is kind of like super bare bones. I don't need any setup around it. I can just open it in a browser. And so that's why we're asking it to build an HTML first. Later, we can change that to a next or like a React Native website. So, okay. Well, sure. Never mind. It wants to build a website. Why not? It will go ahead. I'll just let this thing run for a sec. And so, this thing will always ask you. There's a way to make this not ask you, actually, like similar to yolo mode on cursor.

**11:52** · Yeah. And I can talk about that a little bit more in a second because if we want to take this to the next level, we're actually going to have to make it such that currently it's going to just write code. Claude Code, which I'm using right now, is going to just write code in my workspace. When we want Claude Code SDK, which is our lovable coding agent to write code, we're going to want that to happen in an isolated environment where we can let it do whatever it wants.

**12:18** · We're just going to like put it in a bubble and whatever happens in that bubble is fine. It can blow up. It can break. It can like do anything.

**12:24** · It won't affect the main and it won't affect like my Yeah. The damage will be contained is that that is the point. Yeah. And so if we have time, we can get to that. But for now, we're going to scale things down. We're going to let Cloud Code write something that writes code on my local machine, which probably isn't like too good either. Honestly, I should just spin up a Docker instance. But, okay, simplifying down. Let's see. We have a main function that wraps Cloud Code SDK and a test script that uses the generate how to test it.

**12:55** · First, use your anthropic key in myv file and then run it. I'm going to go ahead and put a key here and we're going to make sure you don't steal that key because this key is very important. Okay, so I just put the key in myv file. I've closed it and I will never open it again because I don't want you to have my secrets. But it's telling me I can just, you know, run this after I put my key in. Let's see if it works.

**13:21** · So you can just run it in a new terminal.

**13:23** · Yeah. So this terminal is housing closet code. So it's busy. This one is a new terminal. I'm in the same directory.

**13:29** · Just going to try this. Okay. Let's see.

**13:32** · It's planning right now. So we can kind of see that this is a system message from Cloud Code. We told it to generate me a tic-tac-toe game. Cloud Code is able to use these tools. It's thinking, I guess. Okay, it's using Opus. Wow, that's really cool.

**13:47** · Opus 4.

**13:48** · Claude is going to run up my bill with Claude. So, that's cool. We're gonna see. So, now what we had is if you notice, I actually had to run a script.

**13:56** · This is the function that I was talking about the super bare bones like I just want a piece of code that uses cloud code to write code. So, I executed that piece of code and now cloud code is writing code. So all these green and blue and yellow and complicated system messages, assistant messages are actually is Claude trying to write code right now because we ran the code, right?

**14:15** · So let's kind of see if it ever creates me anything useful. All I really needed it to do is write me an HTML file. I can tell that it's still thinking. Honestly, that's a little concerning because it shouldn't think too hard. Code generated successfully. I need permission to write this file. So we can see that it doesn't have permission to write files. And so I'm gonna go ahead and flame club code because I explicitly told it to give it permissions.

**14:39** · As you can see, the function you wrote does not allow cla to write. Please make sure all permissions are granted to the claude code SDK such that it writes files.

**15:04** · Okay, here are the docs. Again, just make it work. I'm going to tell it to fix itself because we've identified the issue. The issue is that it basically gave it not enough permissions to do what it's doing.

**15:21** · That's probably why it thought for longer than you were comfortable with.

**15:24** · Yeah. Let's see if the test that cloud code wrote to test this on code is working. I think in this case it's actually better than cursor because it's really annoying to use the terminal that cursors agent uses, right? But it's pretty easy to see what the terminal is doing here because I can click control R and I can see everything that's going on.

**15:46** · I definitely get confused using cursors terminal thing.

**15:50** · Yeah. And what's amazing is we actually already have I see here tic tactoe.html.

**15:57** · So it built it and put it in the codebase.

**15:59** · Yeah. And so we can go ahead and open tic-tac-toe and it open tic tac-toe.

**16:04** · There it is. So our lovable clone which we haven't built a front end for yet.

**16:08** · Yeah. Yeah. Yeah.

**16:08** · Built this tic-tac-toe game. You want to let me play you?

**16:11** · Yeah. Yeah. You want to play?

**16:12** · Yeah, let's play.

**16:13** · Make sure this thing works.

**16:16** · Okay. Wow.

**16:19** · I let you win. What are you doing?

**16:21** · What do you mean?

**16:22** · You could have gone there and won.

**16:24** · Oh my god.

**16:26** · I told you to let me win and I let you win, bro.

**16:28** · And then nobody won.

**16:29** · Let's see what happens. Is there an animation?

**16:32** · It's a draw.

**16:32** · It's a draw. Okay. Okay. Pretty basic, but yeah, it is. We now have a function that writes code specifically HTML code.

### Front-End UI Build for Lovable Clone

**16:40** · And so let's talk about what we must do now and kind of reason through it actually with cloud. So this is actually one of the best parts. We have a proof of concept working as in we are now able to use AI to write code for us.

**16:54** · Mhm.

**16:55** · There's a few things once as you mentioned that differentiate this from lovable. First of all, we don't have a landing page, a real website that houses this, right? And second of all, Lovable can make cooler things than a single HTML script file.

**17:07** · So, what do you want to start with?

**17:08** · And so, there's a few ways we can upgrade this to become more like Lovable. We can build a website around it. We can make this such that the user can type in whatever prompt they want and it'll try to build it instead of hard coding a tic-tac-toe simple game in a single HTML file prompt. Right?

**17:24** · Cool.

**17:24** · We can do that. We can build a website around it. Or we can take this, we can start containerizing things and making the back end more power.

**17:34** · So if you don't mind, since I love the front end, I think Vibe coders love making sure the front end actually looks like a wrapper.

**17:40** · We can take a screenshot.

**17:41** · Wait, can you throw it on dark mode at least? I think the dark mode version of their site is better.

**17:45** · Oh, there we go. Okay, great. You want the dark mode clone? We got the dark mode clone. What I was saying was you can grab the screenshot. It can actually digest images as well. If we want to clone the dark mode of lovable, we can go ahead and screenshot this and we can go ahead and copy this screenshot and go back to cloud code and we can just paste it in. And so we can say something like let's continue our project by building out the UI.

**18:13** · We have tested it and our function works for now. Let's focus on building a website that mirrors the current lovable website. I want the soft gradients and a text input. I notice that, you know, there's a lot of like buttons and tabs here. I don't really care about this. I just want this to work like the nav bar on top, the hero of the website.

**18:46** · So, let's kind of see what it does. There's a few ways it can take this approach. It can build a next project. It can build a React project. I've seen it. Yeah, it likes to default to next. I'll just let it do its thing. I'm not a really good front-end engineer, so I have some idea of what's going on. For the most part, I'm kind of like fumbling through the dark, too. I noticed it ran the project starter script, which will give me a lot of uh oh, lovable UI title. Lovable clone.

**19:14** · Okay, so it's like laying out the websites. Websites have metadata.

**19:17** · Honestly, this is taking it a little too far. like I don't really need this stuff. Okay, but it seems like it's running things fast enough. It's telling me to change directories and run the dev server. It's figuring it out. I need to go into this directory and run the dev server to see it. So, I can go ahead and run this. It tells me it's running.

**19:36** · Click on local host.

**19:37** · And now local host will be here.

**19:40** · Oh, okay. All right. It's kind of there.

**19:43** · Like I don't have the gradient. Um that's why I wanted to snag the gradient. I don't have the logo.

**19:49** · I mean I mean I didn't expect it to build the logo, but you want to test it?

**19:52** · We can try giving it a better prompt.

**19:55** · I don't see the gradient. I would like a gradient similar to lovables as in an orange circle uh into pink circle into pink into into black black. Give that a try. And then I think you should do one other thing which is um make the input area by default three um by default three lines high.

**20:24** · You like lovables also the input area is a little small.

**20:32** · Lovables is around uh three lines high by default.

**20:36** · Three lines height by default. Ours is one. And then also, yeah, make the generate button an up arrow instead of the generate thing.

**20:47** · Oh yeah, sure. Also make the generate button and up arrow instead of the color full button has right now.

**21:01** · I think we just give it the photo again.

**21:03** · Okay. Okay.

**21:04** · Yeah, I dig it.

**21:08** · I dig it. I dig it. So now let's talk about some more problems that we're going to face kind of immediately down the line. Uh number one is we have a few options. We can either allow it to continue writing directly to our local machine and by that I mean it's just going to write like a folder in here or something with like let's project one,

### Connecting Front-End with Backend Function

**21:31** · right? or I guess currently it just kind of like writes HTML files in my root directory which isn't exactly how we want things to go and isn't very easily like productizable or scalable at all either and that plays a issue when you try to route into the results. We can try to get that but there's going to be some clunkiness in like getting the website to open the website it just built. That's going to be one issue that we can solve pretty easily actually. So we'll we'll probably tackle that next.

**22:00** · Can you hook it up such that the prompt inside the text input is sent to the function we wrote that uses claude code SDK to generate code.

**22:15** · So yeah, let's go ahead and tell it to hook everything up. Make sure amazing because before it tested itself, it made tic-tac-toe and it worked. And we also created this front end. The problem is that they're not connected and we need it to be connected. So the function that we made is a standalone function that lives right here. It's going to go ahead and move that into our website which I see it doing right now.

**22:34** · And then that way when the website sends that it will be able to make an API call to that.

**22:40** · Yeah. So update the front end to call API to display messages. Add message display component. So yeah, it's got a few things to build out. This is actually it's going to earlier into this session we saw all of these. It's going to try to parse these and render these as well as something ideally more readable than this. This is pretty ugly.

**22:59** · So I kind of gave it that task to kind of hook up the first thing that we built which was the function that you know we've tested and proved can build tic-tac-toe and hook that up to the button inside of here.

**23:09** · Right.

**23:09** · Yeah.

**23:10** · Amazing.

**23:11** · And then so what I understand is this becomes like chat on the left and then it becomes the website preview on the right.

**23:16** · Correct.

**23:17** · Okay. Great. Yeah. We can tell it to do that too after this. That is so cool.

**23:22** · So once again, it was trying to go into the website and run the dev server. And once again, that has an issue because its terminal is shorter lived than itself. So every time it tries I try to open it after it runs it, it's not actually open.

**23:35** · Could you put like a rule in for your like whatever the longer memory is called? So that says like always just tell me when to run the dev server instead of doing it.

**23:43** · Yeah. Yeah, that would probably This is a great example of something that would actually belong in like the long-term memory. Okay, I could definitely save that to user memory. You're right. I'll just save that to longterm memory. Good to know. Great. Thanks. I'm going to restart this dev server. I don't think it needs to, but we're just gonna see if this is still It's done.

**24:01** · So, it it was trying to start it earlier. So, make me connect 4. Let's see what it does. It's currently loading. I'm expecting like some user messages or, you know, at least some logs on the back end. Generating code for prompt make me connect 4.

**24:16** · Amazing. We are seeing some indication of life.

**24:21** · Okay. Um, and it's not immediately failing. So, that's good.

**24:24** · It's not immediately failing. I have a theory that it will just make me another HTML file. We could probably embed HTML as an iframe, but what we truly want is like probably for it to go and write its own next website. Oh, no way. Let's go.

**24:42** · Okay. So, it actually did run and it has its whole like thought process here.

**24:48** · Now, let's kind of digest what it's given us.

**24:51** · So, it's given us, you know, it's calling tools like reading files. It's reading a bunch of stuff that it shouldn't be reading, right? So, for example, it's reading all of the code for the website when instead I asked it to make me connect 4. And then it I've created a connect four for you, but where? So, let's see. Let's look through the code again. Do you have Connect 4 anywhere? Uh let's see. Connect 4. We do have a page with connect 4. Now it's inside of my lovable UI app.

**25:21** · And so this is kind of what I was mentioning before.

**25:26** · It's about where the code that is being generated lives. This is about like this becomes a question about scalability, environments and where you want to run code, where you want the code to be created to be housed and how can you orchestrate everything such that it comes back and shows up on your website.

**25:44** · This is actually like great and all because I'm pretty sure that we can access this connect for website that we just generated by could you just go to localhost slash 3000 or connect 4 maybe or something?

**25:56** · I think so. Literally. Yes, probably.

**25:59** · Let's try that. Slash connect four. And we have four. That's absolutely correct.

### Scaling & Issues with Local Code Writes

**26:05** · It did just Can you try and put a little guy in there or uh place a piece?

**26:08** · Oh, yeah. Sure.

**26:09** · Nice. Place another one. Nice. Can you make one of them win? I just want to see what happens. That's cool. Let's go.

**26:15** · Ah, yellow wins.

**26:16** · Player two wins. Let's go. All right.

**26:18** · So, it works. It just doesn't And it's just basically it creates a new file in your actual codebase, which is not what you think we should do. that's really bad on multiple fronts. You know, I can make it such that some bad code, I can make it say not nice things and it would just be on my website as a URL. I think there's a lot of other improvements we can make on the middle ground as well, such as telling it, hey, I want real time messages to be like shown cuz you know what we saw was after its whole thought process, it showed all of its thought process. We want this in real time.

**26:48** · We could say something like that. All the messages shown to us were computer speak. We can make it not computer speak or like more friendly. We can render more friendly text or only strip out the important parts. We can also make it open the page that it made after.

**27:06** · We can do all of that or we can start putting things into Docker images and hosting isolated environments. Where do you want to I don't have an idea of how long either of those would take. I think I would defer to you. We should make this as close to lovable as we can in the next hour and under that frame you decide.

**27:23** · Cool. I'm going to go ahead and I really hated the process of not knowing what's going on. So, I'm going to do a little bit of house cleaning with this code base.

**27:31** · And so, a lot of what that means is okay, great job. Cloud code is a little child. You got to tell it good boy all the time. Great job. It actually does, I think, respond better because you positively enforce that what it has done is in the right direction. So, as long as whatever it's doing is in the right direction, you want to generally follow it up with something to indicate to the LLM that whatever it did was in the right direction of what you're trying to build. And so, that's why I kind of begin this with great job and I'll say exactly what it did, right?

**27:56** · In this case, you made it such that the website builds a page builds a page within itself based on the prompt. And we notice that because uh when we go to slashconnect 4, it will it's in it's within itself.

**28:19** · Yeah. So we're gonna reiterate to itself what it did. This is in the right direction. There are a few problems though. There are no logs in the back end except until it successfully finishes and when it begins. I want more logs throughout the code gen code generation process.

**28:45** · Similarly, the messages don't show up until the whole conversation is complete. I would like these I would like real-time logs.

**29:00** · Ideally, you should just display the user agent message, assistant message, assistant message, and maybe tool call names. Make sure not everything comes at the end. Also, I would like you to try and open the website that was created from the prompt. Not I guess not the website, but the the page that was created from the prompt.

**29:31** · I.e. last time we asked it to make connect for I created a git repo. I want you to create this as a PR. Now we can run this.

**29:45** · We'll see if it cooks.

**29:46** · And then after that we get into some more really nitty-gritty technical things like we're going to find a way to create an isolated environment. We can do that locally first on our machine with Docker to create this little bubble where all the damage inside can be contained and then we can run a bunch of things in that bubble and then we can put that bubble on someone else's computer using putting it basic that's like putting it on the server putting on and then we can run this on the cloud and then the good thing about that is now if you imagine this bubble as a separate new nex.js JS project.

### Creating Isolated Bubbles with Daytona

**30:17** · That way it's a full standalone website instead of a page inside of my website.

**30:25** · Makes sense. And you can add many files to it in theory.

**30:28** · I mean, I think you could technically nest a bunch of that would that would be insane.

**30:33** · It would be bloating my website. I don't actually want the lovable website to be changed every time someone comes on and writes a prompt. That's a terrible design pattern. We'll try to vive code it all, but we're going to v code it.

**30:42** · It's currently doing some git stuff, making me a git ignore. But definitely this is more of the since we're live on podcast and I have previous experience I don't need to do research but this would be a deep question that I would research like how do I make it stop editing my codebase directly and go create another codebase where does that codebase live and how do I port it into yeah so off the top of my head I know there are many

**31:07** · software companies that provide isolated environments I think they're that's a pretty hot space they're like the people selling shovels to companies like us who want to build AI agents that run codegen because it is a problem that we need to solve. That's definitely like another software E2B or E2B is a great example. Daytona is another one. They're both kind of built around giving you this bubble that you can do whatever you want in and then letting you also peek into that bubble and see the code output of the agent.

**31:36** · And so that's kind of what we're going to do next. We're going to go and spawn a little bubble using one of these isolated environment providers and we're going to go and tell cloud code to write the stuff in there and then show me what's in there instead of directly editing my website. Run the npm rundev.

**31:51** · Okay, let's see if it has real time better messaging now.

**31:56** · So, back to UI.

**31:58** · Amazing.

**31:59** · Make me I want this to like run for as minimal time as possible and get into like the like bubbling stuff. So I'm just going to say make me a screen that says hello world. Very basic. Okay. So we're seeing like my assistants doing some a lot of things already. Okay. Yeah. So as you can see it's already like so this is a lot better display. Let me check if the existing project. Okay. So once again it told me that it's going to check the existing structure of your project my project to understand. Now it's going to go and read through all this junk.

**32:31** · I mean, by this junk, I mean like this website itself, which is the exact problem that I don't want it to have, which is why I have no doubt that it's going to go and make me a screen that says hello world. But I'm going to go and make it such that instead of on my website, it goes and opens a bubble in the cloud and writes it there instead.

**32:52** · And so to do that, I'm going to go and yeah, you can see that it's talking to itself, but we have an animation. We have some sort of indication that something's going on. I'm gonna go do a little bit of research on E2B's docs.

**33:03** · E2B.dev.

**33:05** · I think I do have an account here.

**33:09** · Okay, we used to use E2B for our vibe code, but not anymore. I will have to build a new template for it with Docker and everything. Let's go to docs for E2B docs. And then I have a rough idea of how this works, but I'm going to like try to pretend like I don't. And I'm going to just go and tell cloud code to research this.

**33:29** · So once again, the big idea is we need to create these bubbles such that whatever is created there is isolated. It also can peak into it. We can see it happen on our on our end.

**33:40** · It's exploring. Sometimes it's like cloud code really likes to explore a bunch of stuff and oh look as we can see it just made hello world which is this cloud code over here actually just made that.

**33:51** · Oh. So now if you just do go to localhost/hello world probably it told us this right now. If you can you can start the dev server and navigate to localhost 3000/hello world.

**34:03** · If we do that wow they gave us a gradient. The point is once like it's pretty good because it actually went ahead and told us which website to go to. And so that's a super small change from it telling us which website to go to to just making it a link that's clickable. But this is something else.

**34:20** · Cloud code likes to do a lot of dillydally searching. It makes it very powerful, but I don't want to wait for all this junk to happen. I'm just going to tell it what to do differently, and I'm going to tell it what I need it to do. So, it was trying to gain some context on what this project was. I can go ahead and tell it or I can just put it into my cloud. MD file. It should have this. It knows that I'm a lovable clone. Okay, I'll just go ahead and actually save this to memory so it doesn't need a search too much.

### Debugging & Testing Bubbles

**34:45** · We have so far a website that takes in a prompt uses claude code SDK to write code but currently it stores it in our codebase but currently it directly modifies my website's code by adding it as a page page.

**35:12** · The next task we are going to work on going to work on is making the code gen happen in an isolated environment and opening the dev server there. We're going to keep this in local. So now we're going to tell it E2B or we can use Daytona as well.

**35:40** · Honestly, that would be probably pretty interesting because I've used E2B before. Let's just do a fresh like use something you've never used.

**35:47** · Use something I've never used. Just purely vibe code this thing.

**35:49** · All right, let's purely vibe code it.

**35:51** · Purely vibe.

**35:51** · So, we're going to be using Daytona to create these little bubbles that people's code will be created and run and that is the code that we will show on the site.

**36:00** · Yeah, exactly. And so, oh crap, I need to get an API key. So, let's get an API key.

**36:06** · So, I just put Daytona in my ENV key in my environmental firewall. So, I'm going to tell it. Let's talk a little bit about how I arrived here. To reiterate, the main problem was that we have an agent that writes code, but it writes code directly on our website. Instead, we want that code to be somewhere else, and we want our website to be able to show that code some written and housed somewhere else.

**36:26** · And so, the way that we need this is we need someone else to house the code that our agent writes.

**36:31** · And so, we're using Daytona.

**36:34** · Daytona is a provider of these little bubbles. and we're going to so I'm going to go ahead and tell it I want to instead make the code gen happen in an isolated environment.

**36:53** · I have made I have given you a Daytona key inside thev file. I want you to read the docs on daytona.

**37:10** · Verify that it can do what we want. And the end goal is to have the clawed code SDK create a new React Nex.js Nex.js website inside of the isolated environment.

**37:30** · Don't worry about connecting the text input for now. I just want to validate that we can run the at@ generate cloud generate with cloud code function or something similar in a Daytona sandbox. I've been saying isolated environment. I'm going to feed it to docs now. You should have docs somewhere, right?

**37:58** · So just like cursor, you can paste links to docs and cloud code comes equipped with the tool of being able to search the web and do research.

**38:05** · Yeah. And it should ideally be able to continue searching down sublinks. So I gave it a pretty broad link the whole documentation link.

**38:12** · But it'll search and find which part of the docs it needs. Navigate to that and then search that one.

**38:17** · Yeah, I'll just turn on plan mode and see what it says.

**38:19** · All right. It's a big prompt, big task.

**38:22** · At least a lot of buzzwords have been going around about prompt engineering. I think a lot of prompt engineering is being clear about the end goal, what to focus on now, and all the things you need to get to the current goal of what you're focusing on now. I think it's good to give some indication of the direction of the end state. But it's most important to frame and iterate to the agent that we're working on a smaller chunk, but to still have its eyes set on the end goal.

**38:48** · M so because you see a lot of times when you tell cursor to do something that's apparently obvious in your brain and it does it completely wrong it's because it doesn't share the same end goal as you and so that's why I like to always give it a little peak of what the final goal is but I like to if you give it like too much to work on it'll obviously get lost in the sauce and there's also a difference between final end goal and then the iteration end goal or the current task end goal.

**39:12** · Yes. I want instead I want to instead make the cogen happen in an isolated environment. This is the end result or I guess this is actually to create a next.js inside of the isolated environment. Don't worry about connecting the input for now. Just I want to validate we can run. So this is what I mean by scoping down. The end goal is to have the whole Nex.js website inside the isolated environment be spun up by cloud code. I told it instead just work on being able to run cloud code inside of the isolated environment first. Okay, it gave me a plan. Let's see. It's telling me to install the SDK.

**39:46** · Create an integration. Integrate with initialize the client with API key.

**39:51** · Yeah, we gave it the API key. Implement Nex.js project creation in sandbox.

**39:56** · Create a new sandbox generation function. That's true. We're going to need that. Update the API routes. Test the script. And see, once again, it's telling me to do this is the end result, right? This is actually really good.

**40:06** · Test validation. create a simple test that creates a Daytona sandbox, runs a modified version, and creates a basic Nex.js app. Yeah. And return to preview your app. This is perfect. So, we're going to go ahead and say the plan is great. I want you to go ahead and focus only on the test validation for now. I also did some research and found out that you probably want a custom Docker image so that Claude code can run inside the isolated environment.

**40:44** · Have you taken this into account? Plan out the test script in more detail. Show pseudo/real code. And so this way it's doing another plan session. I told it to be a little bit more detailed about what it's planning. Show me the code, how everything's going to come together and also consider the fact that we need a template for how to make these bubbles, how to make these isolated environments, which more technically takes the form of a docker file.

**41:15** · So I kind of gave it some direction. I said, "Hey, look into this docker file thing for me. This is what cloud is telling me that it needs to run cloud code. You should probably like think about that a little at least. And I want you to start showing me your thought process in code. Whenever it's coding, I'm reviewing what is coding. If I see it's going off track, I'll stop it. And at the same time, I'll myself as a human gain more context on the code base.

**41:37** · And this is also another reason why being technical is an advantage is because you can run a prompt like this.

**41:43** · I can't run a prompt like this and look at the code and be like, that's good. We agree on good code. I don't know what that is. But the powerful, as I mentioned before, I've never used Daytona before, but I technical background.

**41:57** · And if something looks outrageously wrong, I can stop it. So I see it, you know, creating a sandbox in JavaScript.

**42:05** · I see it passing down some variables.

**42:08** · I see it starting the sandbox.

**42:11** · I see it testing if cloud code exists in there. I see it trying to make a directory for the generated app and then I see it writing exactly the first thing that we have written which is the first thing we did was make it run write a single piece of code that can generate code so it actually copies that straight into the sandbox and tries to execute it

**42:32** · which is what I see here and it's starting to generate a welcome page yeah so it basically creates a script that says generate me a nextjs great that says hello world and then it'll generate it and then let's see Check what was created. This is pretty good.

**42:47** · Would you like to proceed? Yes, let's just do it. I want ideally it's doing both of these because I do want I think both approaches could work. And this is another good thing. It came to me with two things. Test the script directory.

### Test Execution in Daytona Sandbox

**42:59** · Create the test Daytona integration script. Run the test scripts to validate Daytona verify. Great. Yeah, pretty excited actually because this is getting into like this is really cool. This is getting into like some like senior architect like senior engineer like system design architecting.

**43:15** · So did you want to try with cursor real quick the screenshot? Yeah. Let's give it this copy. I just want to make sure that this is actually the page that I wanted to edit. Yeah. Handle generate. I want you to make this landing page look more like Lovable's actual landing page. And so let's just give it a real landing page.

**43:41** · I see that it is having difficulties with Daytona. We could intervene here and tell it to scope down even more. I see it failed to start a sandbox. So we could say, "Hey, I want you to just focus on starting a sandbox." Should be pretty easy. We'll see if it continues to fail. You know, it said the test failed. It sent three agents in parallel to use a bunch of my money to go and figure out the issue. And then now it's removed my friendly comment. Fine, whatever. And then it's adding some more code.

**44:11** · So great, it's finally getting back to work after making me wait for a good 5 minutes. Meanwhile, 03 has also promised me that we have a better landing page now. So I'm just going to go accept all on here, close this thing again, and then actually see if we do have a better landing page. Where are you, local host?

**44:29** · What the Oh my god. First of all, this is a war crime to have this emoji here.

**44:37** · Okay, thank you. Center thumb below the text input.

**44:44** · Okay, I like it. And then can you make the you just make the other one tiny like 1x?

**44:51** · Which one?

**44:52** · Very small on the actual site. So it's telling me that time that the core functionality works generated a sandbox with this.

**45:02** · So tell me how I can preview the dev project inside the sandbox with the ID.

**45:15** · Oh, not lovable. Sorry. With this ID.

**45:19** · Cool. And let's just accept all of 03's changes again. be optimistic. Okay.

**45:24** · Like, yeah, it just needs to be like 10 times larger, but we Okay, we're getting there. Good job. Lovable's design is actually pretty nice. This is just very depressing. But we got the gradient.

**45:34** · Actually, the gradient is the same. It's just so small and there's just random gradient here and here. It's trying to run it and it is failing. But let's see.

**45:43** · So, it's telling me it worked, but I have no way to confirm. And this is apparently cloud code is telling us that we have a bubble and inside of that bubble we do have a next.js project. The only thing is I can't view inside of that bubble. And so now we're trying to figure out how to view inside of that bubble. So currently we're debugging a lot of things about does the bubble actually get spawned? Is there a nextjs project in there? And how can I look at that nextjs project?

**46:09** · After we get that sorted out, we're going to go back, inject our agent again, which is actually just cloud code SDK, and tell it to build it what website we want.

**46:19** · And then after that, we're going to hook it back up to our website. And then we're going to have a website that creates a bubble with cloud code inside of it. And cloud code can go crazy and code up our website. It will expose that website so that people can see it from the outside. And then we'll be able to see the issue.

**46:35** · Amazing.

**46:36** · Oh, not the issue. The Do you want to check your texts? I sent you a gradient that you can use as the background. I think it'll look really good. Can you please make this image the background of the web app that we've created? This is going to be behind the text input field. And then for the text input field, keep it exactly the same. I just want you to make it really dark, like almost black, so that you can hardly see through it. So this image should be the background and then yeah, make it darker behind the input field with white text as you type.

**47:08** · Nice. So, we'll let 03 cook on that. But let's get back to the main project. I see it and this is an issue that it continues to like to do where it tries to run it, but obviously it's shell inside of itself is, you know, like doesn't live long. So, I'm going to tell it to stop and I'm just going to run it myself. And then, okay, it failed because it cannot find it. So, where is this npxtx scripts scripts? Where is the script?

**47:36** · So I actually have to CD into lovable UI and then run this. And so it's created a sandbox. Okay, great. It's creating an next.js project. Let's see if it actually does that. And so I'm running the script that Cloud Code wrote me to see. We can look for public. Create sandbox preview. I think it does have public true. Yeah, it does. Create next dayu.work.

**48:02** · So, I mean, this actually does look pretty much like, let's see. This is saying, and I'm going to use this as a text input, but let's see. It's saying, what is our sandbox ID? Important sandbox ID is this thing. So, sandbox, that doesn't look like a sandbox ID.

**48:24** · Sandbox ID. Okay, maybe it is. Is there any way I can SSH into this sandbox? So to do some more complicated debugging.

**48:33** · So we have a bubble now.

**48:36** · Okay. Okay. Okay. It does seem like we are spinning up these bubbles. Inside of the bubbles there do seem to be some resemblance of a website. I'm not very familiar with Nex.js. I guess we can see the app and see like what's in here.

**48:50** · Okay. We have page.tsx.

**48:52** · Yeah.

**48:53** · Okay. Yeah. I think there is indeed a website on the bubble inside of the Daytona server. But the problem is we're struggling peeking into it.

**49:00** · Yeah. Okay. So this is the sandbox running. This is now we want to peek into this bubble. So we do have confirmation that there is you know. Okay. I still can't open the websites.

**49:14** · I am getting 503 service temp unavailable.

**49:21** · Can you do some deep research on why this is the case? I am running what script am I running? Test Daytona simple. Daytona simple.

**49:38** · I noticed that inside what did I notice? I noticed this the sandbox ID seems to be different from the ones we are getting. For example, on this website, the sandbox says that this is the ID which the ID seems to be something like this from the docs. But we are getting UYU ids like what am I getting?

**50:08** · I'm getting something like this. Oh, wait. Yeah.

**50:13** · So, yeah, that was an observation I made. Please search the web think. Oh, yeah. Cloud code has specific reserved key terms for how hard you want it to think. I'm pretty sure the the highest level of thinking is literally ultra think. I don't know. Maybe they were just like having fun. I'm pretty sure clad code ultra think. Yeah. Yeah. It's actually like the way to tell it to use the most juice. So, I'm just going to tell So, this be $10.

**50:40** · Yeah. Basically, it'll just use as much tokens as it can possibly use basically and try to figure out the issue. So, if Daytona's documentation is right, this indeed should be something that gives us a URL that we should be able to see inside the bubble. So, we were able to confirm that a bubble was created, code was being written there, but we can't see inside the bubble. And that was because cloud code did not read enough documentation just like the average engineer.

**51:09** · Right. Right. Right. Right. Right.

**51:10** · So I had to read some documentation myself and I found out that it's not using the preview link.

**51:18** · It is not using get preview link which conveniently returns to you a URL and the token to access it. Let's run that test preview urls. Okay. Now it likes to break things down. It broke itself down into smaller tests. So now it's creating another test to test if this previewed URL thing works as it promises.

**51:37** · Right. But once again, it's running this thing inside of the bash of itself. I'm gonna run the script myself.

**51:46** · Creating sandbox creating next.js app.

**51:49** · Okay.

**51:50** · Then let's just read what the script does.

**51:53** · So now we created another bubble. The sandbox is the bubble that we were talking about, the isolated environment.

**51:58** · And then we're going to have it create me a next.js app inside of the app.

**52:03** · It's going to go and create a custom page at preview. It's going to install dependencies. And then it's going to start the dev server, which is what we're trying to peek into, right?

**52:11** · Amazing.

**52:12** · So, um, and then we'll get the preview link to that server.

**52:15** · Yes.

**52:15** · And that's what we'll be able to see.

**52:16** · And ideally, we could render that in the site itself in the front end of the lovable site.

**52:21** · Yes.

**52:22** · Okay. Amazing. And that's probably like something similar to what how they do it.

**52:26** · I mean, I don't know how they do it, but Oh, it's here.

**52:30** · No, this is the website. Hey.

### All Components Working Together

**52:32** · And so they're telling me that this dash preview is a website that it built.

**52:38** · Preview works.

**52:39** · Let's go.

**52:40** · Okay. So now we can finally look into the sandbox. So we have all of our pieces together. Now we have a way to create bubbles on someone else's cloud.

**52:50** · We have a way to write code inside of that cloud. And we have a way to trigger it through our website. So let's just ask cloud code to put it all together. And so we have great this one did indeed work. So we're just going to go ahead and say wonderful job.

**53:12** · You sounded white when you said that.

**53:14** · Wonderful job. Sorry.

**53:16** · Wonderful job. No, it did a great job.

**53:18** · Wonderful job, Claude. We now can successfully look at the NextJS project. And so actually, hold on. Okay.

**53:30** · Well, anyways, so to reiterate what just happened, we finally were able to peek into the sandboxes, which is the bubbles that we were talking about this whole time.

**53:40** · And you blamed Atono when it was probably Cloud Code's fault, maybe.

**53:43** · Yeah. Yeah. Yeah, it was probably Claude Code's fault. Daytona actually had decent documentation. I found it pretty quick. There was a function that Claude Code refused to use, probably because it did not find the right thing to read.

**53:53** · So, once again, that's, you know, a context management mistake on my end, to be honest. So, we found that though. We did some digging. We gave Claude the context and it fixed it immediately with the last script that it ran which was what was the script? Oops. The script was mpxtscripts.

**54:11** · Preview. So I'm going to I'm currently updating the markdown of cloud.md.

### The Big Reveal & Testing

**54:17** · Remember this is the kind of memory that it has attached to every prompt that it kind of gives it like structure. And this is, you know, how earlier we were mentioning how it's good to give the agent like a picture of the final output and kind of like what has happened so far. This is kind of like a conversation history. I'm updating it a little bit so that we can type less every time we submit a prompt. So I said, you know, the goal is to make a lovable clone. We want to use cloud code SDK. We have a website that takes in a prompt.

**54:45** · It uses cloud code SDK to write code, but currently it modifies the website by adding it as a page. We want to make this happen in an isolated environment.

**54:55** · So now we have created a way to create sandboxes which is the bubble using Daytona to preview them and preview them. Get preview what is it called? Get preview.

**55:05** · You have it on your clipboard too.

**55:06** · Yeah. Using the get preview link function. The script confirms this.

**55:14** · Okay. So this is our progress so far.

**55:17** · I'm going to save it to its memory. I'm going to go back to good old cloud code and I'm going to say wonderful job. We now have a successful We can now successfully look at the next.js project. It does have a preview page.

**55:32** · Scripts.js worked perfectly. Oh yeah, and this is another thing we kept on noticing that it tries to run the script but it can't like do anything. So don't try to run the script with your own bash tool. Write the scripts going forward. And this is probably like project like let's see like what is this preferences.

**56:00** · Don't try to run the script on your own pouch. Write the script and tell me how to execute it asking me for its outputs instead. So let's just leave that there.

**56:14** · It does have a preview page scripts. The script worked perfectly. Now I want you to go back and make it such that I can create a Daytona sandbox and using cloud code SDK build a custom website based on a prompt that I pass in this.

**56:41** · Let's keep this as a script for now, but we will implement it into our website as soon as we confirm that it works.

**56:56** · Amazing.

**56:57** · Great. It's created a script that creates a Daytona sandbox, installs Cloud Code, generates a website, installs the dependencies, and gives me the preview link. That sounds perfect.

**57:10** · That supports Markdown support and dark theme. You know, that's a great idea.

**57:14** · Let's just do this basic usage. And then notice that it wants me I told it that I want to run the script myself. So, it gave me some options to run the script. And that's a great idea. Thank you Claude Code for that. I will go ahead and do that.

**57:27** · Okay.

**57:28** · Create a blog website with markdown support and a dark command is required.

**57:32** · Let's see. Cloud code running cloud code command is required. Sandbox is still running for debugging. This is going to be a hassle to debug because oops.

**57:45** · Wait, is that permissions issue or no?

**57:47** · So, we don't know cuz this is uh the only error that is thrown command is required. We can go ahead and run this.

**57:55** · I have a good feeling that we can get through this though. So I tried to run the script asking it to build me a what did I ask it to build? Uh blog website.

**58:13** · This is the output.

**58:16** · How can we debug the issue? Remember the sandbox which is the bubble is still alive and I can SSH into it with a terminal.

**58:31** · Oops, pasted that in. Okay, so now it has the error. It will either give me directions to debug or it will try and solve the issue. So the error is command is required suggest there's an issue with how we're executing the command.

**58:45** · Let me do a debugging script. Okay, I think I know the issue. Once again, I might have to pass down this to claude code. Let's actually just tell it.

**58:55** · I don't think you need to debugging script first. I want you to read this documentation and make sure you are using Daytona properly. And so this is actually a common issue with the fact that the LLM can browse the web.

**59:14** · But since Daytona and all these new companies are writing things that are often changing and since they're so new, you know, Daytona, if they don't follow strict industry standards or like whatever the training data that cloud code is on, it might have like enthropic or cloud code might default to like what it thinks is right oftent times. and just go back to like writing broken code because it thinks that's what it should look like and Daytona is not following that or something.

**59:46** · So yeah, we found the issue already. We our hypothesis was correct.

**59:50** · It was not doing execute command properly which makes sense because our error was actually something like command is required. So hopefully this will fix it and we can run this again.

**1:00:00** · We can check on the design now. accept these changes instantly.

**1:00:05** · And drum roll, please. Oh. Oh, god.

**1:00:09** · Nope. 404 gradient.png. Can you please Let's see if it's telling me to do anything. Do I need to restart you?

**1:00:20** · No. No. No. Because serves everything in public. The background should not automatically load once it's there.

**1:00:26** · Create a public folder. Okay. It doesn't exist already. Drop the provided image.

**1:00:31** · Okay. So, it's telling me to create a public folder in here. New folder.

**1:00:37** · Public. And then move this into here.

**1:00:40** · Okay.

**1:00:42** · Now, will you work? No. Okay. At drop the provided image because the next js serves everything in public on the site folder, the background will now load automatically.

**1:00:54** · It's not.

**1:00:56** · Oh, it is not. Oh, wait. Gradient is in public. Yeah.

**1:01:02** · I still don't see it. Slashpublic at slashpublic. I put the image in.

**1:01:11** · Yeah. Yeah, I really don't see it. Okay, let's see.

**1:01:13** · Maybe the gradient design is over the image.

**1:01:16** · Oh, yeah.

**1:01:17** · I'm not sure. Maybe that is a good idea.

**1:01:19** · But back to this exciting thing. It says that the air messages will be more explicit. Great. Cloud code installation before running. Great. And then it will run. So let's try to run this thing again. Let's go.

**1:01:34** · Come on.

**1:01:35** · Yeah. Come on. Come on.

**1:01:37** · So ideally, oh website generation failed. Cannot find package import from.

**1:01:43** · Okay. So that means let's see. It says running cloud code to generate but it says installing cloud code SDK. Let's see exactly how it is installing cloud code SDK because something is definitely not installed properly. Generate website simple and generate website in sandbox.

**1:02:01** · Which one am I running? Generate website in sandbox undefined. It definitely failed to install this somehow.

**1:02:09** · Install cloud code.

**1:02:12** · Yeah.

**1:02:13** · Interesting.

**1:02:13** · So let's see. This is one way we can debug this quite simply by going into here. Oops. I mean I guess Okay. Let's see. Sandbox ID is this one. We can go ahead actually and go into Daytona.

**1:02:28** · Sandbox started with F9, right? Nope.

**1:02:30** · F5. So, we can just go connect here and we can see what happens when we try to run the command that failed, which is sandbox.

**1:02:40** · Oops. No, it's going to be here. Let's see if this works. Okay, I'm on the sandbox. I'm in the bubble right now. I only have a terminal. And I'm gonna go ahead and feed cloud code some more context on what exists inside of the bubble to helpfully help it debug what is going on.

**1:02:56** · Amazing.

**1:02:57** · Okay, I'm just gonna go and take all this stuff and give it the cloud code as well. This is the error. It seems like cloud code is not being imported or downloaded properly. I also sshed into the sandbox and did some snooping.

**1:03:18** · This is some more context to help you debug. So, this is telling cloud code that there's more information available.

**1:03:27** · It got a little further, right?

**1:03:29** · Uh, no. I still think it's the same cloud code. Okay. No, no, no. We now have cloud code process exited. So, we have cloud code now. I think this might be because it's sandbox is blocking out perhaps. I think there's something we can do to debug this. How do can I easily check if a sandbox has access to the internet? Well, I can just ping Google. Oh, no. It does have internet access. Okay.

**1:03:57** · So, my initial thought was that maybe the bubble doesn't have internet access. It needs internet access if you want to run cloud code.

**1:04:04** · You ping Google and it does have access.

**1:04:07** · Yeah, I can also ping api.anthropic.com and see if this one Yeah, this one is getting a response.

**1:04:14** · What does ping? Ping means just like check if it's Yeah, it just pokes the website and sees if it like gets a response. Cloud code exited with bear one and let's see.

**1:04:24** · Nope. Wow. I now so this is the drawback of getting AI to do everything for you.

**1:04:31** · I have no idea what is wrong or I can only like believe that only context manage.

**1:04:37** · I can't create my own context. I told it look use the right documentation and it's reading the web again. So hopefully this time it'll figure something out that actually works and we can have lovable clone. Cloud code has actually used 70% of its context. I'm going to go ahead and compact this since I don't care about the specifics because if you remember we are trying to create a proof of concept script that uses Daytona to spin up an isolated environment where we

**1:05:09** · want to run cloud code to create a next.js website.

**1:05:13** · So this is a broadstroke. Currently we've been failing and a lot of the time is because we are not implementing code execution properly inside the sandbox properly with Daytona's SDK.

**1:05:30** · Let's create another script. But going forward, I want you to create the script inside of Daytona and I want you to execute it. And I also want you to install and log if you installed it by checking using ls in terms of where it should be installed and do not install dependencies globally.

**1:05:57** · Also, I want the script to be able to take in a sandbox ID. So, if it's already spinning up a sandbox that exists, don't create a new one. Just use the sandbox that we already have. And so I'm going to go ahead and once again feed it some Daytona Docs process execution. Running commands. Yeah, running commands and code execution.

**1:06:18** · Let's see. Run code.

**1:06:21** · Run commands.

**1:06:23** · I am going to feed it these docs. And I'm going to say I want you to actually create the file inside of Daytona and not just pass in the whole JS as code to execute.

**1:06:41** · Okay, let's see if this would be a bit better. So now I'm just going to try again and I want you to make what's a good website idea? website idea. Please make a site that lets me upload an image and I can resize it or crop it by adjusting a slider or some Let's do it. Make me a site that lets me upload an image and allows me to resize it. And so great. Currently, we have a script that runs generate website. And now it's going to try to generate that website.

**1:07:13** · So this is super exciting. Once we confirm that this works, we're just going to hook it up so that our lovable clone website runs. This will look like Lovable.

**1:07:21** · Yeah. Yeah. Where's our Lovable website clone? We haven't seen this in a while.

**1:07:24** · This bad boy that we spent two hours on.

**1:07:27** · We're good, dude. We're hitting the home stretch here.

**1:07:29** · That's I currently don't see the background image. I think this might be because you are covering it with other stuff. the image is replacing that other stuff.

**1:07:45** · Yeah. Make sure that the image is shown and nothing is on top of besides the UI of the beside the text input field, right?

**1:07:57** · The text input field.

**1:08:01** · Amazing. Okay, great. And this thing also just finished generating a website.

**1:08:06** · And so now it's creating some link here.

**1:08:09** · Ideally.

**1:08:10** · Yeah. Yeah. Yeah.

**1:08:11** · Amazing.

**1:08:11** · Ideally, ideally. Yeah, installing dependencies. After that, it should spit out a link.

**1:08:16** · This is crazy, bro. This is actually insane.

**1:08:19** · Oh, man. Once again, I think it's caught on the server, so it never fixed the issue. But we do conveniently have a script to just solve that issue right here. Oh, no. No, it did. Amazing.

**1:08:31** · Let's go.

**1:08:32** · Good job.

**1:08:33** · All right.

**1:08:33** · So, now this is No way. Let's go. Let's go.

**1:08:36** · We can go and resize this image.

**1:08:39** · So, you can gradient.

**1:08:40** · Oh my god. It just works.

**1:08:43** · Wait, wait, wait. What happened?

**1:08:44** · I'm resizing the image.

**1:08:45** · Oh, I see. I see. I see. Let's go.

**1:08:47** · Oh, okay. I can make this like I don't know like what was the original image size? But yeah, no, we have an image resizer website now.

**1:08:54** · Let's go. Let's go. Okay. So, now the main functionality works. We just need to put it on our app.

**1:09:00** · Yeah.

**1:09:00** · Go see if the styling worked.

**1:09:02** · Local host.

**1:09:03** · Oh, yeah. Yeah. Yeah. Okay. True. Let's try this thing.

**1:09:06** · Accept. Right.

**1:09:07** · Let's see. Switch the background div to be in line. Yeah. the only element layered above. Do I need to accept you or anything?

**1:09:14** · Maybe. Cool.

**1:09:16** · Ain't no way. That's our website.

**1:09:18** · No, it's not. Oh, that's ours. Let's go.

**1:09:21** · Okay.

**1:09:21** · Yeah, it is.

**1:09:22** · All right. All right. All right. Can you Can we Let's do one more styling prompt.

**1:09:25** · We need to get rid of that weird thing on the left there.

**1:09:27** · What? This thing?

**1:09:28** · Yeah, that thing's nasty. Just get rid of it.

**1:09:29** · The public plus and public button on the left of the text input.

**1:09:36** · Yeah. And then make the background of the text input black. Just make it fully black.

**1:09:42** · Make the text input background fully black.

**1:09:48** · Yeah, like opacity zero. I mean like what?

**1:09:52** · Opacity.

**1:09:53** · Go switch. Open up lovable. It's down below. Bro, ours looks better. Oh, they have the like the nice typing. That's okay. We don't need to edit that now.

**1:10:00** · But like all right, come on, son. Yeah, this is and you asked Claude to connect it to the front end. So like in theory it might work, right?

**1:10:08** · I've not asked it to the front end yet.

**1:10:10** · So let's go and see that this script was generate in Daytona.ts. So now we have a script which is the piece of code that we can run that spins up an isolated sandbox, isolated environment or sandbox or bubble whatever we want to call it.

**1:10:29** · And then inside of that bubble, cloud code SDK will go and create a Nex.js website. And then that website we can peek at using the link that we get from here. Preview URL. Great. This script is working great. As you can see, if we open the script, we actually have the image resizer that works. We can give it like a graphic. It's a little ugly, but it's an MVP.

**1:10:52** · We just wanted something to work.

**1:10:53** · We have something working now. We have this script. Now we can go back to clot and we can say great job.

**1:11:00** · This script successfully ran a function that generated a nextjs website and returned the preview URL after starting the dev server. I want you to make the button, make the text input, submit the prompt, and hook it up to our lovable clone.

**1:11:31** · After the generation is complete, I want you to display the preview URL.

**1:11:42** · Wait, shouldn't we specify where? Or actually, it doesn't matter. We can resize it later. We can just say like open the preview URL for now and then we can Okay. And then we can further later.

**1:11:52** · Yeah, we can definitely try to do that too.

**1:11:54** · Now let's update the front end to use the new API to handle the preview URL.

**1:11:58** · Great. Now let's update the page to use the new Daytona API to handle it. Okay, great. So cool. I'm super excited. This is honestly a pretty challenging task.

**1:12:09** · Cloud code did stumble along the way. I think there's a lot of factors that went into it. We did manage to course correct it. But Daytona is super new technology.

**1:12:18** · Test the full integration. No, stop.

**1:12:23** · I'mma just stop it. Don't test that. I want to test it myself. Okay. So, this is the real lovable. This is our lovable.

**1:12:30** · Wait, so it's ready to test?

**1:12:32** · Yeah. Yeah. Make me a blog. Make me a modern blog website that supports markdown support.

**1:12:37** · Oh, wow.

**1:12:38** · Let's go. Let's go. Okay. All right. All right. Let's go.

**1:12:42** · Please. It's verifying. It's generation script. Generation script verified.

**1:12:48** · Create a modern website that a website with markdown support. So, this may take several minutes. Oh, running cloud code.

**1:12:55** · So, yeah, now it's running cloud code generation. Waiting for a server to start. I think we're actually really close. Oh, look. Now it opened. Oh, it failed to do a prompt.

**1:13:06** · All right. That's all right. That's all right.

**1:13:07** · Auto prefixer. Okay. It definitely failed but the idea is there where we have a cuz if it's a preview I mean think about how many times when you use these vibe coding tools where you ask it to make something and then that is the view on the right side of the screen which is that preview error that happens all the time.

**1:13:24** · That is true. You know we can ask it for something simpler maybe like make me a landing page. Just make me a landing page for my banana company. a landing page for a company that sells bananas.

**1:13:42** · Okay. I would like to see the claw code agent trajectory. I'd like to see the cloud code agent trajectory.

**1:13:51** · Currently, it just says this may take a few minutes and goes silent.

**1:14:00** · I would like to see which tool calls are being used.

**1:14:08** · And here is an image. Oops. Yeah, I'll just give you them all actually.

**1:14:14** · All right.

**1:14:14** · Yeah. Yeah. Okay. Yeah, that works.

**1:14:16** · Go cook. So now that guy is cooking. Now at the same time we are also cooking here.

**1:14:24** · I see. Oh, see. Look. Oh, world's All right. Making progress. Let's go.

**1:14:28** · The world's finest bananas. You know why? We sell the classic yellow bananas for $5 a pound, the platinum premium for $4 a pound. Why does that get cheaper?

**1:14:39** · Okay, interesting. 100% organic, fast delivery, sustainably sourced. Wow. You know, I'd like more graphics, but that's fine. Honestly, this looks like not a not a terrible landing page.

**1:14:52** · I mean, it's a pretty bad landing page, but at least it's a landing page. It's a pretty bad landing page, but it's pretty impressive that, you know, we did it.

**1:15:00** · Okay, let's see.

**1:15:01** · Do the image resizer one, but like make it like adding border around the image website that allows me to upload an image and it adds a border to and I can change the thickness of the border. I should be able to change the thickness of the and the um the rounded edges.

**1:15:24** · Rounded edges corners. Corners rounded corners and the color. Okay.

**1:15:31** · Oh, no way, bro. That's crazy. All right.

**1:15:35** · It's it go.

**1:15:38** · Yeah. Yeah. Yeah. So definitely like a little janky like super Yeah. Yeah. Yeah. Like what the hell?

**1:15:46** · That is awesome. Let's go.

**1:15:49** · Yeah. You can see exactly what the agent is thinking now. You know, it's Oh, actually, no. No. This is the prompt.

**1:15:54** · Okay. It goes silent again. But this is kind of the prompt. Make me a website that allows me to upload an image and adds border to it. I should be able to change the prompt. I don't know if it managed to successfully catch like the messages that are being That's okay. Hey, that's okay. If it renders on the side, I'll be like super hyped.

**1:16:12** · Yeah, I definitely know.

**1:16:13** · What does it go? Wait, scroll up slowly on the right side. Yeah. Yeah, right there. What is that? Oh, spinning up preview. It's just centered in the whole thing. Yeah, we definitely need to tell it to like keep this max height.

**1:16:23** · We can't fix that.

**1:16:27** · It's still working.

**1:16:30** · And then, oh, it should automatically render in the right side. Ideally the chat should take up like 30%.

**1:16:39** · And the website preview should so please also fix that.

**1:16:46** · After these fixes we can generate a cool website on cool website little app.

**1:16:51** · Think of a little fun website.

**1:16:53** · Fun app that will render on the screen.

**1:16:56** · It looks pretty good and it is stored not in your own codebase. stored in a container or a isolated environment.

**1:17:04** · Let's see if it works.

**1:17:05** · Yeah. What would you want to generate?

**1:17:06** · Let's generate something really cool.

**1:17:07** · So, let's build something with our lovable clone that we created with cloud code that uses cloud code.

**1:17:13** · Should we tell it to generate create lovable?

**1:17:15** · Build let's tell it to do exactly what we did today. Build something with lovable built with clawed code.

**1:17:24** · All right. Build something with lovable.

**1:17:26** · Wait, can you put that in the subtitle?

**1:17:28** · And we should we can move this down into like H3s. H3 built with build a website.

**1:17:36** · We can think about this.

**1:17:37** · Flappy bird.

**1:17:38** · A pomodoro timer.

**1:17:42** · What about a link tree?

**1:17:44** · Yeah. Link tree.

**1:17:45** · I like it. I like it.

**1:17:46** · Yeah. Yeah. Yeah.

**1:17:47** · All right. All right. Let's do that.

**1:17:48** · Okay. So, build me a personal link tree. personal link tree that allows me to upload my links with name and I can name each link and name each link make it sleek sleek

**1:18:06** · make it sleek modern and beautiful my personal link tree that allows me to upload my links and name each link make it sleek modern beautiful amazing let's try it let's run it all right our lovable clone is going to work nice work. Good job. There it is.

**1:18:24** · And so, can you scroll on the left side?

**1:18:26** · Right. That's how it should work. Yeah.

**1:18:28** · So, cool. Build me a personal link tree that allows me to upload my link and name each linking computer.

**1:18:34** · And this is Wait, wait. Run it on lovable. Run the same copy the prompt. Run the same pro.

**1:18:39** · Oh, you probably don't have a lovable account.

**1:18:41** · I don't, but I mean, do do I do I have to pay? Do I not get a Yeah, just you get you get a free one.

**1:18:45** · There you go. Basic.

**1:18:48** · Great.

**1:18:48** · Okay, so we're running it on Levelable.

**1:18:50** · Now, go back to our other one. So, this is the lovable that we made. You know, similar pretty similar. I'm surprised they chose such a gray.

**1:19:00** · Gray. Yeah. Like maybe there's something there though, like they want you to like get bored by it and then like your site captivates you.

**1:19:09** · Maybe something like that.

**1:19:11** · Yeah. I do have to say ours is better. Yeah.

**1:19:15** · No, I like a lot of what Lovable has done.

**1:19:17** · Me, too. It doesn't feel very crowded given how many I know they have a lot of features though like oh okay these are cool these are cool quality of life things we failed to get our agent to properly speak to us that was something it's not too difficult but I don't feel like reading any more Daytona docs today this is cool let's go back to ours and wait for it to load our project is nearly done okay Oh.

**1:19:47** · Oh. Okay. So, we have these links. You can paste a link here.

**1:19:53** · You can manage links.

**1:19:55** · Yeah. So, wait. Can you paste? Can you add one like manage links?

**1:19:58** · Oh, what does this point me to?

**1:20:00** · Oh, it took you to the link.

**1:20:01** · How did it know what my No, no, there's a manage link button on it. So, hit manage links.

**1:20:06** · Okay. So, you can manage the link and No, this is pretty cool. We can edit our own links. So, I can go ahead and grab my GitHub, actually. Yeah, just grab anything.

**1:20:16** · Let's grab this.

**1:20:17** · Young Khan. So, this is Lovables and this is ours.

**1:20:21** · All right. You know what?

**1:20:22** · They look I mean, the gradient's like somewhat better. I mean, fine. You know, it's harder to read their text, but I add in one manage one of the links here.

**1:20:31** · I mean, I'm just genuinely shocked at like how similar they are.

**1:20:34** · Yeah. I mean, we've only been working on this for two hours. So, yeah, I know. I mean, crap. Is this Lovables? Oh, this is love voice. Yeah.

**1:20:43** · GitHub link.

**1:20:44** · Yeah.

**1:20:45** · Paste the URL.

**1:20:47** · Oh, I mean I mean that's it, I guess.

**1:20:48** · That's You know what? They're similar. They're similar. But the point is in two hours we created like a respectable clone. I mean go if you want to go over to ours.

**1:20:57** · Hit add link.

**1:20:58** · Oh yeah.

**1:20:59** · Wait, how do you reset it so it doesn't look Oh, yeah. Yeah. Back back to links.

**1:21:04** · Yeah. Yeah. Yeah. So I mean yeah, we created this link tree. Uh we also created on lovable. It takes you to the link. Let's go.

**1:21:10** · Very neat. Let's see if Lovables takes us to the lake. Yeah, it does. Cool.

**1:21:15** · Cool.

**1:21:16** · Amazing.

**1:21:17** · Yeah. And yeah, that's what we created in about two hours using claude code. So in summary, within cursor, we ran cloud code. Like we used cloud code in cursor and we used claude code to build a lovable clone that used the cloud code SDK. So cloud code built cloud code which we wrapped and called it lovable clone. And then we used lovable clone to build an app.

**1:21:42** · Build a link tree app.

**1:21:43** · That's what we did.

**1:21:44** · I didn't write a single line of code. If you think about it, I just vive coded this whole thing.

**1:21:49** · Yeah, you did vive code. I mean, there was there was invest. You looked through code in documentation, but like soon basically the limitation was cloud code not looking through the docs well enough. And as soon as that gets better, it probably would have cut a lot of time out of this. I think honestly this project and you know I kind of did say this going forward that it is a little bit more complicated to have separate systems and spin up your own isolated environment and have code development be done there and then port that over to our website.

**1:22:20** · That is definitely more complicated. It is like a pretty powerful thing that we managed to accomplish without me writing a single line of code. I think you're absolutely right about how once you know these models are going to be better at searching for docs online themselves, this could definitely be a problem that it's solved. Currently, I always do think the skill of navigating the LLMs to go in the right direction will be a persistent skill as well as finding projects that people will actually like users would actually want.

**1:22:50** · If we clean this project up, we will actually throw the link on GitHub. We'll put it in the description down below if you want to like test it out yourself. And uh yeah, we'll see you in the next