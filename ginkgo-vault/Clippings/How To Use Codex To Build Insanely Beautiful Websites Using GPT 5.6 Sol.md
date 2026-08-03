---
title: "How To Use Codex To Build Insanely Beautiful Websites Using GPT 5.6 Sol"
source: "https://www.youtube.com/watch?v=pHstb0JGGhE"
author:
  - "[[AI LABS]]"
published: 2026-07-17
created: 2026-07-21
description: "Learn how to use Codex to build pro websites in 7 stages, no AI slop. This OpenAI Codex walkthrough is a full codex tutorial from OpenAI on how to build apps with AI. New to the openai codex cli tutor"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=pHstb0JGGhE)

Learn how to use Codex to build pro websites in 7 stages, no AI slop. This OpenAI Codex walkthrough is a full codex tutorial from OpenAI on how to build apps with AI. New to the openai codex cli tutorial scene? Start here.  
  
Community with All Resources: http://ailabspro.io  
  
The Roundup, our daily newsletter covering the AI stories that matter. Join now: https://www.theroundup.so/  
  
We're a software company, and in this video we walk through the exact 7-stage process we use so Codex builds websites that feel like a real brand, not something that was AI vibe-coded. Whether you've never opened it before or you've been building for a while, this covers how to use codex chatgpt the right way, from the very first setup to a finished, client-ready landing page.  
  
Since Codex is now a mode inside the ChatGPT app, we start with the complete beginner setup, then move through every stage. You'll learn how to use chatgpt codex to define a real purpose for your page, write an AGENTS.md file, and give Codex a reusable design system with the GPT Taste skill so it stops producing the same generic AI look.  
  
From there we get into the parts most people miss. We show how to use codex in chatgpt for browser verification (letting Codex check its own site and responsiveness), how to give a brand its own identity with a DESIGN.md file, and how to generate original brand images instead of stock photos. If your goal is learning how to use codex to build an app or a landing page you can actually sell, these stages are where the "AI slop" disappears.  
  
We finish with layout inspiration, upgrading individual components, optimizing heavy animations, using Git checkpoints, and deploying the finished site to a public link (even with a custom domain), all inside the Codex app. By the end you'll know how to use codex the best way we've found for real client work.  
  
If this helped, subscribe and hit the like button, it genuinely helps the channel.  
  
0:00 Intro  
0:42 From zero to your first Codex project  
2:39 Stage 1: Getting started  
5:58 Stage 2: The Greatest Agent Skill For Design  
9:40 Stage 3: Codex verification  
11:41 Brand Identity  
15:11: Sponsor  
16:11 Stage 5: GPT Image Combinations  
18:47 Stage 6: Inspiration  
20:18 Stage 7: Upgrading the small parts  
22:52 The tip that saves you if Codex breaks something  
23:41 Deployment: putting your site online  
  
Hashtags:  
#ai #claude #claudecode #codex #chatgpt #aiautomation #vibecoding #howtousecodex

## Transcript

### Introdução

**0:00** · If you didn't already know, we're a software company and we've developed seven stages that you can use to make sure Codex builds websites that don't look AI vibecoded, but actually feel professional and belong to a real brand.

**0:12** · Whether you're completely new to AI coding or you already have experience with it, there's something here for you.

**0:17** · If you've never opened Codeex before, that's completely fine because we're going to start from the beginning. And if you already have experience with Codeex, this isn't just the same beginner process. We've found new ways that you can use to build better websites. There are timestamps below, so you can skip anything you already understand and jump directly to the newer stages. By the end, you'll be able to create some really awesome landing pages and websites and actually sell them to clients as well. So, let's not waste any time. Let's get into the video. If you \[snorts\] already use Codex, you can skip this setup and move to the first stage.

### Do zero ao seu primeiro projeto Codex

**0:45** · But if you've never opened it before, you need to download the chat GPT app because Codex is now a mode inside it. After you download it, you're going to see something like this.

**0:55** · Then, you have to sign into your account. While the free version does give you very limited usage, we do advise that you get the $20 plus plan if you want to build and that will be enough for your usage. If you want to build more with it, you can upgrade to the $100 or $200 plan, but for now, the $20 plan is fine. The first thing we're going to do is switch into Codeex. As you can see, we have multiple projects here. To create a new project, you can start from scratch and call it anything you want. It's going to create a folder for you. To start working in that folder, you just type out your very first prompt.

**1:25** · As you can see, codeex has started working and it's going to reply here. Now, you can think of these as different chats inside a folder. If we open a new chat, you can see that it creates another one here. If you don't already know, Codeex calls these chats threads. Here you can see that we have the model picker. For this video, we're using the latest model GPT 5.6. If you haven't used these settings before, effort controls how much work the model puts into its answer. We recommend that you always keep it between light and high and never go above that because it just eats away at your usage and doesn't actually give you any benefit.

**1:57** · For speed, we recommend that you keep it on standard. These Codeex models are comparatively faster than other models such as Claude. So, we've never felt the need to switch it to fast because that also uses additional usage. To check your limits, you can click on this menu here. You'll see that we still have 81% of our weekly usage remaining. So, you need to make sure that you keep an eye on this. Now, there's one more thing we want to explain before we actually get into the building part. If you don't already know, a Codeex project is an actual folder on your computer.

**2:25** · If we click here and open the files, it's going to show all the files inside that folder. So, you never need to leave the Codeex app. You never need to open the terminal and you never need to open any IDE such as Visual Studio Code. Let's \[snorts\] start with the first stage.

### Etapa 1: Primeiros passos

**2:40** · Before Codex designs anything, it needs to know what the website is supposed to do. A prompt like build a landing page for an AI community gives it a topic, but it doesn't explain who the page is for, what that person needs to understand, or what action the page should lead them towards. So, Codex has to guess those decisions, and even if the page looks good, it can still solve the wrong problem. So, here you can see that we started by telling it that we wanted to build a landing page. You can mention that Codeex should use Nex.js.

**3:08** · If you haven't worked with it before, Nex.js is basically the system Codex will use to build the website. If you don't understand what this means yet, just include this line. Then you need to define the purpose of the landing page and what it's for. For example, here we're creating a landing page for an app called Beacon, which is a podcast analytics platform. After that, we define what the platform is going to do based on which it generates the actual content for the landing page. Then we have the most important part. What is the actual function of the landing page?

**3:36** · Here the function of the landing page is to get users to click and join the weight list. This is the most important line in the prompt. Some landing pages are for products that have already been built. You'll usually see a sign up button on those landing pages, but here we just want people to join our weight list. So, Codex knows exactly what to build. Now, Codeex can build a website from a single prompt, but it only knows what you've told it inside that conversation. So, when you start a new thread or move on to another section, it can start making different decisions about the same project.

**4:04** · If you haven't used an agents.md file before, it's basically the instruction file C codeex reads before it works on your project.

**4:12** · It gives Codex the context it needs about what you're building. So instead of repeating the same instructions in every prompt, every new task starts with the same information. So in order to generate an agents.md file, you don't have to actually write all of this down.

**4:26** · There is a custom command built into codeex that you can use. You just have to type a forward slash and it's going to give you a bunch of options. We're going to cover the important options in this video, so you don't need to start thinking about all of them right now.

**4:39** · Down here, you'll see that we have the init option. Once you select it and press enter, it's going to give CEX this prompt. Using this, Codex will create an agents.md file and include all the context that we gave it in the initial prompt. If you want to view the file, you can open it up. You'll see that we have a lot of files here. That's because the project has already been built. But don't worry, we'll guide you through all the stages one by one. If we open the agents.m MD file, you can see that it contains some basic information about how codeex needs to work along with important details such as the project structure and folder organization.

**5:10** · Codex has basically listed all of our important information in the appropriate places. For example, it has written here that this folder contains the next.js landing page for the beacon website.

**5:22** · Further down in the file, it has listed all the other details as well. One other important thing is that you need to tell Codex to add an instruction at the top stating that whenever Codex can perform an action itself, it should do so. This includes starting the app and verifying that it was built correctly. We'll come back to this later, but the reason for this is that these Codeex models have one flaw. Although it has improved a lot with the release of the latest models, they tend to ask you to do things for them even though they can do them themselves. So adding this instruction at the top of the agents.mmd file really helps Codeex work autonomously.

**5:53** · So you don't have to continuously monitor it.

### Etapa 2: A habilidade de agente mais importante para design

**5:58** · Now that \[snorts\] Codeex knows what we're building, the second stage is giving it a reusable set of design instructions. If you haven't used skills before, they're basically instruction files that Codex reads whenever it's doing a specific type of work. So instead of explaining the same web design rules in every prompt, you save them inside a skill and Codeex loads them before it starts designing. This matters because a better model doesn't automatically give you a unique design.

**6:22** · Even without additional instructions, the model can generate a pretty good website from a short prompt. The problem only becomes obvious after you've generated enough of them. The content changes, but the same design language keeps appearing. And because thousands of people are generating websites with the same models, that design language starts appearing everywhere. This is what people mean by AI slop. A website might look good on its own, but it still feels like it came from the same template as every other AI generated website.

**6:49** · The original front-end design skill from Anthropic was created to prevent the older AI design defaults, but newer models already avoid many of those choices and have developed a different visual style that the original skill doesn't account for. So, for this website, we're using the GPT taste design skill. It gives Codeex updated rules for the entire visual system and pushes it away from the patterns newer models now repeat. Now, the GPT taste skill comes from this set of 13 skills.

**7:16** · While there are lots of skills, the one that's best for use with the GPT models is the GPT taste skill. If you're using any other model, you can experiment with the rest as well. Adding it to Codex is pretty easy. You just have this install command, copy it, go back into Codex, and tell it to install it for you. You can see that it installed all the skills first. Now, before you can use them, you have to quit codeex and come back to this chat again. Since this is a thread, everything is going to be saved and you won't lose any of your work. After that, you need to reference the GPT taste skill in codeex. Type the /ash command and write out the name of the command.

**7:49** · Once you press enter, it's going to be inserted into your prompt and C codeex will basically read everything that's inside the skill. Now, you can see that after we added the skill, we told it to start the build and specifically told it not to use the site skill. If you haven't used the site skill before, it's OpenAI's replacement for Anthropic's front-end design skill, and it copies a lot of the same concepts. But we've experimented with it, and it doesn't really produce good outputs. So, we would advise you to stay away from it and specifically tell Codeex not to use it because it will default to using it if you don't mention it.

**8:20** · You can also ask it to write in the agents.md file that it should never use this skill for designing. We're specifically saying for designing because there is one other use for this skill that we'll look at later in the video. After that, it's basically going to build the whole website. You can see that it worked for 17 minutes and built the entire site. Once the site was built, it gave us this link. If you haven't worked with a local website before, local host means the link only works on your computer. If you share it with someone else, they won't be able to open the website you just built.

**8:49** · But don't worry, we'll come to that later in the video. To preview the site, you don't actually need to leave codeex. You can open the side panel and here you'll see that you have a browser. Just enter this link there and you can see the site that it generated for us. So this is the site that it generated and honestly it looks really really great. The animations are properly done and they're not janky. There are some small issues that we're going to fix in the later stages such as the stock images, a few animations being too janky, and one other issue that we'll bring up later.

**9:19** · But one thing we want to mention is that because we clearly defined what this site was for, it accurately set up the user journey. First, it gave us the product showcase. If we had an actual product, it could showcase that here as well. Then it gave us these smaller graphics, which again look really amazing. And finally, because we clearly specified that this was a weightless landing page, it created a CTA asking users to sign up early. \[snorts\] The third stage is browser verification. A website can run correctly and still have visual problems because working code doesn't mean the finished design looks right.

### Etapa 3: Verificação Codex

**9:50** · Browser verification gives Codeex the actual website as feedback, so it can catch problems that only become visible once the page is on screen. This is also one of Codeex's strongest areas.

**10:00** · If you haven't heard the term computer use before, it's basically the model's ability to understand and interact with what's on screen. GPT models are the strongest models for computer use. So, in our testing, Codex's browser verification has been much more reliable than what we've seen from other coding agents. Now, we didn't have to manually ask it to verify that everything on the landing page looked correct. This is because in the agents.md file, we already told it that it should perform the verification itself. That's why it didn't ask us to do anything.

**10:28** · If we scroll down, you can see that it used the browser multiple times to inspect the website. It didn't find any errors, which is why it didn't edit any files during the browser verification. It did edit some files here, but those were code related changes that you don't need to worry about. Another thing it does during browser verification is check responsiveness. If you don't already know, responsiveness is basically how the website adjusts to different screen sizes. For example, if we stretch it out, which is how it's going to appear on a desktop, you can see that it looks great.

**10:58** · And if we make it narrow, which is how it's going to look on a mobile device, you can see that codeex has automatically taken care of that.

**11:04** · Normally, you had to tell models to make the website responsive. You don't need to do that anymore because they automatically handle it. But as a quick test, you should still drag the window and make sure everything is responsive.

**11:15** · If any element isn't responsive, you can just take a screenshot and give it to the model. There is a tool called the annotate tool, but we found that it's really janky and not very reliable, especially when you've zoomed in. So, we just use the screenshot method, and we'd say it's the better option at the time of recording. Maybe later on this feature will improve and you can start using it. And if you're enjoying the video so far, subscribe to the channel and hit the like button. This small gesture of support goes a long way for us. The fourth stage fixes the other problem we mentioned earlier.

### Identidade visual

**11:43** · Even after using the GPT taste skill, the website still falls back to the same kinds of colors that GPT models use across other designs. The skill improves the model's general design decisions, but it doesn't give this specific brand its own visual identity. So, if everyone uses the same model with the same skill, the results can still start looking similar. This is where design.md comes in. If you haven't come across it before, Google introduced the design. MD format through Stitch which is its AI design tool.

**12:10** · A design.md file is basically an instruction file containing the complete visual system for one brand. It gives the model specific design direction to follow instead of letting it choose from its usual defaults. So the GPT taste skill teaches codeex how to make better design decisions in general while design. MD tells it what this particular website should look like. So here's an example of the problems we're facing here. You already know that the design skill made this website, but without the design skill, GPT 5.6 was able to achieve this.

**12:41** · Now, again, it's a pretty good website even without all that flare. But you can clearly see that a lot of the elements have been reused, especially the color scheme. This green color and this purple color are reused quite a bit. The design skill used the purple color a little less, but it still used it. This is why design.md files are so important. Now, the question is, where do you get these design files? There are lots of resources out there. One of them is called getdesign.md and it has loads of designs from different people. You can get the design systems of Claude, Cursor, Discord and other well-known companies as well.

**13:12** · But we really like this design.md collection from Aurabuild which is actually a website builder. But they also have this free design.md library. You can scroll down, click on the popular ones, and you'll find these amazing design systems. It's not like this will change the layout or style of your website. Instead, it applies things like spacing, colors, and other design details that give your site a completely different look. That's why we downloaded this design.md file. You can just click this button, and it'll download it to your downloads folder.

**13:42** · After that, go into CEX, click this button, and attach any files or folders that you want. You can see that this is the file we downloaded. After attaching the file, we told Codeex that it needed to create a design.md file in the project, copy the contents of this file into it, and then revamp the site according to that design.md. We specifically told it that the structure, layout, and animations should not change. Because one important thing is that the GPT taste skill we installed is really good at animations.

**14:11** · You don't really need to do anything else in terms of the overall page animations. It handles most of them on its own. And you can clearly see that they look really good. And you can see that after it finished, it told us that it had created the design.md file and applied the visual system to our beacon platform. Now you can see that the layout and the structure are still the same and it hasn't changed those, but it has completely changed the color scheme and the site looks completely different.

**14:35** · If you compare it to the original greenish design, it doesn't look like it was generated by one of the GPT models.

**14:41** · This is why having a design.md file is really important. One more thing before we continue to the next stage. Whenever we're building landing pages or even full apps, we always use phosphor icons and we always add that to the agents.md file so that whenever CEX has to create anything new, it can use those icons.

**14:59** · This is our favorite icon set because it's really minimal and looks great.

**15:03** · Even though it's mostly used in small places such as the arrows, it's still in our opinion the best icon set out there.

**15:09** · But before we move to the fifth stage, let's have a word by our sponsor. Let's talk about how I launched an e-commerce store ready to take real orders in just minutes without spending weeks on setup.

**15:19** · I pasted one link into Copify and minutes later I had a completely live Shopify store. Product descriptions, copy, design, everything AI generated and ready to convert visitors into buyers. Real storefront, fully stocked and professionally designed. That's the actual win. Not just having a store, but having a business ready store that makes money before your first sale. Here's exactly how it happened. I clicked connect to Shopify straight from store AI and it pushed everything live instantly.

**15:46** · Then I added more products to the same store and built a second complete store from a totally different link in just minutes. There is no manual setup or design work required. But here's what makes this genuinely powerful. AI Chat hands you proven marketing angles for every single product and Creative AI generates the actual ad creatives to sell them.

**16:05** · Everything you need to run a profitable converting store is already built in and ready. Head to the link in the pinned comment and launch your store. Now, the fifth stage fixes another problem we pointed out earlier, which is the stock images. The design file has given the website its own visual system, but the stock images still don't belong to that system. They can fill the empty space, but they rarely match the exact brand.

### Etapa 5: Combinações de imagens GPT

**16:27** · This is another reason AI generated websites can feel assembled instead of designed. This is where original GPT images come in. Codex already understands the product through the agents.md file and it understands the visual direction through design.md. So it can use that context to generate original brand imagery with the GPT image model and add those files directly to the website. So what you need to do is give it a prompt telling it to create an assets folder and link it in the agents.md file as well.

**16:53** · This folder will contain any assets that the GPT models generate or anything that we want to add to the landing page ourselves. For example, if we want to use our own custom images. After that, we told it that it needed to replace all the stock images on the landing page. Here are the important things that you need to mention. You need to tell it that the images should match the design and the content they're meant to represent. That way, it doesn't just generate random visuals. It generates visuals that are actually relevant.

**17:21** · Here, we asked it to generate illustrations for us since there was a higher chance of it making mistakes on this task. And especially if you're on the $20 plan where image generation might be limited, we highly recommend turning on plan mode first. If you haven't used plan mode before, it lets Codeex work out what it needs to do before it changes the project. You don't need to mention it inside the prompt.

**17:42** · Just click this button. After that, it's not going to touch any code or make changes to the website. Instead, it's going to come up with a plan first and then generate the images. We went through the plan, told it that everything looked good, and then asked it to implement it. After that, it generated these images and you can see that they match the design of the website really well. If you're wondering why some of these images are different from the previous ones, you'll find out when you see where they were placed. It also added instructions to the agents.md file about where the image files should be placed.

**18:11** · If you look inside the app folder under the public folder, you'll find the assets folder. Whenever you need to add images, just put them in there and tell Codeex what to do with them, and it'll add them to your site.

**18:21** · As for the final result, this is what we got. And you can see that these illustrations look really amazing. It's not just that they match the design of the website. They also match the descriptions written below the cards.

**18:32** · That's the advantage of using these custom models to generate images. Other than that, you can see that it also placed these images in this animated section. If you're wondering why the last three images were different, it's because it generated these avatars for the testimonials. Honestly, they look really, really good. The sixth \[snorts\] stage is improving the layout with visual inspiration. At this point, the website has its own design system and original images, but Codex still decided where everything should go using the layout patterns it already knows.

### Etapa 6: Inspiração

**18:59** · So, the colors and images can feel original while the structure still feels like a standard AI generated landing page. This is most noticeable in the hero section because it's the first thing people see.

**19:11** · Layout is also difficult to explain through text alone. So, giving Codex a visual reference shows it the type of composition we want. The goal isn't to copy another website. It's to use the layout as inspiration while keeping our own brand and content. So, where do you get inspiration? One of the most common places is Pinterest where you can find a lot of inspiration for whatever you're building. For example, we searched for hero sections for SAS apps because that's what we're building and we've got lots of different designs here. This one is really interesting and you can see that we've got layouts similar to this as well. So, this is a really great place to get inspiration.

**19:42** · Other than that, we have awards which showcases some really amazing websites. If you go into their directory, you can find some really awesome looking designs. These are some of the best places to get inspiration if you're not satisfied with the layout that the model has generated.

**19:58** · In our case, as you already saw, most of the hero sections we found on Pinterest for SAS apps looked very similar. We're honestly satisfied with this one, so we're not going to change it, especially this section here. It looks really great and clearly showcases all the features that the app has. But if you're not satisfied, you can always give the model a screenshot of another design and ask it to recreate it. The seventh and final stage is improving the individual parts of the website. If you haven't worked with components before, a component is basically one reusable part of the page, such as a button.

### Etapa 7: Aprimorando os detalhes

**20:28** · At this point, the overall design is already in place, but some of these smaller parts can still feel generic. Instead of asking codeex to redesign the entire website, we can replace only those parts with components made by other designers. This gives us more control over the smaller details without changing the design direction we've already created. So to get these individual components, there are lots of sites. One of them is 21.dev and it has both free and paid components. Other than that, there's godly and fancy components. All of them give you components for specific parts of your app.

**20:59** · For example, we have this navigation switcher with liquid glass, this background for a hero section, and this navigation expander with a fluid animation. There's lots of stuff and whatever you feel would improve your application, you can just add it. For example, we only felt that we could improve the landing page in one way, which was by improving the background of the hero section. So on 21.dev, we found these backgrounds called shaders. And we really like this one. It looked really good to us. All you need to do is copy the prompt. It contains all the information needed to apply it.

**21:27** · Give CEX the prompt and tell it to apply it to the hero section. We specifically asked it not to use the skills because it would use an optimization skill that we're going to talk about later. After that, it applied the change and then we asked it to tweak the colors a little.

**21:42** · This is the final result that we got and honestly it looks really amazing. It's a huge improvement over what we had before. Now, you can see one thing when we navigate around the app, it feels really slow. That's because of how many heavy animations it has. It's not that you need to remove these animations. You just need to optimize your site so that it loads quickly. In order to do that, you just need to ask the model to optimize the site and that alone can fix most of your problems. But we've made a custom skill for optimizing animationheavy landing pages. Since it's a skill, you can activate it using the slash command.

**22:12** · After that, it took quite a long time and you can see the metrics showing how it reduced a lot of the latency in the website and made it much faster. Now, this is part of our AI labs design system which we use when building our own products and working on client projects. You can see that the optimized skill is right here. And we have lots of other skills that we use throughout our design process. This custom skill along with other resources can be found in AIABS Pro, which is our community.

**22:39** · That's where you'll get the resources, the starter packs, and more along with a place to interact with a bunch of like-minded people, including our team.

**22:46** · So, if you found value in what we do and want to support the channel, this is the best way to do it. The links in the description. Now before we move on to deploying this so that anyone on the internet can see it, we just wanted to give you a small tip. If you haven't used git before, it lets you create local commits which are basically checkpoints for your project. You don't need to sign up for anything to use them on your computer. For example, here you can see that we asked codecs to make a local commit. It created the commit and gave it a name. What this does is create checkpoints that you can revert to if anything goes wrong.

### A dica que te salva se o Codex quebrar alguma coisa

**23:16** · You can see that we built this entire website and we've been using these checkpoints to go back and show you the different stages of the project. Right now, we're at the final commit where the website is complete.

**23:27** · So, you just have to ask codeex to make local commits and it'll know exactly what to do. It'll also give you the name of each commit. You can even ask it to list all the commits if you've forgotten their names. And then you can easily go back to any of them if Codeex messes something up. The website \[snorts\] is finished, but right now it only works through localhost, which means it can only be opened on your computer. If you haven't deployed a website before, deployment is basically the process of putting it online so anyone can visit it through a normal link.

### Implantação: colocando seu site online

**23:55** · Previously, deploying a website meant creating a Versal account and connecting the project through GitHub. The process worked, but it involved several separate steps. Codex now makes this much easier through the site skill we mentioned earlier. We didn't use it for designing the website, but we can use it to publish the finished project directly from Codeex. So, all you need to do is click on this plus button, add the site skill, and ask it to deploy the site for you. It's going to take some time and after that it'll deploy it. Now, before you actually visit the site, you can see this separate site section in the sidebar.

**24:25** · Open that and this is where you'll find all the sites that you've published through chat GPT. For example, this is the old site that we designed using the site skill. This is why we were asking you not to use it because the design is so basic and we just weren't satisfied with it at all. This is our second site. If you click on the share button, it'll initially be set to just me. Change it to anyone on the internet and then publish it. After that, you can copy the link and send it to anyone and they'll be able to open the site and visit it. Since it's now deployed, you can visit it yourself as well.

**24:55** · If you want to use your own custom domain, just go to settings and there you can add a custom domain. It'll guide you through the whole process and you can deploy a landing page for yourself or for a client all through the Codeex app in just a few simple steps. That brings us to the end of this video. If you'd like to support the channel and help us keep making videos like this, you can do so by using the super thanks button below. As always, thank you for watching and I'll see you in the next one.