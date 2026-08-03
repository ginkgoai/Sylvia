---
title: "Build and Deploy a Fully Responsive Modern Website using ReactJS and Tailwind CSS"
source: "https://www.youtube.com/watch?v=yS7B1W2SwaU"
author:
  - "[[PedroTech]]"
published: 2025-10-28
created: 2026-07-02
description: "Want to Learn ReactJS? 🌟Check out my Course: https://www.webdevultra.com/reactBuild a beautiful and modern ReactJS Website using TailwindCSS. This website will be fully responsive and will teach y"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=yS7B1W2SwaU)

Want to Learn ReactJS? 🌟  
Check out my Course: https://www.webdevultra.com/react  
  
Build a beautiful and modern ReactJS Website using TailwindCSS. This website will be fully responsive and will teach you react and tailwind fundamentals.  
  
📖 Video Resources:  
Code Repo: https://www.webdevultra.com/video-info/yS7B1W2SwaU  
  
💻 Check out my Blog: https://www.webdevultra.com/articles  
🐤 Follow me on Twitter: (https://twitter.com/pedrotech\_)  
📸 Follow me on Instagram: (https://www.instagram.com/pedro.fmachado\_/)  
🧳 Follow me on Linkedin: (https://www.linkedin.com/company/pedrotech)  
  
📋 Business Email: pedro@pedrotech.co

## Transcript

**0:00** · Most successful websites you know have one thing in common. They have a beautiful landing page. In this video, I will be teaching you how to build the most beautiful React JS website with a modern UI UX design. We will use React JS and Tailwind CSS to build a landing page that includes a modern-looking hero section, an insightful feature section, an eye-catching pricing page, and a part to show the testimonials of your website.

**0:29** · Not only will you learn how to build this incredible design, but you will be able to replicate it for your own use case. However, if you're interested in learning React JS even more in-depth, check out my React JS ultra course for beginners. The link for it will be in the description. And before we start the video, if you could leave a like and subscribe, I would massively appreciate it. So, let's get into it. Okay, everyone. So, let's get started.

**0:57** · I open up here a folder inside of my code editor of choice, which is VS Code, and I want you guys to do the same. Now, we're going to be using a Vite to create our React project. So, in order to create a Vite application, I'll open up the terminal, and I'm going to run NPX create Vite. And I'm going to do at latest so that we get the latest version of Vite. Now, when we install this, it's going to ask for a project name.

**1:23** · Since I want to create this app inside of the folder that I'm already inside of, I'm going to put a dot, but you can make another folder uh by putting the name of it over here as well.

**1:32** · Then, it's going to ask us for our framework. We are using React for this video, so I'm going to choose React.

**1:38** · Then, it's going to choose for a variant. They have a lot of different uh example projects that you can choose from, and I personally will choose for this video to create a project using JavaScript plus React compiler. Now, if you're not familiar, React compiler won't make any difference in the coding for this video. You can choose just normal JavaScript as well. Uh I want to use JavaScript because I want to make it inclusive for everyone, but if you want to use TypeScript, you can use it as well. Now, I'm going to put no for this option, and I'm going to put yes for uh NPM and start.

**2:08** · And it will start installing uh all of the dependencies that we should have in this application.

**2:15** · As you can see, we should have the project set up over here. So, right off the bat, we have here our project running on localhost 5173. So, what I want to do is go to this uh URL inside of my web browser so I can see the application. Now, the first thing I want to do is I want to set up Tailwind CSS in our project. To do that, I want to run NPM install, and I want to install two packages. The first one is the Tailwind CSS.

**2:44** · The second one is at Tailwind CSS, but the Vite package for it. Now, we're going to install both of them. They don't come with Vite when you set it up.

**2:54** · Uh as that is installing, what I want to do is I want to go to our Vite config.

**2:59** · In our Vite config, we have to set up the Tailwind CSS plugin. So, at the top over here, I'm going to import Tailwind CSS from at Tailwind/vite, and in the list of plugins, I'm going to add Tailwind CSS over here.

**3:16** · Perfect. Now, to actually get Tailwind to work in our project, we have to open up our source folder, and inside of here, we're going to start by arranging some stuff. So, in our app.css, I want to delete this. We're just going to have one CSS file, which is going to be this index.css over here. Now, in here for now, we're just going to delete everything that is here. But, what I would do want to do is I want to at the top import Tailwind CSS. Just like this.

**3:44** · And what this will do is it will now apply the different Tailwind classes that we want to use into our project. So, now let's get started. The first thing I want to do is I want to set up our app. jsx, which is the entry point component in our application, and I want to make it such that this component will serve all of the other components we're going to have in this project. To do this, I'm going to delete a bunch of the stuff that initially came with this page, and it should become just an empty website.

**4:16** · Now, right off the bat, in our main div that is \[clears throat\] being served over here, I want to put the following class name. I want to make the app component fill in vertically the minimum height of it to be the height of the screen.

**4:31** · Then, I want to put a background color to it. The background color I'll be using is called slate. That's one of the Tailwind CSS colors, and I want to use the darkest version of it. So, it gives this kind of blue aesthetic to it. Now, the second thing I want to do is I want to make all of the text inside of this page to be white. Also, I want to set the overflow of this page to be hidden.

**4:52** · Now, the first thing I want to do is I want to add some really cool gradient glows that should appear on this page.

**4:59** · Now, the first thing I want to do inside of here is I want to set up the structure for this page. So, what I want to have here is I want to have the different parts of the website serving as components. So, for example, the first part of the page is going to be a navbar. So, I want to create a navbar component that is going to contain the UI for the navbar. We don't have that yet, but we're going to create, and for now, we're just putting it over here to at least have an idea of the structure. The second thing is we want to have a hero section.

**5:30** · So, I'm going to add a hero component that we're going to create.

**5:34** · We're also going to have a features component, which should show all the features of the website. Then, a pricing section.

**5:44** · And we're going to have a list uh a place for us to display testimonials of our service. And in the end, we're going to show a footer.

**5:55** · Now, the reason why we are laying them out into individual components is because it will make it easier for us to be able to identify what UI is part of which section. Now, we're going to organize those sections inside of a components folder we're going to create in our source folder. Now, we're going to create a file for each of this sections. So, we'll start with the navbar. We're going to create a jsx file for that.

**6:19** · And inside of here, what I want to do is I want to export default function and create the navbar component. For now, I'm just going to return a div that doesn't have anything inside of it.

**6:34** · And the reason for that is because what I want to do is I want to create all of the different sections and the files for them first to then start writing code inside of it. So, the second section is going to be the hero section. So, I'll create a hero.jsx, and in the hero.jsx, we're going to change this to say hero.

**6:53** · Then, we're going to come back here. We have the features, so I'm just going to copy and paste this. Create the features.

**7:00** · jsx. Same thing, I'm going to update this to say features.

**7:04** · And we're going to have the pricing and then the testimonials and the footer.

**7:09** · So, I'll create three files. The first one, I'm going to say pricing. The second one, I'm going to say testimonials.

**7:18** · And the last one, I'm going to say footer.

**7:21** · Now, in each of them, I want to make the change that we did on the other one. So, on the pricing, I'm going to change this name to be pricing. On this one, I want to change it to say footer. And then on the testimonials, I want to change it to say testimonials. Right now, we're just setting up the structure for our project. Now, what I need to do is I need to import those components at the top here.

**7:44** · So, I'm going to import the navbar component from, and then I'm going to put a dot slash and access that navbar component in our components folder. Then, I can do the same thing for all of the other sections, and just change the name from navbar to hero.

**8:03** · This will also be hero, and so on. I'm going to cut to when I do it for all of this, and I'll be back. Perfect. So, as you can see, now the page isn't white anymore, and that's because this we were calling a component that didn't exist previously, but now it does because we are importing it at the top, so there's no error. And we can start building the project by starting off with the very top, the navbar.

**8:25** · The navbar usually does take a while to make because not only we want to make a beautiful navbar that extends it well on web, but also a navbar that is fully responsive on mobile. So, we're going to start with the web version. And to do that, I'm going to replace this div component or this div element with a nav element. In this nav, we're going to define the classes for the navbar. We'll start by saying that the navbar is going to be fixed at the top. We're going to put it right at the top, so top zero.

**8:55** · And the width of it is going to be full so that it extends the entire width of the screen. Then, I want to make sure that the navbar is always at the top, so I'm going to put a Z index to be 50. I'm setting a transition all, and that transition is going to have a duration of 300. Now, if you're not familiar with uh Tailwind CSS specifically or these classes over here, you'll understand as we move on.

**9:20** · Right now, the navbar will be very simple, but we do want it to have uh some sort of animation as we scroll down through the page. Now, what I want to do is I want to start by making this have a BG, which is exactly like the color of the background, so BG slate 950. It's the same color, but I'm going to give it a less opacity. So, you give it less by dividing that color by 20.

**9:48** · And then, I'm going to add this class name called backdrop blur, which allows us to put a little blur into the element. And I'm going to give a blur with a small size. Now, none of that is visible yet, but as we add stuff into this navbar, you'll be able to see it. Now, the next thing I want to do is I want to add a div that is going to encompass the entirety of the elements inside of this navbar.

**10:17** · We'll start by setting a maximum width that this div can have. And I'm going to give it a maximum width of 7 XL, but you can make it whatever you want. Now, I'm also setting a margin in the X direction to be auto and a padding of in the X direction to be four.

**10:35** · And that padding should only be applied to the mobile screen. We're going to be building the responsiveness of this page as we build the app. So, the way it works in Tailwind CSS is you can put styles that only apply to a certain screen size and above, similar to CSS.

**10:53** · So, we are putting here a padding X to be four in the smallest screen possible, but on a large screen and above, I can put this padding X to be eight. And in between these two values, I can check to see what I want to put the for the padding in a small screen and above, which I want to make it be six. So, if this the if the screen is very small, it will be a padding of X of four. If it's small to medium, it will be of six.

**11:21** · And if it's large and above, it will be of eight. Now, none of that right now is very visible because again, the background of this navbar is the same color. But if I were to make, for example, this be red, now none of this is really visible in the moment because we haven't really set a height to this navbar. But that's what we want to do right now. So, inside of this div, I want to add another div. And this one will have a display of flex.

**11:49** · I'm going to justify the items in between, to justify between, and I'm going to center the items. Now, here it comes.

**11:57** · I'm going to put a height for this navbar of 14. And that's only for a small screen. Between a small and a large screen, I want to make it be 16.

**12:07** · And in a medium and above, I want to make it be 20. Now, you still don't see Now, you might not see the navbar still because again, we're using the same color. But if I were to change this to red, for example, you can kind of see how it applies here. Now, why are we using the same color for the navbar? It isn't actually the same color. The thing is, when you scroll down, we're going to put a border at the bottom of this section over here. We're going to do something like this.

**12:34** · Border bottom, so that it is the same color, but you can clearly see where the navbar begins and where it ends. But we only want to show the border bottom when the user is scrolling, which is a functionality we don't have yet. So, for now, we'll have to be happy with just this.

**12:51** · Now, below this, what I want to do is I want to have another div. And this one is going to be for the logo of this website. So, inside of it, I'm going to put an image.

**13:04** · And in this image, we're going to show the logo for this website. Now, I already have a logo that I want to use for my website. If you want to copy the logo, just go ahead and get that image.

**13:13** · It'll be in the code in the description.

**13:15** · But I put that logo as a logo.png on the public folder. Now, what that means is that I am able to come here, say source, and access the logo.png directly. Now, obviously, it's a huge image, so we do want to put some class names to it to make it smaller.

**13:35** · Also, for accessibility reasons, we're going to put an alt. And in here, you should put the name of your website. In this example, we're making a website called CodeFlow, which is like an AI coding website, just as an example. But you can name it whatever you want. And for the class name, I want to set this logo to be a square-shaped element with a width of six and a height of six, so it's pretty small. I also only want to have that be the case if this is mobile.

**14:06** · If this is web and above, we're going to put here the width to be eight and the height to be eight as well. So, it's a little bit bigger.

**14:19** · Now, what I want to do is I want to put the name of the website next to this logo. So, right below this div, I want to add a span.

**14:26** · And in this span, I want to add two spans. Now, why are we using span here?

**14:31** · Because I want to apply a different color to each of the words in the logo.

**14:36** · And a span is very good for this because a span doesn't come with any extra styling or padding in it. So, the name of the website is going to be CodeFlow, and you'll see that for now, it shows over here, but we're going to add some style to make it that it will appear right here. But you'll see that they're right next to each other because a span doesn't come with padding. So, it's very easy for me to make the colors be different. For example, this one will be white, and then this one is actually going to be blue.

**15:04** · Uh just like this. And I think it gives a good aesthetic to it.

**15:08** · Now, on this overall span over here, I want to make the text be a little bit larger, so I'm making text large. But on a on the web, we'll actually make it be XL.

**15:21** · Then, on a medium screen, we'll make it be 2XL, and I'm going to make the font be medium. Now, this is the boldness.

**15:29** · You can make it be actual bold if you were to do this, but medium is a good weight to this. It doesn't make it look too bulky and it still looks good. Now, above these two divs two sections that we have over here, I actually want to put another div that will wrap both of them so that we remove this space that exists in between them. That space existed because we had the justify in between, which we only added because we want to have the logo and the name of the website here and the links on the right.

**16:00** · Justify between will put a space in between two different sections. So, the logo section should be made through this div over here. And what we want to do with it is we want to set a display flex. I want to center the items.

**16:14** · So, I'll say item center. And I also want to put a space in the X direction of one, so there's a small gap in between them.

**16:22** · Then, I want to add a group and add a cursor pointer. So, when you hover it, it becomes a cursor. Now, I want to create the different links that we're going to have in this website. So, I'm going to come outside of this div right over here. And I want to add a comment here saying nav links.

**16:44** · Then, inside of this, I want to put a div that will have a class name, which is hidden.

**16:51** · Now, we don't want to have it hidden right now. And the reason for that is because when you give the class name hidden, it will actually hide whatever's inside of this. So, if I put a text here, you clearly don't see it. If I remove this, you'll be able to see it.

**17:05** · Now, we will eventually have it hidden.

**17:07** · And the reason for it is because we want to hide the different menus in the navbar for depending on whether or not the user has a small screen or a big one because we're going to have some logic to decide which kind of navbar we want to show. Now, for now, we want to remove this hidden and just set the normal styles that we have. Now, what I want to do is I want to set a display of flex and I want to center the items. Then, I want to put a gap in between them of six.

**17:34** · Now, we only have this text over here, but if we were to add all of the links, each link will have a gap of six in between them. Now, if this is a large screen, I want to make that gap even more, so I'll put it as eight. Now, inside of here, we're going to put all of our links. We're going to start with the first one. It's going to be the features section, so I'll say features. And to make a link, we're just going to put here an href. And what are we linking to? This is a landing page.

**18:02** · So, when you click on a link, we want to be brought to a part of that landing page. So, we want to scroll down to that section in this page rather than having different URLs and different routes. So, we're going to create different sections, and for each section, we're going to put an ID to the section. That ID can be referenced here in the href through this hashtag symbol, so that when you click on the link, it will scroll down to that div with this ID.

**18:31** · So, when we create the features section, we are going to come here and put an ID of features, so that when we click on this, it will actually scroll down to that section.

**18:42** · Now, another thing I want to do is I want to do some make some styling on this nav link. First, I want to make the color be gray 300, which it'll be just slightly more gray.

**18:54** · And when I hover it, then it becomes white. So, you see it's a bit gray, but when I hover it, it becomes white. Now, I also want to make the text be small.

**19:06** · But if you are in a large screen and above, it's going to be base. Now, a lot whenever I put this kind of stuff, it doesn't actually apply, so we're seeing here the UI for a smaller screen. But if I open this up, you'll be able to see what it looks like in a larger screen. Even the logo on the top left is changing as well. Now, what I want to do is copy this and paste it two more times because we want to create a link for the pricing.

**19:34** · So, I'll come here and say pricing, and I'll change this to say pricing. And I also want to make the testimonials.

**19:43** · Uh and I accidentally made that capitalized.

**19:47** · Perfect. Now, I want to create the infrastructure for us to have a responsive mobile navbar. To do that, right below this section over here for the links, I want to create the button that is going to show up for us to open the mobile navbar when the screen is small enough. So, how do I do that?

**20:06** · Well, I'm going to add a button over here and instead of this button, we're going to use an icon that is a hamburger icon. To do that, we're going to install a an icon library and there's a bunch of them out there, but I personally like to use Lucide React. It's going to give us access to a bunch of different icons that we can use. Specifically, we can use the menu icon from Lucide React.

**20:30** · Now, right now it's just going to show us no matter what, but you guys will see how we can change that to only show when the screen is really small. Now, the next thing I want to do is I want to set a class name over here, set the width to be five, the height to be five in general, but also when you're a small screen, uh it will become a width of six and uh height of six.

**20:53** · Perfect.

**20:54** · Now, on this button, I want to make it such that it is hidden unless uh we are in a small screen. The way we do that is from a medium screen and above, we're going to set the display to hidden.

**21:11** · Now, you see that this doesn't impact us at all, but if I were to open this up more, you'll see that it will disappear because right now we are currently in a small screen.

**21:22** · And what that also means is that now we can come up here into our nav links and do that thing that I mentioned to you guys where if we are in a small screen, we want to set the display to hidden so that we only have this button. But now, how do I get that back when I am in a bigger screen? What you do is in a bigger screen, you set the display to flex because you can't have a display of hidden and a display of flex.

**21:46** · We only want to set the display of flex in a medium screen and bigger because then when we get to a smaller screen, when the screen's not medium anymore, it will then become this beautiful hamburger menu. Now, in this button, I also want to center the items.

**22:05** · And now, on this button, I also want to set a padding of two. I want to set the color of it to be gray 300 so it matches the color of the navbar and I'll do the same thing here, however, text white.

**22:19** · Perfect. Now, I want to be able to click on this button and open a completely separate navbar menu that is only for mobile. How do we do that? Well, the way we do this is by keeping track of the state of whether or not a mobile menu is opened or not. And to do that, we can use the use state hook from React. So, I'm going to create a state, set it equal to use state and import that from React.

**22:45** · And a state will allow us to keep track of this boolean which we're going to call uh mobile menu is open. That's a uh a boolean true or false. And we're going to have a function that we're going to use to change the value of that boolean. We're going to call it set mobile menu is open.

**23:07** · Then, initially, this boolean will be false. But when you click on this button, I want to set the boolean to toggle. Now, what does that mean? It means that if I click on this button and the mobile menu is open, then I want to set it to false. But if it's false, I want to set it to true. So, this is how it's going to look.

**23:31** · We're going to click on this button and we're going to alter the value of the previous value of the state to be the opposite of what it was.

**23:43** · So, you'll see that if, for example, I were to come over here and render something that depends on it, like the the word uh hello.

**23:54** · You'll see that now it doesn't show the word hello because mobile menu is false.

**23:58** · But when I click on this button, mobile menu will become true because true is the opposite of what it was before, which is false, and now we should see the word hello. And if I click on it again, that should disappear because now it becomes false.

**24:11** · Now, we don't want to show the word hello when this is true. We want to do a lot more. For example, I want to change what the icon is inside of this button depending on whether or not mobile menu is open. So, I'm going to wrap this icon or the label inside of this button with some curly braces. And then inside of here, I want to check to see if the mobile menu is open because if it is, we don't need to show a hamburger menu. We actually need to show something else. I want to show an X icon because it's kind of like you want to close the menu.

**24:40** · So, I'm going to use the X icon from Lucide React and you'll see that when I click on this, this now should become an X. Let me just remove this because it will make it look better, but you see you see it will become an X and as I click, it keeps switching.

**24:55** · Now, I'll also apply the same kind of class names we applied for the hamburger menu into the X so that it is uniform.

**25:02** · Perfect. Now, we also want to show the actual menu or the links appearing in a vertical manner when you open the mobile menu. So, I'm going to uncomment this over here or at least I'm just going to copy this and I'm going to go two divs down.

**25:18** · And we're going to create a whole separate menu that is just for when the mobile menu is open. So, what I want to do is I want to render here a div.

**25:29** · And this div will show another div which is going to contain the different links.

**25:35** · So, I'm going to copy all of the links we have over here.

**25:38** · I'm going to paste them inside of this div.

**25:41** · And you'll see that when I click on this, it should show the links, but they are not showing up the way that we want to. We want them to show up in the middle and also for them to be vertically stacked. So, to do that, I'll go to the first div and I'm going to set a class name where if you're in a medium screen and above, I want to maintain that hidden. Now, why do we want that?

**26:02** · Because imagine this scenario. I am on a small screen, I open up the mobile menu and I decide to open up my web browser and make it bigger. We don't want that menu to still appear because if this over here wasn't set, this is what was going to happen. We would have two menus. See? We'd have the one over here and this one over here. By making such that no matter what, this menu will never show on a medium screen and above, this will now work. So, what we want to do now is I want to set the structure or the styling for the mobile menu.

**26:35** · So, I'm going to set this to be a BG slate 900 and I'll make the opacity be 95 instead of 90. I'm also going to apply the backdrop blur and I'll make that be large. Then, I want to set a border to be top.

**26:56** · So, there's a clear distinction between the actual top navbar and this new mobile menu.

**27:02** · Then, what I want to do is I want to change that color of the border to be slate 800, which is a slightly different color to the color that we are already using.

**27:11** · Then, I want to actually animate whenever this navbar appears. So, if you look at this, when I open and close, you see it just appears out of nowhere, but I don't want it to be like that. I want it to animate in and also slide in from the top of this section. To do that, we're going to create a animation in our CSS file over here that is going to correspond to that. To do this, I am going to come inside of here and I'm going to create a utility class.

**27:37** · Now, if you're not familiar with Tailwind and obviously the different layers of Tailwind that you can create uh and what the utilities are, I recommend you checking out my 1-hour crash course on Tailwind CSS. I go over absolutely everything from the very beginning up until the and I highly recommend you checking that out as well.

**28:03** · Now, in this utility layer, what I want to do is I want to create some classes that I want to reuse multiple times in this project. Now, this one is going to be an animation class. So, I'm going to say animate in and in the animate in, I want to set an animation fill mode to be both. Now, that only makes sense if we do have an animation.

**28:27** · So, I want to also create here an a class name called slide in from top, which is going to represent the animation that this navbar should have. Perfect. Now, what we need to do is we need to create a uh oh, I just realized uh I made a misspelling here. So, I need to change this to animation.

**28:49** · Um what we need to do now is we need to apply a duration to this animation because if we were to come over here and we were to put those two classes here, right? The slide in from top and the animate in classes that we just created, what will happen is the animation is happening, but it's happening instantaneously, so there's no really any duration to this animation.

**29:15** · So, we want to create a duration class that can be reused whenever we want to have, for example, animations that last a certain length, like 300 milliseconds, which is what I usually like my animations to be. So, whenever we want to set an animation to 300 milliseconds, I'll create this class and make the animation duration be equal to 300 milliseconds.

**29:36** · So, that means that now if I were to pass the duration to be 300 here, which it means I'm just calling this class that we created, it should have a slight delay, which makes like it's fading in. But, we don't want it to just fade in. We also want it to kind of look like it's sliding in from the top. So, to do that, I'm going to also pass a transform that is going to translate in the Y direction from the start the item to be -1 rem from its original place.

**30:09** · And then when the animation is finished, it should be at its original position, which is just a translate Y of zero. So, you see now, if we try to animate this, it will look a bit like it's sliding in from the top.

**30:24** · Perfect. Now, what I want to do is again structure these elements so that they appear stacked against each other. So, I want to put some class names to this div. So, in this div, what I want to do is I want to set a class name to be a padding axle four, a padding Y of four.

**30:42** · Now, you might be wondering why are we not just using a PO four in here? And that's because that's only for the mobile screen. But, we also want to set here in a mobile screen to be a padding Y of six and nothing for the padding of the X direction. Now, between the items, I want to put a space in the Y direction to be three.

**31:02** · Now, in a small screen and above, I'm going to make that space be four.

**31:08** · Now, to make the items actually each link actually appear in a different line, we have to make it so that they are display block. So, for each of these, I'm just going to pass a block value here and each of them will appear now to be stacked on top of each other.

**31:25** · Perfect.

**31:27** · And now our navbar is almost complete.

**31:29** · The only thing I want to do left is I want to come up here to our nav and now we're pretty much done. The only thing left that I want to do is whenever I click any of these links, I will navigate to the place, but I also want to close the navbar in a mobile state so that it doesn't cover half of the screen. So, to do that, all I have to do is I just have to add an on click similar to what we added for this button so that we can manually force the navbar to close. But, instead of toggling it like we were doing with the button, we're literally just going to set it to false.

**32:00** · And we're going to do this for all of the links on the mobile menu so that for example, if I were here and I wanted to go to the pricing page, I go to the pricing page, but also the navbar closes.

**32:12** · Perfect. So, now we're pretty much done with the navbar. It looks good on mobile, it looks good on web, and it's time for us to start building the hero section. So, to start off with the hero section, I just want to turn this into a section element.

**32:28** · And I want to apply the groundwork for the class names that we're going to be using to structure this page. So, I'm going to set the hero section to have a position of relative. I'm also going to set the height of it to actually be the minimum height of the screen. The reason for that is because I want the hero section to be the first thing the person sees. They are not going to see any of the other sections, they have to scroll to be able to see them.

**32:49** · Then, I want to set a display flex and I want to center the items.

**32:54** · Now, I also want to justify everything from the hero section right in the center.

**33:01** · And I will put a padding on the top of the hero section to be 16 if you're in a small screen, but in a bigger screen, that padding will be even bigger. It'll be 20. I'm also going to set a padding the X direction in a small screen to be four and on every other screen to be 16.

**33:19** · With the exception of a large screen, which we're going to make that padding be eight.

**33:25** · I don't know why I made it 16, it should be six.

**33:28** · Now, we also just want to set an overflow to be hidden. Now, none of this is going to be clear yet because we don't have anything inside of the hero section, but the first thing we want to add to the hero section is actually going to be something super cool. It's going to be the effect that I had in the demo where as you hover through the elements, it's actually going to be the effect that I had in the demo, which you can see over here from the final product, where as I hover as I move my cursor through the page, it is going to show this little glow around it.

**33:59** · Now, to do something like this, what we need to do is we need to keep track of the user's mouse position. And to do that, we're going to create a state called mouse position, create a function called set mouse position.

**34:17** · Then, this state is going to be a an object that is a combination of an X and a Y value. Now, the X and the Y value represents the position of the cursor and by default is going to be zero.

**34:31** · Then, we're going to have a use effect that is going to have an event listener that is going to subscribe to. This event listener is going to be the user moving their mouse. And whenever the user moves the mouse, we're going to run this function called handle mouse move. It's going to take in an event and it is going to do something with it. Now, to do that, we need to again subscribe to the event listener of the user moving their mouse.

**35:00** · And to do that, you access the window, you add an event listener, you choose the event called mouse move, and you pass the handle mouse move function here. Now, if you want to I'll just show you we can console.log the X and Y values. How do you do that is you get the X value by getting the event and then you access the client X and the Y value through the event client Y.

**35:30** · You see that if I do that, which by the way, let me just clean this use effect up. If you're not familiar with use effects, it is important if you are subscribing to an event listener like this for you to return a function in this use effect that will remove that event listener.

**35:47** · Because what happens is if you don't do that, then the component might unmount without actually removing the event listener, causing memory leaks. So, you have to do this whenever you're subscribing to an event.

**35:59** · Now, now that we've done that, I also want to put here an empty dependency array so that we don't run this use effect infinitely. And I want to open up here the console log so you guys see that it works. So, if I open up the console log, you see as I move my mouse, it will show the different X and Y values of my mouse based on that.

**36:21** · Perfect. Now, we don't want to just console log those values. We want to show a glow around the mouse. So, to do that, inside of this section, I want to create this div that is going to be a self-closing div and it's going to have a class name of absolute an inset of zero and an opacity of 30. Now, most of the styling for this, we're not going to be using Tailwind just because it's a lot easier for us to manually do it with just normal CSS through the style.

**36:47** · So, inside of here, I'm going to add a background value so that we can build that little glow coming out of the mouse.

**36:58** · And inside of here, we're going to create the glow by using a radial gradient, which it will make a gradient out of a circle. To make a gradient a radial gradient, we have to first set its size. I'm going to make it 600 pixel, but you can make it bigger or smaller if you want. You choose the the shape, which I'm going to choose to be a circle, and you need to put the position of it. So, the way you put the position is kind of interesting in CSS. You put at and then you put the X position as a pixel. We get that X position because we have it over here.

**37:31** · So, what we can do is we can use this state to keep track of that position.

**37:36** · We'll use the set mouse position function and we're going to set an object inside of here where the X value is equal to the client X and the Y value is equal to the client Y.

**37:49** · Now, we can use that mouse position.x in here and get the X position as a pixel for the mouse. We'll do the exact same thing in the Y position for the mouse and we should be able to get that glow.

**38:06** · Now, we're not seeing anything because we are not done yet. We have to set a color to this glow. Now, I'm going to set the following color, which is an RGBA of a similar color to what we have in the background. It's going to be the following values: 59, 130, 246, and 0.15 cuz I don't want to make it too visible.

**38:27** · Now, after this, I want to set this to be transparent and set 40% so that we get this cool effect at the top left. Now, why is it at the top left? Because initially, the mouse is set to 0 0. So, you see that as I move my mouse, this should move along with me.

**38:48** · Perfect. It's a really cool effect and it's really nice whenever you can add this this won't go through the entire website because we're only adding this to the hero section. However, because I also think it would look kind of weird and goofy if you add it to the entire website, but for the hero section, it's a really good eye catcher. Now, on top of that, I want to add two different glows that are going to be stuck permanently on the page and they're going to be pulsating as well. Now, why do I want to do that?

**39:14** · Well, because even though we have this little mouse that is moving, sometimes if you're if the mouse is down here, I still want to have those two glows at the tops so that it gives a nice aesthetic to this page. So, to do that, I already have the two glows over here and I'll just go over what they are. So, you can put them wherever you want. I put them on the top left and on the bottom right so that they have a good distance between them. It's a similar glow to what we have on our mouse, but it is stuck and it's pulsating. So, how we do this?

**39:42** · Well, we set an absolute positioning and this is where you can choose where you want. I put it on the top left by making the top be 20 and the left four. So, it's on the top left and then the bottom right by using the bottom and the right. I change the positioning based on the size of the screen and I choose the color to be blue and cyan. So, they're different kind of a different color. This one is lighter and this one is a bit darker. To make them animate, you can just call the built-in Tailwind CSS animation called animate pulse.

**40:09** · So, Tailwind has some animations that are built in. We just had to create one of them for the navbar, but some of them can be reused like this one. And now we have those two glows around our page.

**40:24** · Now, what we want to do is I want to start building the skeleton for the actual content. So, I'll build this div and put another div inside of it.

**40:34** · Then, I'm going to put another div. And if you remember, the hero section has two parts to it. It is going to have the text that is at least in mobile it's going to be appearing on top of this other section, which is the code, but on web this will appear on the left and this on the right. Now, the code we're going to have to do it all manually. So, we're going to be using a lot of CSS for this and a lot of React states for this as well.

**40:59** · Now, for this part we can do it by just putting the content directly in here.

**41:04** · Now, we'll start by building the code part of this, this part over here.

**41:09** · And to do it, what I want to do is I'll come here and I'll create this section.

**41:14** · I'm going to call it the IDE header.

**41:16** · It's just the header section for the code editor that we have here.

**41:20** · And I'm going to add another div. Now, on this div I want to set a class name of display flex, items center, justify between.

**41:32** · And the reason for that is because this is the header. This is this part over here. And I want to have a part on the left, which is those this three dots with the title of the page and then this section over here.

**41:44** · Now, I'm going to say justify between and I want to put a padding X of three on a small screen and above I'm going to make a padding X of four.

**41:55** · Then, I'm going to set the padding Y to be two and the padding Y to be three on a bigger screen. The BG will be white, but with only five of opacity, so you can kind of start seeing it right in the center.

**42:08** · And I'm also going to set a backdrop blur to be small, a border at the bottom cuz it's a header.

**42:16** · And that border will be white, but with only 10 of opacity, so it matches a bit more like that.

**42:22** · Then, what I want to do is I want to actually build the class name for the part around the IDE header. This part I'm going to set a BG gradient to bottom right because I want to make this glassy look around the IDE.

**42:38** · And what I do here is I'm going to make the background gradient to be from the color gray 900 divided by 20, so 20 opacity, to gray 800 20.

**42:54** · And I'm also going to set a backdrop blur small and I'm going to make it rounded large.

**43:01** · Now, I also want to set the overflow to be hidden.

**43:07** · And I want to set a manual height and width for this section. Why am I doing that? Because this is a piece of code and it will look ugly. Like I had to manually make this UI, so it will look ugly if we were to allow this to expand and grow as the page grows. I want it to always be this size. So, to do that I'll set a height with a specific size in mind. I'm going to use pixels. I'm going to make it 280 pixels and you'll see that this thing should grow now. And the width should be a fixed size of 350 pixels.

**43:40** · Now, I want to do that only if this is a small screen and above.

**43:49** · And you'll see why in a second. Now, in a large screen and above, since it's going to be very large, I actually want to change the height just a bit more.

**43:56** · So, I'm going to make it be 450 pixels.

**43:59** · This won't impact what we are seeing right now cuz this isn't a large screen, but it will be good. I'm also going to set a border around it and I'm setting a border color to be white 5%, so that it looks similar to what we have in the header.

**44:13** · Now, how do we apply this to have a bigger size in a mobile? Well, in here at this div, we're going to set the position to be relative. I'm also setting the same BG white to be five.

**44:27** · And I'm also setting a backdrop blur, but this time we're setting it to be excel.

**44:33** · Now, what I want to do is I want to set this to be very rounded.

**44:38** · And I also want to in a smaller screen to make this even more rounded cuz there's still a bit that I'm seeing over here.

**44:46** · Then, I want to set a padding of three, but on a small screen and above I'll make that four.

**44:52** · I'll set a shadow around it to be two excel and I'm setting the border to be border white 10.

**45:02** · So, we're building the outer layer, which you could see over here, right? We have this outer layer, we have the inner layer and the header. That's the three things we've made so far. But on top of all of that, we have this div, which we have to set a position relative, the order to be two and most importantly, the width to be full.

**45:25** · Now, we get this beautiful code editor appearing on our screen.

**45:30** · Now, it doesn't fully look like a code editor yet, but it will in a second. The first thing to make this look like a code editor is add the little close, minimize and open buttons. To do that, it's actually easier than you might imagine because if you think about it, it's just three circles with different colors. So, that's literally what we have to do. Inside of here, I want to add a div that is going to encompass the three little dots and each dot will look like this. We're just going to create the dot, make it be a circle, so it will have the same width and height. I'm going to make it two.

**46:03** · And it will be rounded full and it will have a color, which will be red 500 at least for the close one. Now, I also want to change the size if it's a bigger screen. So, in a bigger screen the width will be three and a bigger screen the height will be three.

**46:20** · Now, I'm also going to copy this and paste it two more times.

**46:25** · And the reason for that is because this one is going to be yellow and this one is going to be green.

**46:33** · Now, they're stacked on top of each other. To put them next to each other, we have to have this be a display flex.

**46:39** · And we also want to put a gap in between them cuz they're all closed up together.

**46:43** · Since this is display gap where this is just one row, then I want to set the space X to be two and I also want to center the items.

**46:56** · Perfect. Now, I do think this gap is a bit bigger. I think we want to do this only in bigger screens. In smaller screens, let's make this be one. Yeah, this will look better. Perfect. Now, I want to put a span with the name of the website. So, codeflow.ai. That's the title of the website. I don't want it to appear here.

**47:18** · It's appearing here because of the justify between from this. So, I want to wrap this section and the new span that I created with this div and it should appear here. Now, this div, to be honest, we'll keep it exactly the same, but I'm just going to remove this space X one cuz I think space X of two makes sense between this section and this one. Now, in the title here, I want to make it definitely a lot smaller. So, I'm going to say text extra small.

**47:46** · On a small screen and above we'll make it be just small. The color will be gray 300, so it blends in. Now, what we want to do is just add this last section over here. I'm not going to make it exactly the same. I don't think I'm going to add this AI thing over here because looking back now, I think it looks a bit goofy, but the thing is is I'm going to add this section over here just for UI purposes. To do that, it's pretty simple. Below this div over here, whatever we put is already going to appear on the like top right.

**48:14** · So, all we have to do is just add this chevron down icon, which is an icon from Lucid, which is just an arrow an arrow pointing down. Now, I'm going to make this have a class name of width three and height of three, so it's a lot smaller.

**48:31** · And I also want to make it such that in a small screen and above we'll make it a little bit bigger, so it looks better.

**48:39** · And we'll make the height as well. I'm also making the color be gray 400, so it's not very white.

**48:45** · Perfect. Now, we want to make the code inside of it. And more importantly, we want to make it such that you can move through the different tabs so that you can see the code changing. How do we do that? Well, to do that, we need to create a variable that is going to keep track of the different pieces of code, whatever is written in here for whatever tab we are in. So, we have three tabs and I I just made whatever the names are, but you can change it as you want. But we have three tabs in this code editor.

**49:14** · We have the app.jsx, we have the hero.jsx and the navbar.jsx.

**49:20** · Now, each of them has a code associated with it. That looks even better if you are looking in web. Now, how do we make that? Well, we'll create a variable.

**49:30** · I'll create here a folder called data and in here I'll create a file and I'll call this code samp- example .js.

**49:43** · It's going to be a JavaScript file cuz we're not going to return a component in here. And what I want to do is I want to export const a uh an object called code examples.

**49:57** · Now, this object will take in a key and a value, like every other object, right?

**50:02** · But the key I'm going to actually make it kind of look like JSON. The key is going to be the name that we show up over here. So, the name of the file, like app.jsx.

**50:12** · And the value is going to be actual code that you put here.

**50:16** · Now, to write the code, we need to take into account, for example, spaces like positioning of everything. So, to do that, I'm going to use backticks and directly write the code inside of here.

**50:27** · I already have the code written for this. It is uh this code over here. Now, don't worry about positioning or anything like that because we're going to be using a library that is going to format all of that to make it look good for us.

**50:39** · Now, you can copy the code that I have.

**50:41** · It's going to be in the description. Uh none of this makes any sense. It's just for uh like demonstration purposes, but you should make it applicable to your own website.

**50:51** · Now, we're going to copy this and paste it two more times.

**50:55** · And we're going to make one for the hero .jsx and we're also making one for the navbar.jsx.

**51:04** · Now, like I said, I already have the code written for them. So, I'm just going to copy and paste from the uh code that I already wrote, but you can play around with the values and write whatever code you want.

**51:16** · So, I'll be back in a second when I finish pasting it. Perfect. Now, we have this value and we can access it inside of here. But before we even use that, I want to set up the UI for the header, so the different tabs over here, and the code. So, to do that, I'm going to create a div over here with another div. The first section is the uh file tabs.

**51:41** · And I'm going to create a button for each of the tabs.

**51:46** · Now, it should appear down here and this button should have the label of app.jsx.

**51:53** · Now, we're going to have three of them.

**51:55** · So, app.jsx, then we're going to have one for the hero and one for the navbar.

**52:00** · Hero and navbar.

**52:03** · Perfect. Now, this definitely shouldn't be appearing here. This should appear inside of this. So, we made a mistake.

**52:09** · We need to put this right over here so that it's This is the outer div.

**52:14** · Perfect.

**52:16** · And we want to make it such that we style this to look like the actual tabs here. So, for each of these buttons, I'm going to add a class name and it's going to be a padding x of three, a padding y of two.

**52:31** · Then we're setting a backdrop blur to be small.

**52:36** · The text will be extra small.

**52:40** · And we're going to on a bigger screen make that be small. We're also going to round it at the top as large, not at the bottom because you'll look how it's only rounded at the top.

**52:53** · And finally, to make it look like a tab, we're going to add a border around it.

**52:59** · We're also going to add a BG of white five.

**53:05** · And the text will be gray 300.

**53:09** · Now, I also want to set a transition to be all a duration to be 200. Now, we don't have this duration to be 200. We'll create it down here from similar to what we did with the duration here. We want to have a simple animation for this as well, but we're going to be using 200 because it will make the animation faster. And we change this to 200 milliseconds. Now, I also want to add a class name called white space no wrap.

**53:39** · And we should be good with this. I'm going to copy this and I'm going to paste on all of the buttons.

**53:49** · Perfect. Now, obviously, there should be some spacing between them. So, in this top div over here, I'm setting a flex and a space x of one, so there's a little gap between them.

**53:59** · On a bigger screen, I'm also setting that to be two.

**54:03** · I'm setting a margin bottom to be three and on a bigger screen, that will be four.

**54:11** · And I'm going to set the overflow on the x to be auto.

**54:16** · Then on the top here, we're going to give some space. I'm going to add a padding of three and on a bigger screen, that will be four.

**54:26** · Position will be relative and the height will be full.

**54:29** · Now, this doesn't really look like this, right? I know. Just wait a second because what we need to do is we need to find a way to keep track of which tab we're in cuz if you notice the UI clearly changes based on which one we're in. So, to do that, we're going to create a state up here that is going to keep track of the active tab.

**54:51** · We're going to also call this set active tab.

**54:54** · And this state will be a string that will just be the key of whatever values we have here. So, you know, we have app.jsx as one of them, hero.jsx as the other, and navbar.jsx as the other.

**55:08** · By default, it should start as app.jsx.

**55:11** · Then, what I do is if the class name, if this is the active tab for each of the buttons, I want to change a bit the styling in it. Now, how do I do that? Well, I'm going to change the quotation marks on this from just normal quotation marks to be backticks because this is going to be dynamic, meaning we're going to insert JavaScript inside of here to change the UI based on some sort of behavior, which in this case is if this is the active tab.

**55:43** · Now, if this is the active tab, what I want to do is I want to change the background color, this part over here.

**55:50** · So, I'm going to insert here a value.

**55:53** · So, I'm going to insert this variable over here.

**55:56** · And the variable is going to be if the active tab is equal to this button. Now, this button is for the app.jsx. So, we know this is the active tab if the active tab is equal to app.jsx.

**56:09** · And if that's true, I want to do something like apply some style, and if not, I want to apply some other style.

**56:16** · Now, if it's not the active tab, I want to make it be BG white uh the same way we did over here. I also want to apply the text to be gray.

**56:26** · And I want to have the border to be white divided by 10. And when you hover it to show that you can click on it, I want to make it be BG white 10 instead of BG white five. Now, if it is the active tab, then I actually want to make it be blue. I'll make it blue 500 and give it 30 opacity. The text won't be gray. It's going to be white and the border is also going to be blue, but it's going to be 400 at a 20% opacity.

**56:58** · What this will look now is you'll see that because app.jsx is the selected one, it has a completely different style than the other ones. And I'll apply this exact same styling functionality to all of the different buttons. So, we'll apply it here and we'll apply it over here.

**57:18** · Now, there is Oh, I need to put a class name here.

**57:22** · And delete this. Perfect. Now, there is clearly an issue because all of them became blue, but the issue is not with anything we did. It's just that when we copy this code, you need to change the values of the active tab here. So, in this case, it's for the hero. So, we change this to be hero, and on this case, we change it to be navbar.

**57:43** · Now, it looks a lot better, but I want to be able to switch between the different tabs. So, to do that, for each of these buttons, we're going to add an on click that when you click on it, we're going to set the active tab to be whatever this is.

**57:56** · So, in this case, it will be the app.

**57:59** · app.jsx.

**58:01** · And on the other ones, such as this one over here it's going to be the hero.

**58:06** · And on this one, it's going to be the navbar.

**58:11** · So, you see now, I can switch between the different tabs by just clicking on them.

**58:16** · Now, this should also change the code that is displayed below, but we haven't gotten there yet. So, I feel like now it's a good time for us to do that. If you go below this file tabs over here, we are going to create the section for the code content.

**58:32** · Now, to do that, like I said, we need to install a library that's going to help us format code into actual code like our actual text that looks like code. The name of this library is React Syntax Highlighter. I've used this library so many times in the past and I think it's awesome for this kind of stuff.

**58:51** · We're just going to install React Syntax Highlighter.

**58:55** · And uh it's very easy. What we do is inside of this code content section, we're going to add a div that is going to encompass the section.

**59:04** · All I'm doing to this div is just setting it to be have a position relative and overflow hidden and I want to grow the flex.

**59:14** · Then on this div I'm going to call the syntax highlighter component from React Syntax Highlighter.

**59:22** · Now, this component is a wrapper component, meaning you have to put something inside of it. Now, what do we want to put inside of it? Well, we want to put the code uh snippets that we put on this object. So, we're going to import that object over here, code examples. We can just import it like that, but we only want to show some specific ones. We want to show them depending on what the active tab is. And we know what the active tab is, so we can access it by just putting active tab inside of here.

**59:52** · And you'll see now that it as you refresh this, everything will be broken.

**59:57** · And the reason for that is because we still have a lot more to do inside of this syntax highlighter component. The first thing is we have to specify a language because it needs to know what language it is in order to properly format. Since we're using JavaScript, I'll put JavaScript in here. Now, I realize that it's causing an error and the error is actually because we are installing the version 16+ of React Syntax Highlighter. I don't recommend installing that one because it's not compatible with the latest version. I recommend you to instead install this version over here, 15.6.6.

**1:00:30** · There's not a big deal to have a low not the latest version. This is just a React Syntax Highlighter library. It's totally fine. Now, to to get that to to that version, we actually need to uninstall React Syntax Highlighter. And after uninstalling it, I want you guys to install the version 15.6.6. There's two ways of doing this. You can do it through the command or you can just paste the version like this on the package.json, then running npm install, and it should have that version now.

**1:01:00** · Now, let me rerun our development server, so npm run dev. And if I refresh this, we should be able to see code. Perfect. We are being able to see code. Not only that, but we are able to move through the different code and the code will appear perfectly formatted.

**1:01:20** · Now, it it's obviously really ugly.

**1:01:23** · So, we do want to change that. Now, to make this look not ugly, we're going to apply a style.

**1:01:29** · Now, there's a bunch of different styles you can choose. I'm going to use a different one from the one I have here.

**1:01:34** · The one I have here is from Visual Studio Code. I'm going to be using the Night Owl style. Now, what this is going to do is it's going to make the code look exactly like this. It's like choosing a VS Code theme for the code in your website. Now, I also want to apply some custom styles and that's because I don't like how it looks right now where it's like kind of the edges are not rounded. So, what we're going to do is first we're going to set a margin to be zero.

**1:02:03** · We don't want any margin on it. We also want to set the border radius to be equal to 8 pixels.

**1:02:10** · Then, I want to set the font size \[snorts\] inside of it.

**1:02:15** · So, font size to be equal to 11 pixels cuz I do think it's a bit too big right now.

**1:02:22** · Then, I want to set the line height to be equal to 1.4.

**1:02:27** · I also want to set the height to be 100%.

**1:02:32** · And that has to be a string as well.

**1:02:35** · So, I'll just wrap this around. And then what I'm going to do is I'm going to set a border.

**1:02:39** · This border is going to be of 1 pixel solid, and I'm setting the following color, 3C3C3C, so that it has this little aesthetic to it. Perfect. Now, I can move around the different pieces of code, and you can see that it shows the different, uh, options appearing in our screen. Great.

**1:03:00** · And it looks even better when you are, uh, opened up like this. Obviously, we have to fix the this because, uh, it shouldn't be filling up this whole screen, but it won't because there's going to be a whole different column here on the left. Now, this is pretty much it for the code content. What we want to do now is actually show the different floating cards. So, floating cards.

**1:03:23** · This is actually hidden on mobile, so we'll have to open up our screen a bit, but if I were to open this up, you'll see that we have this, uh, cards that appear down here that change depending on which, uh, version of this you are. Now, to have a floating card associated with each, uh, uh, tab, we want to do something similar to what we did here for the code examples.

**1:03:47** · So, we're going to create a variable here, probably in the same file. We're going to export const, call it floating cards.

**1:03:56** · And I want to make a key, which is the tab name, so app.jsx, and I'll make an object inside of here with everything that we need to specify for the floating card. Now, here you're supposed to like just describe a couple features that your website has.

**1:04:14** · So, you just put whatever you want. I'm just putting like slop in here. Like this isn't really anything, um, that makes any sense, but you can put whatever you want in yours. And there is a couple things that we need to keep track of because they change on each of them. First is obviously the title, so this part over here. Then is the icon that we have here, right? We have a different icon. Then the description, and then the color of everything.

**1:04:40** · So, in this object, for each of the different tabs, we need to set a BG color, which at least for the first one is going to be BG blue 500 with 20% opacity. Then an icon color, which is going to be text blue 400.

**1:05:03** · Then we need to put a text color.

**1:05:06** · I'm going to set that to be text blue 200.

**1:05:10** · A content color, which is the content that we're highlighting right now, like the actual content inside of it, and that should be text blue 300. You can change the colors to whatever you want.

**1:05:22** · I this is just what I chose. And then we actually get the the data, right? The content. So, the icon, uh, for this first one, since we're talking about AI, I just put AI. It's not an actual emoji, but that's fine.

**1:05:33** · The second one is the title.

**1:05:35** · Uh, I'll put something like this, smart completion.

**1:05:39** · And then the third one is the content.

**1:05:41** · I'm going to put something generic like AI powered code suggestions in real time.

**1:05:53** · Now, we do this for all of the other tabs. So, one for the hero and one for the navbar. I obviously already did this, so I'll just paste the ones that I already did, and it should look a bit like this. You change the color and the content for each of them, and in the end you should have a specific value for each specific type.

**1:06:11** · Now, I want to go back to our hero.jsx.

**1:06:14** · I'll close that up. And for the floating cards, I want to add a div that is going to be actually a div that has a class name that is dynamic. So, we'll do the same thing we did before where we put backticks.

**1:06:28** · First, I want to make sure that it doesn't appear in mobile. So, I'm going to make it hidden. Uh, I only show it in a large screen, and in our large screen the display is going to be block so that it shows. Then I'm going to make it absolute.

**1:06:41** · I'll open the actual content here so we can see. It'll be absolute. Then it's going to have a bottom four and a right four, so it's in the bottom right.

**1:06:53** · I'm also going to set this to transform, and I'm going to translate it on the X direction eight.

**1:07:00** · Now, we can't really see anything right now, but you'll be able to see it when we actually add the color of it. I'm also translating on the right direction to be eight.

**1:07:09** · And what I want to do is I want to put a specific width to it. I'm setting the width to be 72.

**1:07:17** · Now, the thing that changes is the color of it. So, I'm going to add here a variable, and I'm going to access the BG color of this card by getting the floating cards object that we just created, accessing the value through the current active tab, and getting the BG color.

**1:07:39** · So, so we currently can't see it, but when we do, it's going to have the accurate color. Then inside of here, I'm going to put a div with a class name of flex and an items center with a space in the X direction of two and a margin bottom of two. You can start seeing it appearing now since we have some content.

**1:08:00** · Then inside of this, I'll put the first div with the icon. So, in here I'll put the floating cards and get the active tab and just say {dot} icon.

**1:08:13** · And we'll get the icon. Then below this, I'm going to get a span, which by the way, it's one thing that we can make be easier is instead of always accessing the floating cards.activeTab, we can just make a variable up here called current uh, floating card, I don't know. And then set it equal to this.

**1:08:40** · Then I can get this and just reuse it how many times I want without having to always access the active tab. I'll do the same thing here as well.

**1:08:49** · Now, if I go here, I want to add the span, and I want to add the current floating card and access the title.

**1:08:58** · Then I'll do the same thing with Then I'm going to, uh, get below this div that we just created, and I'm going to create another div, which inside of it is just going to include the content.

**1:09:11** · So, I'm going to say current floating card {dot} content. Now, we just have to style that. So, on this div over here, I'm going to set a class name where for the icon, I'm going to say it is going to have a width of six and a height of six.

**1:09:29** · Then, I need to get the color, so that's why I made it dynamic. So, in here, I'm going to get the current floating card {dot} icon color.

**1:09:38** · Then, in here, I'm going to set a display flex, items center, justify center, text to be small, font to be bold. Then, on the span, I'll set a class name where the text is small, the font is medium, and we need to change the color, which means we have to make this dynamic as well. And I'll just wrap this entire thing with backticks. And in here, I'm going to insert the current floating card {dot} text color.

**1:10:09** · Now, what we do after this is I'm going to copy this class name, I'm going to apply it over here. But, we want to actually don't use the text color, we want to use the content color, cuz that's different. And we also don't want to make the content be font medium.

**1:10:29** · And we want to align the contact the the content to the left, just like this.

**1:10:35** · Perfect. Now, we see the card appearing over here, and it changes as we move.

**1:10:40** · Now, it is ugly, right? We still have to edit it to make it look cool like this, but that's pretty simple, because it's just a bunch of stuff that we have to put in addition to what we already put over here. So, what I want to do is I want to add a back drop blur Excel.

**1:11:00** · I'm going to make it rounded large, so it has some border uh radius. Then, I want to make it such that the padding on it is four, so there's some space.

**1:11:10** · I'm going to set a border to it, and that border is going to be colored white with 20% opacity.

**1:11:17** · Then, I'm setting a shadow to be large, so 2 XL. And that should be enough. So, we'll be able to move through the different items, and you should be able to see this moving as well, and it looks pretty good. Now, the next thing we want to do is we want to be able to put this on the right over here, right? Cuz this isn't how it's supposed to be, and have all this text over here. So, I wanted to build the code first just because I know a lot of you guys came for the video for that, but what we're going to do now is build the left side of this page, and it will look a thousand times better.

**1:11:49** · Okay, everyone. Now, it's time for us to add the section that is going to go on the left on web and on top on mobile. So, to do that, I'm going to come back here to our hero.jsx.

**1:12:03** · Going to go up to right below this two glows that we put over here. And I actually want to wrap this entire section with two new divs. This will help us with organization. I'm going to bring the end of this divs to below everything else that we have. You'll see that now that section will stay smaller and not expand, and we'll go up here, and for each of this div, we want to define the following structure.

**1:12:31** · First of all, I want to set a max width for the whole page, and I'm going to set it to be 7 XL, then a margin X of auto, a text center, position will be relative, and the width will be full.

**1:12:50** · Then, inside of this div, I want to set a max width to be also 7 XL.

**1:12:56** · Then, the margin will be auto as well, and I'm going to set a display flex.

**1:13:01** · We're going to make that into a column, but that depends, because if we are in a small screen, we want to make it into a column so that we put uh the text above, and then we have this column over here. But, if not, then we want to make it into a grid with two different separate columns. You'll see what I mean by this. If I were to add here, for example, a P tag that says this, and we are in mobile, this will appear on top of this. But, if I were to open this up, uh we want to change it such that this now appears here.

**1:13:27** · To do that, we come to this second div that we have over here, and we make it such that in a large screen, the display is not even going to be flex, it's going to be grid.

**1:13:40** · And also, in a large screen, we're going to make it such that it is grid calls two, so there's two columns.

**1:13:48** · So, now this appears on the left and this on the right, when previously, when you go to mobile, it becomes a single column. Perfect. Now, I also want to put a gap of six no matter which kind we are. So, if we're in a a single column, this should have a space.

**1:14:04** · And then, I want to change this such that if it is a small screen and above, we're going to have a gap of eight, and in a large screen and above, that gap will be 12. I'm also going to center the items and set the position to be relative.

**1:14:23** · Now, instead of this, we don't want to put this random text. We want to put a whole section full of information. We want to put a like a tagline for the the website, this little thing at the top, and then a description together with two actionable buttons. So, first, we'll build the section above, that first little tag that we have. To do that, I'll add two divs, and I'm going to add an icon called sparkle or sparkles, this one over here.

**1:14:51** · It's an icon from uh Lucide React, which builds this little thing over here.

**1:14:58** · Then, below this, I want to add a span that will have the name of the website.

**1:15:03** · So, I'm going to say introducing Code Flow AI.

**1:15:10** · Just like that. Now, we have a lot of work to make this look good. The first thing is building the pill. So, what I want to do is I want to make it such that this has in a class name of inline flex, so they're next to each other. Then, I'm going to just center the items. I'm going to put a gap of two in between them.

**1:15:32** · Then, I'm setting a padding of X of three in a small screen, but a padding of X of four in a bigger screen. And then, we can apply the actual coloring and all the style to the pill. So, what I can do is I can put a padding of Y of two and put a BG blue of 500. Now, that's way too blue, so we're only getting a 10% opacity in that, so it actually looks like a transparent pill.

**1:15:57** · I'm also setting a border and a color to be border blue 500, but just slightly more less opaque, so 20.

**1:16:09** · Then, I want to set this to have full rounded corners.

**1:16:14** · I also want to make it such that this will have a space from the bottom, so margin bottom of four. And in a small screen and above, we'll set that to be six. Then, I want to use the the animations that we have created so far, the animate in and the slide in from. But, in this case, we don't want to slide in from the top like we have for this. We want to slide in from the bottom. So, we kind of want to have an animation here called slide in from bottom.

**1:16:47** · Now, we don't have that yet, so we do have to create it. So, we're going to come over here, we're just going to copy the key frames that we have here.

**1:16:54** · I'm going to paste it here. I'm going to change it to say slide in from bottom instead of top, and the transformation is kind of going to be the opposite.

**1:17:02** · Instead of going from -1 to 0, it's going to go from 1 to 0. Then, I'm going to come up here, and I'm going to copy this, and I'm going to change this to say slide in from bottom, and pass this animation name into here. Now, we can go over here, and we can just use this animation, and you'll see that when I refresh this, now we should have the animation, but it's not really showing up because there isn't a delay to it, so there's no time set for this animation to work in. So, what I want to do is add a duration here.

**1:17:34** · But, I want it to not be very quick. I don't want it to be 300 seconds, because if you look at how it looks, it's pretty fast, right? I want it to actually be 700 milliseconds. But, we don't have that animation yet, so I'm going to come here, and I'm going to change this to have a class name called duration 700, and it will apply the 700 millisecond animation duration. You'll see that now it takes a little bit more, but it makes it look a lot better.

**1:18:00** · Perfect. Now, we just want to style the individual items inside of it. We're going to start with the sparkles. I'm going to set the width to four and the height of four. I also want to set the color to be blue 400.

**1:18:14** · Then, I want to set for the span the same thing. We're going to make it be extra small, so it's a lot smaller. We want to make it such that on a mobile screen and above, we need to make it a little bit bigger, and the color is also going to be blue, but it's going to be blue 300. Perfect. Now, the next thing we want to do is add the tagline that this page is going to have. So, we're going to come down one div here, and we want to add an H1 tag that is going to encompass the entire title section.

**1:18:39** · Now, this H1 tag is going to have three spans, because it will be the three different words that we have here. Now, why are they spans? Because we are going to have different styling for each of them. The first one is going to say code faster. The second one is going to say something like um build better, and the last one is just the name of the website. So, I'm going to say build better, and then on this one, we're going to say with Code Flow AI.

**1:19:12** · Something like that. Now, to style them to appear one on top of each other, we're going to come to this H1 over here. We're going to first set it to be set the size. So, I'm going to put 5 XL in mobile. I like to make it bigger in mobile so it's more visible. But on a small screen and above, we're going to set it to be 3 XL. On a medium screen, we're going to set it to be 4 XL.

**1:19:35** · And on a large screen, we're going to set it to be 5 XL. So, similar to what we have on mobile.

**1:19:42** · Then, I want to set it such that it is the font is semi-bold.

**1:19:49** · So, it looks like a title. I also want to put a gap from the bottom. So, margin bottom of four.

**1:19:55** · On a small screen and above, we'll set that to be six. I want to use the animate in uh class. I also want to use the slide in from bottom.

**1:20:08** · So, that it has that animation.

**1:20:10** · And I want to set the duration to be 700. Now, you'll see that this should show up at the same time as this, but we actually want it to look like it is there's a delay. You see that this shows up before this shows up. To do that, we have to apply an animation delay to this animation.

**1:20:28** · And we can do that by creating a class called a delay.

**1:20:33** · We'll create a delay class similar to what we have here for our durations. And we'll put a different delay depending on how much we want. For example, in this case, I want it to be a simple 100 ms delay so it goes fast it goes after this one which doesn't have a delay. So, I'm going to apply an animation delay in here of 100 ms. Later on, we'll create more delay classes so that we can have the different sections appearing one at each time. So, in here, I can just say delay 100.

**1:21:04** · And now, you'll see that this should appear before this because there is a slight delay in the second animation.

**1:21:11** · I also want to set a leading tight so there's a bit more space in between the lines.

**1:21:17** · And this should be good to go. Now, for each individual span, I want to do the following. I want to for the code faster one, you can see that it is kind of like a um there's kind of a gradient, but it's a very non clear gradient. This gradient is more clear. But this still has a gradient. You can add the gradient if you want to. I am going to edit to here. What we're going to do is we're going to create a gradient which is from the background.

**1:21:43** · And it goes to the right. So, it goes from the left to the right. Now, if you're not familiar to how to make text in Tailwind look like it it has a gradient, it's actually pretty interesting. You can't just apply the gradient to the text. You have to create a background with that gradient. So, you give here the color like from white via blue. So, I want it to be a little bit blue in in between.

**1:22:06** · And in the end, it's going to end up being cyan 100. Now, this looks weird because the background has the gradient, not the text. But then, what you can do is you can apply a BG clip text and it will clip the background onto the text.

**1:22:21** · And then, the text will now have that gradient. Like I said, it's very very like dim so you barely can see the gradient, but it is there.

**1:22:29** · Now, I also want to set the text to be trans- parent.

**1:22:34** · And then, I want to set the display to be block.

**1:22:37** · And a margin bottom of one, but on a small screen and above, we'll set that to two.

**1:22:43** · Great. So now, I want to copy this entire class name and apply it here.

**1:22:49** · I'll do the same thing here.

**1:22:52** · But we'll change the middle one to have a different gradient. The middle one is not going to go from white, it's going to go from blue cuz I want it to be very blue. So, blue 400. It's going to go via cyan 400.

**1:23:08** · And in the end, it's going to go back to blue 400. So, it has a slight gradient in between like this. Now, one thing I also like to do is I don't like the gradients to go from left to right when it's very clear. I like to make them from bottom from top to bottom. Uh I always do this on my websites. I don't know. I just feel like it looks better. So, we're going to change that to be to the bottom. Just like that, we have our H1 class set up. The next thing is adding a paragraph with a description of the website right here. So, I'm going to add a paragraph tag here.

**1:23:38** · And we can add a paragraph of whatever we want. Now, this looks fine already. If you just want to leave it like that, you can. But we do want to make it also animate a bit. And we want to apply some styles to it. Like for example, the size I want it to be medium. But on a bigger screen, I want it to be base. On a large screen, I want it to be large.

**1:23:59** · I also want the color to not be just white. I want it to be gray 400.

**1:24:04** · Also, I want to make the max width of this to be 2 XL.

**1:24:08** · And I want to set the margin X to be auto.

**1:24:12** · Then, I want to set that in a large screen, the margin X will be zero.

**1:24:17** · The margin bottom will be six. But in bigger screen, that will end up being eight.

**1:24:23** · Now, I want to use the animate in uh class name so we have the animation.

**1:24:30** · I also want to use the slide in from bottom.

**1:24:36** · And a duration of 700. But I want this to appear after this. So, first this appears and it slides in, then this has its animation and then this one. To do that, we're going to apply a delay. But because the delay of this is 100 and the delay of this is zero, this should be slightly more. So, we're going to create a delay 200 class.

**1:25:00** · Which is going to just be a delay class that applies an animation delay of 200 ms instead. Perfect. And you'll see now that it looks like each of them are appearing like in a sequential order. Now, I just want to add a final thing which is I want to change the the line height. So, I'm going to say the leading is relaxed.

**1:25:21** · Perfect. So, it's a little bit more spaced out. Now, for to finalize this section, I want to add the action buttons. So, I'm going to add a div here with a button which is going to have a span that says start coding free.

**1:25:37** · I don't know. Just like a a call to action. Now, I want to add an arrow here. So, I'm going to say arrow right.

**1:25:45** · And I want to import that from Oh, why did it not import? Let's say arrow right again.

**1:25:54** · And it should import that icon.

**1:25:56** · Perfect. Then, I want to create another button right below this that is going to be similar. But on this one, we actually want to add a little bit more specificities to it. So, I'm going to add a div here instead of a span.

**1:26:10** · And the text in here, it won't be a text. It's actually going to be the icon first. And it's going to be a play icon.

**1:26:17** · That didn't auto import. So, I'm just going to write it again. It's an icon from Lucid React.

**1:26:24** · And it should look a bit like this.

**1:26:25** · Then, after it, we shouldn't put a an icon. We're going to put a span that should say watch demo. So, it's like you want to have a demo on your website of how your website works, right? Now, this looks ugly so let's style it. We'll start with this. We're going to make it such that it's a display flex. And it's going to have a flex of column. Then, on a small screen and above, that's going to end up becoming row.

**1:26:51** · I'm also going to center the items and justify them.

**1:26:55** · In a large screen, we're going to justify all of that to the start.

**1:27:00** · Then, I want to make it such that there is a gap of three in between the items.

**1:27:05** · And the gap is bigger in larger screens.

**1:27:09** · A margin bottom of eight.

**1:27:11** · And then, a margin bottom of 12.

**1:27:13** · I want to use the animate in class just like before together with the slide in from bottom.

**1:27:23** · And the duration will be 700. But the delay will be slightly more. We're going to make the 300 ms class. So, we'll come over here.

**1:27:34** · And we'll create a delay 300. Then, we'll come back here. And there's more that we want to add to this. We want to come down here to the button. And we want to add a class name which is going to apply to a group.

**1:27:49** · So, we're going to say width is equal to full.

**1:27:52** · Then, I want to set it to have a width that is auto in a small screen and above. A padding X of six.

**1:27:58** · But on a small screen and above, that will become eight.

**1:28:01** · Same thing with the padding in the Y direction.

**1:28:04** · We're going to make that be three and then, we're going to make that be four.

**1:28:09** · Then, we're going to set a gradient color to the first button. It's going to be a gradient from the top to the bottom. And it's going to go from blue 600 and we'll just make it be two colors, not three colors in this gradient. It's going to go from blue 600 to blue 400.

**1:28:29** · Then, I want to make it such that the button is rounded large.

**1:28:33** · I'm going to set the font to be semi-bold.

**1:28:39** · And the text is going to be small uh and base on a bigger screen.

**1:28:45** · I'm setting a transition all a duration to be 300 just as the one above.

**1:28:53** · And when you hover it, I want to set the scale of this button to increase slightly by only 2%. So, you see when I hover it, it becomes slightly bigger. Uh a scale of 100 would just maintain it the same size, but 102 makes it slightly bigger.

**1:29:09** · Then, I'm setting the display to be flex. The items to be centered. And I'm justifying everything centered as well and putting a gap in between the different items of two. So, there's a little bit of space in here.

**1:29:22** · Perfect.

**1:29:23** · Now, inside of this, I want to set the class names for the not the span, but the arrow.

**1:29:30** · The arrow will have a width of four and a height of four.

**1:29:34** · But, on a mall screen, there's going to be five and five. Then, we're adding a group hover effect that is going to apply to this.

**1:29:43** · When you hover it, you're going to translate this in the X direction to one.

**1:29:49** · And we have to apply a transition, transform, and a duration of 300. And this is how it's going to look like. You see how when we hover the button, the button becomes bigger. But, the inner icon, when we hover it, also expands a bit to the right. That's what the translate X1 does.

**1:30:10** · Now, the next thing we want to do is go to this button. I'm going to copy the class names from this button and just paste it here. Not that we're going to have an exact replica, because we won't, but I want to just save time with not writing a bunch of stuff again.

**1:30:26** · The main difference here is the background, because we're not going to have a gradient on this one. We're actually going to have a BG that is white and it's only 5% opacity, just like that.

**1:30:39** · Then, a backdrop blur that is going to be small.

**1:30:45** · And we're adding a border around it.

**1:30:49** · And that border will be white, but with 10% opacity. Now, when you hover it, we don't want to scale it. We just want to change the color. So, I'm going to go to where we have the hover effect, which is over here. And when we hover it, I'm just going to set the BG to become slightly more opaque, so 10.

**1:31:08** · Perfect. Now, inside of this, we have this div, which is a bit different, and it's before the the text, which is different from above. And in this div, I just want to set a padding of two, a BG that is white 10.

**1:31:23** · I'm going to set this to be rounded full. And when we group hover it, the BG will become white 20.

**1:31:32** · So, this is how it's going to look like.

**1:31:34** · You see how there's an effect to it.

**1:31:37** · Perfect. I'm also adding a duration of 300 and a transition to the colors.

**1:31:44** · Perfect.

**1:31:47** · Now, we'll go to the icon, which is the play button over here. We're adding a class name, same thing as we did over here. I might even just copy this and paste it here. But, I don't like this icon without a fill to it. You see that the one we have over here has a white fill to it. And you can actually add a fill to an icon in in Tailwind by just using the fill and then giving it a color, like white. And I think it looks a lot better. Perfect. So, this is how it looks. It looks pretty good. There are still some things we need to do, but as of right now, this looks really good.

**1:32:21** · This is how it should look, and this is how it looks right now. Now, to fix that, what we want to do is we want to go to the overall section over here. And where we have the large grid calls two, the section over here, we also want to add a text to be center if this is mobile, and a text to be allowed aligned to the left if it's a large screen and above. This will make it such that the text will then become aligned to the left in this big screen.

**1:32:50** · Now, this is not actually the the one we're writing. This is the one we're writing, but it should look exactly how it looks over here. Also, the text is slightly smaller. So, we do need to apply a bigger height to this H1. So, you see how in here we have 5XL, small, medium, large, and so on. We actually want to apply one to XL. And in that case, we want to make it be 6XL, which is just slightly bigger, so it actually matches that. Now, we're almost there.

**1:33:19** · There's just some small differences. The main difference is obviously this part over here, where the code editor here isn't expanding to the full width. So, to do that, now that is actually because of a bug that we introduced. If you look over here, we are applying the responsiveness of the height, and for some reason, I put a width over here. So, you want to change that to be a height. You'll see that now it will look perfectly fine, just like how it does over here.

**1:33:47** · Perfect. So, we're pretty much done with this section. So, now it's time for us to start building the next section in this website. The next section is going to come below, and it's going to be the section for the features, where you're able to see the different features being displayed in an alternating order. Now, you can put whatever features you want here, but I like to use code as the example. But, in your website, you might want to put images instead of the code.

**1:34:15** · But, if you want to follow what I'm doing, then I'm going to show you how to do that. So, to do that, we're going to come to our features file over here. I'm going to close this off. And in the features, we want to start by defining what the features are going to be. So, I'm going to make an array over here called features, and we're going to use it. Now, this array is going to be an array of objects, and each feature is going to have a title.

**1:34:40** · For example, the first one, I'm going to say that you can code complete using this product. So, AI code completion.

**1:34:48** · Then, we're going to have a description.

**1:34:50** · I'm going to say something like this, like intelligent code suggestions powered by AI, or whatever you want to put. Now, below this, I want to put an image that is associated with this. Now, again, if you want to use real images, like a PNG, you put that image over here. But, in our case, we're going to be using code. And to do that, we're going to be using the same functionality that we've done over here. But, this time, we're going to not put the code directly here, but rather use a name for whatever code this is.

**1:35:20** · So, what I'm going to do is I'm going to give it a name. Let's call it code completion for this one. And we're going to create a code snippet associated with this code completion name.

**1:35:31** · Then, we're going to choose the image position, because they're going to alternate. And one's going to be left, one's going to be right. We can do it however you want, but in a big screen, you see that the first one is on the left, the second one is on the right, and then the third one is on the left as well. You can again change that however you want, or even maintain all of them in the same side, if you want to.

**1:35:51** · Now, to do that, I will create one feature one object like this for each feature. I will say I already created all my features, so I will just copy and paste the ones, but you want to fill in for all of those. Now, inside of this features component, I want to return a section. And this is the first section where we do want to put an ID. And the reason we do that is so we can navigate to the features section when we click on the navbar. So, you see that if I were to click over here and go to features, it should scroll me down a bit.

**1:36:19** · Now, since we don't have any content here, it just barely scrolled me down. But, it should take me to that section. Then, I want to add a class name here, where I'm putting a padding Y of 16.

**1:36:31** · I'm also putting a padding Y of 20. And a padding X of 10 in mobile, and a padding X of six in a small screen to medium. And then, a large screen and above, we'll set that to be eight. Also, a position relative.

**1:36:47** · Then, inside of this section, I want to add the first part, which is going to be a div that is going to encompass the entire section. Now, the first part inside of this div is going to be the title. So, we're making a div with an H2, which is going to include a span. And it will say something like this, your complete development. It's just a tag phrase for you to be able to display your features. Now, below this, we're adding a line break.

**1:37:18** · And then, we're adding another span that should have another type of catchphrase or or word that is associated to your product, like workflow.

**1:37:28** · Now, what I want to do is I want to style this up. I'll make this div center the items.

**1:37:34** · A margin bottom of 12, so there's a lot more space. Also, that should increase if it's a bigger screen, and even more if it's a very big screen.

**1:37:45** · So, here I'll put 20.

**1:37:47** · Now, I inside of this, on the H2, I want to set the class name to be text 5XL.

**1:37:54** · But, then on a small screen and above, we'll make that 4XL. Then, 5XL.

**1:38:02** · Then, on a large screen, we'll make that even bigger, 6XL.

**1:38:06** · Also, the font is going to be bold. The margin bottom will be four. And we'll set that to be six.

**1:38:13** · Perfect. Now, what I want to do is on this first span, we're going to add a BG gradient to it. It's going to be a BG gradient to the bottom. We're going to make it be from white to gray 300.

**1:38:32** · Then, we want to clip the text, like we did before, so the gradient applies to the text. And we'll make the text be transparent.

**1:38:42** · Perfect. Now, we'll do this for this one. And for the bottom one, we're actually going to just apply the a different color. We're going to make it blue instead. So, from blue 400 to cyan 400.

**1:38:58** · And it will look pretty nice.

**1:39:00** · Now, we do want to set a div class name for this overall section. It's going to be pretty simple. We're just setting the maximum width of this entire section to be 6XL, and the margin in the X direction to be always auto.

**1:39:14** · Now, we want to display the different uh code pieces together with a text associated with it. We already have all of that laid out over here, so it's going to be pretty simple. We're going to start by going below this div and adding a div that is going to encompass this section.

**1:39:31** · That we're going to space in the Y direction with 16 and put an even bigger gap in between the the different features in a larger screen.

**1:39:40** · So, in a very large screen, we're going to make that even 32.

**1:39:44** · Then, inside of this div, we want to loop through our features. So, I'm going to loop through the features, features.map, get each feature with their key.

**1:39:55** · And for each feature, I want to return a div.

**1:39:59** · Now, in this div, I want to a apply a key directly into it and a class name.

**1:40:08** · Now, for now, we're not going to touch this class name just because I want to put the content inside of it so you guys can at least see what the class names are doing to it. So, the first is going to be the image section.

**1:40:22** · Or the code section, actually. I'll just say that. I called it image just because I don't know if you guys would rather just make it into an image instead of code, but yeah. Now, inside of here, I want to have a div and I'll put another div to close it.

**1:40:38** · And in here, I'll put another div.

**1:40:41** · And I hate that I have to self-close all the divs inside of a map, but that's just part of developing.

**1:40:47** · Then, I want to start building the structure for this. It's similar to what we build in the above section with this code. We're going to start by adding a ID interface, and in here, we're going to add a div which will contain the header.

**1:41:03** · So, the first section is the header. I'm aware we're adding a bunch of divs, but it's going to make sense. So, in the first section, it's the header, we're going to add another div. And this one is going to have three divs inside of it, but this we've already done before, so I'm going to copy from the hero. It's just this section over here. We can actually just copy this. Actually, I'll just copy this over here, not the whole section. And we can paste it over here.

**1:41:31** · Now, you see, it will make three of those little dots that apply to the code editor header. Then, we do want to put a span in here with the feature title. So, I'll say feature.title.

**1:41:45** · And it should appear right below it.

**1:41:48** · Now, I want to make it such that it's a lot smaller, so I'm going to say text gray 400, a margin left of two, and I'll set that to be even more in a bigger screen and make it be XS, so it's a lot smaller, but then on a small screen, we're going to make it be small.

**1:42:06** · Perfect. Now, below this div, we're going to add another div, and this is for the code highlighting. So, I'm going to add here a section where I want to add the syntax highlighter. So, I can actually copy it from here. Just going to copy this component.

**1:42:26** · And I'm going to put it directly inside of here.

**1:42:29** · Now, the difference is that in here, we don't have the code examples uh active tab thing.

**1:42:35** · Uh what we do have though is actually, what I think I might just do is you just should just instead of putting image name, uh you should make this be the code. So, I'm going to say code snippet.

**1:42:49** · And I'm just going to insert the code snippet directly in here. So, for example, for the first one, it should be something like this.

**1:42:56** · And then I'll copy this and I'll put it here and here as well.

**1:43:02** · And then what we can do is instead of just getting it like this, we can just say that this is going to be the features object and get the current feature.

**1:43:13** · Actually, I can just say feature .code snippet. And then, we should be able to see the code snippet appearing.

**1:43:21** · Now, we do get an error, and I think it's because we didn't import this syntax highlighter component. So, I'll just do this. I'll just write it again, syntax highlighter, and it should import. Also, the night owl needs to be imported as well. Now, it should work, and you should see all three of them appearing.

**1:43:39** · Now, this works a lot better. I do want to change the code snippet for each of them. The first one is fine, but I want to add the correct ones for the other ones. So, I'm going to do that, and I'll be back in a second. Perfect. Now, I'll go down to the syntax highlighter, and there's a couple things that we do want to do. For example, I want to make it such that, for example, I do want to change the font size instead of making it 11 pixels, I want to make it such that it's 0.75 REM.

**1:44:06** · It's a little bit bigger. Then, I want to apply this another class name called wrap lines, and I want to set that to be true.

**1:44:14** · Now, what I want to do is I want to style everything else around it. So, I'll come up here to the first section where we have all of these divs, and we will start by editing this over here.

**1:44:26** · So, we want to make this have a display flex and center the items.

**1:44:32** · Then, I want to make it such that there's a gap in the X direction that is one. So, there's a gap in between this and this, so this appears next to it.

**1:44:41** · Then, I want to set it such that on a small screen and above, it will be X2 and on a margin bottom of three with a bigger margin if it's bigger.

**1:44:53** · Then, on this div over here, we want to make it such that it has that little background, so I'm setting a background gray of 950 that will be around all of this.

**1:45:05** · Then, we're going to set the this to be rounded large.

**1:45:09** · Also, we're setting the padding to be three and a padding to be four in a bigger one. I want to set the font to be mono so it looks like code, and then I'm setting the text to be extra small, but then in bigger screens, we'll just make that small.

**1:45:25** · Now, around this interface, here is where we add all of the styling. Since we already did something similar to this in the previous component, I'm just going to copy and paste the class names, and I'll go over what it does. So, first, we're just setting the position to relative, changing the colors, adding some back backdrop blur, and a bunch of border stuff as well. Now, the big part here is the hovering cuz when we hover it, we do want to have an effect to it.

**1:45:50** · Now, we don't have that logic yet, but when we add more stuff to this div, which by the way, we need to write another div that should wrap this whole thing around that I forgot to add, then on this div over here, what we want to do is add a simple class name where we set it to be relative, position relative, and we're going to set it to be a group. Then, on this one, we want to add it to have a class name of flex one and set the max width to be full.

**1:46:19** · Then, on the outermost one, here's where it changes a bit. So, depending on the position of the image or the code, we want to change this class name. First, we're setting it to display flex, then we'll make it column. And this will make more sense when we open this up like this. You'll see all of them are just appearing one stacked on top of each other. We don't want that. What we want to do instead is in a large screen, we're going to set it to flex grow.

**1:46:46** · Then, we're setting the items to center, a gap of eight in between them, and in a small screen and above, that gap will be bigger.

**1:46:55** · Now, here's where it changes. If the image or if the feature .image position is equal to right, then I want to set the large screen on a large screen to have a flex row reverse. And you'll see that it will reverse where the image is. Now, if it's left, we don't want to do anything because it's by default on the left.

**1:47:22** · Now, you might be thinking, well, that did absolutely nothing. But here's where we change. We need to have a text next to this, right? A text with the uh feature title and the feature content. So, below this section, right where we have the syntax highlighter, we're going to go down around five divs, so 1 2 3 4 5.

**1:47:43** · And in here, we're going to add the text section.

**1:47:48** · In this section, we're going to add a div. You'll see that now, uh oh, if I close this div, uh and I were to add something here, you will see that it actually applies the correct uh distribution. One is uh on the left, and the other ones aren't.

**1:48:03** · Now, we have to check to see how this will look when we do add the entire section, so we're going to do that. The first thing is on this text section, I'm going to set a flex to one and a width to full.

**1:48:15** · Then, inside of here, we're going to add another div.

**1:48:19** · And on this div, I want to add an H3 with the title.

**1:48:24** · So, H3, we're going to add the feature.title.

**1:48:28** · And on the second one, we want to add a paragraph tag with the feature description.

**1:48:36** · So, we should get all of the content just like this. But we have a lot of styling to do still. For example, we want to set a max width to this text, so we'll set it to be large.

**1:48:49** · I'm also setting the margin X to be auto. On a large screen, there shouldn't be a margin X, and the text should be centered, but on a large screen, it should be aligned to the left because uh there is the whole um changing of positioning when it's a large screen. In a mobile, everything should just be centered. Now, in an H3 here, we want to set the text to be 4XL.

**1:49:14** · On a small screen, it's going to be 3XL.

**1:49:18** · And on a large screen, it's going to be text 4XL.

**1:49:22** · Also, the font should be bold, a margin bottom of four, and then a margin bottom of six in a bigger screen, and the text should be white. And here's how it's starting to look. Now, it looks like the ones that are aligned to the left are not working because they should be fully aligned to the left. So, there's something that we have to do, but the one that the code is aligned to the right seems to be working perfectly fine. Now, we're going to get there.

**1:49:47** · We're just going to style the last thing here, which is the description. We're going to set the text to be gray 300, a text with the size base, a text base, and a text XL.

**1:50:01** · But, on bigger screens, we're going to make that large. And I'm going to set the leading to be relaxed, so there's more gap in between the texts.

**1:50:09** · Perfect. Now, if you go over here, the text in itself looks great. Obviously, there's a lot to be done around this over here. So, what do we want to do?

**1:50:17** · Well, first of all, let me just pull this over here. There are some changes we need to make to the code itself because it doesn't look like it does over here. So, the first thing is that we made it such that the color of this background actually applies to the color of the VS code code here. So, here we're using Night Owl, but we might want to change it such that it applies the same background color as what we set for this the header section around.

**1:50:44** · And what we can do is instead of setting the background instead of just letting the background be set by this, we can set the background uh actually in the custom styles. Yeah, we are inside of the custom styles. The background here to be transparent.

**1:51:04** · And then, whatever the background of this section is, it will apply to the code editor. You see that now it looks like it's integrated to it. But, there's a border and we want to remove that. We had that on the other one, but on this one we don't want it. So, now it already looks a lot similar to this. But, there's still some things. For example, where is this cool little color around this this gradient? To add that gradient, here is what we need to do.

**1:51:27** · We're going to come above this IDE interface section over here. And we have this div, but above this div, we're going to add a self-closing div that is going to just set this background. It is a self-closing, it doesn't need to wrap anything, so make sure it doesn't. And it only applies to the background of this section. In my opinion, it makes it look a lot better, but you can change the colors to whatever you want. You can even make this be green or whatever you want. But, I like it going from blue to purple cuz it matches the theme of the website.

**1:51:57** · Now, we have to address the fact that when I make this into a bigger screen, this isn't working. This should appear this code should appear in the left, similar to how this one appears on the right. So, the way we fix this is the following way. Now, right off the bat, I can see that there's a bug over here. We set on a large screen for this to be flex grow, when in reality it should be flex row.

**1:52:19** · And just like that, this fixes the issue. Sorry about that. Obviously, when I'm typing sometimes it might be hard to recognize that I made a misspelling, but if you notice that, then that's good cuz yours didn't end up having any issues.

**1:52:33** · So, we're pretty much done with the section for the features, and it looks pretty good. You can obviously play around with it if you want to. You can add other things to the text. Like, for example, I added here a bunch of thing over here for for this section specifically. You can add that for yours as well, but it looks totally fine in my opinion. Now, we want to add the next section, which is going to be the pricing section. This one is pretty interesting because it actually applies to every single landing page you see out there cuz you do have to have a pricing section so people can purchase your product. Okay.

**1:53:03** · So, now it's time for us to build the pricing section. So, I'm going to open this up and I'm going to restructure this so we can see how it will look immediately as we're writing the code.

**1:53:15** · So, right off the bat, we need to do something similar to what we did with the features. We're going to come over here and create an array, which is going to define the different plans that we're going to have on this website. So, for each plan, we're going to have an object with a name. So, this is the starter plan.

**1:53:32** · Then, we have to have a price. For example, the starter plan is going to be $29.99.

**1:53:37** · Then, we're going to have a description, something like perfect for individuals and small teams.

**1:53:48** · Then, a features section, which you should list up whatever you want. Usually, people make it such that the beginner one has a couple features and the other ones has all of the same features as the ones before plus a couple more. I'm going to add some features here that I already wrote, but you should add whatever makes sense to your website.

**1:54:10** · And finally, we want to add a boolean that is going to determine if this is the most popular or not. So, there's going to be three of them, right? And one of them's going to be the most popular, which is the middle one, but we need to identify which one is which.

**1:54:25** · Now, you do this for all of the plans.

**1:54:27** · Again, I already have that, so I'm just going to copy and paste, and I'll be back in a second. Perfect. So, I just added here a option for a professional plan, an option for an enterprise plan.

**1:54:38** · I'm also going to add .99. I always like doing that cuz I think it looks better.

**1:54:43** · And now, what we want to do is we want to define this section. So, I'm going to replace this here with a section tag. Then, on the section, I want to put an ID of pricing.

**1:54:57** · Then, for the class name, we're going to put the same stuff we did for the uh for the feature section. So, we're going to go up here and we'll just copy this entire class name here and then just edit directly here.

**1:55:11** · Perfect. Now, in this section, what I want to do is I want to start by just adding the title. We can actually copy the same thing we did here for this.

**1:55:20** · It's just this part over here plus the overall div that will encompass everything. So, we need to self-close this div over here. One thing I want to do though is I want to make this be 7XL just because the pricing section might be a bit bigger. Then, inside of this, I want to make it such that it says something like this. It should say simple, transparent pricing plans. And there should be a little description below it. So, to do that, I'm going to first on this first one over here, I'm going to say simple and transparent.

**1:55:55** · Then, I'm adding a line break, and then on this one, I'm adding pricing plans.

**1:56:02** · Then, we're closing the H2, and we're adding a paragraph tag, which is something we didn't have on the other one. On this one, we're just going to add something like this. Choose the perfect plan for your needs. All plans include a 14-day free trial.

**1:56:14** · Then, I'm going to add a class name here, set it to text gray 400, text base, text XL.

**1:56:23** · And on a small screen and above, I'm going to set that to be text large.

**1:56:27** · Setting a max width to be 2XL and then a margin X to be auto.

**1:56:34** · Perfect. Now, we're finished with the header section, and we can go ahead and build the cards. So, I'm adding this div over here, and on this div, I'm adding a class name of display grid, grid columns of one, but on a medium screen and above, we'll make that be two columns, and on a large one, we'll make that be three columns.

**1:56:55** · That will make it such that the pricing plan over here in one like in a mobile screen, it should just show all of them in one column, and a slightly bigger one, it should show two columns, and on a bigger one, it should show three. Now, we're also setting a gap of six.

**1:57:13** · In a small screen, we're going to set that gap to be eight, and in a large screen, we'll put it back to be six.

**1:57:20** · Now, inside of this div, we want to loop through the pricing plans. So, for each of the plans, we want to map and get the plan plus the key.

**1:57:33** · Then, I want to render a div that is going to show each individual card. I'll assign the key to the key field on the div, and I'll start by adding the structure of this card. Now, this class name is going to be dynamic. And the reason for that is because we want to add a different type of style depending on if this is the most popular or the not or just the normal ones.

**1:57:59** · Now, to start this off, I'm setting this to be a position relative, a BG slate of 900, but only 50%, and a backdrop of blur small.

**1:58:13** · Then, we're setting a border. We're setting a rounded XL. So, you're starting to see the three different cards appearing here.

**1:58:23** · And we're setting on a small screen for it to be rounded 2XL.

**1:58:28** · And we need to set some heights to it, so I'm starting with a padding general padding of six, and on a bigger screen, that will become eight. Now, we want to add a transition all and a duration of 300. I'm going to make the overflow be visible, and I'm going to add a group and a display flex. Now, we're setting the flex to be column and the height to be the full length of this. What we want is we want to change the structure.

**1:59:00** · Obviously, say no content inside of it, so it will remain this same height, but we want to change the structure depending if the plan is popular. So, if the plan.is.most popular is true, then I want to add the following class.

**1:59:14** · If not, I want to add something else.

**1:59:16** · Now, what class do we want to add for the most popular? I want to make it such that the border is going to be blue 500.

**1:59:22** · So, the middle one should become like that. Now, did we put a most popular?

**1:59:27** · Oh, for some reason here it says popular instead of most popular.

**1:59:31** · Perfect. So, the middle one should be like that. Now, what I want to do is I want to also set a shadow to be 2XL on the middle one.

**1:59:40** · I want to set that shadow to be blue.

**1:59:43** · So, blue 500 and only put a 20% opacity.

**1:59:47** · \[snorts\] Then, I want to make it such that in a large screen, I want to make it even bigger. So, you'll see that in a large screen when I open this up, we're going to have the three, but the middle one is going to be slightly bigger. Perfect. Now, on a smaller or on a non-popular one, we want to set the border to have a color of slate 800.

**2:00:08** · Then, I also want to make it such that when you hover it, the border will become slate 700. And this should be good to go. You'll see as I hover this stuff, it does affect it.

**2:00:19** · Now, instead of this, I want to start by adding the most popular tag. So, if the plan is most popular, then I want to add this little tag at the top. We're adding a div over here that is going to have a another div inside of it. And inside of the second div, we're going to have a star component, which is an icon from Lucide React.

**2:00:45** · Now, below this, we're also adding a span that says most popular. Now, we do want to make it such that it doesn't appear inside, but rather at the top. So, in this div, we're going to set this to have a position absolute. And also, it's going to be at the top like two above the thing. So, it's slightly up. That's why it's negative. And in bigger screens, it will even be more. So, negative top three.

**2:01:12** · The left is going to be a half, so it's right in the middle. And we're setting this to transform uh negative translate X 1/2. And then, we're setting the Z index to be 10 just to make sure it's above. Now, this div over here, we're going to set the display to flex, items to center, a space in the X direction to be one.

**2:01:36** · And then, we're setting a padding of X of three, and a bigger padding if it's bigger, a padding of Y of one. Same thing, we're just slightly increasing the padding in the Y direction if it's a bigger screen.

**2:01:49** · And we're going to set a BG gradient to the bottom where it's going to go from blue 500 to cyan 500. So, it's the same color we've been using kind of for the different texts. Then, I'm going to make this be rounded full, so it's a pill. And I want to make the text be extra small, so that's a lot smaller. And we'll make it small in a bigger screen. The font will be semi-bold.

**2:02:18** · And a shadow is going to be large. Then, inside of this, we want to apply some styles to this the star. We're going to put a width of three and a height of three. Then, we'll copy this and apply it again, but for the small. Perfect. And then, what I want to do is next to this, I want to make it such that this will also have a feel white.

**2:02:48** · Oh, I need to put this inside of here.

**2:02:50** · Feel white.

**2:02:52** · \[sighs\] And now, we have this pill appearing at the top. Perfect. So, now it's time for us to add the first part of this card, which is the plan name, description, and price. So, I'll add this div over here that should encompass all of that. In the first section, we'll add the plan name. So, we'll add an H3 that says plan.name.

**2:03:14** · We'll then add a plan description. So, this will become a paragraph tag, and it will say plan.description. Then, I want to add a div that is going to encompass this whole thing. And it's going to include the price of this through a span. So, we're going to add a money sign, and we're going to insert the plan.price in here.

**2:03:40** · Now, I also want to add a span right next to it that is going to say that this is a monthly subscription. So, 29.99 per month. And this should be enough for this section. Now, above here, we want to make this have a text that is centered, and a margin bottom of six with a margin bottom of eight in bigger screens.

**2:04:01** · Then, for the plan name, I want to set the text to be XL and 2XL in bigger ones, and the font to be bold with a margin bottom of two. Then, for the paragraph, we'll make the color be gray 400, a text that is extra small, and a text that is small in bigger screens with a margin bottom of three, and a margin bottom of four.

**2:04:26** · Then, on this section, the reason why we made it into a div is cuz there's the whole part over here where it's two spans connected. So, what we want to do is we want to say display flex, so it's in the side, and then we're going to set the items to actually be aligned to the baseline. And then, next to it, we're going to justify everything to the center.

**2:04:51** · Now, after that, we want to change this span to have a text that is way bigger.

**2:04:56** · So, 3XL.

**2:04:58** · We're then going to make it even bigger on bigger screens, and 5XL as well. The font is going to be bold, and we want to make it such that it has a gradient color to it. So, what I'm going to do is I'm going to apply this gradient to the right that we've been using where you can clip the text and make it be a gradient from blue to cyan.

**2:05:22** · Then, what I want to do is on this div on this span, I want to make the text be gray 400, margin left of one, margin left of two, the text is small, and the text is base.

**2:05:37** · Perfect. So, now we have a similar card to the rest of this. Now, there's a bit more that we need to add. We need to add the features for this section, and also the button at the bottom. Now, for the features, here's what we want to do. We'll get this div, we'll go below here, and we'll create an unordered list that will loop through the plan.features. We'll loop through each feature, get them.

**2:06:02** · Get the uh since we're inside of a map already that has a key, we need to name this key feature key. Then, inside of this, we want to create a list item. And in this list item, I'm going to set the key to be equal to the feature key.

**2:06:21** · And for each item in this list item, I want to render a check mark on the left since this is a it's this the features over here. So, I'm going to use the check mark icon. It's called check from Lucide React. Then, I want to have a span below this that will just show the name of the feature.

**2:06:43** · Perfect. Now, let's obviously style this. For this list item, what I want to do is I want to set a display flex. I want to set them to the left, so I'd start, and I want to put a space a gap in the X direction of two. And on a bigger screen, that should be a bit more.

**2:07:02** · Then, for the check mark, what I want to do is I want to set this to have a flex shrink of zero. And also, I want to make it have a width of four, a height of four. Uh and I'll make that be different on a bigger screen.

**2:07:20** · Then, I want to make it be rounded full, so there's a circle around the icon, but for that, we need to put a background so you can see that it's a circle. So, we'll make it be 500 divided by 20. Then, we want to center the check marks inside of that. So, I'm going to say uh display flex, and items center, and justify center.

**2:07:43** · And then, we need to put some margin, right? So, I'm setting a margin top of very small amount, 0.5. Now, to make the check mark the look like it has some padding around it or some margin around it, I'm going to put a width of 2.5 and a height of 2.5.

**2:08:02** · Then, I want to make it such that it is going to have a text blue of 400. But since we're also applying a different height for the overall circle when it's a bigger screen, we'll do the same thing here, but the height and width is going to be three. Now, you can see that when I expand this, it becomes bigger, and it already looks pretty nice.

**2:08:23** · Now, we do want to change the text for the feature. I want to add a text gray 300, so we change the color. Then, I want to set the text to be small, and a text to be base when it's bigger.

**2:08:36** · Now, I also want to come to this div that is an ordered list that we're wrapping this whole thing around. I'm just going to put a gap so that spaces this out a bit in the Y direction. I'm going to set it to three. Then, in bigger screens, we're going to set that to be four. A margin bottom of six, and a margin bottom of eight and we're setting the flex to be row.

**2:09:03** · Perfect. Now, you see that we can expand and it looks pretty good.

**2:09:09** · Now, we just have to add the action button at the bottom. So, since we've added this action button before, it's going to be very similar to this action button from the top up here. So, what I want to do is I want to come here and I want to add this button. This button will change depending on if this is the popular plan or not.

**2:09:31** · We just have to make this say most popular. If it's the popular plan, then it should show a gradient around the button. If not, it should just show this generic button which has a background color of white with 5% opacity.

**2:09:45** · Perfect. Now, below this section over here, so right over here, we want to add a little text that allows the user to be able to contact us if they need a custom plan. This is done whenever a business or something wants to purchase your product for a lot of people, so you can make a custom plan so that you earn more from uh providing more of your service to more people. Now, in here, I'm going to add a text saying need a custom plan.

**2:10:16** · And I want to add an A tag that is right next to it. Not an AP tag, an A tag that will have a link to you being able to contact you. So, I'm going to say contact our sales team. Now, what I want to do is in this div, I'm going to add a margin top of eight. And we'll make that 12 in a bigger one and I want to center this right in the middle.

**2:10:42** · Then, I want to come to this paragraph tag. I'll make the color of it be text gray 400, a text base, and a text excel. Then, to make this look blue because it's a link, we just have to pass an Href here. Now, you'll pass the Href you want. This is also This is obviously a fake website, but if you want, you can put a link to your email or a link to a different part of your page where someone can contact your team.

**2:11:11** · Now, for the styling, I want to make this be blue, so blue 400, so it looks like a link, and I want to make it such that when you hover it, it just becomes text blue 300.

**2:11:24** · Perfect. And now we have this beautiful pricing section that has uh the most popular plan is the one in the middle with different UI for them and it looks really nice. There's just one minor thing I want to change, which is this over here. I added this thing. I love adding this, which is a glassy effect when you hover something. I think this gives a good aesthetic to it and if you want to do something like this, it's actually pretty simple. So, what we want to do for that is we want to go above where we are rendering the most popular pill and we want to add this div over here.

**2:11:56** · I add this a bunch of times into my different projects. It's pretty big, but basically, it just has an absolute positioning at the top and when you hover it, it expands a gradient from the top left to the bottom right. Now, it looks really good when you hover it, but one thing I just noticed is there's a small gap in here, so I think what we need to do is we need to add here a rounded full so that that doesn't happen, but then that happens, so let's just make it be rounded large.

**2:12:28** · Yes, it fits perfectly now. So, if you want to add this, either get the code from the description where we're going to have this or you can just try to pause here and look at the code, but this is how it looks. It has some hover effects, some translation, and a duration, and a gradient. Perfect. So, we're pretty much done with our project.

**2:12:53** · We just have to do one more section, which is the section Oh, this is interesting. Why did Why did that disappear? I don't know, but it's back. So, we want to make the section for the um uh for the testimonials and then add a simple footer. So, for the testimonials, we're going to come back to our section over here, testimonials.

**2:13:16** · And similar to everything we've been doing so far with the last two sections, the testimonials is going to have an array which we're going to use to loop through. Now, \[snorts\] you can add as many testimonials as you want. I added three. I think that's perfectly fine.

**2:13:29** · So, testimonials. And obviously, you want to make sure to get real testimonials, okay? I know it's tempting to put fake ones, but if you're going to have a real website, you put real testimonials. Just add fake ones in this example like I have because it's just for the experience of building the website.

**2:13:47** · Now, for the testimonials, each testimonial requires the name of the person who created the testimonial. So, for the first example, I'm going to use a woman called Sarah Chen. Then, you put their role, so their job, like a senior developer.

**2:14:04** · Then, we're going to have an image. Now, an image is the image of the person and since this is like fake, this is a mock data, I'm using an a URL from Pexels, which is a free copyright website where you can get pictures of people or other things as well. Now, we're also going to put a content, which is just what the person said about your platform. So, I have this fake data here. It's just some silent It's just some simple quotes saying that like this platform makes me I don't know work a thousand times more efficiently.

**2:14:38** · Whatever you want to put. Now, it's time for you to add your other ones. I already have them over here. I created two more and they I usually like to put different roles and different kinds of people, but we have three people to show up. Great. Now, it's time for us to build the beginning infrastructure of this section.

**2:14:56** · Now, to do that, it's going to be very similar to the previous one as well. So, I'm going to copy this logic over here, even the header, and I'm just going to paste it over here. Now, we have to fix some stuff like I have to add a self-closing div and a self-closing section, but we should have a header with a section appearing at the bottom. We'll change this to say testimonials.

**2:15:20** · And also, I feel like Oh, here over here, we want to change this. Instead of saying instead of having a span, uh we actually want to just have an H2 tag that will say what developers are saying about us. And then, what I want to do is for the speed tag, I'll add something else like uh just more promotion for your website.

**2:15:46** · Now, there's a bit of styling that we want to do here. Like I don't like how this title is set up. It should be like this. So, what I want to do is this section this title should be particularly different from the other ones because in a larger screen, this section has a title on the left and the content on the right. And on the other ones, it just has a title in the middle.

**2:16:04** · So, to address this, I'm going to open this up and here's what we were going to do. We're going to start by setting here a thing that says left side, which is the header.

**2:16:16** · Then, we want to wrap this entire thing around with a div that will wrap even the section below. And this div is going to have a class name of display flex, flex column. In a large screen, it's going to become a flex row. And I'm going to set the items to the start, a gap between them of eight. Make that gap bigger in bigger screens and even bigger later on. So, gap 16.

**2:16:47** · Then, on the left side over here, I want to remove this and what I want to do instead is I want to make it such that it has a on a large screen, the width is going to half of the screen. So, in a large screen, it should only be on the left and it should fit in half of the screen.

**2:17:04** · The other section The other thing I want to do is I want to make the width be full if it's not a large screen, which is the case if it's mobile because then, you'll see when it's mobile, it actually goes and stays the full length and puts the other stuff in the middle.

**2:17:20** · Now, after that, I want to center the items and on a large screen, I'll just set them to the left. Now, this looks fine both on a large screen and on a small screen. So, so now, what I want to do is I want to create the right side, which is the testimonial. So, right side testimonials.

**2:17:45** · So, to do that, I'll create here a div that is going to have a class name of which is a large is going to be half of the screen just like we just did with the left side. And the width is going to be full in mobile. Then, inside of this div, we're going to add a another div that is going to wrap the list of testimonials. So, testimonials.map, we're going to get each testimonial.

**2:18:15** · And we're also going to get a key. And for each testimonial, we want to render a div.

**2:18:22** · Now, in this div, I'm going to add a key, which is just going to be the key like always, and I want to make a class name that is going to build the infrastructure for the testimonial. The class name is going to have a BG slate of 900 with 50% opacity. If you see when we start building the uh the size of it, like a padding of four, you'll see that now the items should appear.

**2:18:46** · But, they're all grouped together, so it will look like a giant blob. I'm also making the padding be six when it's a bigger screen. Then, I want to make it such that there's a back drop of blur that is small. I also want to make it such that there's a border between them. Now, you can clearly see the division.

**2:19:06** · The border is going to be slate 800 and it will have a border radius. Now, if it's bigger screen, let's make that border radius even bigger. Perfect. Now, inside of this div I want to set a div that is also going to encompass the rest. This div will have a class name of display flex and item start and a space in the X direction of three with a bigger space when it's bigger.

**2:19:38** · Now, inside of this div, I want to add the two parts of uh the testimonial card. It's going to have this part over here, which is the quotation mark, and the second part is the actual testimonial. So, to do that, what I want to do is I want to first create the left part by creating this div that is going to have a flex shrink of zero.

**2:20:06** · Then, in this div, I want to add a div with the quotation mark. So, I'll just add the quotation mark directly in here. Now, we do want to make the quotation mark a lot bigger and have a gradient. So, since we've done that with other texts, I'm just going to copy and paste. What we did here is just set the size of the text, the text to bold, and we set it to have a gradient color.

**2:20:28** · Then, below this, we'll go down two divs, we'll make the right side. And the right side is going to be the actual testimonial with the user image and everything else. So, I'm going to set this to be flex grow. And inside of this div, I want to add a P tag that is going to list the testimonial. So, testimonial.content.

**2:20:50** · Now, we also want to put the image of the user. So, below this P tag, I'm going to add a div that is going to have an image that shows the profile image of the user by using the source which we can get from the testimonial.image. Now, we want to specify an alt as well for accessibility reasons. So, I'm just going to say testimonial. image, just the URL. Uh actually, no.

**2:21:21** · Let's put the name of the user as the alt. Then, in the class name here, to make the image uh look like a circle, I'm going to make this have a width and a height that is exactly the same. And then, it looks kind of smashed, but you'll you'll see it will look good.

**2:21:38** · We're going to make the width be 12 and the height be 12 in bigger sizes. And then, I'll make this into a full circle.

**2:21:48** · Then, I want to make the object cover, which then what this makes is it makes it such that it doesn't squish. It just clips around the image. Now, I'll come to the testimonial over here. I'm adding a class name. Make this text white. We're then going to set this to text base. On a small screen, this will become text large and we're going to have a leading that is relaxed.

**2:22:12** · And a margin bottom of three with a margin bottom of four when it's small. Now, for this div over here, we're going to add a class name where we say display flex. We're going to center the items.

**2:22:25** · There's going to be a space in the X direction of two, and you'll see because we'll have to put the name of the user as well next to their profile image. So, that's the gap for that. And we'll make it bigger as well. Now, below this image, I want to add a div to put the name and the role of the user.

**2:22:42** · So, in here, I'm going to add a an H4 tag. I feel like H4 makes sense. And we're going to add a testimonial.name. Then, below this, we'll add a paragraph tag for the role. So, I'll say testimonial .role. Now, we want to make the H4 have a font that is semi-bold, a text that is white and I also want to make the text be small, but on a small screen, we'll make the weight be base.

**2:23:14** · Then, I'm going to copy this and I'm going to paste it over here. Now, we want to change just a bit. We want to make it Actually, we're just going to change everything. We're going to make the text be extra small uh and it will be small on bigger screens, and the color won't be white, it will actually be gray 400.

**2:23:33** · Perfect.

**2:23:35** · And now, we are pretty much done with the section. Let's look to see if it's uh identical. Yeah, the only thing that we need to do is put a gap in between this uh different items over here. And to do that, we can come here to our looping. We have this div over here.

**2:23:51** · And we have to add a space Y of six. This should be good. But on a bigger screens, we want to make that gap be even bigger. So, I'll make it eight. Perfect. And now, we have this beautiful testimonial section that adapts, fully responsive, uh in whatever kind of screen we're in. Now, we're almost done with the website.

**2:24:11** · We just want to add the footer. For the footer, I'll be honest, I don't think it matters that much, especially if you're building a website like this. Like, we don't have any of these links in this website. We're just building the the landing page. So, for the footer, I'm actually going to go a little bit faster than what we were in the other pages.

**2:24:30** · So, for the footer, what I want to do is I'll close all of this. We'll come here to the um footer section. So, where's the footer? It's uh here. And I'm just going to copy and paste the entire code for this section and go over everything that we do. So, first of all, we are seeing that the footer is now here. You can clearly see it works and it works in mobile as well.

**2:24:52** · If you come over here, it actually in mobile, I made it such that the footer becomes way smaller just because it would look kind of weird to show off the different uh links in a mobile setting. Now, this is what this code looks like.

**2:25:04** · First of all, we choose the links that we want to have. So, footers usually have a bunch of links depending on what kind of uh company you have. So, you divide it into different sections.

**2:25:14** · Then, in here, we create a section normally like we would before. We put the logo and the name like we did on the nav bar and a little bit of a tagline for the company. Then, we list out all of our social media platforms, this part over here. And if you have a company and you have a profile in those, you'd go ahead and put the H ref to link to that. Now, we used a icon from Lucide React for each of them.

**2:25:38** · And then, we loop through the footer links through this object.entries.map because object.entries will make a list out of an object and it loops through all of them and makes a link for each individual section. So, this is pretty much it. There is one more thing I do want to do though, which is if you notice on this one over here, it has a border bottom uh to the nav bar when we are scrolling.

**2:26:04** · But when we get to the top, that border bottom disappears. In this case, it just never has that border bottom. Now, some people might like it like this. Might like it without the bottom bottom with the uh glassmorphism uh because of the backdrop blur that we added. However, I like this and this is what I promised, so this is how we do it. So, we're going to come back here to our app.jsx and we're going to have to create a variable called scrolled which detects if the user has scrolled or not.

**2:26:35** · And we're going to pass this as a boolean to the nav bar component. Now, to detect if the user has scrolled or not, it's similar to what we did with the other sections. So, we're going to come here and we're going to create a state called scrolled and a function called set scrolled. Set this equal to a use state which will be false.

**2:26:56** · And then, I'm going to pass a use effect that is going to subscribe to a scroll listening event. So, I'm going to come here, add an empty dependency array.

**2:27:12** · And then, in here, I'm going to add a window .addEventListener and we're going to subscribe to the scroll event. And when we subscribe to that, we're going to call this function we're going to create called handle scroll. Now, we'll create that function up here. We'll say function handle scroll.

**2:27:33** · And this is exactly like what we did for the mouse, but it's for the scroll. And we can set the value of the scrolled boolean to be true if the user has a scroll positioning in the Y direction to be greater than 50, which is I believe the height of the nav bar.

**2:27:54** · And we'll set that to true if the scroll Y of the user is set to that. So, we need to now return something here cuz we need to clean this up so there's no memory leaks. So, we're just going to copy this and I'm going to say remove event listener. Then, we pass this value to the nav bar.

**2:28:15** · Now, in this nav bar, we need to get that, so I'm going to say scrolled as one of the options here. And all I want to do is in our nav bar over here, this should become a dynamic nav bar. So, I'll close this up. Make it into a dynamic uh class name.

**2:28:31** · And you know where we put the background color over here with the back uh blur and the background color over here, we're just going to wrap this around with a variable. And we're going to check to see if the user has scrolled. We want to do something. If not, we want to leave it how it was.

**2:28:49** · Now, what do we want to do if the user scrolled? Well, I'm going to copy this, paste it over here, and I want to change it a bit. I want to make the actual opacity be a lot bigger cuz I do like the glassmorphism, but I want to be able to have more opacity on the navbar when we're scrolling.

**2:29:07** · But most importantly, I want to make the blur be large and set a border to the bottom. The border will have a color of slate 800, so it blends in with the color. And now you'll see when I scroll down, it should now have a border, which it didn't have before. Now, we just have to fix one more thing. So, obviously, there is two issues here with the code.

**2:29:29** · The first one is that it's still kind of not filling the entire section, and the second one is that if you go into a smaller screen, it does work and fill up the section, but then the code inside of it is centered, which doesn't make sense because who codes in a code editor where the code is centered? Now, to fix that, we're going to go here to our hero, and we're going to go to uh let's take a look to see what it could be. Okay, it seems like I remember fixing this.

**2:29:54** · Maybe we have two of these, but uh you see how we are setting the class names for this, but I remember fixing this. We changed this to become a height instead of a width. And I believe now this will fix this. I clearly remember us fixing this. Maybe I command Z for some reason, but now it works.

**2:30:12** · Now, what we want to fix is the alignment of this because this shouldn't be aligned to the center. Now, to fix that, I'm going to go to our syntax highlighter, and I want to add some minor things that we haven't added so far. So, let me just expand this more like this. What I want to do is I want to set the word wrap to break word. This is just a minor thing in case there's an issue with that, and I want to make the white space be pre-wrap.

**2:30:43** · Now, we need to go to where we set the text positioning. So, let me go to where I say text left.

**2:30:50** · Uh is it on this one?

**2:30:54** · Uh no. Actually, I can just come to the code editor over here, and I can pass a text align and set this to be aligned to the left.

**2:31:04** · And then no matter what, it will always be aligned to the left. That works better. Perfect. So, now we're pretty much done with the website. If uh you don't want to deploy this, then you're pretty much done. But now, what we're going to do is be able to deploy this very easily by using Vercel as our host. So, if you don't have an account, I recommend going to Vercel and creating one. I already have one, so I'm just going to come here and add uh add project. And what's going to happen is it's going to import our Git repositories.

**2:31:35** · The reason for that is because I created a vercel.com account by using my GitHub account as the link. So, I recommend you doing that as well. So, we're going to go to GitHub just like this, and we're going to create a new repository. I'm going to call this the modern UX UI uh website. Something like that. And I'm going to click on create repository.

**2:32:03** · Then I'm going to copy all of this. I'm going to come back to our code over here, and I want to open up our terminal, and run the command get init, get add dot, and then paste all of that. Now, our code should be in the GitHub repo. And by the way, this is the code that you guys have been looking at ever since the beginning of this video.

**2:32:26** · But most importantly, now that repository should appear here in our Vercel account to be able to deploy. I'm going to click on import, and it's going to detect that the framework is Vite. If you for some reason used a an environment variable in this project, which I didn't because it wasn't necessary, you can add them right over here. But we don't need to, so I'm just going to click on deploy. And hopefully, if everything is right, in less than a minute, we should see our website deployed live. Great. As you can see, again, took less than a minute.

**2:32:53** · I'll click on continue to dashboard, and I'll click visit, and as you can see, our website is live and ready to be used. Feel free to go to those website, play around with it, see whatever you think.

**2:33:05** · If you find any issues, any bugs, let me know, but this is how you build a beautiful landing page with a modern UI and UX design. Now, I highly recommend that you, whenever you're building something like this, don't fall into the trap of using AI for all of it.

**2:33:22** · I personally code with AI a lot of times. I've mentioned this multiple times. Some of you might even think that I built this entire thing with AI. And the reality is, no. And the reason for that is because I can notice if a website is built with AI or not immediately. There's some aspects to it, and that's totally fine, but for landing pages, it is actually detrimental, in my opinion, because every landing page ends up looking the same.

**2:33:46** · One thing that AI always does is this pill over here at the top. I used to do this pill before AI was even a thing, so I still like it, but a lot of the things that AI would make, for example, will make your entire website be purple.

**2:33:58** · That's very well known. I would recommend you to just um try to build something yourself. Also, you'll be able to practice uh the skills of building UI like we did in this video, and yeah, that's pretty much it. Now, if you like this video, and you want to learn more about React, I have my ultimate React JS course for beginners. I'll link that in the description. Also, if you're looking to learn another framework, such as the Next JS framework, I also have a Next JS course that will teach you everything from the absolute beginning to the end, so you're able to master Next JS and build really good projects with it.

**2:34:30** · So, if you're interested in any of that, just go ahead and click the link in the description. If you enjoyed this video, please have a like and comment what you want to see next. I am trying to see if I can create more UI-based tutorials because you guys showed the love for the personal portfolio ones that I built, so I want to see if you guys want to build more of this. So, thank you so much for watching, and I see you guys next time.

**2:34:53** · \[music\]