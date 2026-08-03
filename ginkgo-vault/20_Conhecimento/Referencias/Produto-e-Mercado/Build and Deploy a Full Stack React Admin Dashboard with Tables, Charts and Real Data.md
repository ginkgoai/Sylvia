---
title: "Build and Deploy a Full Stack React Admin Dashboard with Tables, Charts and Real Data"
source: "https://www.youtube.com/watch?v=xZ1ba-RLrjo"
author:
  - "[[JavaScript Mastery]]"
published: 2025-04-25
created: 2026-07-02
description: "Build a dynamic travel dashboard with personalized travel suggestions, charts and tables using React Router v7.Syncfusion: https://jsm.dev/tourvisto-syncfusionAppwrite: https://jsm.dev/tourvisto-ap"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=xZ1ba-RLrjo)

Build a dynamic travel dashboard with personalized travel suggestions, charts and tables using React Router v7.  
  
Syncfusion: https://jsm.dev/tourvisto-syncfusion  
Appwrite: https://jsm.dev/tourvisto-appwrite  
Sentry: https://jsm.dev/tourvisto-sentry  
WebStorm: https://jsm.dev/tourvisto-webstorm  
Junie AI: https://jsm.dev/tourvisto-junie  
  
🎁 Video Kit (Codebase and more!): https://jsm.dev/tourvisto-kit  
🚀 Upgrade this project: https://jsm.dev/tourvisto-upgrade  
  
⭐ Join JSM Pro: https://jsm.dev/tourvisto-jsmpro  
📙 JavaScript Pro Course: https://jsm.dev/tourvisto-cpjsm  
💎 Next.js Pro Course: https://jsm.dev/tourvisto-nextjs  
  
https://discord.com/invite/n6EdbFJ https://twitter.com/jsmasterypro https://instagram.com/javascriptmastery https://linkedin.com/company/javascriptmastery  
  
Business Inquiries: contact@jsmastery.pro  
  
Time Stamps:  
00:00:00 — Introduction  
00:02:36 — App Setup  
00:13:16 — Syncfusion Setup  
00:19:26 — Routing  
00:26:26 — Dashboard Layout  
00:56:17 — Admin Dashboard UI  
01:25:47 — Appwrite Setup  
01:35:40 — Auth Functionality  
01:53:30 — Auth UI  
02:16:54 — Entreprise Error Tracking & Monitoring  
02:30:06 — Users Table  
02:49:26 — Add new trip form  
03:37:33 — AI Trip Generation  
04:00:58 — Trip Details  
04:41:42 — All Trips  
04:53:25 — Finish the Dashboard

## Transcript

### Introduction

**0:00** · How many times has that budget travel hack left you broke in a hotel room with no Wi-Fi and a construction site for a view? Come on, admit it. Planning trips sounds fun until it's not. 50 tabs later, you're overwhelmed, frustrated, and somehow booked a two-star stay next to a nightclub. Perfect. But what if you could solve that chaos not just for yourself, but for thousands of people with one powerful app?

**0:27** · Hey, I'm Adrian and in today's video, we're building and deploying a full stack travel agency dashboard. Not just another static page, but a real product designed for travel businesses to plan and manage trips for their clients with AI and Stripe payment processing. And the star of the show, the admin dashboard. A polished travel agency back office where you can see user insights, trending trips, and signup analytics.

**0:57** · Browse all generated trips and customer profiles. Use AI powered trip generation to create new travel plans in seconds and then view, edit, and manage those trip details on demand. And yeah, it's fully responsive.

**1:14** · So you can also manage trips on the go.

**1:16** · Now by becoming JS Mastery Pro member, you can even upgrade this dashboard with a public-f facing site for travelers featuring a beautiful landing page with curated destinations, a pageionated list of all trip packages, and a full trip details page with day-to-day itineraries, images, and pricing. And of course, to make it real, a stripe checkout to finalize that trip.

**1:40** · Throughout the project, you'll work with modern ReactJS with React Router V7, the latest Tailwind CSS V4 for styling.

**1:50** · Syncfusion UI component suite used by Visa, Disney, McDonald's, Netflix, Starbucks, IBM, and even Apple. Apprite, an open- source backend for all your app needs. Free Gemini AI for dynamic trip generation. Stripe integration for secure payments. TypeScript for clean type- safe code, Sentry for air tracking and monitoring, and much much more. From code architecture to clean codebase structure.

**2:17** · So, if you're ready to go beyond basic tutorials and build something pitchable, polished, and portfolio worthy, this is the video you've been waiting for. Let's dive right in.

### App Setup

**2:37** · To get started building our amazing travel agency dashboard application, we'll head over to vit.dev, the build tool for the modern web. See, the application you'll build in this video is a dashboard and React excels at dashboards. So technically here, we don't have a need for Nex.js. So in this case, I'll use React and I'll quickly spin it up with VIT for instance service starts and out of the box support for TypeScript and more.

**3:07** · But with that said, if you want to follow along with Angular, NextGS, Vue, or any other technology you want, you're completely free to do that. I'll show the setup for the technologies I'm using, but later on when we're implementing the design, if you want to try out some other technologies, you're free to do that.

**3:25** · Still in this case, I want to make it work with Vit. So right here under getting started, scroll down to scaffolding your first V project. We'll use mpm and V at latest. So I'll copy this command and head over to my IDE.

**3:40** · Throughout this course, I'll be using WebStorm, a super powerful JavaScript and TypeScript IDE that as of recently became completely free for non-commercial use. Before you had to pay to use all of these great functionalities, but now you can use it for free. So throughout the video, if you see me use some cool features that pop up and they're maybe not available in your text editor, well that must mean that they're built into WebStorm. So if you want to follow along with that as well, you can download it and start using it there. Once you're in, feel free to create a new folder already and then jump right into it.

**4:13** · Within it, open up a new terminal and paste the Vit command we just copied. If you're not already within an empty folder, you'll want to add a travel app right here, which is the name of the application.

**4:25** · So, it actually creates a new folder.

**4:27** · But because I already created a new empty folder, I'll just say mpmcreate vit latest slash to set up the application in the current repository.

**4:36** · And I'll say why to install the V installer. Now, it'll ask us a couple of questions. I'll just say ignore files and continue. Choose our own framework.

**4:45** · In this case, of course, we're continuing with React. And it's asking us to choose a variant of a React application. We have TypeScript, JavaScript, but we also have this new React Router V7. Yep, that's right. In this course, not only will you learn how to build your own React dashboard, but you'll learn how to route it using the newest version of React Router. So, press enter and install the create react router installer.

**5:14** · This took just a couple of seconds and it's asking me whether I want to initialize a new git repository. And you know what? Let's go ahead and do that. So, I'll say yes, initialize it. Install dependencies with mpm. Yep, we could say yes to that as well. While our dependencies are getting installed, let's quickly set up our app account. It's an open- source tool we'll use to manage our back end. I'll leave the link down in the description. So go ahead and create a new account. As you can see, I'm using it for many projects already. But now go ahead and create a new project.

**5:46** · You can call it travel agency dashboard. Click next. Choose your region and create. Perfect. And while we're at it, you can also set up Sentry. I recently partnered with them, so they decided to give you 50,000 errors to track. And trust me, you won't be able to break that much stuff soon.

**6:07** · So simply create your account right here. Feel free to enter JS mastery as the organization name. So let's go ahead and create a project with React. I'll call it travel agency and click create.

**6:19** · Perfect. We'll get back to this page later on. There we go. Get initialize dependencies installed and we are ready to run our application. If you didn't have a new folder before, you'll have to cd into this travel app you created. But in this case, we're already in. So, I have all of my files right here. The only thing I have to do is just run mpm rundev, which will spin up the application on localhost 5173. So, back into the browser, if you open it, you should be able to see something that looks like this.

**6:50** · You can go ahead and open up this React Router docs. It's pointing us here because I'm guessing this is something that is new to a lot of people. They've made some significant changes from v6 to v7. And I want to make sure that you understand exactly how everything works so you can not only make it work for this application, but every future application you're working on. We'll dive a bit deeper into this later on. For now, just keep it open.

**7:16** · Let's take a second to clean up our file and folder structure. Currently, we have the folder called welcome here, which I will completely delete. I will also clean up our root home.tsx tsx by simply running rafce within it, which will just spin up a new React functional component called home. If this shortcut didn't work for you, that must mean that you don't have a React plug-in installed.

**7:43** · So, just search for plugins or extensions and search for modern React snippets, which will allow you to very quickly spin up new React components.

**7:53** · Great. Let's also head over into the app.css CSS and remove everything besides the import of Tailwind CSS.

**8:02** · We'll definitely need that. Now, since we'll be using Tailwind, we also want to add some Tailwind Power Apps. So, right within a terminal, I'll open up the second one. I'll call the first one dev environment or we can call it just dev.

**8:16** · And I'll call the second one terminal.

**8:18** · So, when we need to install some additional packages, we can do that right here while we know that our development environment is still running.

**8:26** · So let me run mpm install clsx as well as tailwind- merge right here and press enter. These packages will allow us to use tailwind a bit more responsibly so we don't go ahead and override some styles without knowing it. And it also allows us to very easily add dynamic styles using Tailwind. This should leave you with a very simple plain looking homepage. But keep in mind that our app is big and I really do mean it.

**8:57** · Throughout this course, we'll first build the admin dashboard that'll consist of this nice looking authentication page. We'll then switch over to building this dashboard which has a lot of moving pieces. And then we'll continue with all of the other pages as well. The ability to add trips, see them right here, and even generate AI itineraries. The dashboard part of the application where you can see the users where you can create new trips and see them on the dashboard will be released completely for free on YouTube.

**9:27** · But in case you want to take it a step further and also build a public-f facing website that works seamlessly with the dashboard we'll create, but this time for the users trying to book some trips, not for the admins trying to generate them. You can access it on jsmastery.pro Pro, where you'll be able to watch this entire course lesson by lesson, and for each lesson have a lecture summary, a transcript, a branch including only the

**9:54** · code for that specific lesson that shows you exactly what has been implemented up to that point, and even a quick quiz making sure that you have properly adopted all of the knowledge within that specific lesson. Or if you maybe didn't and you got stuck, you can ask questions directly within that lesson and get immediate help. Oh, and I almost forgot.

**10:16** · Alongside the public facing website, we'll also integrate Stripe with your dashboard so that we can process payments and actually allow people to go on these trips. So, if that sounds interesting, click the link down in the description. But with that said, even the content you're watching right now is far more than what you can find in other paid courses. This admin dashboard you'll develop will be enterprise ready using the tech that the biggest companies in the industry use. So I'm super excited to share a bit more about that later on.

**10:45** · But with that said, let's ensure that we have everything we need in order to develop this application.

**10:51** · Everything from this nice looking background on the O even to the smallest detail like this logout icon. I want to make sure that we have everything you need in order to develop this seamlessly and focus on improving your skills rather than searching for different icons online. So, for that reason, I prepared all of the assets you need right within this project's video kit.

**11:13** · You can find it in the description and then click over on the assets. That'll point you over to Google. So, you can simply rightclick it and download them.

**11:22** · Once they're downloaded, make sure to unzip them. And within it, you'll find the app and the public folder. The public folder will contain all of the assets that we'll need, such as the icons and the images. So, let's go ahead and delete the current public folder and just drag and drop this new one right in. Make sure to put it at the root of your directory. And we'll do the same thing with the app. We don't really have anything in there, so let's just delete it. And now I'll drag and drop the app right within it.

**11:52** · And if you check it out, you'll notice that it's still almost the same as we left it before. It has a home, the root where we have the HTML file, and just one single route right now. But what I've added are some types. They're going to make it easier for us to use TypeScript types in the future as well as some fonts in which we've set up the theming of our application so that we don't have to write all of these styles one by one.

**12:18** · Rather, we have them right here. But don't worry, this contains zero logic.

**12:23** · It just contains some CSS that's going to make it easier for us to style specific aspects of the application.

**12:28** · Now, if you go back and reload, you'll still be able to see the same thing that we had just before. So, with that, we've got the setup out of the way, which allows us to already in the next lesson dive into the setup of the complete React UI components library called Syncfusion. We'll still use Tailwind CSS to style our application, but Syncfusion will provide us with over 90 higherformance, lightweight, modular, responsive components that are perfect for building dashboards. And Syncfusion isn't really like material UI.

**12:59** · They're used by some of the biggest companies in the world such as Visa, Apple, Disney, McDonald's, Netflix, Starbucks, and IBM.

**13:10** · Do I have to go any further? Hopefully, you're excited because in the next lesson, we'll set it all up. Just before we go ahead and start setting up Sync Fusion, I want to make sure to push our code to GitHub. Follow along and commit to your GitHub as well.

### Syncfusion Setup

**13:25** · I'll open up the terminal, run git init commit-m app setup. This will add all the changes we have implemented so far.

**13:37** · Then head over to github.com/new and create a new travel agency dashboard. I'll keep it as public and click create. Once you do that, you'll have to switch over to the main branch.

**13:53** · So get branch m main get remote add origin and finally get push u origin master or in this case main. If you do that in a couple of seconds if you reload you'll be able to see all of the files committed right here. What I typically like to do is remove these releases, packages, and deployments and give a short description such as a travel agency dashboard. We can add the URL later on.

**14:26** · For now, I'll add some kind of a placeholder. And I will also say that the topic is React React Router V7. And what else? Well, yeah, it's a dashboard, right? So, we can say dashboard. And already our repo is looking much better. So with that said, let's set up Syncfusion. First things first, I want to tell you that it is completely free.

**14:48** · Okay, so click the link down in the description and within the video kit, I'll also leave a link to the documentation where you can see all of the different components that you can use. For example, charts. Here you have the getting started guide on how you can use charts. And you can notice that the Syncfusion components have been split into multiple different dependencies such as base, data, charts, PDF export, and so on. So we'll need to install these different packages separately.

**15:16** · So head over into your application within the terminal. And here we'll need to install all of these different packages.

**15:25** · Just so you don't have to type them all one by one, you can find them right here under mpm install Syncfusion where you can just copy it and then you'll have the full installation command. Super simple, right? Press enter and this will install all of these different components allowing us to implement enterprise ready dashboards for free.

**15:44** · There we go. That was quick. Now we'll have to update the Vcon config file. So head over to vconfig.ts. And here we'll need to prevent the list of dependencies from being used for SSR allowing us to use Syncfusion components without any issues. So I'll say SSR no external. And here we can just use a regular expression to target at Syncfusion.

**16:10** · Perfect. Now if you click set up Syncfusion link down in the description, you should be able to see a page that looks like this. As you can see, the free license is valid for 30 days, but I'll show you how you'll be able to continue using their components even after that period ends. The only thing you need is a free community license.

**16:28** · I'll use Google here at the second step.

**16:31** · If you used a personal email to create your account, you'll also need to add a work email, which they need for compliancy. But don't worry, what you can do is just type support atjsmastery.pro. You can use this as the company email. That way, you can proceed to the next step. For the company, you can also type JS Mastery. You can enter your phone number and create an account.

**16:57** · Once you do that, you'll be redirected to your Syncfusions dashboard. Here it says start your free trial for the Essential Studio. This will offer you a ton of stuff. But don't worry, this doesn't mean that you'll only be able to use your components for 30 days. What you need to do instead is head over to the bottom right part and click get your license. Here you'll be redirected to different types of licenses that exist such as team unlimited, but what we're going to go for is the community.

**17:24** · This allows you to get access to the entire product line for free if you're making less than a million dollars of course or have five or fewer developers in your team. So click claim your free license and fill in some details. You can say individual, student or hobbyist. For the organization name, feel free to type in JSMy. I don't believe these are necessary, but you might want to save whether you want to use this as open source, in which case you can also provide a repo.

**17:54** · And then you can finally provide a LinkedIn profile and say who is going to be owning the code. Of course, that is yourself. So submit it.

**18:03** · And this request can take some time, but what matters the most for us is that already we got an email containing the 7-day free trial that'll include the access to React components. So, if you head over there and scroll down, you'll be able to find your license key, which you can copy, or you can also get it right here within your dashboard by specifying that you'll use JavaScript and type JSM travel agency and get a license key right here as well. Perfect.

**18:34** · Once you do that, you can head back over into your code, create a new file called env.local, and within it, you can say vit Syncfusion license key and paste the key that you just got. Then you'll need to head over into app root.tsx. And right at the top above the layout, you can import the register license coming from Syncfusion EJ2 base.

**19:04** · And then you can call it register license. And you want to get access to that ENV variable by saying import meta envision license key. And that's it. We have successfully registered and we can use Syncfusion's enterprise ready components. Let's focus on routing.

### Routing

**19:27** · Or in other words, let me give you a quick React Router V7 crash course where I'll teach you how to do routing in modern React. Let's start from bare beginnings by deleting our current home route because we'll do everything from scratch. Within the routes folder, I'll create another folder which I'll call admin. And within admin, I'll create a new file called dashboard.tsx.

**19:58** · Instead of which we can run rafce to spin up this new react page. Now unlike Nex.js, this won't work automatically. So that if we just go to forward/dashboard, you'll be able to see it. What you have to do first is head over into this routes.ts ts file which you can think of as the configuration file. Here you can see that our index route points to the homepage which no longer exists. So instead of having this index we can use two additional methods.

**20:31** · One is called layout and the other one is called route. To start off we can simply create a route which you'll need to import over from react router dev routes. So I'll say route right here. It requires you to pass a name of that route or in other words the path. And then you need to pass a location to the file. So that'll be the routes admin dashboard.tsx. And notice how WebStorm automatically tells me what each one of these params means.

**21:03** · The first one dashboard is the path and the second one is the file. Pretty cool. And if you do that, you can see that this dashboard right now coming from here. I can even call it dashboard page shows up right here on localhost 5173/dashboard. Pretty straightforward, right? But now, let me also show you how we can add something known as a layout.

**21:29** · So within admin, I'll create a new file and I'll call it admin- layout.tsx. within it. I'll run rafce and I'll give this div a class name equal to admin- layout. Now this admin layout is coming from index.css. The only thing we're doing here is applying a bit of a light background color with some padding on the top for the navbar. And we're also making it a flex container.

**21:58** · So what we can do now is head over into routes and wrap our route with a layout. So right here I'll say layout coming from React router at the top. It's not a component but a method. As the first parameter it requires a path to that file. So I'll say forward sloutes/admin/admin-layout dsx.

**22:24** · And as the second one it requires an array of children which are different routes within that specific layout. So I'll simply put this dashboard route right within. If you do it properly without providing the starting forward slash right here, you should be able to see just the admin layout in your page even though you're currently on the dashboard route. So what you can notice is that by putting something into a layout, it doesn't mean that you have to prepend that route with that name like it is in Nex.js.

**22:56** · You can think of it more like a Next.js GS route group where the route still remains its original part, but the layout allows you to style it a bit further. So, for example, we might want to display a mobile sidebar right here or maybe like a regular sidebar. So, I'll put an aside, give it a class name of W-ful, max-W of 270 pixels.

**23:25** · typically make it hidden but only show it on desktop devices. So this is a sidebar for desktop and I'll say sidebar right here. So now on mobile we can see the mobile sidebar. But if we head over to desktop we can also see the regular sidebar. But now what matters most is showing the pages within that layout.

**23:44** · They will all have something in common which are the sidebars. Sure. But how do we show the actual page? Well, I'll render another aside which is an HTML 5 semantic element. Give it a class name of children and within it I will render something known as an outlet coming from React router. This outlet is a component that renders the matching child route of a parent route or nothing if no child route matches.

**24:12** · In simple words, it just shows you the page or the route that we're currently on that is inside of that admin layout. So for example here now this admin layout allows us to have this mobile sidebar but also the contents of the dashboard page. So if you needed to add a second route you can do that very easily. You just create it right here within the same folder and I'll call it all-users.tsx.

**24:40** · I'll run rafce and this is the page within which we'll display the users table. This will of course also be a part of the admin dashboard.

**24:51** · So now back in the routes you can just duplicate this route still within the same layout and I'll say all users and pointing to routes admin all users. So now if you wanted to, you can very easily switch over to all users and both that one and the regular admin dashboard have the mobile sidebar which we'll implement next. That's more or less it when it comes to routing. It's actually pretty simple.

**25:19** · But if you wanted to read a bit more about it, you can see that React Router is a multistrategy router for React, bridging the gap between React 18 and 19 where you can use it maximally as a React framework or as minimally as you want. So there are different ways of using it, but in the most simple way, you can create some routes and then use them as parts of different layouts as I just showed you.

**25:45** · Don't worry, we're going to dive into more depth of how we can use it later on, such as how you can create dynamic routes as well, but more or less it is super intuitive. For example, if you wanted to nest routes, you would be able to do that just by creating a single route and then adding additional routes as an array to that route. But with that in mind, you already know not only the basics, but also how to put those basic routes within the layout.

**26:08** · So, I'll close all of the currently open files, and I'll go ahead and commit this by heading over into the terminal, running git addit commit-m, and I'll call it routing. Perfect. Ready to move onto the next lesson.

### Dashboard Layout

**26:28** · Considering that most of our pages will use the mobile or the desktop sidebar, what do you say that we focus on the layout of those sidebars first and then we can focus on the pages that'll be within it. So let's start with the sidebar component. I'll first create a new folder within the root of our application and I'll call it components and then our first component will be called nav items. nav items.tsx tsx and then there we can run rafce to quickly spin it up.

**26:59** · We don't need this react import so we can always delete it. And we can also create a new component within the components folder called index.ts. We only need to do this once because from this one file, we will export all of our other components by saying export default as nav items and then from slashnav items. This allows us to very easily import all of the components within one line.

**27:28** · I'll show you how we can import it very soon, but for now, let's head over into the nav items component and let's implement it.

**27:37** · First things first, I'll focus on the layout. So instead of a div, I'll turn it into a section and give it a class name of nav dash items. Within it, we of course need to have a link coming from react router and it'll point to forward slash. This will be our primary link and it can also have a class name of link- logo. So right within this link, we can render an image.

**28:05** · So that's an img with a source pointing toward/assets/icons/lo.svg with an al tag of logo. And we can also give it a class name equal to size of 30 pixels like this. And just below it, we can render an H1 that'll say tour visto, which is the name of our application.

**28:33** · You can see that WebStorm doesn't recognize this word, so it might think that we misspelled it. But I'll tell it no, save this to dictionary because we'll be using it much more often later on. Okay, so now where can we see this nav items component? Well, we can use it within our admin layout. So head over into the admin layout and right here where it says sidebar within this aside here we want to render that nav items component but we don't want to just render it like this.

**29:03** · We want to wrap it within a Syncfusion sidebar component.

**29:09** · So I'll first render a sidebar component coming from at Syncfusion EJ2 React navigation. I'll give it a width of about 270 pixels and a prop of enable gestures equal to false because this will be our desktop sidebar and within it I will then render the nav items coming from data /components like this.

**29:34** · So you can see if we didn't have that index.ts within components then we would have to import every single component like this in a new line. import nav items from components nav items import something else from somewhere else but in this case we can just do this and now we can add additional components like com 2 com 3 all in a single line okay so

**29:58** · let's also self-close these now items and now right on top you can see that this application was built using a free trial of Syncfusion Studio so we'll have to get a valid license key and that's completely free so soon after you register serial license, that message will be completely gone. If I covered this before in the video, that's great.

**30:17** · If not, don't worry. Even if the message is still right there, we can continue developing everything and then we'll remove it later on. But with that said, let's actually expand our browser so we can see what's happening on desktop devices. There we go. Right here, we start seeing the sidebar. Perfect. And we can see this to Visto logo that basically points us to the homepage, which right now doesn't exist. So with that in mind, we can continue developing the left sidebar right here, so-called the nav items component.

**30:46** · So right below this link, let's render a div that'll have a class name equal to container. And within it, we can render a nav. That's an HTML 5 semantic tag for the nav items within which we can map over our sidebar items, which you can import over from constants.

**31:08** · So say sidebar items.m map and then you get each individual item from which we can dstructure the properties such as the ID anref an icon and a label and then for each one of these we can automatically display a new div within which for now we can maybe display just the label. So, if you do that and save it here, you can see dashboard, all users, and AI trips. But hey, where are these items actually coming from?

**31:40** · Well, if you commandclick into sidebar items, you'll see that this is a simple array of objects that I prepared before. Each one of these objects has an ID, an icon, a label, and a path that it points to. Perfect. So now for each one of these instead of a div we want to use a react router component called nav link. Of course you want to automatically import it from react router. The two path will be equal to the href or the link and we can also give it a key equal to ID.

**32:12** · Now what this nav link allows you to do is to open up a dynamic block of code and then have a callback function within it. And that callback function looks something like this. So you have the parenthesis and then an immediate return. Within the parenthesis you can dstructure the is active state. So this tells you whether the component is active. And we can also use typcript here to say that is active is of a type boolean. And now within it we can render a div within which we can render the label.

**32:43** · If we save this now all of them are exactly the same as before. But now we can use that is active state to style it further. For example, this div can have a class name equal to. And now here we want to make it dynamic. So we typically want to apply some styles. But we also want to change the styles depending on the is active state of that nav link. And for that in Tailwind we use something known as CN, short for class names.

**33:11** · So within our file and folder structure, create a new folder and let's call it lib as in library. Within the lib folder, create a new file and call it utils.ts. This stands for utility functions. Functions that we can reuse across the application that deal with specific functionalities.

**33:36** · The CN util typically comes directly with Tailwind, but you can very easily get it right here from the video kit as well. So, just copy the entire app lib utils and then paste it over into the utils right here. Here we'll have a couple of simple functions like formatting the date, parsing the markdown to JSON so we can use it, parsing the trip data which we'll use later on, and some functions that'll help us calculate the percentage later on. More on that soon.

**34:04** · The only thing we needed right now is this one tailwind merge which will take in the static and the dynamic class names. You can also notice that this utils file uses dayjs library to manage date and time. So I'll open up my terminal and I'll run mpm install dayjs. Also we can keep this library within the app. That way we have everything important stored right within it. There we go.

**34:29** · So now within this class name you can say CN and then import it automatically from the top from lib utils and pass the styles that it'll always have such as a group and a nav item class name. But now as the second parameter to the CN method you can also provide an object and say when these additional class names will be activated.

**34:55** · For example, the bg primary 100 and important text- white will only be active if the is active state is turned on. If it's not, then they won't be active. We can do a similar thing for the image next to the label.

**35:12** · So, I'll render a self-closing image tag that'll have a source of icon, an al tag of label, and a class name equal to I'll make it dynamic one more time, and I'll make it a template string this time. On group hover, we want to change the brightness.

**35:35** · So, I'll say brightness to zero, typically size of five. And on group hover, we'll also want to invert the colors. You know that effect when you kind of hover over it, the background then turns darker, but the icon therefore needs to turn lighter in order to be visible on that darker background.

**35:57** · So we can open up a dynamic block of code and say if is active is true. In that case, we can change the brightness to zero and invert. But if it's not, we can just leave the text color to dark.

**36:12** · So text-d dark 200. Perfect. So now if we check this out in action, we can see the logo on the top. And you can see that the dashboard is the currently active tab. But if you click on the all users tab, it still has the same layout because remember we implemented this page before and gave it the admin layout. The trips of course will lead to a 404, but we can now nicely switch between those two. And as you hover over it, you can see that it actually changes the background color, indicating that it'll become active.

**36:40** · So now we can switch between those two pages within our nav items. Let's also add a footer to this sidebar, sharing a bit more info about the currently logged in user. For the time being, I will hardcode the user information just so we have something to display. But later on, of course, this will be coming for real from authentication.

**36:59** · So say const user is equal to I'll give it a name of Adrian an email of contact atjsmastery.pro which is my email address and an image URL of a path pointing to assets images David.webp. I found a random David developer online. So now that we have this user, we can head down below this nav and create a new footer.

**37:30** · This footer component will have a class name equal to nav-footer. And right at the top of that footer, we can display an image with a source of user question mark. URL or if that doesn't exist, we can always point to that David thing. So forward/assets/im images/david.webp and we can give it an al tag of username. So that's going to be user question mark.name or David maybe in case the user doesn't exist.

**38:05** · Perfect. So now if you check it out you'll see this developer right here at the bottom left right below the image.

**38:11** · We can render an article. Article is like a div but it says that the pieces of content within it actually are related. So within it, we can just display an H2 that'll render the user question mark.name. And then below it, we can render a P tag that'll render the user question mark. So if you save it and check it out, you can see Adrian and contactjmastery.pro, which is the email.

**38:37** · For you, of course, it could be something different. And finally, below this article, we need to display a button through which will allow the user to log out. So to this button I'll add an on click and I'll just do a callback function and say console.log logout. Of course later on we'll actually implement the functionality right here. I'll also give this button a class name of cursor-pointer to let people know that it is clickable.

**39:08** · And then right within it, I'll display a self-closing image that'll have a source of forward slashassets slashicons slash logout. SVG with an al tag of logout and a class name equal to size of six. So now if we save this and check it out, you can see that we have a nice looking logout button. And that concludes our left sidebar. But now, what happens if we go to a mobile view?

**39:42** · We cannot really let the sidebar take that much space. So that's why we're hiding it on tablet or smaller devices.

**39:49** · So now if I actually put this to a mobile view, you'll see that this left sidebar entirely disappears and we have this new mobile sidebar that is there instead. So let's implement the mobile sidebar, too. I'll do that by heading over into components and I'll create a new component called mobile sidebar.tsx. I'll run rafce to quickly spin it up and we can export it from our components just by changing the name of the export to mobile sidebar.

**40:20** · And then we can import it directly within the admin layout. Instead of the mobile sidebar, we can just render the real mobile sidebar. coming from components. There we go. So now if you did that, you understand that we have a mobile on mobile. We have this one on desktop. And then we show the rest of the page content. Perfect. So that looks something like this. Nothing fancy yet, but it'll look much better soon.

**40:51** · In this case, we can actually see both the code and the view at the same time. So it's going to be even easier to implement it.

**41:01** · I'll start by giving this div a class name equal to mobile sidebar and I'll also give it a class name of wrapper making it act as a flex wrapper. Within it I'll display a header component and within that header we can have a link coming from react router pointing to home just forward slash within the link we can display the logo as before. So I'll say image. That'll have a source equal to assets icons logo.

**41:34** · SVG with an al tag of logo, a class name of size-30 pixels. And there we go. You can see this shortened version of the logo.

**41:49** · And then right below it, we can render an H1. That'll simply say to Visto, which is the name of the application. Of course, feel free to use something else if this doesn't look good. And then since this menu will open up, we actually need a button. So below the link render a button component. And this button component will have an on click that'll be a callback function that simply needs to collapse our sidebar. Okay. So how do we get access to this sidebar? Implementing this on our own would be super difficult.

**42:24** · sidebars and mobile navbars and whatever opens and closes. Even though is seemingly super simple, it's actually a pain in the ass to implement so it works properly across all devices. So that's why here we'll once again use Syncfusion's sidebar component, same as we did for desktop. So I'll say const sidebar of a type sidebar component coming from Syncfusion EJ2 react navigation.

**42:52** · And then what we can do is within this button we can simply say sidebar dot toggle which will actually open up that sidebar. But instead of a const for now I'll simply set it to let because for const since you cannot redeclare the variable you have to declare the value immediately. But here we really don't.

**43:14** · We can just set it as undefined at the start. You can see that our TypeScript is complaining right here because we're using this variable before being assigned. But we'll actually make this functionality work with Syncfusion's component. So for now, I will simply suppress this warning with a TS ignore which I will add right above this button as a comment. Perfect. So we are toggling this sidebar and we'll have a regular image. This is going to be a menu icon. So I'll give it a source of assets icons menu.

**43:44** · SVG with an al tag of menu and a class name equal to a size of 7. So if I save this, you should be able to see a menu icon on the right. Now, right below the header component, we can actually render this mobile sidebar. So I'll render the sidebar component coming from Syncfusion and I'll give it a width of about 270.

**44:11** · And of course we'll have to import it from Syncfusion but not just as a type which is what we have done so far.

**44:18** · We'll want to import the actual cyber component like this. So if you do this you'll see that it'll automatically be opened and it'll hide our logo. So, we'll need to give it a ref. A ref where we have a function of sidebar. And then we'll make this sidebar equal to the sidebar object that we created above.

**44:39** · I'll also add a ts ignore right here just so we don't have any typ warnings.

**44:44** · Next, we can give it a created property.

**44:47** · So, once this sidebar component gets created, what we want to do is automatically hide it. So, I'll say sidebar.hide.

**44:55** · Looks like our TypeScript will complain here a bit as well. So what I'll do is remove these TS ignores. And just at the top of the file, I will add a TS no check directive, which will make sure that no TypeScript errors show for this file. Then we can also say close on document click. This is very important to turn on for mobile sidebars because if you click on a specific element in between the sidebar, we want it to also automatically close.

**45:21** · We can also render the show backdrop to true which will give it a bit of a background right here. And then also we can give it a type equal to over because it's showing over the content. And now the only thing we have to do is pass over the nav items component we have created before for the regular sidebar and it'll also work here as well.

**45:45** · So just import nav items coming from nav items and you should be able to see the full desktop sidebar also works incredibly well on mobile but now it also has some behaviors of a mobile sidebar such as you can click outside to close it. Still when you click on a specific element it doesn't actually collapse itself so you can see the page you're on even though it actually does the redirect. You can see we're in the user table but we cannot really reopen it anyway. So, there's definitely some more improvements we have to make to it.

**46:17** · One thing is taking this sidebar toggle outside of this direct click and turning it into a new function. So, we can pass it over into the nav items themselves.

**46:28** · So, I'll simply copy this sidebar toggle and call it toggle sidebar. So, now right at the top I can say const toggle sidebar is equal to a callback function within which we can just toggle that sidebar. Now we're calling it right here on button click, but I'll also pass it as a prop over to the nav items. So I'll say on handle click toggle the sidebar.

**46:55** · So now we can head over into the nav items and we can accept this handle click as a prop which will be of a type handle click a function that returns void meaning nothing and it'll also be optional. So now we can use this handle click when we're clicking something right here. So I'll pass it as the on click to this nav item div right here where we have the classes. I'll also add an on click and I'll say on click handle the click.

**47:28** · So what this should do is when you click on a specific link, it should actually collapse the dashboard.

**47:34** · Oh, I see it doesn't do it just yet. I think I know where the issue is here.

**47:39** · when we give it a reference, I should actually be making this sidebar object coming from Sync Fusion equal to the ref, not vice versa. So, what we need to do is switch it around. So, the sidebar object will be equal to the sidebar ref.

**47:54** · If we do this, you can notice that now it actually closes and you can reopen it. Perfect. We now have a mobile nav that allows us to navigate in between different pages. So the last part of the layout that is shown across all the pages, can you see what it is? We have the sidebar. We have the mobile sidebar in mobile. But what is that other element that also appears across all of the different pages? Well, it's the header. See, with a title, subtitle, and potentially an action button allowing us to do something for that specific page.

**48:28** · Almost every single dashboard has this.

**48:30** · Oftentimes it is also called breadcrumbs because it tells you on which part of the dashboard you're on such as admin users or this could be admin trips. But in this case since our dashboard is pretty simple we just have a title subtitle and an action button. So let's implement it as well by creating a new component in the components folder which I'll call header.tsx tsx run rafce and for now I'll just add it to the top of the dashboard page.

**48:59** · So right here we have the page contents but we'll wrap everything in a main. So this is the main page with a class name equal to dashboard and we'll also give it a class name of wrapper. Within it we'll display the header component coming from components header. See this is what I was telling you about. If you don't export it from this components index, then you'll have to have a new import for every component.

**49:27** · But if I came in here and just exported it right here as header coming from header, in that case, you would just be able to import it like this by saying import header from components. Again, doesn't make a big difference now, but as you start importing more components into the file, it really makes your code that much cleaner.

**49:51** · This will be a self-closing component.

**49:53** · And we immediately know that we'll have to pass different props to it such as the title and the description. So title for now can be something like dynamic template string that'll say welcome. And we can say maybe if a username exists. So I'll create a new user right here. const user is equal to an object that has a name of Adrian.

**50:19** · Of course, you can put your own name there and we'll say welcome if user question mark.name name exists then use the name else just say guest and we can also render an emoji of a wave right here at the end near the title will also render the description equal to we can

**50:41** · do whatever we want to say here but maybe something that explains that page we're on such as track activity trends and popular destinations in real time perfect now copy this header And we can also add it over to our second page, which is the all users page. As a matter of fact, we need to do the same thing right there. Give it a main, a class name that says dashboard and wrapper. Then we can render the header right here.

**51:14** · This time we won't say welcome. We can say something like trips page like this. And then the description can be something like track users for now. Of course, we can actually modify it later on or not track users. That's a bit too creepy. We can say something like check out our current users in real time. And of course below that we have the actual page contents.

**51:42** · So this will be the all users page contents. And then on the other one that was the dashboard, we'll instead say dashboard page contents. Perfect. So now if we actually head over into our app, you'll see that we have the header and we have the dashboard page contents. And if I move over into all users, we have the header, all users page contents. But now we have to dive into the header component and accept those props to show the differences in between those pages.

**52:13** · So I'll immediately accept the title and the description. We can actually define this as props. So we can define an interface of props right at the top that'll have a title of a type string and a description of a type string as well. So now we can display the header component with a class name equal to header.

**52:42** · Within it, we can have an article because it contains two related pieces of info. Within it, we can have an H1 that'll display the title and below it, we'll have the P tag that'll display the description. If you do this, you can now see trips page, check out our current users. But if I head over to dashboard, you can see welcome Adrian, track activity, trends, and popular destinations in real time. Great. Of course, the only thing remaining for us to do is to style it a bit better.

**53:11** · So, let's do that by giving this H1 a class name equal to text-d dark 100. And we actually want to make this a bit more pronounced. If we're on the homepage, see here, it shows up right here at the top. But on dashboard, we want to make it a bit larger. So, for that reason, I'll wrap this in a dynamic CN class name like this. And we need to properly close it as well. So the text dark 100 will always be there.

**53:42** · But if the URL is homepage, then we'll apply some different class names. And how can we do that with React router V7? How can we figure out the path? Well, it's super simple and very similar to Nex.js. I'll just say con location is equal to use location hook. That's it. You import it from React Router and you know the URL.

**54:06** · Oh, and let's not forget to import the CN as well from utils. Okay, so now next to this default style, we can also check if the location.pathname is triple equal to forward slash. And if that is the case, we can give it a text of 2 Excel. On medium devices, text of 4 Excel and font-bold. But if we're not on the homepage, we can give it a text of Excel. on medium text stuff 2XL and font- semi bold.

**54:36** · Of course, we have to properly close this now. So now, if you compare the differences between this header size and this one right here, you won't be able to notice the difference.

**54:48** · That's because all of these are not on the homepage. This is dashboard and the other one is all users where these ones need to be the same to have enough consistency in between the pages. But I'll also teach you how to reuse this header on our public facing website.

**55:05** · Whereas we want to make it much much larger. So that's where the difference will be. But for now, we can also copy this H1 and paste it below. But change it to a P tag for the description. This one will be text gray of 100 and font normal by default. But if the path name is forward slash, it'll have text-base. And on medium devices, text-LG and we don't need this font bold.

**55:35** · And if it's not on the homepage, we'll make it a bit smaller and give it a text-s as well as on medium devices text-l. And within it, instead of the title, we'll display the description. So now we have a proper title and description right here. So, this is already looking great on mobile. We have a fully functional mobile sidebar and it's starting to take the shape of the final application. Of course, where dashboards truly shine is on desktop where we have more screen real estate.

**56:07** · So, we can see all of the different stats, charts, tables, and charts. So, what do you say that we focus on the main dashboard page contents next? Okay, the primary layout is done.

### Admin Dashboard UI

**56:21** · So let's focus on the content displaying what matters on the page. I'll collapse it for the mobile view and mobile first development is taking over anyway. So it's always good to start developing for mobile and then expanding over for desktop. Although I would say there is one exception to that rule and that is dashboards. Dashboards are typically meant to be viewed on desktop. So prioritize proper desktop views. Okay.

**56:47** · So, let's focus on creating the UI of these trip cards right here to have something nice to display on the dashboard right off the bat to the user.

**56:56** · So, let's develop a reusable trip card layout. But you know what? Before that, let's start from the top, let's focus on the stat card layout, the one that has a nicel looking chart and displays some information. I'll do that by creating a new component right here in the components folder. And let's call it something like statsc card.tsx run rafce. And while we're here, we can also create another card. This one will be the trip card.

**57:28** · So I'll create a new trip card.tsx. Also run rafce and just display it right here. What we need to do, of course, is export them both from the index.tsx. So that's going to be the stats card as well as the trip card.

**57:49** · Perfect. So now we can head over and import both of them within the dashboard so we can start implementing them. I'll first head over into our routes dashboard and right below the header I'll display the trip card coming from trip card components and right on top of it I'll also display a stats card coming from components. So now we can see that we have a stats card and a trip card.

**58:19** · We first have to ask ourselves what will each one of these stats card have? If you already have a design, well then you have everything you need. Take a look at these cards and ask yourself what is different about them and what is the same. The regular card layout is the same, the background, the borders and everything. But what is different is the title, total users, total trips and so on. The number of course the value, this up and down stat is different value.

**58:49** · And then we also have the chart itself. So these are the different pieces of data that we have to pass into it. So we can start by forming that for now fake data but later on we'll make it real once real users start creating the trips and they start joining the platform. So for now I'll say const dashboard stats is equal to and I'll create a stat for total users.

**59:15** · And actually doing this is a pretty good idea. Starting to create everything static from regular JavaScript objects.

**59:23** · So if you do this and maybe define 12,450 users as it says on the design right here, technically what you're doing is creating a structure for your future database. You now know that you have to store this field in the database and that it'll be of a type number. We can do a similar thing for users joined which in this case can actually be an object where you keep track of the current month maybe like 218 and the last month.

**59:54** · That way you can compare that data. So last month I'll set it maybe to 176. This will allow us to have this nice looking chart right here. After that we can render the total trips card.

**1:00:10** · maybe 3,210 and then we can also have the trips created. So this will be for the chart where we can have the current month data maybe like 150 and the last month data maybe like 250. Let's say there were more that month. And finally we need to know how many active users do we have. So I will say user role we have a total of about 62.

**1:00:34** · Maybe current month maybe let's say there were 25 and last month let's say there were like 15. So we're growing very fast.

**1:00:48** · Perfect. So this is some fake data that we can now pass over into the cards. So let's focus on the stats card first.

**1:00:56** · Below the header I'll create a section.

**1:00:59** · And this section will have a class name equal to flex flex- call and a gap of six. So we can display all of them one next to another. Within this section, I'll create a div that'll have a class name of grid. So specifically the grid for the stats card where we want to make it have only one column. So calls one.

**1:01:26** · On medium devices, we want to have three columns. So, this will be on larger devices. And then a gap of six in between the cards and a full width. And right within it, we can display our first stats card. So, I'll say stats card self-closing. And we can already start figuring out which different types of props do we have to pass into it. So, I already told you that we'll need to have the total users, right? So that's the title header. Title is total users.

**1:01:59** · Next, we can pass the actual amount which I'll call the total.

**1:02:06** · So this will be equal to dashboard stats dot total users. We'll also need the current month count which will be equal to dashboard stats dot users joined dot current month. And then we can do the same thing for the last month. Count is equal to dashboard stats dot users joined dot last month.

**1:02:35** · And we can maybe dstructure this dashboard stats just so we don't have to repeat ourselves every time. So I will dstructure the total users and users joined from the dashboard stats by saying const total users users joined total trips trips created and user ro equal to dashboard stats.

**1:03:02** · So now if you head here you don't have to explicitly say dashboard stats for every single one of them. You can just refer to total users and users joined. Perfect. So now we can very easily duplicate this card two more times. For the second one, instead of total users, we'll have total trips. So we can pass the total trips. And instead of users joined, we can refer to the trips created. And then for the last one, we can talk about just users.

**1:03:30** · So we can say user rot total. And then here we can say user rotc current month and last month. So if you head back over to your application, you'll see that we still have just three empty cards, but now we're passing the right data to them. So it'll be super simple to take that data and display it.

**1:03:55** · The only thing we have to do is head over into the stats card and implement its layout. Of course, starting with dstructuring all the props that we're passing into it. such as the header title, the total, the last month count, and the current month count. These will be of a type stats card.

**1:04:17** · So what you could do is you could either define an interface right here of stats card and then say what the header title will be, what the total will be and so on. Or you can do what I did right here, and that is to define the stats card within a special file called index.d.ds, which allows you to declare interfaces, which can be used across your entire application without needing to import it.

**1:04:48** · So here we're saying that the header title is a string, the number is the total, last month count, and current month count are both numbers.

**1:04:58** · And that's it. It just immediately knows that the header title is a string.

**1:05:02** · Pretty cool, right? So now that we have that card, we have to take the last month and the current month count and get some useful data out of it such as figure out what is the trend. Is it increasing or is it decreasing? This will be useful for us to figure out the color of the chart and then also by how much has it decreased since the last month. And this is actually a pretty interesting challenge if you want to work on it.

**1:05:26** · What I'll do is say const dstructure something and make it equal to the call of the calculate trend percentage. And to it I'll pass the current month first and then the last month second. And this calculate trend percentage will give me exactly what I need which is the trend and the percentage. Now how does this calculate trend percentage work and where is it coming from? Well, I declared it within the utils function. It's a utility function, but of course, I invite you to implement it on your own.

**1:05:58** · This is a great type of function that chat GBT excels at. You give it a very small task such as to give you a trend and a percentage. You say what the inputs are such as the count this month, count last month, and then you tell it what you need to output. So in this case, it says if count of last month is zero, then there is no change. So what is it doing is it's taking a look at the difference.

**1:06:26** · It's grabbing the percentage of that difference and then if the change is greater than zero it returns a trend of increment and a percentage. If change is lower than zero then a decrement percentage and if there's no change it just returns zero. Makes sense right? So once we get that trend, we can then say const is decrement is equal to and that's going to be equal to trend is equal to decrement.

**1:06:52** · What we're doing here is we're just checking for equality and then turning that equality into a boolean variable so we can more easily use it within the card. So now that we have all the necessary data we need in order to implement the layout of the card, let's actually do it. Cards are typically articles. So, I'll use this article and give it a class name of stats dashcard, which will automatically give it a white background and a bit of a shadow.

**1:07:20** · If at any point you're wondering which styles are being applied when you add a specific class name, you can commandclick into it or just search for it across the codebase until you find it within the app.css. You will see that we're giving it some padding, making it a flex container with a gap in between the items, giving it a background, a shadow, bit of a rounded corners, and a dark text.

**1:07:44** · Next, right within this article, we can render an H3 that'll have a class name equal to text-base font- medium, and it'll render the dynamic header title. So now each one of these says a different thing.

**1:08:02** · total users, total trips, and then total users. Once again, that's because I forgot to change the last one. So, if I head over into the dashboard, yep, you can see here I left total users, but actually it was supposed to say active users today. Perfect. So, now we have three different cards or just active users is fine.

**1:08:29** · So now we are ready to start implementing the rest of the stats card.

**1:08:34** · Right below the H3, we can start focusing on the main content. So I'll wrap it in a div with a class name of content. And within that div, I'll create another div with a class name of flex flex- call and a gap of four in between the elements within which we can start rendering an h2. That'll render the total number.

**1:08:57** · So now we have the number, but to make it look a bit better, we can give it a class name of text-4xl and font- semibold because the total number is more important than the title. You need to see those numbers very clearly. Right below this H2, we can render another div that'll have a class name of flex items center and a gap of two. And within it, we want to render a figure.

**1:09:26** · This figure will contain the percentage as well as the arrow pointing up or down. So right here I'll give it a class name equal to flex items center and a gap of one. And within it I will render an image with a source equal to it has to be dynamic. So I'll open up a template string and point to assets icons and then if it is decrement I will render the arrow down red.

**1:10:02** · SVG else I will render the arrow up greens SVG and I'll also give it a class name of size of five and an al tag of arrow. If you save that you should be able to see up down up which matches our

**1:10:19** · data and right below that image I'll render something known as a fig caption which is basically just a p tag within which I'll render the math.round And within it, I'll pass the percentage and then add the percentage sign right after it. So you can see it says 25% up, 40% down, 67% up, or something different for you if you used different numbers.

**1:10:45** · Let's also style that text a bit by giving it a class name. I'll use a dynamic CN class name.

**1:10:53** · It'll always have a text small and a font medium. But if it is decrement, then it'll also have a text red of 500.

**1:11:06** · Else it'll have a text success of 700.

**1:11:10** · So now you can see that the number also matches the color of the arrow. And then outside of this figure, I'll also add a bit of an explanatory P tag that'll say versus last month so we know what this number is referring to. Let's make the text a bit smaller by giving it a class name of text-s font- medium and since it's not so important text gray of 100 and truncate. So if it's too long, we can just remove that part because it's clear what it is referring to. Great.

**1:11:41** · And now we can head over below this B tag and below two more divs and we can render an image. This image will have a source of forward slash assassets slash icons forward slash dynamically we can check if we are in the is decrement and in that case we'll display the decrement.svg else we'll display the increment. SVG.

**1:12:10** · So if you save it, you'll be able to see those different charts. Now a challenge for you and something that we can look into later on would be to actually make these charts functional using a library like charts.js or something similar. For now, the most important thing for me is to display the value and the trend. And making this real is a beautiful challenge for you to try out. So, you might want to check out Syncfusion's chart components because they have a lot of functionalities that allow you to very easily display that chart data.

**1:12:40** · But for now, let's also style it a bit more by giving it a class name of on extra-large devices W of 32. Typically, W full H full on medium devices H32 on extra-large devices H full. And I'll give it an al tag of trend graph. So if I save this, they're now a bit larger.

**1:13:08** · And if you check out the desktop version, this is looking exactly like it does in the design. Pretty cool, right? And later on, this will be super functional because you can make these cards clickable. So it actually points to a page where you can show more details about those users like active users and total users can point to the old users page and total trips can point to the AI trips page where you can show more details on the trips. But for now let's focus on implementing the trip card.

**1:13:38** · This will bring so much more life into our dashboard because each one of these trips will have its own thumbnail.

**1:13:46** · So let's collapse it. So now is the time to implement that trip card. Before we start implementing the UI, we'll have to figure out the data for those components. And similarly, how in the dashboard, we rendered some fake data for the dashboard stats, which soon enough will be imported into our real database. We need to have the data for the trips. So, I prepped some fake data for you right here so we can very easily get going. It'll be right here under all trips dummy. And you can see that here we have all the trips.

**1:14:16** · So let's simply import it and paste it right here at the top. It doesn't have to be within the component. As a matter of fact, I'll also pull these outside of the component because this is just fake static data which later on will be converted over to be real database data. And I'll paste it here. You can see that each one of these trips has an ID, a name, image URLs, the itinerary with different locations, tags, travel styles, and estimated prices.

**1:14:48** · But it's never a good idea to keep static data right here within the JSX file where we're trying to do some logic or represent some UI. So, what I'll do instead is I'll copy these trips user and dashboard stats and I'll move them over to the bottom of the constants file. So, this is the constants index.ts and I'll paste the dashboard stats, the old trips and the user data.

**1:15:19** · I think later on we'll also have the users data. So, I'll copy it while we're here and also add it here. So we have some fake users. This one uses the format date functionality. So make sure to import it from lib utils. There we go. This is only to help us focus on the UI. But very soon we'll be pulling all of this data directly from the database.

**1:15:41** · And you can see there's no more snippets to copy. Everything else in this entire application will be done entirely by us together. So let's make sure to add an export statement at the start of each one of these lines. And we can import it right here within the dashboard. So I'll say import dashboard stats from constants. Also the user and also what else do we need? I think it's going to be the all trips. So we can render the cards for each one. See how clean the file is.

**1:16:11** · And we can even pull this dstructuring right here. So we have nothing in the component. We only have the JSX. So now below the stats card, I'll actually just hide them for a second. I'll display a whole another section. Right below this section that shows the stats cards. This one will be another section that has a class name equal to container. And it'll also have an H1 that'll have a class name equal to text- Excel and font- semibold as well as text- dark 100.

**1:16:45** · And it'll say created trips. So now right below it, we can render a div that'll have a class name equal to trip-grid. And keep in mind, nothing is showing up right here besides this trip card, which we can remove.

**1:17:03** · But now within here we can use that dummy trip data by saying all trips coming from constants dots slice which means that we can only get maybe the first four trips and then we can map over them by getting data for each one of these trips and then for each one of them we can automatically return a new trip card like this.

**1:17:30** · So if you save it, you'll now see four different trip cards to which we can pass all of this trip data. So I'll give it a key since we're mapping over it of trip ID. And as a matter of fact, we can dstructure those properties from the trip. So I'll dstructure the ID, the name, image URLs, itinerary tags, and the estimated price. All the info that we need. And now we can very easily pass it over as props into the trip card. So the key is just ID.

**1:18:02** · The ID will be equal to id to string because typically when you store ids in databases they can be of some other data type not necessarily a string. We can get a name equal to name image URL equal to image urls zero. So we're going to take the first one. The location can be equal to itinerary question mark.0ero.

**1:18:31** · So if it exists get the first one and then get its location or if it doesn't exist maybe display an empty string like this. For the tags about the trip display the tags and for the price display the estimated price. Perfect. So now we're passing all of these important props into the trips card. So, what do you say that we go ahead into it and we accept them and we start implementing that card? It won't be that tough, trust me. Maybe even easier than the stat card. The data is what matters.

**1:19:00** · For now, it's static, but soon users will be able to create it using Gemini so that the trips contain real suggestions on the trips where your users want to go. So I'll dstructure that data such as ID, name, location, image, URL, tags, and the price. All of these are of a type trip, card, props. And now we can make each one of these cards a link coming from React Router. Why?

**1:19:31** · Because we want to be able to see the trip details once we click on it. This link will render an image with a source equal to image URL and then alt tag can be the name of the trip that they're going to. If you save this, you'll be able to see four dummy images. For me, there are four of the same images right here, but for you, I might change it up a bit and actually put different ones. But of course, what matters more is that each one of these cards will actually point to a real trip details page.

**1:20:03** · So let's actually add a two-part and we have to get access to the current path. So right here it's very similar to how we do it in XJS const path is equal to use location coming from react router. Then we can check whether we're clicking on this card from the public facing website or from the admin dashboard because depending on that we're going to link them to a different page.

**1:20:33** · So I'll say if path.pathname is triple equal to forward slash meaning public facing or path.pathname dot starts with forward sltra that still means that they're on the public facing website. In that case we'll point them over to travel and then the ID of that trip.

**1:20:59** · else will point them to trips forward slash ID. Why? Because for the admin, we want to display the details of that trip. Whereas for the person, we just want to show them the trip that has been created. Let's close this properly. And if you click on it right now, you'll get redirected to a 404. So don't do that just yet. But with that said, let's continue adding more data to this card.

**1:21:23** · I'll give this link a class name equal to trip-ashcard which will kind of collapse it a bit. Next, right below this image, I will create an article that'll contain most of that cards or most of that trip's data such as the H2 that'll render the name of the trip.

**1:21:42** · Maybe also a figure. In this figure, we'll contain an image that'll have a source of assets, icons, location mark.

**1:21:54** · SVG with an al tag of location, and a class name of size of four. That's much better. Now, why do I use figure? Well, if you have an icon that is related to a specific text, then you might want to put them into a figure and put a figure caption like this instead of a paragraph. It's just better for screen readers and overall usability. So now we can see that this is New York, Paris, Tokyo, and so on.

**1:22:25** · Next, we can exit out of this figure and the article as well and create a div right below it. This div will have a class name equal to margin top of five to divide it a bit from the top. A padding left of about 18 pixels like this. Padding right of about 3.5 and padding bottom of about five. So we're creating space to display some tags right here. And for the tags, I'll use a Syncfusion chip component. So I'll just start typing chip list component.

**1:23:01** · I'll give it an ID of a travel chip and within it we can display the chips directive component and these one will look something like this. You have different styles like simple choice chips, filter chips, dynamic chips. It is super customizable within it. We can map over our tags by saying tags.m map where we get each individual tag and the index of that tag.

**1:23:24** · And we'll render a chip directive, not chips directive, this time without the s as a self-closing component that has a key equal to index. It has a text equal to get first word of a tag because tags can contain multiple words. You have to import this from utils. Basically, we just trim it out, split it and render the first word.

**1:23:52** · And then we can also provide some CSS class to it to style it further. And I'll say CN from utils. If index is triple equal to 1, then give it a bg 50 and you have to add an exclamation mark in front to make sure that the style is applied as well as text pink 500. else give it a bg success of 50 and a text success of 700 and save it.

**1:24:25** · So now you'll see that we have different colors for those two different tags.

**1:24:34** · First one maybe New York is about adventure and culture. Paris is relaxation culinary and so on. Finally, we can head below this div that's wrapping the chips and render the article that'll contain the information about the price. Of course, we can style it a bit better by giving it a class name of trip card dash pill. And this will just make it a pill that's going to show up on top of this image right here on the right. Looking great.

**1:25:01** · Also, I automatically added some images right here to match what you're seeing on your screen right here. And with that, we're done with the trip card. But of course, it looks even better on desktop where we can see all of these cards. Later on, we'll be able to visit them as well, but you get the idea. We can see the latest trips that the agents within our travel agency are creating. So now we have a beautiful layout, but with fake data.

**1:25:25** · So the next obvious step is to implement the full functionality for our application including authentication allowing users to add real trips storing it all within the database and then displaying it right here on the dashboard as we are right now but with the real data to get started adding functionality to our application and some persistent storage.

### Appwrite Setup

**1:25:52** · We'll use AppRight, an open- source platform that allows you to create your entire backend within minutes. In this course, we'll use it for their databases, storage, and authentication functionalities. So, click the link down in the description to be able to follow along and see exactly what I'm seeing and then create your account. As you can see, I already have quite a few projects running on AppRight. So, let's create another one.

**1:26:16** · I'll call it JSM Travel Agency dashboard. You can do something similar.

**1:26:23** · Click next. Choose a region and your project will be created. Within here, we'll need to grab a couple of IDs and store them within our application. So, I'll collapse my browser so I can see my code editor 2, and I'll head over into myv.local, which is where we can add those apprite keys. The first one I'll add will be a vit apprite project ID and that'll be equal to this key that we can copy right from here.

**1:26:49** · I'll add a comment that right here these are going to be our apprite keys and then above we have some coming from Syncfusion. Perfect. Now here it's asking us how do we want to integrate our application and I'll say that we want to integrate it with the server using an API key. So if you click right here, you'll be able to choose your API key name and give it access to all the scopes. That'll give you your API key secret.

**1:27:19** · So copy it and create a second variable of vit apprite API key and paste the one that you just copied. Now head over to databases and create a new database. You can call it anything, but I think travel is suitable right here.

**1:27:39** · As soon as you do that, you'll be given your database key. So, also save it.

**1:27:44** · I'll call it vit apprite database ID and just paste it right here. Within it, we'll be able to create additional collections within our database. So, you can create our first collection and call it users, which will allow us to authenticate and store those users right within our database. As soon as you create it, you'll be able to copy its ID as well. So I'll call it vit apprite users collection ID and paste the key that I just copied. And we want to repeat the same thing with the trips.

**1:28:19** · So I'll create another collection called trips and create it. And I'll copy its ID. So I'll create another one called vit apprite trips collection ID. And you can paste that one as well. Now each one of these two collections has to have some fields within it. So first let's head over into the users collection and head over to attributes. So we can start defining how our database structure will look like. So let's ask ourselves what does every single user need to have?

**1:28:51** · Well, they'll need to have a string that is a name. So they need to have a name and we can make it a size of well we could do something like 20 characters and make it required. Alongside the name we also need an email. So we can create another field of email. I'll call it email and I'll also make it required. Alongside the name and the email, we'll also need an account ID. So create a new string of account ID.

**1:29:20** · Make sure to put the I in ID uppercased because this will be case sensitive. And we can make it about 1,000 characters just to stay on the safe side. And I'll also make it required. I'll also create another string for the image URL attached to that specific user's profile photo. And I'll make it a,000 characters. Should be enough. I won't make it required this time as maybe some users don't have a profile photo.

**1:29:49** · And I'll also add a date time of a type date time. And I'll call it joined at. So when did this user join? And I'll make it required. Next, we'll add a more complex type called an enum. So this is basically a string, but it can only be made up of a couple of different values.

**1:30:11** · I'll call this enum a status. So each user can have a status or you can also call it a type, but I'll stick with status right now. And it can either be user or admin. So you can add a comma after each one to actually add it as an element.

**1:30:30** · Then I'll pick the user as the default value. And I'll create it. That should be it. And finally head over to settings of the user collection. Scroll down to permissions. Click plus and select any.

**1:30:46** · and then select all the permissions right here so that everybody has all the permissions just so we don't get blocked because we don't have the necessary update permissions. Perfect. So now we'll be able to create different users that have all of these different fields. Next, let's create some attributes for the trips. So head over to trips collection attributes and create a first attribute.

**1:31:09** · I'll call it trip detail. We don't need the s at the end. I think trip detail will be fine. I'll make it a big size, like very big. I'll go with maybe 10,000 characters, just so we can have the entire itinerary, details, budget, and everything right there. And I'll make it required. After that, I'll create another string. Call it image URLs. Give it a size of about well, let's do 5,000.

**1:31:37** · Since these URLs can be large, I won't make it required, but I will make it an array to indicate that this is an array.

**1:31:43** · I'll also create a dated time like before called created at so we know when specific trip was created and I'll make it required and I'll also add a URL which will be a link to the stripe payment. So I'll call it payment link and I won't make it required. I'll also add a user ID which will be a string so we can connect the user with a trip. I'll give it a size of about a thousand characters. Perfect.

**1:32:14** · So now you should have image URLs which is a string array.

**1:32:20** · You should have trip detail which is a required string. You should have a created ad property which is the required date time, a payment link of a URL and the user ID which is a string.

**1:32:32** · Now head over to that collection settings. Scroll down to permissions.

**1:32:37** · Select any and give it all permissions.

**1:32:39** · Perfect. That's it for our AppRight setup. Very soon, we'll be able to use all of these functionalities such as the API integration, the AppRite project itself, as well as the database collections, and even authentication.

**1:32:54** · But the next step into making all of this work is connecting our authentication. And we'll do that using Google. So for that, we'll need the app ID and the app secret coming from Google. So you'll have to head over to console.cloud.google.

**1:33:11** · google.com. Head over to projects and create a new project. I'll name it something like JSM agency dashboard and create it. It'll take a few seconds for it to get created. And then you'll be able to open that specific project. Then where you have the search, you can search for clients. Here you'll be able to see Google O platform. And before you click get started, head over to branding and then click get started. Here you'll be able to choose your app name.

**1:33:41** · So you can do something like JSM travel agency and you can enter your email for support. You can choose external for the audience and then you'll have to provide an additional contact info address and create it. Once you create the OOTH config, you'll have to head over to clients and create a new client.

**1:34:05** · Select web application as the application type and you can call it something like JSM travel agency and add an authorized JavaScript origin. Here you can do something like http col// localhost 5173 and you can click create. Later on, we'll need to update this with the URL of our deployed application. What matters most right now are the key and the secret that will just pop up. So, copy the key first.

**1:34:36** · Head back over into Apprite and provide this app ID that you just copied as well as the client secret which you can paste in the second step.

**1:34:46** · Then copy the URL at the bottom of apps card and click update. This will say that the Google authentication has been updated. And then head back over to Google. Click edit on this client and add an authorized redirect URI by pasting the apprite redirect URI that you just copied and then click save.

**1:35:06** · Now, another thing we have to do on Google to be able to retrieve Google profile photos is to search for Google People API. It's this one right here. And enable it.

**1:35:19** · This will allow us to extract the profile photo from every user. Perfect was a lot of setup. I know. But now we prepared ourselves to handle authentication and we have also set up everything regarding apprite. So we have very seamless development time from now on. So in the next lesson, let's implement it within our codebase.

### Auth Functionality

**1:35:42** · To get started implementing our backend system, I'll head over into our terminal and just run one simple command. MPM install appite. We'll use it to handle our back end. It got installed in a couple of seconds. And now I'll head over into ourv just to add one more environment variable which I'll call vit apprite API endpoint. We can add it right here at the end. And this is something that is the same for every single apprite project. So I'll set it to https col/cloud.apprite.io slashv1.

**1:36:19** · This is where the cloud version of apprite is hosted. So our app needs to know it so you can hit those proper endpoints. Now we'll need to set it up. So I'll check out this documentation that is very simple. It guides you through everything we have done so far. But then it asks you to set it up from within the code.

**1:36:38** · So to get to this page, you can just head over to Appra documentation quick start for React and scroll down to the part where we have the code. Perfect. So it says to create a new file under lib apprite.js and add the following code to it. But instead of just copy pasting what we have here, we're going to write it together from scratch. That's what you're watching this video for anyway, right? to learn how to do things properly from scratch.

**1:37:04** · So, back within the code, let's head over into our file explorer and head into app, create a new folder within it called apprite. And within the apprite folder, create a new client.ts file where we'll set up the app client. Here we'll first get access to all of the apprite variables coming from constants and then we'll export them so we can use them from within the rest of our application.

**1:37:33** · So export const apprite config is equal to an object where we're going to have the endpoint URL set to import meta.env\_apprite\_i env\_apprite\_appi endpoint. And now we can duplicate this a couple of times because we'll need to change it for different things.

**1:37:59** · The second one will be the project ID and then of course we'll have to change it to vit apprite project ID. After that we'll need the API key which will be vit apprite. You can guess it API key. After that we have a database ID and then we'll point it to database ID. After that we have the user collection ID pointing to V appride users collection ID.

**1:38:30** · And finally we have the trip collection ID pointing to V appride trip collection ID. Let's just make sure that we have called them properly. Trips, trips, user, user. It has to be the same. So if you open up your envir users plural as well as trips plural as well. So make sure to spell it properly otherwise the app will not work.

**1:39:02** · So you have to do this very carefully. What you can do is maybe a global search for the entire thing. You can do that with control or commandshift F and it should search it across the entire codebase. So I can immediately see that this one matches. This one matches as well. Database ID is here as well. I can see it here. This one matches as well. Apprite API key is there. Project ID is here. And API endpoint is here as well. I think I should be good.

**1:39:30** · Now that we have this entire configuration, we can say const client is equal to new client coming from apprite. So new app client and on it we can call a method called set endpoint to which we can pass over the app right config endpoint URL and I'll also call the set project to which I'll pass the app config dot project ID.

**1:39:57** · So this way this app right client knows exactly which project and endpoint we're working on. After that, we'll have to set up additional appre functionalities such as const account to manage user accounts. We'll be equal to new account. Make sure to automatically imported from apprite at the top account and client from apprite to which we'll pass this client that we have above.

**1:40:28** · I'll do the same thing for the database.

**1:40:31** · So con's database is new databases coming from apprite and to it will pass the client and con storage is equal to new storage also coming from apprite. Make sure to import it at the top and I'll pass the client. So now that we have the general apprite client as well as these three additional functionalities, we can just export them from this file so we can use it within other files.

**1:41:01** · Client, account, database and storage. Perfect. So now that this implementation is done, the next step will be to implement authentication.

**1:41:15** · There are two different approaches we can take right here. The first one would be to focus on the layout or the UI first like what we have been doing before and the second one would be to first implement the functionality. In this case we have Google O connected to apprite o and then later on we can very easily do the UI. So what do you say?

**1:41:36** · Let's do the harder thing first. Back within our codebase I'll create a new file within the apprite folder which I'll call o.t RTS here we'll create all sorts of different methods that allow us to handle authentication starting with of course the login. So all of these different methods will start with export const because these functions will be used from within our front end. So I'll say export const login with Google.

**1:42:12** · It'll be equal to an asynchronous callback function. that'll have a try and catch block. In the catch, we will simply console.log that error and that's going to be it. Now, we'll have all sorts of different functions that'll follow this same exact structure. Export const async function with a try and a catch block where we console log something.

**1:42:38** · So, what do you say that we automatically duplicate it a few times and then rename it for all sorts of different functions that we'll need?

**1:42:46** · I'll do it a couple of times and then we can start renaming them. So, we have login with Google. Of course, we'll also need a log out user to log them out.

**1:42:58** · Next, we'll need to get the user. This is to get the user profile. We'll also need one to get the Google picture, their profile photo, and we'll also need one to store the user data into the database once they first log in. So, store user data. And if I'm not mistaken, we'll also need one to get the existing user if they existed before.

**1:43:25** · Right now, how did I know that we'll need all sorts of these different functions? Or the other question is, how can you know when you're just approaching this project? The answer is you can't. I actually took the time to build this application beforehand so I can teach it to you properly. If you were building this for the first time, you would just start with one massive big function and you would start noticing that that function actually is getting too big and it's doing too many different things. With proper code, one function should have one job.

**1:43:55** · So as soon as you start noticing that it's starting to get more jobs, you separate it into other functions. Okay. But with this in mind, we can start implementing these one by one. Starting with the login with Google functionality. Here we want to leverage apps functionalities that we have exported from the apprite client file.

**1:44:19** · such as for login with Google, we want to leverage the account functionality coming from apprite client specifically the create oath to session method that accepts a couple of different parameters. The first one is the oath provider. So I'll say oath provider.google. That's going to look like this. And as the second parameter, we have to provide the success URL. And as the third one, the failure URL. But all of these are optional.

**1:44:51** · So I think if we just leave them empty for now, we should be good. What provider Google and you might need to import this oad provider coming from apprite. Perfect. Believe it or not, this is it to log in the user. Now for each one of these errors, in case you want to make them a bit more descriptive, you can say before the error itself, you can render a string with the same name as the function. So you know exactly where that error is coming from. Great. So login with Google is done.

**1:45:22** · But once we actually log the user in, we might want to focus on getting that user's information. Okay. So we'll leverage the same account functionalities, but this time not to create a new oath session, but rather to get that user that we have just created.

**1:45:40** · So I'll say con user is equal to await account.get. Then if we don't have access to a user, so if no user, I'll simply return a redirect to forward/signin. Something obviously went wrong. But where is this redirect coming from? Well, it's going to come directly from React Router. Pretty simple way to do it. But in case we do actually get back the user, we want to extract something out of it.

**1:46:12** · So I'll say const dstructure the documents and say that is equal to await database.list documents. And here you're basically telling it hey extract some documents from the database from for me. But you have to actually say exactly from where in the database you want to extract them. So you have to provide the ID of the database, the ID of the collection and then finally the query with which you want to query that database.

**1:46:42** · So thankfully we have stored all of those pieces of data within our apprite configuration. So as the first parameter I'll provide a database ID and this is coming from apprite config. So make sure to import this app config right here at the top and then we have to provide the collection ID. So that's apparate config user collection id and as the third parameter you have to provide the actual query that you want to use to query these documents.

**1:47:12** · So I'll use appreite's query functionality which we'll need to import from apprite equal. So we want to return documents where the account ID equals to the user dollar sign ID. So we're only returning the data for the user that is currently logged in. Then I want to run the query select to tell it which fields do we need such as the name, email, image URL, when did the user joined.

**1:47:44** · So joined ad and the account ID. Perfect.

**1:47:50** · And of course make sure to import this database coming from app client. Great.

**1:47:57** · So this function should give us back our logged in user. So I'll shift it above right above our logout user because we might not need that functionality for some time yet. But what we will need is a Google picture. So extracting this seems like a perfect thing for an AI to do as we don't have to necessarily write all the code ourselves especially repetitive or boring code which doesn't really deal with any logic. So this might be a perfect chance to give Juny a try.

**1:48:27** · See, Juny is Jet Brains or WebStorm's new smart coding agent for productivity, and I wanted to test it out a bit to see whether it can help us with this. I started using it recently, and I'll link it in the description in case you want to test it out, too. But let me give it a shot and see what it comes up with. So, I'll open it up by pressing command shiftp and then typing jun, which will open it up right here on the right side. Now I'll give it a task to fetch the profile photo from the Google people API and return its URL.

**1:49:01** · Okay, I really wasn't descriptive enough. So let's see if it can actually do it based on this limited amount of information. Okay, it created a plan which it will use to do that. It actually checked out the enving the odd file and now it should actually write some code. After some thinking, it looks like the get Google picture function has been implemented to fetch the user's profile photo from the Google people API using the OOTH token.

**1:49:31** · It's also changing the store user data and get existing user. Oh, it also implemented the logout function. This is pretty cool. So, it seems like it actually did a lot of stuff right here.

**1:49:43** · It stored the user data into apprite by fully understanding how apprite actually works. Creating a new user document and it even fetch the existing user from apprite. All of this is super amazing.

**1:49:57** · But did it do what we asked it to do?

**1:50:00** · Well, let's check it out. First things first, it is getting the current session and it's getting the OAT token from that session. Then it's checking whether it got that access token. And by the way, if you don't have Juny, you can just pause right here and write out this code as well. Then it's actually making a request to the Google people API to get the profile photo. So it actually scouted the web and found the right endpoint. People Google apis.com v1 people me person fields photos.

**1:50:30** · This is exactly how it should be. and it passed the headers with the authorization bearer oath token. If it failed, it console logs it. Else it extracts the data, gets the photo URL and returns it.

**1:50:47** · This is pretty crazy. This is the exact implementation that I had in mind. So I can now collapse it and they just told me get Google picture function was implemented. The implementation is error-free and all the related functions were updated accordingly.

**1:51:04** · I got to say this is amazing and it even tackled the logout user functionality where it simply deleted the current session and return true. So feel free to pause and implement this as well. And if we look into the store user data here, it's getting the user. It's checking whether the user already exists in the database.

**1:51:25** · And by trying to list that document, if it does exist, we simply return it. else we get access to the Google photo and then we create a new user await database.create create document within this database the user collection we make it unique I think here we can do a bit better by saying ID coming from apprite dot unique so here we can

**1:51:54** · really use a unique ID and then it passed over the account ID the email the name the image URL and the date we joined that finally it returned the new user This is the perfect implementation of this function. And I got to say, I am amazed. It did everything I asked it to and even more. It's even checking for the existing user and returning it if it exists. But with such a great implementation of the get user function, it's even checking for that here.

**1:52:25** · So that additional function might even be redundant. Okay. Since Juny coded this for me, it's possible that while trying to replicate it, you maybe have some typos. So for that reason I'll provide this o.ts file within the video kit as well. So you can copy it and ensure that you have the same exact implementation that I have even I'll do it right here by deleting it and putting it here just to ensure that everything is exactly the same.

**1:52:52** · And with this in mind I'll also push this over to GitHub by running git add dot getit commit-m and I think I forgot to push for the last couple of lessons. So since then we have implemented routing dashboard layout dashboard UI as well. So dashboard layout and UI and now even the o functionality. So I'll commit it and push it.

**1:53:23** · And in the next lesson we can focus on implementing the UI of this great authentication page.

### Auth UI

**1:53:32** · To get started with Oth UI, let's first create a route for the O page. So, head over to app and notice how currently we have the routes right here for the admin. But now we'll create it outside of the admin layout, which means that this page won't share the layout we created for the admin dashboard because it doesn't have the header, the left sidebar, the navbar, or whatever. It just has a singular login.

**1:53:58** · So, I'll create it right here within a new folder called root. And within root, I'll create a new file called sign-in.tsx within which I'll run rafce.

**1:54:15** · Now, we'll have to head over into routes.ts because this doesn't just work like Nex.js's file-based routing. You still have to define it right here. So, above the current layout, I'll add a new independent route pointing to sign in.

**1:54:31** · and its path will be routes root signin.tsx like this. So now if you head over into that route, we can also try accessing it on the dashboard by heading over to sign in. And there it is. Sign in cannot read properties of null. So let's actually implement it. If I reload it one more time, the error is gone. So I believe we should be good. I'll start with the UI.

**1:54:59** · So, I'll turn this div into a main and give it a class name equal to off. What this will do is it'll automatically apply the background photo right here.

**1:55:09** · Looks okay on mobile, but once again, it really stands out on desktop. If you want to check out how I did it, the only thing you have to do is basically apply a full width, a full height, and then there's this background o background cover, and background no repeat. And this image is taken over right here from our assets. We have just added it as a CSS variable right here within Tailwind.

**1:55:35** · So now I'll create a new section within this main. And this section will have a class name equal to size-ool glass morphism flex-c center and a padding x of six.

**1:55:52** · This will basically create this glassy feel over the entire background so the card is more visible. So within this section I'll create a new div with a class name equal to sign in card and within it I'll create a new header with a class name equal to header. Within this header we can render a react router link.

**1:56:18** · So make sure to import it and we can point it to forward slash meaning just the homepage and within it we can render our logo. So I'll render an image with a source of assets forward/assets/icons/lo.svg with an al tag of logo and a class name equal to size of 30 pixels. There we go.

**1:56:44** · And below that link, we can render an H1 that'll say tour Visto, which is the name of the application with a class name of P28 bold and text-d dark 100. Thankfully, I added the tour visa name to our Webtorm dictionary. So now, even when I misspelled names, I know I misspelled them. There we go.

**1:57:12** · Below this header, we can create the article for the rest of the card. That'll have an H2. And this can say something like start your travel journey. We can style it a bit by giving it a class name equal to P28 semibold text- dark 100 and text- center. And below it, I'll also render a P tag that'll say something like, let's see what do we have in the design.

**1:57:45** · Sign in with Google to manage destinations, itineraries, and user activity with ease. So, I'll copy that from the design and paste it right here. I'll also give it a class name equal to P18 regular text- center text-g gray 100 and exclamation mark leading dash 7. So this will change how the characters are structured.

**1:58:16** · Right below this article I want to render a button and this button will come from Syncfusion. So I'll say button component coming from Syncfusion right at the top that is Syncfusion EJ2 React buttons and we can render an image right within that button with a source of for/assets/icons/google.svg SVG within it.

**1:58:43** · I will also render an icon CSS that'll be E search icon so we style it further with a class name of button class exclamation mark H11 for the height an exclamation mark W full.

**1:59:02** · Sometimes you have to add the important style to the class names so that they're actually taken into account. And now you'll see this huge Google G. So, let's instead give it a class name of size-5 to make it smaller. And I just noticed that I applied some styles to this image right here, but those styles were actually meant to be applied to the button itself. So I'll move them up and say this button will be of a type button with the icon CSS a class name and an on click equal to handle sign in.

**1:59:37** · So right at the top I'll declare this handle signin function as an asynchronous basic function for which the logic will implement very soon. But now what matters is that we have this button.

**1:59:56** · Within it we have this image. We can also give it an alt of Google. And below the image we can render a span that will say sign in with the Google. And we can give it a class name of P-18- semibold and text-white so we can better see it on this blue button.

**2:00:23** · There we go. Sign in with Google. Now the only thing we have to do is implement this handle signin function which right now will be super simple to do. Actually, believe it or not, we have already done it. So right here at the top, the only thing you have to do here is say await login with Google which basically renders this entire function not needed.

**2:00:48** · So instead of declaring this handle signin function, what we can do is just head down and call the login with Google right here when the button is clicked. But there is one thing that we have to add at the top though and that is a loader.

**2:01:08** · See, in React Router, a loader is an asynchronous function tied to a route and it runs before the routes component renders and provides the data to that component so that it can use it immediately once it appears. This makes the app feel faster and more structured because data fetching happens before the UI shows.

**2:01:31** · So to implement this very cool React router loader, you can do it right at the top of the sign-in function export async function client loader. You can open up a try and catch block. In the catch, we can simply console log the error saying something like error fetching user. And in the try, we'll actually try to get the user data beforehand.

**2:02:01** · So we'll say const user is equal to await account.get. And then if there is no user dollar sign ID, we'll simply return a redirect coming from React Router to the homepage. And if we get the user, that's great because then we'll already have access to it before. And we also have to import this account functionality from apprite client. So now if you reload, you can see that it loads super nicely.

**2:02:32** · And we can also copy this client loader and also add it to our admin layout. But we'll change it up just a tiny bit. Within the admin layout, head over above the current admin layout component and paste this client loader. Here we'll do something a bit differently. Keep in mind this will render when we're on the dashboard page.

**2:02:58** · So here we want to check apps o for the currently authenticated user and if there is no authentication redirect user to the signin. So we'll do account.get if there is no user ID then we'll redirect to sign in. So a bit differently than in the other one. But if there is an existing user.

**2:03:18** · So const existing user is equal to a wait get existing user coming from apprite o to it we have to pass the user dollar sign id then we can check if existing user question mark status is equal to user in that case we again want to redirect like this to the forward slash why because

**2:03:50** · regular users should not be able to visit the dashboard. Only admins can. So this is another check to see if we need to reroute them somewhere else. Finally, we'll return existing user question mark dollar sign ID. If we have it, we'll return the data for the existing user.

**2:04:11** · Else we'll say await store user data like this. Here I am missing user and here instead of saying error fetching user I'll say error in client loader and I'll return the redirect to sign in because most likely we have to sign in if we experience the error fetching the user. What you can do now is open up your terminal, expand it a bit and stop it from running.

**2:04:38** · That way all of these changes regarding routing will be applied. So you can then rerun your application by running mpm rundev which will spin it again on localhost 5173. If you do this and if you head over to forward/dashboard, you'll notice that it'll automatically redirect you back to signin, which means that our redirects and authentication are working.

**2:05:02** · Now, just before we click this signin with Google button, let's head back to Apprite to make sure that all of our settings are correct. As of recently, AppRight is making a lot of improvements to their infrastructure. And one of those improvements are the regions.

**2:05:19** · Right now, Frankfurt is one of the primary ones, but in the future there could be more. So, depending on which region is closest to you, you'll need to click on it right here to copy the endpoint. And then you'll have to use what you copied over right here as the apprite endpoint. Since I'm in Frankfurt region, for me it's FRA. Alongside that, we can head back over to O, head over into settings and look for Google.

**2:05:43** · We have already added our app ID and secret before, but I think I forgot to enable it. So click enable. Recheck your app ID and app secret over from Google. on Google. You can also head over to the client you created and remove the authorized JavaScript origin for 5173 localhost. It's not needed since we have this apprite redirect.

**2:06:08** · And once again, just copy the URI from apprite and paste it over right here to make sure that you have the same exact one. As of recently, I think they're also adding the region at the start. Once you do that, click save and also head over into your branding and make sure your app is published. If your app is not published, somewhere on this page, you should see a publish button. So once you do that, you'll be able to upload the logo of your application to further customize how your authentication behaves.

**2:06:37** · So if everything is looking good on the Google side, click update right here on Apprite to confirm our setup. Just like that, Google authentication has been enabled.

**2:06:50** · So you can head over to our application and click sign in with Google. And just like that, Google authentication has been implemented. In case you want to further customize your workflow, you can do that by implementing your app domain and your app logo so it shows up on Google so that people know what app they're signing into. But with that said, I'll just sign in. If you do that, you can notice that we'll be redirected to localhost 5173. And now, if you try to be sneaky and manually navigate over to the dashboard to be able to see what admins are seeing, check this out.

**2:07:23** · you'll automatically be redirected to the public facing homepage which right now is completely blank. And if you navigate over to sign in, you should be redirected back to the homepage as you're already signed in. But it looks like that redirect is now working. So if you head back to your sign-in page, it looks like we need to reverse this operation. If there is a user already logged in, then redirect to homepage.

**2:07:49** · So, if you save this and now head over to sign in, you can notice that since we're logged in, we can no longer see the login page. Perfect. But now, hey, how do we actually continue developing the rest of our dashboard finally that we're logged in since we are now being redirected? Well, let's give ourselves admin permissions. Head over to your app, right databases, travel dashboard, users, and notice this one single user right here.

**2:08:18** · If you look at its data, you'll see my name, email, and and account ID. The image URL as well, joined ad. And then at the end, there's a status. It's either a user or an admin. So, I'll switch it over to admin, save it, and head back over to localhost 5173 and navigate over to dashboard. If you do that, you can notice that now we can see the dashboard, and we're no longer getting redirected. Perfect.

**2:08:46** · This means that the entire signin and account creation process are working properly.

**2:08:54** · Let's also hook up the logout functionality so we can test the full circle of logging out and then authenticating one more time. To do that, we can head over into our nav items component. And right at the top of it, we can try to access the user data to replace this dummy user. I can do that by saying const user is equal to use loader data. And this is coming directly from React router. So this is a new functionality. But wait, how does this use loader data know exactly what data to fetch from where?

**2:09:26** · And why did I set it to be equal to the user? Well, let me show you. The use loader data gets the data from the loader function of the nearest route. Now, the nav items component itself is not necessarily a route, but it is used within our admin layout. So if you head over to the admin layout, you'll see that here we have a client loader function that returns only one thing. What is that? The existing user.

**2:09:58** · So that's why we know that we can fetch that user right here. Pretty cool, right? Alongside the user, we can also get access to the navigate functionality coming from the use navigate hook also provided to us by the courtesy of react router which now is working much more similarly to Nex.js which of course I embrace. And then here we can handle the logout functionality.

**2:10:25** · It'll be equal to an asynchronous function where we want to await the call to the logout user function coming from apprite off. And then after that we simply want to navigate over to forward slash sign in. Now let's also render the real user information. So right here we have the username and user email. I think it's already done, right? Because we're now fetching it from the real user instead of the fake user data object that we had before.

**2:10:52** · The only thing we have to do is on click instead of this console log, we want to call the real handle logout. So if I now save this, head back over into the dashboard, we'll see that we now have a real Adrian name right here with a real email, but the photo is missing. So to fix it, I Googled Google profile photo not loading in Vit React development.

**2:11:15** · So just trying to see what would be the reason that even though we have the access to the actual URL of the photo and I know we have it because I console logged what was coming back from that photo. If I then head over into it, you'll see that it's actually publicly accessible online but for some reason it wasn't showing within our application. So I Google that and then if you head over to the response it'll say that by adding refer policy of no refer to the image tag you can solve the Google image not showing.

**2:11:47** · So just add the refer policy of no referer to this image where we're rendering the image URL. If you do that and go back to your local host, you should now be able to see this image right here. Perfect. So finally let's test out the logout functionality.

**2:12:05** · If I click it, I get redirected back to signin. Now I'll head over to the dashboard manually and you can see that I can't see it. I immediately get redirected to the signin. Can I maybe go to the local host just the root route?

**2:12:21** · Well, yes, because currently there's nothing on there. Later on we'll implement the redirect from there too.

**2:12:27** · But now if I go ahead and sign in. Okay, now we got redirected to the homepage.

**2:12:32** · Later on, we'll implement a great public-f facing website right here. But for now, let's head back over to our admin dashboard since we have the full privileges to it. And one thing that I noticed is that right here, even though it says your name, it's not the same name that we have here. It's still using the one from constants. So to fix this, we'll have to use the React router pre-fetching one last time for now. So would you know how to do it based on how we implemented it previously? If not, I'll show you how to do it one more time.

**2:13:02** · First, we have this additional function that we create. Export async function client loader within it. It allows you to prefetch some data you need on that page. The only thing we need is the user. So, I'll say const user is equal to await get user like this. And this get user is coming from apprite o. So make sure to import it from there and then simply return it.

**2:13:30** · Or in an even simpler way, you can just say return await get user. Or if you want to be really cool, you can turn this over into an ES6 arrow function by saying export const client loader is equal to an asynchronous arrow function with an immediate return. So you can just skip the return statement and the braces and just say return await get user.

**2:14:00** · And with that you can turn this client loader into a nicel looking oneliner which fetches the user. And now you can retrieve it from within your page. Just right here under params you get access to the full loader data. And we also need to assign a type to it. This type will be provided to us by react router.

**2:14:26** · So I'll say router or rather route component props and we can import this type. So saying import type route in curly braces from dot slash plus types slash dashboard.

**2:14:44** · If you do that and remove these curly braces because we don't need them as we're not within an object, you can see that now our TypeScript knows that the loader data will contain the data returned from the loader or the client loader which in this case is the user. So how do we now accept that user? Well, the only thing we have to say is const user is equal to loader data. And we can even assign a type to it by saying as user or null if it maybe doesn't exist.

**2:15:15** · Now, it looks like TypeScript is still complaining saying that this could be unknown. But that's not really the case because we know what we're going to get back from the client loader. Oh, but it looks like I forgot to add an export statement right here. If you add it, you'll see that it'll no longer complain and it knows exactly that the username is either a string or undefined.

**2:15:37** · Perfect. So, with this in mind, we are good to test it all out. So if you head over to your dashboard, you can see that at the bottom left we have the username and now it says welcome Adrianjs Mastery right here at the top which means that we're successfully gathering the user data and we're successfully signed in.

**2:15:56** · So with that we have now implemented the full circle of authentication everything from the UI to functionality to log out and also fetching the user data and storing it within the database. So if you head over to apprite, you can already see that we have this user that we created. But if you also head over to O, you'll see that we have created a user over there as well.

**2:16:17** · So not only have we implemented the full authentication, but since we have the user in the database here, that means that now we're also successfully creating documents within our database collections. Which means that we can also not only fetch them to show the username on the left sidebar or the dashboard, but rather we can render a full table showing all the users that have joined their application so far and display their statuses. They can either be users or admins.

**2:16:48** · So in the next lesson, let's focus on implementing the users table. Just before we go ahead and set up our user stable, what do you say that we make our app enterprise ready or maybe should I say enterprise secure using Sentry? See, Sentry is the application monitoring software that's considered not bad by 4 million developers. And it'll allow us to track all sorts of different errors when you actually bring your app to production.

### Entreprise Error Tracking & Monitoring

**2:17:19** · Since I've partnered with Sentry, they decided to give you 50,000 errors to test out. And trust me, that's more than you'll need. So, I'll leave this special link down below. So, feel free to create your account. And then you'll need to create a new React project like what we've done at the start. Once you're there, don't follow this setup right here where it asks you to install Centry React. In the docs, I found a special guide for the React router framework v7 for building full stack web apps with React.

**2:17:49** · I'll leave the link to it within the video kit. So, let's go ahead and follow it together. You need a Sentry account, check. A Sentry project check.

**2:17:58** · And an application up and running, check as well. Let's choose what we want to use Sentry for. I'll turn everything on from air monitoring to tracing session replays and profiling. And I'll copy the command given to me. Then head over within your terminal and paste the installation command. This will take a couple of seconds and it'll get installed. Next, we can run react router reveal, which will reveal some files that'll allow us to set up Sentry. So, I'll just run that command.

**2:18:27** · And now you can see two new files created for you right here within the app. Entry client and entry server. Next, let's do the client side setup. The only thing you have to do is just copy this file from the docs. I believe Sentry has already taken the DSN, the ids and the pro and everything regarding your projects directly from your application. If not, make sure that it did that by making sure that you have some ids or links right here at top.

**2:18:56** · Then copy it and override the client DSX with this new one that you just copied here. We enabled the replay integration as well as the browser tracing integration. Now, we'll need to update our root.tsx tsx to report any unhandled errors from our error boundary. So copy the import statement and paste it right at the top of your route and then also add this century capture exception within the else if of our error boundary.

**2:19:27** · That'll be right here at the bottom error boundary. And here we have the else if. So alongside just reporting it, we want to allow Sentry to capture it. Now let's scroll down and let's do the server side setup by copying this instrument server mjs file. So let's go ahead and create it within the root of our application. I'll call it instrument.server.mjs and simply paste the one that you just copied.

**2:19:57** · Scroll down and then we'll have to update our entry.server.tsx. So head over into it.

**2:20:06** · That's going to be entry server.tsx tsx for this file. We'll have to copy the import. I'll paste it at the top. Then you'll have to take this handle request.

**2:20:17** · But you can notice that it already exists within our codebase. So what we can do is just we can wrap the current handle request. That'll look something like this at the bottom of the screen.

**2:20:28** · We can just say export default handle request. And then we can wrap it within sentry.

**2:20:35** · sentry handle request like this. And now you can find where we're exporting the handle request in the first place and just remove it rather just make it a regular function that we're then wrapping with sentry handle request and exporting at the end. And then also copy this handle error part right here and paste it right above it. You can import the handle error function coming right at the top from React Router.

**2:21:04** · And the only thing that bothers me right here is that it says that sentry handle request has been deprecated. But thankfully, if you scroll just a bit down, you'll see that if you need to customize your handle request, you can just get this wrap sentry handle request, provide this pipe within it, and then finally export it like this. So, let's just enable this distributed tracing between the client and the server by adding it below this resolve. So, I'll head right here, find the resolve, and add it right below.

**2:21:35** · So, you can see we have the same thing here, but now we're wrapping it with this get metatag transformer coming from Sentry.

**2:21:46** · And then also at the bottom, we're not going to use Sentry handle request.

**2:21:50** · We're going to use the wrap sentry handle request. Perfect. Docs are on point. so far. So, let's continue with the updated scripts because React Router is running in ESM mode and we need to use the import command line options to load our serverside instrumentation before the application starts. So, we'll have to update the start and dev scripts to include that instrumentation file.

**2:22:15** · I'll copy these dev and start commands and head over to package JSON and update the dev and start. Perfect. And then we can set up the source maps upload by updating our V config. So you can notice that Sentry automatically prepopulated the organization in the project for me. In case you have multiple, you can select one right here. And then make sure to generate the O token as well. I mean the fact that you can do this from the docs directly is super cool. Now copy this sentry config.

**2:22:46** · Head over to vit.config.ts and add it right at the top. Make sure to import this type from sentry options. And now we can define this config. So let me just copy this entire config part and paste it below our current one. You'll notice that we have two. Now we're going to keep the one from Sentry, but make sure to add Tailwind CSS to it as the first plugin and add TSC config paths right here as the second plugin as well.

**2:23:16** · Then we have the React router and the Sentry React router. And then make sure to add the SSR right below the plugins or in this case below the Sentry config. If you do this, you can delete the current config.

**2:23:33** · And notice what's happening here. We're actually exposing the default config and then passing it over into the Sentry React router config alongside the Sentry config. Make sure to import all of these from Sentry and make sure that you have your O token right here alongside your project and organization information. If you did that correctly, you'll want to include the Sentry on build end hook in React Router config. Head over to the React router config.

**2:24:00** · Copy this entire build end part as we don't have it and paste it after the SSR and import sentry on build end. Perfect. And that's it.

**2:24:12** · Everything has been set up. I got to give props to Sentry for creating such a wellstructured documentation page. I mean, I was just able to go through it and everything worked just seamlessly.

**2:24:26** · Even though React Router V7 is a super new framework, they knew exactly what they were doing. Sentry showed me how we can expose the entry server and client files. So we can change the configurations and they only added the minor changes to all of these files. The minimum for what's required for Sentry to work. So with that in mind, the only thing left for us to do is to verify.

**2:24:51** · This snippet of code will include an intentional error so that we can test that everything is working as soon as we set it up. So throw an error in loader to verify that sentry is working. After opening this route in your browser, you should see two errors. One capture from the server and one capture from the client. So instead of copying this entire file, we can copy this error right here. Throw a new error thrown from a loader. Close all the currently open files and head over into our dashboard.

**2:25:22** · That'll be right here within app routes admin dashboard and we'll have to add a loader. So, you know what?

**2:25:31** · I'll just copy the entire loader, paste it right here, and save it. Now, if you go back to the browser and reload the page, you'll be able to see, oops, some error thrown in loader. Believe it or not, this is exactly what we wanted to see. So, if you head back over to your Sentry dashboard and reload the page, you'll be able to see your error dashboard and you can see that this index increased and that has been one error right here. So, at the top right, click view all issues. And there we have it.

**2:26:02** · A minute ago, a new error was thrown in a loader. And I mean, just take a look at the amount of information that we're getting back right here. We can see when the error has happened. We can see how many users has it happened to on how many occasions. We can mark it as resolved or archived. And we even have a replay attached to it. So you can see exactly what the user was seeing before the error happened. In this case, it happened as soon as the dashboard loaded.

**2:26:33** · But how do we know that it was actually on the dashboard? Well, believe it or not, here you have the breadcrumbs of everything that led to that event.

**2:26:43** · You can see that the user was trying to load the dashboard data and then there was an error in the loader. This actually tells us a bit more about how React Router V7 works. Why? Because we didn't manually make a request to the dashboard. URL, but it looks like when you try to access the dashboard page and you have a loader attached to it, it actually tries to fetch the data for that page first and then we weren't even able to get to the dashboard page. So having all of this information is super useful.

**2:27:14** · Not really right now while we're in development, but in production. Why?

**2:27:21** · Well, because your users will not be able to tell you this, right? You're going to ask them, hey, where are you experiencing this error? Why did it happen? Which device you're using? They will have no clue, right? But here, you can just check it out. the user was trying to access the dashboard page and then immediately after we got an error in the loader. You can see when the error happened. Oh, and as I was explaining this to you, looks like I got this little tool tip that's going to explain it to me too. So, we can go through it together.

**2:27:50** · So, you can see this error in aggregate across all the different users as well, so you know whether it's one that you should fix very soon or the one that can wait. You can also narrow your focus on when this error has happened. You can explore the details of the error like the context around which it happened which is the IP address, the browser, the operating system, everything that Sentry has access to, they'll share it right here.

**2:28:17** · Then you can compare different examples of errors. Take action on it by marking it as a priority or not a priority one or maybe assigning it to the team member that you don't really like as you don't want to fix that error. And finally, you can share the updates or maybe even track it on GitHub or Jira. But with that said, let's remove this error from the loader. And let's also try to throw one not from the loader but from the client component itself. So this will disallow us to see the dashboard in the first place.

**2:28:47** · And I'll say some error thrown in a dashboard. You'll see the second error appear. This is a client side error now.

**2:28:56** · So if you head back to the issues, you'll see that we have another error thrown within a dashboard. And for this one, of course, you'll get different kinds of information because it's coming from a different context. Overall, Sentry is just the go-to tool for tracking and monitoring errors in production. And you can also check out traces, which allows you to see exactly how that specific error has happened by checking out the descriptions of what was happening before it. There's profiles that you can implement to find slow code.

**2:29:25** · There's replays that allow you to see exactly what was happening on the screen before the error happened.

**2:29:32** · And you'll also just get a lot of quality insights like the first Contentful Paint, your web vitals, and more. You can check it all out in the onboarding. So with that in mind, let's remove this error from here as we don't want to break our application.

**2:29:47** · And if you head back over here, it's like nothing ever happened. But now we have an enterprise ready error tracking monitoring system put in place. So once we actually deploy this application, if something happens to it in production, we'll know exactly what happened and to how many users it happened so we can act on it quickly. To get started working on the all users page, first navigate over to it and then open it up right here within our codebase. we have already added it to the routes.

### Users Table

**2:30:17** · So if you check it right here, you can see that you can access it by going over to all dash users, which is exactly where we're on right now. And here we'll use Syncfusion's grid component. They have this very nice guide that shows you how you can install it and set it up. But basically what you have to do is use the grid component, pass the data source to it, and then render a couple of different columns for the different fields that you want each one of your rows to have. So let me show you how we can make it work.

**2:30:48** · First things first, I'll change the class name right here from dashboard to all-ash users. And then instead of trips page, I will say manage users. And we can change the description to something like filter, sort, and access detailed user profiles. Perfect. Right below the header, I'll render the Syncfusion grid component. This grid component will be coming from right here at the top.

**2:31:19** · Add Syncfusion SLJ to React grids. Tables are not easy to work with. So let me show you what we can do with this grid.

**2:31:31** · First things first, you have to pass a data source to it. So let's say data source is equal to and now what you need to do is just basically pass an array of different objects into it. But instead of declaring it right here, for the time being, we can use the static data coming from our constants. So I'll simply say users and we'll import those users coming from constants index.js. It is basically just an array of three different users that I want to render right here on the page.

**2:32:01** · And then once we render them, we can switch it over to use real data. And there we go. Already just by doing that, you can see a table.

**2:32:10** · Of course, tables are better viewed on desktop devices. So if you check it out, it's pretty cool, right? You get the ID, the name, email, image URL, they joined, itinerary created, and a status of either user or an admin.

**2:32:25** · Now I'll collapse this just a tiny bit so we can see the code but also the rest of the stuff. As you can see it is mobile responsive but we can definitely make it so much better. So within it I will render a columns directive but make sure that you spell it columns plural and use the one coming from React grids.

**2:32:46** · Next right within it you can render each individual column directive. So import that one too and then self-close it.

**2:32:55** · Within it, you can specify exactly what you want each field to have and how you want it to look like. So, I'll give this field a name equal to name. I'll give it a header text equal to name with a capital N. I'll give it a width of about 200. And I'll even align the text on the left by saying text align is equal to left. And the second one will be just a column directive. Not columns, but rather a column.

**2:33:25** · So you'll also have to import it right here at the top. And you can see now that we have decided to manually decide how we want to present all of these different columns and rows.

**2:33:36** · Now we only have one column with names John, Jane, and John. What you can do is also say grid lines and set it to none.

**2:33:45** · That way it looks a bit cleaner. You do this to the regular grid component. Now, what else can we do with each one of these fields? Well, we can also define a template that allows us to choose exactly how each one of these will be rendered. So, for the template, I will open up a callback function inside of which we get access to the props, which will be of a type user data because we're mapping over the users. So for each one of these props, we want to automatically return a div.

**2:34:14** · And each one of the divs will have a class name equal to flex items center, gap of 1.5, and a padding x of four. And within it, we want to display an image. So instead of simply displaying a name, we want to render an image with a source of props.

**2:34:38** · image URL with an al tag of user, a class name equal to rounded- full size of 8, and an aspect of square. If you do this and reload, you should be able to see a profile photo for each one of our fake users.

**2:34:58** · And below the profile photo, you can render a span element that'll render the props.name. Perfect. This is already better than what we had at the start. It really shows how customizable it is.

**2:35:12** · Now, let's also declare another column directive right below. The future ones will be even simpler. They'll have a field. This one will be for the email so that it knows how to match the data.

**2:35:25** · See, this value right here matches exactly the value of the key in that specific object in the array. So the first one was the name and now we want to show email addresses. So the field is email. The header text will be set to email. The width can be maybe set to 150. And text align can be set to left.

**2:35:50** · And you put this column directive properly within the columns, not outside of it. You should be able to see it appear right here immediately. What we can do next is just copy that column directive and maybe duplicate it two more times. For the third field, I will render the date joined and change the header text to date joined with a width of maybe 120 will be enough. So now we see January as well.

**2:36:18** · And maybe the next one can be trip created or I think in this case it's itinerary created. We can again say itinerary or maybe trip is shorter created and this will be when the trip was created. So about 130 characters is enough. So if I save it now you can also see trip created but I need to spell it properly exactly as to how we have it in the user data. So if I head over into users it is itinerary created.

**2:36:49** · How many of them have we created? So this user has created 10 four and eight. And finally and most importantly, we need to show the status or the type of the user. So I will duplicate this column directive one more time right below. And I'll call the field status a header text of maybe here we can say type of the user width of about 100. And for the template, we can once again get access to the props of the user data.

**2:37:21** · And then for each one, we can return an article that we're going to close. And within it, we can render a div. Within the div, we can render an H3 that will render the props.

**2:37:40** · So here you can see that now if you reload you can see the type of either the user or the admin. But let's also style this a bit differently to make it like a chip component within it. First, I'll style the article by giving it a class name equal to and I'll make it a dynamic CN class name that'll always have a status column class. But then depending on the props status, which I can just dstructure from the props right here.

**2:38:11** · So I'll simply get the status out of it so we don't have to repeat ourselves too much. If the status is triple equal to user in that case we'll return the BG success of 50 else we'll return the BG light of 300. So if you save that you should be able to see a light background on each one of these articles. Now right below within this div I'll also give it a class name. I'll also make it a CN.

**2:38:44** · It'll have a size of 1.5 and rounded dash full. And if the status is triple equal to user, I will then give it a bg success of 500. Else we can give it a bg gray of 500. So if you save that, you'll now see that little dot that we have right here.

**2:39:10** · And now we can style this H3 within it by giving it a class name of CN font- enter text- extra small and font- medium and finally if a status is triple equal to user in that case text success of 700 else text-g gray of 500.

**2:39:37** · So let me style this properly. And if I go ahead and save this, you can see that now the text matches the color. But it doesn't yet look good. And that's because this div should not close the H3. Rather, the div should be a self-closing component as it is just a dot that appears right here before the user. So you can see how customizable the table is. You can show the photo within it. You can change how much space each one of these fields takes. And you can also change whatever is presented right within each one of these rows.

**2:40:11** · Perfect. And believe it or not, that is it. A fully functional table where you can actually hover over fields and implementing filtering or sorting and pagionation within it is also super simple. I'll show you how we can do that once we actually get more users. But for now, I actually want to load up the real users right here, not these fake ones.

**2:40:32** · So what we can do is head over into apprite o.ds and create a new function called get all users. We can do it right at the bottom. The goal of this function is to fetch all of the user. So let's export a new async function called get all users and make it equal to an asynchronous function like this.

**2:40:59** · So export const get all users is equal to an async error function and we can open up a try and catch block. In the catch I will simply console log the error saying error fetching users and in the try we need to list the documents coming from the database. So I'll say const dstructure something and make it equal to an await call to database coming from apprite dot list documents.

**2:41:37** · As before we have to tell apprite from which database ID to get it and that database ID is stored in the appread config database ID. Then we have to specify from which collection. So I'll say appreconfig.

**2:41:51** · This time it'll be a user collection ID.

**2:41:54** · And finally, we need to provide a query to fetch this. In this query, I want to limit the amount of users that we get back by a specific number. Let's say five for now. And then to implement the pagionation, I also want to offset the query by a specific number. Let's say two. Essentially with the limit and the offset, you are implementing the pagionation. Why? Because if the limit is 10 and you're offsetting five, you're basically dividing this into two pages.

**2:42:24** · One that has five and page two that has the other five. Hopefully this makes sense. So to make this pageionation dynamic as the params into this function, we can accept a limit of a type number as well as the offset of a type number two. So instead of hard coding them, we can just declare them right here. Limit and offset.

**2:42:44** · Now the call of this function will give us back the documents and these documents we can rename to user because that's what they are and we also get back the total number of documents. What we can say is if total is triple equal to zero we can just return users equal to an empty array and total equal to the total which in this case will be equal to zero.

**2:43:10** · But in case we do get some users, we can then return the users equal to users as well as the total equal to the total we're getting. Hopefully this makes sense. So now the only thing we have to do is call this function within the all users table right here at the top. Instead of declaring it right here, we'll use the React router new functionality to fetch it before the page loads by implementing a loader.

**2:43:40** · So above the function I'll say export async function loader or you can use ES6 to say export const loader is equal to an async function. And here we can get access to those users and the total number of users by awaiting the get all users coming from apprite o and let's say we want to limit it to 10 and offset by zero at the start because we're in the first page.

**2:44:11** · Once you do that we can just return an array of users as well as the total number.

**2:44:19** · Basically what we have done is we have exposed it right here to within our function.

**2:44:24** · So let's dstructure the loader data of a type route coming from react router types and this is going to be coming from all users dot component props and then we can just say const users and dstructure them from the loader data.

**2:44:44** · Here we have a bit of a warning saying that users does not exist on type get all users. Let's see if we're properly returning it. we are here but we also can return it in the catch. So if something goes wrong we can return the users as an empty array and the total also equal to zero. If we do this then it'll know that always there's going to be a return of users and total. Also let's fix this route import because I can see that it's coming from the wrong file.

**2:45:16** · Basically it should be coming from just dot slash plus types forward slash in this case we can get it from all users and we have to specify that we're importing a type of route. Perfect. So now we're getting the users and you can immediately see that instead of having the fake users coming from the constants which we can now completely remove now we're getting a single user from our real database.

**2:45:46** · There are a couple of things we have to fix though. The name and the profile photo are looking good. We can give some more space to the email address. So, let's scroll down to the email address and maybe give it a width of 200.

**2:45:58** · That'll give it some more space to breathe. After that, we have the date joined. So, I'll just rename this to join at because I believe that's we're saving it into the database. And you can see that now we're getting that date joined. And we also need to parse it a bit better. Do you know how to do that?

**2:46:19** · Well, you need to create a template for how you will render it. So just create a template have a callback function where you get the props in this case the joint ad date. So I'll just dstructured join ad from it and then we can just return what you want to show. In this case, I'll call the format date function coming from lib utils and then I'll pass this joint ad right into it. If you do that, you'll see April 23rd, 20.

**2:46:47** · Let's also give it some more space to breathe just so we can see it a bit better.

**2:46:55** · April 23rd, 2025. Beautiful. Did you see how simple that was? We can also say that joint ad is of a type string.

**2:47:05** · Perfect. So I was just able to take this piece of data from the database, take its field and then nicely present it right here. I don't think we'll need the trips created thing. So I will just remove it from now because we're not actually storing it within the database.

**2:47:21** · But what we care about is of course the type of the user which in this case is the admin. So with that in mind, we now have our first and only user and we have a table with which we can check it out.

**2:47:33** · We can head over to the dashboard and check out our only user. Looks pretty cool, right? What do you say that we go ahead and sign in as the second user as well to see the differences? I'll log out, we have this great looking sign-in page and I'll log in with my second JavaScript mastery email address. And now if I try to head over to the dashboard, you'll see that I'll be redirected back to the homepage. So later on when we implement the public facing website, I'll be able to check it out. But right now as I'm a mere public user, I cannot see the admin dashboard which is its whole point.

**2:48:05** · So open up inspect element and head over to application and clear your cookies session storage as well. And once you clear it, just reload your page or just manually head over to the sign-in. I've logged back in with my admin user. So, if I head over to all users, you'll be able to see this second account that says JavaScript mastery. I can see that the image is not loading properly, but I think we know how to fix that, right?

**2:48:35** · We have to head over to where we're rendering that image. And we have to give it a refer policy of no refer. If I save it and reload, you can now see that we have two of the same profile photos.

**2:48:51** · For you, it should be something different if you used a different profile. But what matters most is that the type of these two users is actually different and the email address as well.

**2:49:02** · And they're both showing on our table where we can manage the users. So that means that our all users table has now been completed. So now that we have the basic dashboard, the authentication system, and our users are actually logged in, it's the time that we actually create the trips. That's what this app is all about, right? So, let's focus on creating the form that'll make all of that possible. And finally, we are ready to create new AI trips.

### Add new trip form

**2:49:30** · Well, you could say that this is the moment that we've been waiting for. We'll do that through the help of a form. Everything starts with a form, of course, but then we'll fuse it with functionalities using AI generation. But first, let's focus on the basics. Everything starts with some inputs. And as Shhatzian likes to say, forms are tricky. They're one of the most common things you'll build in a web app, but also one of the most complex.

**2:50:00** · You have to structure them, and they have to be semantically correct. They have to be usable and navigable using the keyboard. They have to have proper area attributes to be accessible, support both client and server validation, and they should be wellstyled and consistent with the rest of the application. Thankfully, in this case, I'll show you how to do enterprise level forms using Syncfusion.

**2:50:22** · So, with that in mind, let's create a new route that allow us to create trips that we'll be able to navigate to by clicking this AI trips button. Right now it points us to a four of four that is available under forward/trips. So let's just create it.

**2:50:43** · Right here under app we have routes and then under routes and admin I'll create a new file and I'll call it create trip.tsx. Within it I'll run rafce. And then to be able to visit it on the page I'll head over to routes.ts. I will duplicate one of the last routes within our admin dashboard interface. I'll change the path to point create trip and also the path to the file also has to be a create trip path.

**2:51:18** · So if we do this, what we might want to do is just change the route to maybe trips/create. That will allow us to have proper REST API routes where we're following good naming conventions. On this page, we'll be able to create the trips. But just above it, I'll create another table that'll allow us to see all of the trips, including the table of trips. So, I'll call it just trips, and I'll point it to admin trips.tsx.

**2:51:47** · So, let me create that file by heading over to right here under admin. And I'll create a new file called trips.tsx. I'll run rafce. And here we'll be able to see all the trips. If you now head over to your terminal, stop it from running and then rerun it and reload your page on trips, you should be able to see it. So, one of the things that we'll have on the trips page will be a button that will allow us to head over to the trips creation page.

**2:52:16** · And we'll actually do that through the help of a header. We're already using the header in the all users table. So let's just go ahead and copy this starting main tag and the header from the all users page and let's just paste it right here and properly close the main tag.

**2:52:33** · If you do this, of course, for now it'll say manage users, but here we want to say trips and we can give it a description of something like view and edit AI generated travel plans. But here's the kicker. In this case, we'll actually give some additional functionalities to the header by adding a call to action button to actually generate a new trip. So, I'll give it two new props.

**2:53:03** · A CTA text equal to create a trip and a CTA URL pointing to the new route we created of forward slashtrips slashcreate. And then we can head over into that header and accept those two new props which are going to be optional. The CTA text which is optional of a type string and a CTA URL also optional of a type string.

**2:53:34** · And we can accept them as props CTA text and CTA URL. And now we can render them right below this article by first checking if they exist. So CTA text and CTA URL and

**2:53:50** · only if those two exist then we will render a link component coming from React router pointing to that CTA URL in this case the new create trips route we created and within it we can render a button component coming from shot CN that'll have a type equal to button a class name equal to

**2:54:14** · button-class excl exclamation mark H11 because sometimes when we need to add additional class names to Syncfusion components, we need to denote them as important. Same thing for the W full and on medium devices W of 240 pixels. I found that value works the best. Within that button, we can render an image with a source equal to assets icons plus.svg with an al tag of plus and a class name of size of five.

**2:54:47** · This is a very simple plus icon. And then on the right side, we can also render a span that'll simply render the CTA text. And we can give it a class name equal to P16 semibold as well as text-white.

**2:55:08** · So if you add this, head back over into trips and check whether we have properly added the right CTA URL like this, you should be able to see a create a trip button, which on desktop looks something like this. So now right from the page where you can see all the trips or at least you will be able to see them soon you can also navigate over to create a trip page which is exactly what we wanted. So now we can start implementing that create trip form.

**2:55:40** · Let's start off by wrapping everything into a main tag to denote that this will be a page with a class name of flex flex dash call a gap of 10 padding bottom of 20 and a wrapper property. This will give it some padding and nicely position it on the screen within it. We can also render another header. Yep, we really want to reuse them as much as possible.

**2:56:06** · We'll give it a title of add a new trip as well as a description of view and edit AI generated travel plans. And we can end the header right there. Right below it, we can open up a section within which our form will go.

**2:56:27** · So let's give it a class name and give it a margin top of 2.5 to divide it from the header as well as a wrapper MD. What is this wrapper MD? Well, it is to ensure that the form stays in the middle of the screen and it doesn't extend throughout the entirety of the dashboard.

**2:56:44** · See on web screens you have a lot of space but sometimes you want to use that space like for the table and in other times you just want to be able to see what you need to see and that is nicely structured inputs that don't necessarily need to extend from the left to the right edge rather you need to have them right in front of you so heading back over within our section right within it I will create a form that'll have a class name equal to

**2:57:17** · trip-form and on submit we can call a handle submit function which I will declare right above by saying const handle sububmit is equal to an asynchronous empty function at least for now we'll add the logic very soon now if you save this you should be able to see a cardlook layout so within this form I will now add a div. And within that div, I'll add a label that'll have an HTML 4 country.

**2:57:51** · Why country? Because the first thing you got to figure out when you're planning a trip is where you want to go to. So, I'll basically add a label that'll say country right here. And then below it, we want to implement a component known as a combo box. See, a combo box is like a select element, but it also allows you to start typing within it. Something like this, where you can type and then you can find results faster.

**2:58:17** · Like selects are pretty good if you have a limited set of options like five, two, or 10. But if you have more than 100 or 200 countries, well, you want to make your life easier and start typing the name of that function so you can more easily find it. That's exactly what a combo box component is for. And in my early development career, I remember creating those combo box components on my own. And trust me, you don't want to do that. It takes a lot of time.

**2:58:44** · So, we're going to make our life a bit easier here and actually use good programming practices, which is not to reinvent the wheel. And we'll use a shot CN combo box component, which you'll have to import at the top. And then once you import it, coming from Syncfusion, EJ2, React dropdowns, you'll have to pass some props to it to actually make it work.

**2:59:12** · First things first, you'll want to pass in the ID, and this will be for selecting a country. Once you have the ID, you'll also want to have a data source similar to what we had with our table. This can accept an array of maybe different titles like country one, country two, and so on. As you can see, it is super intuitive that I didn't even have to take a look at the docs and I immediately understood how this component works. I can start typing.

**2:59:39** · It suggests me option and I can just select one with my keyboard. But now we're going to have more countries and we want to display it in a bit of a better way.

**2:59:51** · Maybe something that looks a bit like this, right? So to achieve that, we'll have to have a list of different countries that we can fetch. Thankfully, there is a simple endpoint called restcountries.com v3.1/all. And if you just head over to that URL, it'll give you a JSON formatted list of all of the countries in the world, which is exactly what we need. So what do you say that at the top of this page we make a simple fetch request to fetch those countries?

**3:00:23** · To do that I'll actually use react router loading functionality by saying export const loader is equal to an async function within which we can get access to a response by calling that API. So I'll say await fetch and I'll make a call to https col/restcountries.com/v3.1/all.

**3:00:54** · Then we want to get the data by awaiting the response JSON as you typically do with fetch requests. And then what do you say that we simply console log them. So I'll console log the data we're getting back.

**3:01:08** · I'll head over into our application and I will just open up the console and reload the page. And if you do that, you'll get an error. That's because we're not returning anything from this loader. So let's actually just return this data. And if you do that and reload, we will be good. So instead of console logging it here, where we actually need that data is down below.

**3:01:32** · So let's just put that console lock here. And we can actually dstructure the loader data which is of a type route dot component props. And this route has to be imported right at the top by saying import type in curly braces route from dot slash plus types forward slashcre. So it knows exactly what we have within it. And we can dstructure the countries from the loader data.

**3:02:03** · So I'll say const count countries is equal to loader data as country array. Perfect. So now we know that this is an array of one of the countries and later on we'll return the name coordinates value and the open street map view. So let's just console log the countries and reload the page.

**3:02:29** · If you do that and inspect the element, you'll be able to see that we get back an object of a ton of different countries, each having a name and a ton of other details. But we don't need those details for every single one of them. So instead of returning the full data, let's actually map through it and only return some pieces of the data. So I'll say return data.m map where we get each individual country of a type any.

**3:02:59** · And for each one we want to automatically return an object. You do an automatic return by wrapping this first in parenthesis and then returning an object. And we want to take the name.

**3:03:12** · We'll make sure that the name is equal to country.fl country.name.com.

**3:03:20** · We'll take in the coordinates which will be equal to country.latt LNG latitude and longitude.

**3:03:28** · The value will be equal to country.name do common. And I'll also take in the open street map which will be equal to country.maps question mark. Street map. So now we're returning only the data that we'll actually use and we have it right here within our application. So you already know how Syncfusion works magically when you have a data source. The only thing you have to do is actually provide that data source right here within this combo box component.

**3:04:00** · If you do that and reload the page, you'll see that we have a list of a lot of something. That something will hopefully turn into a lot of countries soon. But for now, it is just a list of emptiness. So let's go ahead and modify this combo box component to actually show the right fields.

**3:04:21** · So I'll say fields is equal to an object where text will be text and value will be value with a placeholder of select a country and a class name equal to combo box. If we save this, you can see the placeholder but still no countries. That's because we have to take this data and we have to modify it a bit.

**3:04:49** · So what I'll do is right here where we have the countries, I'll create those countries in a way that we need it. So I'll say const country data is equal to countries.m map where we get each individual country and for each one we can automatically return an object where we take only the text of country.name name and the value of country do value and these values will

**3:05:20** · then match the ones that we are referring to right here text and the value. So let's just say countries is equal to country data. You can see that the format matches and we immediately get both the flag as well as the text.

**3:05:38** · Are you wondering how are we getting the flag as well? Well, that's because each one of these flags is basically an emoji, like a set of characters. So, you don't necessarily need to render an image to be able to see it. And with that said, we have this greatl looking combo box. Well, not that great looking as of now, but it will make it better looking. But hey, you can try to start typing something and it won't yet update. We'll also work on that very, very soon.

**3:06:03** · So, what we can do is fix the class name right here, which will automatically make it look so much better. Let me just reload the page right here. Check this out. So, now I can go here and I can select one of the countries. And we'll also have to keep track of the selected value. So, I'll have to add a change property where we'll take a look at the event which has a value which is either of a type string or undefined.

**3:06:31** · And then within it we want to check if a value exists and if so we'll call the handle change function and to it we'll change the field of country to the value that was selected. This is a function that we haven't yet created. So let's just create it right above here where we have the handle submit. I'll also add the const handle change and it'll be a function that takes in the field and the value.

**3:07:04** · So right here I can already type that it'll take the key which will be a key of trip form data and a value which will be either a string or a number and then we can do something with those values within the function but more on that soon. What we want to focus on right now now that we have the change is also to turn on the allow filtering. It is a very simple boolean prop.

**3:07:34** · But once you enable it, you can head over here and you think you'll be able to start typing but not yet. That's because we have to define what property will we filter by.

**3:07:47** · So I'll turn on the filtering and here we get access to the type event and we'll try to get access to the query that the user has typed. So query is equal to e.ext dot to lowercase so we can actually not mind the case. Then we want to call the e update data and we want to take the list of countries that we have and filter them by getting each country and we'll filter it by name.

**3:08:21** · So we're going to check whether the countryname to lowercase includes the query that has been typed.

**3:08:32** · Once we get that list of countries, we'll map over them by saying dot country. And then once again, for each one of these countries, let's do it properly. For each one of these countries, we will automatically return.

**3:08:48** · So once again, make sure that you have a parenthesy right here. We'll automatically return a text of country.name as well as a value of country.

**3:09:02** · So if you do this properly then you'll be able to start typing and you'll immediately be getting all the countries matching that search term. So let's go for United States. There we go. We can also immediately search over for India.

**3:09:20** · All of it works. Wonderful. So that's it. That's how you very easily create your very own combo box and make it fully functional. So, what other information do you think is important when deciding where you want to go for a trip? The country where you want to go to and the location surely matters a lot, right? But what else can we do?

**3:09:44** · Well, let's head below this div that is wrapping our combo box. And below it, I'll create another div within which I'll have a label and it'll have an HTML 4 for the following input. And this one will be about the duration of your trip.

**3:10:05** · So I'll say duration and below it I'll render a regular HTML 5 input with an ID of duration a name of duration a placeholder equal to enter a number of days for example 5 12 and so on and we can also give it a class name of form input and we'll also change the placeholder color to gray 100.

**3:10:35** · If you do this, you'll be able to see a duration input so people can enter a specific number of days. And we can also give it an onchange. So I'll say whenever something changes here, take that key press event, call the handle change function that requires a key. In this case, we're changing the duration as well as the value.

**3:11:03** · But before we pass the value, I'll convert it over into a number. So number constructor and then e.target value so we can actually work with it. Because I don't know if you knew, but every single input, no matter if you make it like a type of a number input, it'll still take in the values in form of a string like the URL bar. So you have to convert it back into a number. Great. So now we have the duration as well. What else do we need?

**3:11:34** · Well, we'll need a couple of different select elements that allow us to choose the type of our travel. Are we traveling with a group? Maybe solo, maybe as a couple. Then we have to choose our travel style, our interests, and finally a budget estimate. Select elements are super useful because you're nudging your user in the right direction. You can propose a couple of different options that a user can choose. For example, travel style can be luxurious or maybe adventurous. Maybe budget can be low, it can be high.

**3:12:06** · You can tell your user what you need to hear. And we're collecting all of this information in order to make the best trip possible for them. So, now that we have this second div, which holds the duration, we can focus on mapping on all of these individual select items. Below the div, I will map over our select items coming from constants. See right here, I created an array that has these couple of inputs.

**3:12:35** · Group type, travel style, interest, and budget. And we'll actually map over them. So we don't have to create each one of these one by one. So I'll just take the key and I will automatically return a div for each one of these. This div will have a key since we're mapping over it. And the key will be equal to key. Within it, we will render the label and this label will be an HTML for the key, right?

**3:13:06** · Because we're going to have different properties. So this is a little lesson on how you can map over the elements so that you don't have to repeat yourself. Whenever you map over something, you have to ask yourself what is consistent across all of these different things. We always have a div.

**3:13:25** · We always have a label, right? So these will be there, but the contents of it are going to change. So within it, we'll render the key. So now if you do this and go back, you'll see that now four different labels will appear, each with its own key. I'll call a function called format key. and to it I'll pass the key.

**3:13:47** · What this will do is that it'll actually capitalize some of the letters. So what we're doing here is that we're taking the first letter of every word and then we are uppercasing it. Another little function that AI could very easily create, but AI can't create entire experiences and ideas such as this application that we're creating that allows agencies to generate trips for themselves. Trust me, developers will not be replaced because imagine an agency owner wanting to create this great software for themselves.

**3:14:18** · They can take Vzero Open AI and chat with it for days, but as soon as they need to code something, they will experience bugs. So being able to chat with AI is not enough. You have to know how to engineer things and think of ideas. Perfect. So now that we have this label, let's also create a new combo box component right below. And as a matter of fact, this combo box component will be very similar to the one created above.

**3:14:49** · But you know what? Let's actually create all of its props one more time so you learn how it truly works. First, we have the ID, which will be the key. Then we take in the data source, a very important part of the combo box component. And here I'll say combo box items. We'll take each key and then we'll map over different items within it.

**3:15:15** · And for each one of these items, I will automatically return a modified object where the text is equal to item and the value is equal to item as well. So we want them to be the same.

**3:15:29** · So if I do this, you'll be able to see that now we have solo, couple, family, friends, business for the group type. We have a travel style with a couple of options, interests as well, and then finally a budget. So we could technically select the fields still and say that fields will be text of a type text and value of a type value. Even though in this case, I don't think it's even necessary. We can have a placeholder. We have to make it dynamic.

**3:15:57** · So I'll say select key. That way this will say select travel style, select interest and so on. And actually we can say select key but I'll wrap it with format key so it looks a bit better so that it's not lowercased. Select interest, select budget, select travel style and so on. And then we also need to handle the change. This change will be the same as in the previous select.

**3:16:27** · So I'll copy this part where we're changing. And I'll also copy this part where we're filtering and choosing what to filter by. So let me copy these parts right here. Collapse this back again. And then paste these additional props to it. But of course, we have to properly end it.

**3:16:49** · So let's see what we have. We have the change where we're taking in the value and passing it over to the handle change function. But this time we should not be selecting a country to update. Rather we will dynamically update the key with the value. Okay. Next we head over into allow filtering and then we will try to filter it by the query. So, we're going to run the eupdate data, but we're not going to map over the countries.

**3:17:19** · Rather, we're going to map over the combo box items under a specific key. We're going to then filter over each one of these, not countries, but items. I will render the item to lowercase and I'll check whether it includes the query. If it does, I'll then map over these items. And for each item, I will return the item right here.

**3:17:48** · And then I'll return for the value item as well because they are the same thing. Perfect. Now I have to properly close this. So let's count the closing curly braces and parenthesis together. 1 2 3 4. Do we have more? We do. And we also have to close this one and this one. That's a lot of curly braces. And also here we're not checking for the item.name. Rather it'll just be item.

**3:18:20** · For countries we had names. For items we have just the item itself. And by item I mean each one of these values relax, luxury, adventure or for the group type couple, family, friends, business and so on.

**3:18:34** · And at the end of the day, we can also just give it a class name equal to combo box. And this style or this class will actually apply some paddings, borders, lights. It'll round up the corners, change the text to a bit of a darker color, and it'll just make it fit the rest of the UI a bit better. And you end up with something that looks a bit like this. A much more complete form.

**3:19:03** · Perfect. So now let me collapse this part where we're mapping over these select items. And by the way, if at the end of this form something is not working for you, it could be possible.

**3:19:15** · Following along with me while I'm typing these very complicated ends of curly braces might not be ideal. If you have a typo, that's totally okay. It doesn't mean that you don't understand something. It just means that you made a typo. So, for that reason, I will leave the entire create trip.tsx page in the video kit below. So, you can just copy it over and make sure that your app works. So, now that we have all of these items, what do we do next? Well, believe it or not, I want to display some kind of a map.

**3:19:46** · But in this application, we're focusing on not a very specific location, but rather the entire country.

**3:19:54** · Let's say you wanted to visit Croatia, a country I'm from, and you wanted to find out about the best places you want to visit within that country. That's what this app is made for. So, we don't need to necessarily show a Google map, but just show that country on the world map.

**3:20:11** · So, let's do that by heading over into our app and below these select items, I will render a div. Within that div, I will render a label. And within that label, we'll have an HTML 4 location.

**3:20:27** · And it'll simply say location on the world map. And then within it, this would be super hard to implement otherwise, but now we can just use the maps component coming from Syncfusion. Within it, you can show a layers directive. And within layers directive, you can show a single layer directive to which you can pass some additional props that defines how you want that map to look like.

**3:20:54** · So let's actually head a bit above and like we format the data for the countries, we want to format those countries for the map. So I'll say const map data is equal to an array where we have a country. We can take this from form data country. So we want to figure out which country was selected. But as of now we don't yet have access to the form data. This is a state that we have to create.

**3:21:24** · So right at the top I'll create a new use state snippet and I'll call it form data. Set form data equal to the use state call where it'll be an object of different values. First, let's make sure to import use state from React. And we can also define the type of this state by saying that it'll be a trip form data and it'll have properties such as country.

**3:21:55** · By default, we can select countries zero question mark.name or just an empty string if we cannot get it. We can also set the travel style to an empty string at the start. We can set the interest to be equal to an empty string at the start. Same thing for the budget as well as the duration. And the same thing for the group type. All of them will be empty strings at the start.

**3:22:25** · Let's fix this typo right here. And let's make sure that we actually have access to the countries beforehand. So this const countries coming from the loader data should appear above where we're setting the state. There we go. So now we have this form data and in the map data we're using the one from the country that we have selected right here in the first place. Alongside the country itself, we can also choose a color in which we'll color that country.

**3:22:56** · So I'll say hash E A382 E. I found this color to look pretty good. And then we can also choose the coordinates of that country. So I'll say countries.find we want to find C that specific country. And if that country's name matches the one from the form. So form data. country. In that case, we want to take its coordinates or just an empty array in case we cannot find it.

**3:23:29** · And that will form our map data. So now we can take that map data and pass it over as data source is equal to map data. But a very important question is how are we going to shape that data? So for that reason, Syncfusion has prepared a prop called shape data which gets the set data for the maps to render. And here I'll say world underscore map. I've actually provided this for you right here next to the constants.

**3:24:00** · This contains the list of the coordinates of all of the countries in the world. So if you pass it in and reload the page, you'll be able to see the world. You can also change the shape data path to change it by the name of the country and we can change the shape settings which will be a color value path of color and we can also provide a fill color.

**3:24:31** · So I'll say fill will be equal to E5 E5 E5. So now if you save it you can see that everything will be red.

**3:24:42** · So if we leave it like this, it looks like the entire world has been selected.

**3:24:47** · So we have to say shape data path. And I'll set it over to country. But for the name, we'll actually say shape property path. So now if you go ahead and select a country like United States, you would hope that it'll all light up like a Christmas tree, but that's not really the case. And that's because even though the select fields are here, they're not actually yet storing the values within our state.

**3:25:15** · So what we have to do is we have to implement this handle change function which right now just takes in the data but we have to set that data to the state. So I'll say set form data. We will actually modify the entire object by spreading the previous form data in order not to lose any of it.

**3:25:38** · And then the only thing we'll do is we'll dynamically update a key only the key that we're updating with the value that we're trying to update it with. So, if we do this, you'll notice that now we should be able to change the value of any kind of these fields and that it'll automatically light up right here. Same thing if we select United States. There we go. It's pretty big. So, we can very easily see it on mobile.

**3:26:07** · But, of course, where this shines is on desktop, as you can see it much better. As a matter of fact, you can see even a such a small country like Croatia, which is right here in Europe, you can barely see it on the world map. So now we have a fully functional map that shows you where you want to travel to. For extra points, maybe you can take in the country you're flying from and then create some kind of a flying animation to point to the countries you're going to.

**3:26:36** · But with that said, let's just head a bit below this map component, which for now I will collapse. And let's create a single self-closing div that'll have a class name of BG gray 200 HPX and W full. And this will simply create one line saying that we're at the end of the form. Below it, if we have any errors, we might want to display them.

**3:27:05** · So what do you say that we create a new use state for the error right here at the top? I'll do it right below the current use state. So where we have the form data, I'll create another use state and I'll call it error set error at the start equal to null. And I'll also do another use state called loading set loading at the start equal to false.

**3:27:38** · And I'll also specify that the error can be either of a type string or a type null. So just because it starts with a null doesn't mean that it cannot get any other value. So the way that type inference works with React or Nex.js GS is that if you pass the initial value, the value of that variable will automatically be loaded as the type of that value like in this case the boolean. So for null, it'll by default be just null.

**3:28:05** · But we know that later on we want to switch it to string which is why you have to manually specify which type you want it to be.

**3:28:13** · Perfect. So now let's head back down and let's say if there is an error we will render a new div with a class name of error and within it a p tag where we'll render that specific error. Finally, below the error, we can also render the footer of this form component that'll have a class name equal to padding x of 6 w full.

**3:28:39** · And within it, we can render a button component coming from Syncfusion with a type equal to submit. So, we wanted to submit the form and I'll give it a class name of button class exclamation mark H of 12 and exclamation mark AW of full. Also, if we're currently loading, I'll set the state to disabled. That way, the user will not be able to click it multiple times.

**3:29:10** · Finally, within the button, I'll render an image with a source equal to it'll make it dynamic pointing to assets icons forward slash. But then if we are loading, I'll render the loader.svg else I will render a magic star. SVG.

**3:29:32** · You'll soon see how that looks like. a magic star, I think, has become the official icon or the uh official visual representation of AI generation. So, if I save it, you'll be able to see this button right below. And the image is not really loading. That's because I missed an S right here under icons. So, now we can see those sparkles, the stars. You see what I meant, right? And below that image, I'll render a span with a class name equal to P16 semibold and text-white.

**3:30:05** · And right within it, I'll check if we're currently loading. And if so, I'll say generating dot dot dot. Else, I'll say generate trip. And we can save it. So now we have that final submit button. So this was a super long lesson. We have implemented the front end of the form. But what have we actually done?

**3:30:32** · Well, let's try to summarize everything by console logging all of the values of the form that the user has selected within the handle submit function. Right here, I'll access the event which will be the form click event. So I'll say react dot form specifically of a type HTML form element. First things first, we want to prevent the default behavior of the browser by saying event.prevent default. Oftentimes the event is just abbreviated to E.

**3:31:03** · And the default behavior of the browser is to reload the page, which we don't want.

**3:31:10** · Next, we want to start with the loading.

**3:31:12** · So I'll say set loading is true. And then just before we console log those values, we want to make sure that the user has actually filled in all of the necessary fields because we need them to generate the trip. So I'll check if the form data country or the form data dot what do we have? travel style or the form data interest or the form data budget or the form data dot group type.

**3:31:46** · If any of these don't exist, so if they're empty, in that case we want to set the error to say please provide values for all fields. There we go. So now if you try to generate a trip, it'll say please provide values for all the trips. Oh, looks like we have this huge loading icon right here.

**3:32:10** · Definitely not what we want to have. So we have to change the class name of this image to make it have a size of five.

**3:32:21** · And actually I want to make it spin. So I'll render dynamically by rendering a CN property which will always have a size of five. But it'll have a class of animate dash spin only if loading is turned on. So if I do this, you can now see that it's smaller and it says generating even though that's not really the case, right? Because we have the error, please provide fields or values for all the fields. So let's head back over to the form.

**3:32:51** · And alongside setting the error that we have, we also want to just set the loading to false because obviously we're not submitting.

**3:33:01** · Something went wrong. So I'll set loading to false and simply return out of this function because there's nothing for us to do here. We're missing the values. So now if I reload the page and click the generate trip button one more time, you'll see that it'll stop loading immediately and it'll say please provide values for all fields. Now what else do we need alongside these fields? We also need a duration.

**3:33:29** · So I'll say if form duration is lower than one or if form data duration is greater than 10. Make sure that it says form data here as well. In that case, we'll also render the error loading in the return statement. But the error will say something like duration must be between 1 and 10 days. So I'll save it.

**3:33:53** · And now if I select the duration of 55 days, which is a lot for AI to generate the trip based off of. And when we actually fill in all the other things, you'll notice that it'll actually say that the duration must be in between 1 and 10 days. Perfect. Finally, we should not be able to generate a trip in case our user is not currently logged in. So this functionality is only there for the logged in users.

**3:34:24** · So after this if statement I'll try to get the user by saying await account coming from apprite.get and then if there is no user dollar sign id in that case I will console. And say user not authenticated I will set the loading to be false and I will exit out of the function.

**3:34:52** · Finally, after all of these checks, I'll open up a try and catch block. In the catch, I will just render the error. So, con error is error generating trip and we'll say what the error is if we have already gotten to this point. I'll also add a finally block. So, whatever happens, whether we're successful or not, we want to set the loading to false.

**3:35:19** · And in the try for now, let's just console log the user so we know which user is trying to create a trip. And let's also console log the form data so we know what kind of trip they're trying to create. So with all of that in mind, let's try to generate a random trip. Trust me, I will just randomly scroll through all of these countries. So, I was just about to create the trip, but my app crashed for some reason.

**3:35:51** · So, I just reloaded the server. Oh, it looks like we're getting this process fetch failed. Interesting.

**3:35:59** · What is it failing for? Is it maybe for the countries? Well, if I manually head over to this API, this endpoint seems to be working well. So, it must be something that we have recently added to the application. Well, looks like we're good again. Well, we'll see whether we can try to replicate that error soon.

**3:36:20** · But with that in mind, I'll try to create a new trip completely randomly.

**3:36:25** · Okay, I'll be selecting some of the values here. For example, Virgin Islands, maybe a couple of days. Let's go with a family. I want to see some culture. Let's do museums. And let's do a budget of luxury. Perfect. And I'm not sure whether United States Virgin Islands are so small that we cannot see them. Or maybe our map is not working properly. So let me select something else. Let's go with Bahamas. And there we go. It's also barely visible, but I can see it there.

**3:36:55** · So now if I click generate trip and go to inspect and open up the console, check this out. We are getting back the user information as well as the form data including the budget, country, duration, group type, interest, and travel style. All the information that we need to generate a proper travel advice. So now that we have this proper form, let's actually use that data in the next lesson.

**3:37:26** · Let's use that data to generate the AI trip.

### AI Trip Generation

**3:37:34** · Okay, the form is here, but my trip to Bahamas is not yet ready. Why is that?

**3:37:41** · Well, it's because we haven't yet implemented the Gemini AI itinerary generation. So, let's do that next. You can head over to a studio.google.com and consent to sell your soul. Once you do that, you'll see that you can get started with Gemini, but you'll have to sign in to get access to the dashboard.

**3:38:03** · Within the dashboard, you'll be able to create your API key. So just click create API key on the top right and you can search for your Google project. It automatically finds it right here and you can create it in that existing project. Once it get generated, copy it.

**3:38:20** · Head back over to your application within yourv and add it as Gemini. I'll call it Gemini API key. and I'll paste the key that I just got. But Gemini is not the only thing we'll use to generate our trips. You'll want to head over to unsplash.com/developers. Unsplash being the largest image provider in the world that offers stock free images. So, you'll want to register as a developer by filling out this form.

**3:38:49** · Once you verify your account via email, just go ahead to create your application. Let's agree to all of these right here. and I'll say travel agency and create the app. Now it'll let you actually create the app. So if you scroll down, you'll be able to see your key. I'll copy the access key and save it to my app as Unsplash and I'll call it Unsplash access key. Perfect.

**3:39:20** · Now let's actually put these great APIs to use within our codebase. To do that, I'll head over within my terminal and I'll run mpm install at google slg generative AI and press enter to install it. Then we'll want to head over to routes.ts and we'll add a new route, but this time we'll add an API route.

**3:39:48** · Can you believe that? an API backend route within ReactJS. No Nex.js, just React. That's what's possible with React Router V7. So head over here and create a new route with a path of API create trip and the file will be routes API create-trip.ts instead of TSX.

**3:40:21** · So if we do this properly and add a comma that now allows us to create that file. So head over to your file explorer head over within the app routes and within routes create a new folder called API and within API create a new file called create trip.ts. within it will deal with the logic of creating this trip and all of that will be just a regular function.

**3:40:52** · In this case, we can even call it an action. So I'll say export const action is equal to an asynchronous function that gets access to the request which will be of a type action function args coming from react router and then we can define exactly what this action will do.

**3:41:17** · For example, we're going to pass some props to it through the request object so we can automatically dstructure them.

**3:41:26** · This is the data coming from the form.

**3:41:28** · So what do we have coming from the form?

**3:41:32** · We already saw it in that console log.

**3:41:35** · So I'll say const and dstructure the country. I'll also get the number of days. Let's also get a travel style interests budget group type and the user ID. and that'll be equal to await request.json. Let me save this and reload the page. I might also need to reload my terminal.

**3:42:03** · That is one thing that I noticed needs to be done after you add a new route. So if I do this and reload, we should be okay, I believe.

**3:42:14** · But now we're getting cannot read properties of null reading use context.

**3:42:19** · But after that, we're good. So, there's still some things that could be improved with the overall developer experience, but again, being able to use server actions within React. Pretty crazy, right? Okay. So, now that we have all of this info or the data from the form, how do we actually pass it to AI to generate it or to make something useful out of it? I'll say const genai is equal to new Google generative AI to which we need to pass the key.

**3:42:48** · So I'll say process.env.jemini API key and you can add an exclamation mark to let it know that we know that that variable will be there from env. We can do the same thing with the unsplash key by saying const unsplash API key is equal to process.env unsplash access key just like this.

**3:43:12** · We can then open up a try and catch block and in the catch we can simply console that error saying error generating travel plan and then we can console log the error that happened. But if everything is going well then we need to figure out a prompt that we'll use to generate that trip. So say const prompt is equal to a template string.

**3:43:44** · And here you can really go all out. Template strings allow you to split them into multiple lines. So you can be very descriptive. The more descriptive you are, the better it'll be. So we'll need to say something like generate a number of days day itinerary for country based

**3:44:11** · on the following info and then you can pass additional user information such as the budget can be set to well a string of a specific budget. You can repeat the same thing for what else do we have?

**3:44:27** · Maybe interests. So, we can close the interests right here and then pass over the interests. And you can keep repeating that until you pass over all of the information. But typically, when you're telling AI what it needs to do, you also need to be very descriptive of the format in which you want to receive that data back. So, if you head over into the video kit, you'll see that here I provided the entire create trip prompt. So just go ahead and delete the current one that we started typing. Or you know what?

**3:44:58** · Type one yourself and then paste the one that we have right here. You'll notice that this one looks like this. It is exactly the same as we started typing it, but it also covers more different pieces of info such as interests, travel style, group type, and then I specify how it should return the itinerary and specify the lowest estimated price in a clean non-markdown format with the following structure.

**3:45:27** · We wanted to have a name, a description, estimated price, duration, budget, travel style, and so on. Specify the best times to visit. Share some weather info, the location, the itinerary, and then we specify how the itinerary should look like dayby day.

**3:45:47** · The more info you give it, the better the result will be. Finally, we are going to call that AI and pass over the prompt and that will result in the text result. We can do that by calling await genai.get get generative model. And here you can choose whatever model you want. In this case, I'll aim for something like let's do Gemini 2.0 flash.

**3:46:15** · I think this one is pretty fast, so we should get the results very quickly. And we can also do generate content based on the prompt like this.

**3:46:29** · So now we're passing that prompt into it. And then we get back the trip data.

**3:46:35** · So const trip is equal to parse markdown to JSON of the text results.ext. This parse markdown to JSON is a function that while I was writing this app for the first time, I asked AI to actually write it, which basically takes in a markdown text and it turns it into well JSON, right? The way it works is it simply parses it and then it runs JSON.parse on it.

**3:47:05** · So now that we get this trip, what do you say that we also get the image of that country from the Unsplash API and then merge it with that result of the itinerary. That's what'll make it stand out.

**3:47:21** · So I'll say const image response is equal to await and we want to make a fetch request to https col/ slash api.unsplash.com slarch slphos question mark query is equal to and then we can pass the country and then we can also pass some interests. So that way it'll match very closely with what we need.

**3:47:51** · Alongside the interests, we can also pass in the travel style. And then we can append the end sign and then pass the client ID. Client ID is equal to unsplash API key because without it, it would not return anything. So now that we have this image response, let's actually get some image URLs.

**3:48:17** · So I'll say const image urls is equal to in parenthesis await image response.json JSON. Outside of this parenthesy, we want to say dot results dot slice from 0 to three to get the first three. And then we want to run the map on it where we get each individual result of a type any. And for each one, we want to get back the result urls regular or if it doesn't exist, we can get the null.

**3:48:50** · So once we have that, this will actually give us the images and prepare the URLs so we can save them into the database. Finally, we are ready to create a trip within the database. So I'll say const result is equal to a weight database.create document. Make sure to import this database coming over from apprite.

**3:49:16** · And we can pass in the database ID coming from the apprite config as well as appite config dot trip collection ID.

**3:49:28** · We need to give it the id of that specific trip. So it'll be id dot unique also coming from apprite. And let's see why do I not have access to this create document. Oh no, I have access to it, but it's saying that I need to pass a few more props such as the last object which contains the trip detail. Again, I think in the database we call the detail without the s. So make sure that you stay consistent.

**3:49:54** · And what we'll do here is say JSON.stringify and we'll pass over the entire trip that was generated for us by AI. We are using the stringify because it allows us to save the trip detail object as a string in the database and later on safely restore it by using JSON parse. Alongside the trip details, we can also get the created at which will be a new date to ISO string.

**3:50:22** · So we're getting the current date and time, the image URLs attached to it as well as the user ID.

**3:50:31** · So once we create this new result in the database, we'll return the data and pass over the id as result dot dollar sign ID. And this data is actually coming from react router because we need a way for us to return the data that is the result of this server action. And in this case, I have this error issue. It is just E. Perfect.

**3:50:56** · So the only thing that remains for us to do is to call this API endpoint within our codebase that is then calling additional API services from within our form. So we can head back over to create trip.tsx and go right here to where we were console logging the form outputs.

**3:51:19** · So if I now head back over here, we know where we were right here. I'll just say const response is equal to await. We're going to use a simple fetch to hit our API create trip endpoint. And I'll also pass some options to it such as a method of post headers equal to content type will be set to application JSON because just we want to pass some JSON over.

**3:51:48** · And finally and most importantly, we want to pass over the body which will be stringified. So I'll say JSON.stringify an object that'll have the country coming from form data dot country number of days which is form data dot duration.

**3:52:12** · We'll also get access to the travel style which is equal to form data.t Travel style interests equal to form data.inter interests budget equal to form data.budget budget group type equal to form data.group the group type and yeah, you definitely could have dstructured the form data so it'll be much easier to get it. That way you wouldn't have to repeat yourself here.

**3:52:42** · I believe we stored it without the s just interest. And then finally group type and to it we can also pass the user ID as user dollar sign ID and this is making a request to the trip. So this response right here should correlate with what we are returning from the actual server action which is basically the generated trip. So let's actually extract it right after the response.

**3:53:14** · I'll say const result of a type create trip response will be equal to await response.json JSON and then we can check if result has its own ID then we can navigate over to that trip's detail page. So right at the top of this component I will use the use navigate hook. So I'll say const navigate is equal to use navigate which is coming over from react router.

**3:53:46** · And then right here I'll navigate over toward slash trips slash result ID. So we want to go to trip details page. And we can also add an else. So I'll say else we can simply console. Say failed to generate a trip.

**3:54:12** · Perfect. So now we have completed the second piece of the puzzle. The first one being the actual Gemini generation and adding Unsplash images and returning that as an output of our own server API endpoint action. And then the second part was actually passing the data to it while calling it from our front end and then navigating over to the trip details page. So what do you say that we give it a shot? I will open up my browser in its full glory. Enter a country. I'm very interested.

**3:54:43** · What will it do for my country? In this case, you can put yours to see what kind of trip does it generate. I'll give it 7 days. For the group type, let's be romantic and do a couple. Travel style will be interesting. Let's do relaxed. Let's do historical sites for interests. And for this person, let's say that budget is not really important. They want to do luxury. Perfect. So, let's generate a trip.

**3:55:14** · It'll take some time to actually generate it as you can see because AI right now is thinking it's producing the output and it's sending it over to our app. Looks like the generation stopped.

**3:55:29** · So, either something went right or something went wrong. So if we open up the console, it looks like we got error generating trip with a syntax error of unexpected token U. Unexpected is not a valid JSON. It's good that we console log the error. So it actually comes from error generating trip. So that should help us a bit. You can see that it's not coming right here as the else statement.

**3:55:58** · It's not coming as part of our own API response. Rather, it's failing right here. error generating trip. If I open up my dev terminal, we can see that we got the issue here as well and it says value is not JSON serializable and we got another error this time from our API saying apprite exception collection with a requested ID could not be found. Okay, interesting. So now it's pretty clear where the issue is. It is back within our server action where we're trying to generate a trip that is right here.

**3:56:32** · So I'm pointing over to apprite config.

**3:56:35** · It's saying that collection with the requested ID could not be found. So obviously this is the issue. App config trip collection ID. Let's see. Trip collection ID. Importing it from vit apprite trips collection ID. And if I head over to my env. I'm saying apprite trips collection ID. So, this is looking good to me.

**3:56:59** · So, it might be best to crossverify over on AppRight dashboard by heading over to databases and then trips collection. I'll recopy this ID and then back in our application, I'll paste it here. Oh, looks like I missed the number right there. So, it's actually highly likely that it worked for you on the first try. But while I was messing with my env. Well, looks like I deleted a number accidentally.

**3:57:28** · So, if I head back over to my application and click generate trip one more time. Let's see what happens.

**3:57:37** · Now, it is generating. And it looks like it stopped one more time. If it didn't stop, we would be redirected to another page. So, if I open up the console, looks like it's pointing to the same issue. Is it? Maybe I have to reload the terminal.

**3:57:54** · Now that I reloaded it, it might work.

**3:57:56** · Who knows? Third time's the charm. Okay, the third time didn't work. It's not the charm. So, it looks like this time we got a different error saying that our document structure is invalid. Missing field trip details. So, it looks like I did actually rename it to details and not detail. So, if I go right here and change this over to trip details, we can crossverify that right here. Yep, it's trip details for you.

**3:58:24** · It might be detail you'll need to check out with your own database. So, let me give it a go. Maybe it worked for you in the first try and you're just seeing me fail. How does that make you feel? Okay, there we go.

**3:58:36** · Um, I didn't think I would be so happy to see a 404 page, but I am. Uh the fact that we're seeing this 404 page means that we came all the way to the end of our process because if everything goes right and if the new record has been created in the database only then will it redirect us to that trip details page. And even though we cannot see the whole thing right away at least we cannot see it in this beautiful layout it doesn't mean that it doesn't exist.

**3:59:05** · If you head over to Apprite, go to the trips database and check out documents, you'll see that one of our users has created their first trip. So, if you want to check it out, you can just head over to data and check this out. We have three separate image URLs matching what a user searched for. Yep, you can actually see those images already by simply navigating over to this URL and you'll see some of the nice photos.

**3:59:34** · These are looking good. And we also have the created ad field, the payment link which we will add later, the user ID that created it, and most importantly, the trip details generated by AI. So here you can see that it actually gave a name to a trip, luxury, creation, history and romance, a couple's escape. And it gave us a lot of information that we might want to use to nicely display right within our application, which is exactly what we'll do in the next lesson.

**4:00:04** · But first, I'll go ahead and commit the changes we have right now. I think I might have forgot to do it in the last lesson, but that's fine. We'll do it right now. I'll say get add dot get commit-m and I'll call it generate trip using AI and I'll push it.

**4:00:23** · So in the next lesson let's focus on generating this beautiful trip details page so we can finally see what our app actually does now that we have spent a lot of time making it happen. Great work. We're past the most complex parts of the app.

**4:00:44** · So, if you reach this point, leave a comment down below and let me know, "Hey, Adrian, I passed the AI trip generation and now I'm ready to dive into the trip details." See you there. Once we create a new trip, we'll redirect the user to that trip details page. But that page doesn't yet exist, and we don't yet have the function to retrieve our trips. So, let's start with that.

### Trip Details

**4:01:11** · I'll head over into appreite and then I'll create a new file called trips.ts. Within this trips, we can do the full logic for fetching all the trips or fetching just a single trip by ID. So I'll start by exporting a new function called get all trips and it'll be equal to an asynchronous function inside of which we'll try to fetch those trips.

**4:01:39** · So I'll say const all trips is equal to await database coming from apprite dot list documents and then you know the drill. We have to provide the database ID coming from apprite config database ID as well as the collection ID coming from app config dot trip collection ID and finally we have to query the trips that we want to get.

**4:02:04** · So to implement pagionation here as well, we can accept the limit of a type number as well as the offset of a type number into this function. And then once we turn on the query coming from apprite, we can limit it by a specific number of elements per page and we can query it by a specific offset. So if we have already seen the first page, we can move off to the second one. And finally, I'll also add the query.order order descending based on the created ad.

**4:02:37** · So we can see the newly created trips at the top.

**4:02:42** · Finally, if all trips total is triple equal to zero, in that case, we can simply console. And say no trips found. And we'll return an object that says all trips is equal to an empty array. And the total will be set to zero. But if we do have some trips, I'll return an object that'll say all trips is equal to all trips. And the total number of trips will be set to all trips dot total.

**4:03:18** · Perfect. So this is the function that allow us to fetch all of these different trips. And I also want to create a function that allow us to fetch the trip details for a specific trip. So I'll say export const get trip by id and it'll be equal to an asynchronous function that accepts a trip id of a type string and it simply fetches it.

**4:03:40** · So I'll say constrip is equal to a wait database get document singular this time and we again have to provide the database ID. So app config database ID the collection ID so that'll be app config trip collection ID and finally the ID that we want to fetch it based off of which is going to be the query.

**4:04:08** · So just trip ID like this and this will be called trip not trips. So once we get that trip I'll check if there is no trip dollar sign ID. In that case, we can simply do a console log and say trip not found and we can return null. But else if we actually fetch the trip, we can return that full trip details. Perfect. So now we have those two functions that allow us to fetch the trip details either a single one or all of the trips together.

**4:04:40** · So what do you say that we go ahead to our routes and we create a route for the trip details page. We can do that by creating it like this and then pointing it over toward slashtrips slash colon trip id. So this is the first time that we're defining a dynamic route based on the ID. And you do that by simply providing a colon right here at the start similar to what you do in express for example.

**4:05:08** · And we can point this over to routes/admin/trip-detail.dsx. And now we can create that trip details page by heading over to roots admin. And we can create a new trip detail. DSX where you can run rafce. And here we just want to be able to quickly fetch the details of that specific trip. So let's do just that.

**4:05:36** · I'll create a new loader at the top by saying export const loader is equal to an async function that gets access to params of a type loader function args. Now what are these params that I'm trying to fetch right here?

**4:05:55** · Well, the params are going to be whatever is dynamic. So in this case, remember this ID? Well, that'll be fed into params ID. So we can extract that number. So in this case I want to say const trip ID and I want to dstructure it from the params. Then once I have the trip ID I'll say if there is no trip ID I'll throw a new error saying trip ID is required. But if there is a trip then we can fetch it by saying con trip is equal to await get trip by id.

**4:06:27** · This is the function that's coming from apprite trips right at the top and to it we have to pass the trip ID of course. Once you get it, we can simply return that trip.

**4:06:42** · So if you do this properly, you'll be able to fetch this trip data right here at the top because you already know the drill. We're getting it through the loader data of a type route dot component props. And this route is coming right at the top by importing the type of route from slash plus types forward slash and then the name of this file. So if you have done this properly, you should be able to just say const trip data is equal to parse trip data.

**4:07:18** · This is coming from lib utils. And to it we'll pass the loader data question mark. Trip. So let's see what exactly this parse trip data is doing. Basically the only thing it's doing is it's taking that trip and it's parsing it because before remember we passed it over as a stringified version. So now we want to extract the actual data. So what do you say that now that we get this data we extract the name out of it.

**4:07:42** · So I'll say const name and then is equal to trip data or just so it doesn't break if we don't have the trip data try to get it from an empty object. So now we can show this trip details. First I'll wrap everything in a main tag. Give it a class name equal to travel detail and a wrapper class name.

**4:08:04** · Then within it we want to render a header component coming from components with a title of trip details, a description of view and edit AI generated travel plans and we can close it right there.

**4:08:20** · Below it, I'll render a section that'll have a class name equal to container and a wrapper MD so we can see the content in the middle of the screen within which I'll render a header within which I'll render an H1 where we can render the name of the trip. To style it a bit better, let's give this H1 a class name equal to P40 semibold index-d dark 100 just so we can see it clearly.

**4:08:50** · So if you do this, it's possible that the app is not working because we have added an additional route. So let me actually rerun it one more time. It'll quickly spin up on localhost 5173, which is when we can reload. And now if we head over to AI trips, we don't really have any trips yet. We could go ahead and create a new trip so we get redirected to it. But what we can also do is just head over to trips forward slash and then we can get the ID of the trip from apprite database.

**4:09:19** · So head over to appite databases trips and then copy the document ID. Once you do that you can append it to a URL. So we get redirected to the trip details page.

**4:09:32** · But now the issue is that we don't yet see the name of the trip. So something could be wrong with us fetching the data. So first I want to see what we're getting outside of this loader data by console logging it. So if I console log it right here and open up the console, it seems that we're getting the object that then contains the trip details within which we finally have that string. So what I'll do is I'll try to render the loader data dot trip details instead of a trip.

**4:10:05** · And if we do that properly, you see that now on the right side, we're getting a luxury creation history and romance, a couple's escape.

**4:10:13** · So that means that we have successfully retrieved the trip details coming from the database. In this case, we can just automatically return the trip. No need to declare the variable and then return it. So I'll just simply say return await get trip by ID. Perfect. So now we're fetching the trip details. And now we can slowly start rendering all of the additional information about this trip.

**4:10:40** · But before that, we'll need one more component to show the trip duration and location to make sure that it looks exactly like it does on the Figma design. So let's create a component for these two little chips. We can do that by creating a new component within components and I'll call it info pill.tsx.

**4:11:01** · tsx. I'll run rafce and I will export it through our components folder as info pill and then we can import it over within our trip details right below the header. I'll call it info pill and render it from components. Now to it we'll have to pass some props maybe such as a text in this case for the duration. So I will render a dynamic duration and then we can say how many days. So 7 day plan for example.

**4:11:32** · But the question is where is that duration coming from? And the answer is that it's coming from the trip data. So here we can dstructure alongside the name all of the other properties that we'll have such as the duration, the itinerary, the travel style, the group type, the

**4:11:57** · budget, interests, estimated price as well, the description, the best time to visit, the weather info, and the country. So, we're getting all of that info from the trip data. And now we can just render this text. And we'll also render the image alongside that info pill, which will be forward/assets/icons/cal.svg. So, if I now save it, we need to head over into this info pill and implement it.

**4:12:28** · It'll be super simple. We will just accept those two props such as the text and the image which can be of a type info pill props. And then we can return a figure with a class name equal to info pill.

**4:12:48** · Within it we can also render an image that'll have a source equal to image with an al tag of text. And below the image we can render the fig caption that'll simply render the text. So, if you do this, you can now see a nice 7-day plan right here. And you can simply duplicate this info pill. And for the second one within here, we want to render the location or rather that'll be the itinerary.

**4:13:15** · So, if you try to render it like this, you'll notice that it's actually an object that has day, location, and activities. So, we have to parse it so we can properly show it. So, I'll say itinerary question marks slice from 0 to two. So we only want to show the first two elements and then we can map over those items. So map where we get each individual item and we only want to extract the location for each item and then we want to join them together by using a comma.

**4:13:45** · So join with a comma and a space or if it doesn't exist an empty string. So if you do this now we can see split split uh which doesn't stand for JavaScript split function actually it is a name of the city in Croatia for some other one maybe it gets two different cities that actually make some sense and instead of a calendar we can render the location marks SVG. So you can see that this is actually the location. Perfect.

**4:14:17** · So now we have those two pill components right here. And that allows us to focus on creating the rest of the layout. So I will actually put those pills within the header component right below the name.

**4:14:33** · And I actually want to put them one next to another. So I'll put them within a div. I'll open it here and close it here. And I'll give this div a class name equal to flex items center and a gap of five. So now they will appear one next to another and then we can head over below this div below the header but still within this section we can create another section within it. This one will be for our gallery the most important point of our trip.

**4:15:05** · So I'll say class name of gallery and within it we want to map over the image urls. So now the question is where are these image URLs coming from? and they are going to be a part of the trip as well but not part of the trip details. This is the text that was generated through AI. The image URLs are going to be a separate property under these trips. How can we know that?

**4:15:32** · Because if you go into our apprite trips, right? You'll notice that when we return the get trip by ID, we're returning the full trip. And if you remember how this trip has been stored into the database, you will know that trip details and image URLs are two separate properties.

**4:15:52** · So we have to extract them separately.

**4:15:55** · Image URLs is equal to loader data question mark image URLs or an empty array if we don't manage to get any of them. So if we do that, we now have image URLs. And you can see that we're mapping over three of these image URLs right here. So instead of simply mapping over them, what we can do is say map and we are going to get a URL of a type string as well as an index for I of a type number.

**4:16:24** · And for each one of these, we want to simply return an image that'll have a source of URL and a key of I. If we save this, you should be able to see three images appear right away, but they are of different aspect ratios. So, we want to make sure that it actually still looks good. So, I'll give it a class name equal to CN. And it'll always have a wful, a rounded- excel, and object- cover.

**4:16:57** · So, we round up the corners a bit. But then if it's the first index, so if I is triple equal to zero, in that case we'll give it a on medium devices call span 2 on medium devices row span 2 and a bit of a bigger height of 330 pixels.

**4:17:21** · But if it's not the first one on medium devices, I want to give it a row span one and a height of only 150 pixels. So if we save this, you'll see that now the first one takes more space and the second two take less space. This is okay on mobile, but where it really shines is of course on desktop where you can see that now we have this nicel looking layout that gives you the idea of that trip in a glance.

**4:17:52** · You don't have to take a look at three separate pictures. You just take a look at this portion of the screen and you get a general idea of what these places are all about. Now we can head below this gallery section right here and we can create another section this time for different chips talking about what this travel is all about.

**4:18:14** · So what I'll do here is I'll create a section and give it a class name of flex gap of three on medium devices a bit more gap of five items center and a flex- wrap so they wrap nicely on mobile devices.

**4:18:31** · Within this section, I will render a chip list component coming from Syncfusion with an ID of travel chip and within it I will render a chips directive so we can choose exactly how each one of them looks like and then we have to figure out what we will map over.

**4:18:51** · So right above I'll create a new object const pill items which will be equal to an array where we're going to have different objects we're mapping over such as the text where the first one will be we'll talk about the travel style which we're taking from the trip data and we can also provide a background color to it so we differentiate all four of them maybe something like a BG pink of 50 and uh text of pink of 50 as well.

**4:19:23** · And now we can repeat this three more times. For the second one, we can talk about the group type. For the third one, we can talk about the budget. And for the fourth one, we can maybe talk about interests. And we can change the color for each one. So the second one will be BG and text primary. After that we can have BG and text success. And finally we can have maybe BG and text of Navy.

**4:19:52** · And in this case I think we'll have to make the text a bit more pronounced. So for the primary I'll call it 500. For success I'll do 700. And for navy I'll do 500 as well. Perfect. So now if we do this, we'll be able to head down and we can map over these pills right here within chips directive. So I'll go right here and map over the pill items.

**4:20:20** · And for each one, we'll get access to a pill as well as the index. And for each one we want to automatically return a chip directive also coming from Syncfusion which will take in the key of I a text where we can render the pill.ext and also the CSS class which we can use to style it a bit more. So I'll make it dynamic and I'll render the background right here.

**4:20:53** · So pill.bg BG text-base font-bium and a padding X of four. If we do this, you'll be able to see four different chips, but they're not really that visible, are they? And it seems like some have multiple words. This one doesn't have any text at all. So, what we can do is we can style the text a bit more by wrapping this build text into the call of the get first word function.

**4:21:24** · What this will do is it will extract the only the first word of that text. You can see it trims the words, splits it and then returns the first one. So now here we can see only historical for example. Also the colors don't seem to be matching. So let's see what's happening with this pink one right here.

**4:21:42** · Maybe we should do pink 500 in order to be able to see it better. There we go.

**4:21:46** · That's a bit better. So now on a glance we can immediately see what this trip is all about, how long it lasts, which cities are we visiting, the look and feel of it, and then we can see that it's relaxed, couple-based, luxury, and historical. What else can we show for this entire trip? Well, let's follow the design. Right now, we have this part done. And the last part before we can render the actual AI generated itinerary is going to be the rating. So right here we can render the rating.

**4:22:15** · So to do that we'll remain in the current section but we'll go below the chip list component and I will render a ul an unordered list with a class name equal to flex a gap of one and items center. And within it we can create a new array of five elements that will fill with no values. So, null.

**4:22:46** · And then we want to map over those values. I'll simply put an underscore right here because we don't really care about what the values inside, but we do care about the index, which is the second parameter. And then for each one of these empty elements in the array, we want to return a list item with a key of index. And we simply want to render an image that has a source equal to assets icons star. SVG with an alt tag of star and a class name of size of 18 pixels.

**4:23:24** · If you do this, you should be able to see five stars appear right here. And we can also head below this dynamic part and render one last list item with a class name of ML1. So margin left one to divide it a bit. And we'll render one last chip list component with its chips directive with a single chip directive inside. So that will look like this.

**4:23:53** · And this one will simply render a text of something like 4.9 out of five. We're not collecting the data on the quality of these strips.

**4:24:04** · So that might be something that you might want to implement to be dynamic later on. And I'll give it a CSS class of bg red 50 and text- red 500 just to see how it looks like. There we go. We can also maybe make it yellow just so it matches the stars.

**4:24:23** · So if you do this, you should be able to see it like this. We can even make it a bit darker because yellow is not that visible. There we go. This is looking good. So now we can exit out of this li ul and the section. And we can focus on creating the last section, the one that matters the most, which will be the header of the trip. So it'll take the title, the description, and the budget.

**4:24:46** · And then after that, we'll be able to render the entire itinerary. So let's do that by giving this section a class name of title and then within it we can render an article within which we can render an H3 that'll say duration dash day country travel style trip. So we're combining everything into one. 7-day Croatia relaxed trip.

**4:25:13** · After that, we can render a P tag that'll render the budget, the group type as well as interests. So, if we save this, we can also see that this is a luxury couple and historical sites. And outside of that article, we can also render an H2 that'll render the estimated price. So, we're taking all of these different pieces of info and putting them together. Finally, check this out. I'll head below this section for the header and I'll render a p tag.

**4:25:44** · That'll render the description. If you do that immediately, you'll have a very short description. So, we can give it a class name equal to text-sm on med devices-l font-normal and text- dark 400. So, we can kind of style it a bit more like a regular description. And then below it, we're finally ready to map over the important info. So I'll head below the P tag.

**4:26:15** · And I'll create a UL, an unordered list with a class name equal to itinerary. That simply means kind of like steps in the trip like how is the trip going to play out. We want to take that itinerary and map over it by using the map. And what we get is a day plan.

**4:26:36** · So for each part of the itinerary we get one special day plan and we get an index of that day. So then for each one of these we can automatically return an LI. We have to close it as well properly and I'll give it a key equal to index. Let's see if I have closed that properly. We have a ul.

**4:27:02** · Oh, looks like I have one extra parenthesy right here. Now we should be good. And within this LI I will also render an H3 that'll say day plan day and then day plan. So this way we can specify in which cities we're in within which day.

**4:27:25** · So let's see if we can somehow show more of the locations right here. Maybe instead of uh just uh slicing two, we can maybe get more just so we can see that we see different cities right here.

**4:27:38** · There we go. I think this is good. So now we get the idea that there's going to be more cities, but you can see all of them right here, right below.

**4:27:45** · Perfect. So let's scroll a bit down and alongside just the title of each day, we want to show the activities planned for that day. That's what actually matters.

**4:27:55** · So I'll create a ul and map over the day plan activities dom map where we get each individual activity and an index for that activity of a type number and for each one we want to automatically return a list item with a key equal to

**4:28:15** · index and within it we can return a span that will render the activity time and below it we can render a p tag that will render the activity description. So if we do this you should be able to see that now we have morning afternoon evening and we have that for each one of the days right here. We can style it a bit differently by giving this span a class name of flex-shrink-0.

**4:28:49** · We can also give the P tag a class name of flex grow. So if it needs more space, then it'll actually expand to fit that space. But already this is looking great on mobile. What we can do is maybe just bold this span a bit by giving it a P8 semibold maybe.

**4:29:11** · There we go. That's a bit better. So now it's standing out. We see morning, afternoon, and evening. And we have some emojis so we can very quickly browse. We just scan through what's happening. I won't yet show how it looks like on desktop. If you want to, you can check it out on your end. But I want to just finish it off by also sharing some information about the city as well as the weather information. So below this ul where we have the itinerary, I want to map over something new.

**4:29:38** · Actually, I want to map over two different things that I want to combine into one. So, right at the top below the pill items, I'll create another array called visit time and weather info. And within it, I'll render the title for each one. This one will be best time to visit. And here we can render the items of best time to visit.

**4:30:09** · And for the second one, the title will be something like weather info. So we know what clothes to wear and the items will be weather info. So if we now save this, we can take it over and map over it right here below the ul by saying visit time and weather info map where we get each individual section. For each one of these sections, we can return a section.

**4:30:42** · And let's properly close it as well. We can give it a key equal to section.title and a class name of visit. And then within the section, we can render a div with an H3 that'll render the section.title. So if we save it, you should be able to see that we have best time to visit and weather. And then below that H3, I will render another ul that'll simply map over the items.

**4:31:12** · So section do items do map where we get each individual item. And for each one of these, we want to return a list item with a key equal to item. So let's fix this typo right here. That's going to be a key. And I'll just add a question mark here in case we don't have access to the items. And we can render a P tag that'll have a class name equal to flex- grow. And within it, we can render the item itself.

**4:31:43** · So if I save this, you can see best times to visit April to May, June to September, September to October or November to March. And we can see different temperatures in different parts of the year. So, if you like summer more, it's very warm, 25 to 35 degrees or 77 to 95 Fahrenheit. Or in the winter, it's getting pretty cold.

**4:32:06** · Depending on where you are in the world, this maybe isn't warm and this maybe isn't cold, as maybe you're experiencing some very different temperatures. So, since this is a travel application, comment down below and let me know where you're watching from. So, just drop in the name of your country and maybe a flag emoji just so we can see where you guys are from. But with that in mind, we can head over below this section.

**4:32:30** · Basically, below all of the sections.

**4:32:32** · So, I'm going to get down below this one and below this closing one where we have all the details. And I'll create one last section. In this one, we're going to have an H2 that'll say popular trips. So, if the user has scrolled to the end of their trip details, it means that they like it so much, so they're going to go for it.

**4:32:55** · Or maybe it means that that trip isn't really their favorite. So, maybe they want to check out some other popular trips on our site. So, to do that, let's give this section a class name equal to flex flex- call and a gap of six. And we can give this H2 a class name of P24 semibold. Text-d dark 100. So that's going to make it stand out a bit more.

**4:33:22** · And right here we need to map over our trips. And for that thankfully we have created our server action that does just that. It fetches all the trips. We have done that just before we have created the fetch trip details function. So fetching it will be super simple. The only thing you have to do is say const all trips is equal to loader data dotall trips as a trip array or maybe an empty array if we don't have anything else.

**4:33:55** · And now we have to actually call that within the loader. So currently we're just returning the trip details. So you can see that here it's complaining that loader data does not contain all trips.

**4:34:07** · So what we have to do is right below trying to fetch a specific trip we can also try to get all trips. So that'll look like this. const trips is equal to a weight get all trips. And to it we have to pass the limit of trips. So maybe we can just limit it to four of the most popular ones. And make sure to import this get all trips from apprite trips. And then once you have it over here, you can simply return it as well.

**4:34:37** · So now we'll actually have to put this into a new variable. Const trip is equal to await get trip by details. So so far we have been only returning a trip. But now alongside returning a trip, we also have to return the trips. So let's actually do it as part of an object where trip will simply be a trip and then all trips will be trips dot all trips do map and

**4:35:08** · we only want to take what we need from each one. We don't need all the info. So I will dstructure the dollar sign ID, the trip details as well as the image URLs and then we can automatically return like this parenthesis and then curly braces the ID equal to dollar sign ID. We can parse all of the details by saying data.parse trip data because remember it's in a string format.

**4:35:36** · So we have to first pass it into this parser function and then we can say image urls is going to be image urls or simply an empty array. Perfect. So now we're returning that from this function. You can see we immediately lost all of the trip details because now it'll actually be coming as part of the trip. So we have to say loader data. URLs and trip.trip details.

**4:36:02** · If you do that, you'll see that now we get this data back. If in case it's not there, I'll just add a question mark so TypeScript doesn't bother me with this. And now we are ready to show the other popular trips. We can do that by just mapping over them.

**4:36:21** · So right at the bottom I'll create a div below this h2 that'll have a class name equal to trip-grid and we'll call the all trips and then say map where we get each individual trip and for each trip we want to render a trip card which we have already created as a reusable component that needs to accept all of these different things. So let's give it an ID equal to trip ID.

**4:36:52** · Let's also give it a name. And just so we don't repeat ourselves, we can dstructure those properties directly from the props right here. So let's do just that. I will dstructure the trip into ID, name, image URLs, itinerary, interest, travel style as well as the estimated price. So now we can pass all of them right there. ID is ID. Since we're mapping over it, we also have to give it a key.

**4:37:23** · Name will be name. After that, we have location, which will be equal to itinerary.

**4:37:31** · Question mark.0ero. So, we're going to take the first location.loation or an empty string in case it doesn't exist. Image URLs. Well, we'll only take the first image. So, image URLs zero. For the tags, we can pass an array of interests. So interest and the second one can be travel style and for the price we can pass the estimated price. So if we save this you can now see that all of the details are back and now we have one other popular trip.

**4:38:04** · In this case it's the same that we're currently on as it's the only one that we have but later on we'll show different trips right here. and how nice it was to just reuse the card we have already created before. Just before we admire this trip details page, I want to show you a little optimization that actually goes a long way. And that is that here we're making two separate asynchronous await requests. Each one of these takes time, maybe about 500 milliseconds.

**4:38:35** · So if we try to wait for both of these one by one, it's going to take a total of 1,000 milliseconds, which is a lot of time if you're trying to fetch the data. But the thing is that we don't have to have both of these fetched at the same time. They don't depend on one another. We show the trip details right here and then we show other trips at the bottom. They can happen at the same time instead of one after another. To do that we can use the promise that all functionality.

**4:39:05** · That way they will happen at the same time in parallel. Okay, that's the key. The way you do it is you say const and then dstructure what you want to get. So we first want to get the singular trip and then we want to get the trips. Then you make that equal to an await promise.all call to which you pass an array of different calls. The first one will be giving us our trip details. So I'll paste it here.

**4:39:36** · And then the second call will be giving us all of the trips.

**4:39:42** · So we can put it here. And you don't need a weight because we already have a weight right there. So if you do it like this now, both of these requests will happen in parallel at the same time. And they will reduce the time it takes to load the page in half. Pretty cool, right? So always remember that when you have multiple asynchronous calls that don't depend one on another, you can simply put them within the promise that all. So with that in mind, check this out. We're looking at the trip details.

**4:40:12** · We have this one trip detail that we can see. We can read what it is about at a very first easy glance. See the estimated price and then we can start seeing what this trip is all about. For example, we have a private guided tour.

**4:40:27** · first relax at the pool, romantic dinner at a fine dining restaurant. Well, this is how life should be lived, right? Just kidding. But yeah, in general, you have a couple of days of different trips, and it's all separated into morning, afternoon, and evening to know exactly where you have to be at a specific point in time. You can get more info on when you might want to visit it based on the season that you like or the weather. And I just noticed that on desktop, this card looks very narrow. So we might want to expand it a bit.

**4:40:57** · So if you head right here, we have to take the section for the popular trips, copy it and then put it below the section for the details.

**4:41:08** · That way we'll allow it to take the full space as it doesn't depend on the details. So we can show 1 2 3 4 in the full width right here. Amazing. With this lesson, we're finally taking everything we have created so far and displaying it right here. But to reach this page, we had to manually navigate over by grabbing the ID from apprite, which let's be honest, regular users won't be able to do. And then we came over here. But for now, if you head over to trips, they're completely empty. So, what do you say that next we implement the all trips page?

**4:41:38** · Great work so far. So, now that we have the trip details page, we have to have a page that allows us to visit all of those great trips. So, let's create it. First, I'll head over into our routes right here. I want to check whether we already have a route for the trips. And we do.

### All Trips

**4:41:58** · It is the trips.tsx page. So, let's head over into trips.tsx. And currently on there, we only have a header. But within here, we also want to access all the trips similarly to how we got access to these popular trips at the bottom of the trip details. So, I'll head over to the trip detail one more time and I'll copy the part where we have the loader that fetches that data.

**4:42:25** · So, I'll copy this alongside the top part of the trip detail that actually has the loader data. So, I'll copy it and I'll override the top part right here. Of course, we have to change this over to trips, but the loader data will remain the same.

**4:42:45** · It's just the import of that route that'll change as it'll point to slashtypes slash trips instead of trip detail. Perfect. And we'll also make the loader a bit simpler. We don't need to fetch the individual trip. So we don't need the params to get the trip ID. So I can remove that part. But instead we'll need a request. Why? Because we'll implement the pagionation. So we need to know on which page we're on. And what is the offset?

**4:43:15** · So I'll say that the limit per page is eight. And then we have to get access to the current URL which will be equal to new URL. And we'll get it from the request URL. Once we have that, we'll have to figure out on which page we're on. So I'll say const page is equal to parse int URL dot search params.get page.

**4:43:40** · So similar to nex.js JS this is working in the principle of search params and I'll say if we don't have it we can default it to a string of one and the radics of that parse int can be set to 10 that means that it's a decimal system finally we need to get the offset to figure out how many pages do we have to skip and that'll be equal to page minus one so we want to take the

**4:44:05** · previous page and multiply it by the limit or in other words the amount of trips we're seeing on that page with that info We can now call the get all trips no longer within the promise all.

**4:44:19** · It can be a very simple call to const all trips is equal to await get all trips. But now instead of passing the fake limit and offset, we can actually pass the limit and the offset coming from the page params. Perfect. And alongside all trips, we're also getting the access to the total number of trips. So what are we returning?

**4:44:49** · Well, we'll return trips, which will be equal to all trips do map. We want to take the ID trip details image URLs. We do the same thing as we did before, but now as the second parameter, we'll also pass over the total number of trips. Perfect. So now we're returning that data from the loader and we can consume it right here within this page. Not the trip details, but rather trips.

**4:45:18** · So it'll be as simple as saying cons trips is equal to loader data. trips as a trip array. So we know what each one of those has. And now we can map over them. So I'll head it right here below the header. And I'll create a new section. That section will have an H1 that'll have a class name equal to P-24 semibold and text-d dark 100. And it'll say manage created trips because we are in the admin dashboard right now.

**4:45:53** · Then right below the H1, we can render a div that'll have a class name equal to trip-grid. And if you remember correctly, we already rendered a trip grid on the details page. So head over to trip detail all the way down at the bottom. And you can see that here we have a div where we're mapping over all of those trips. So copy it and paste it right here. trips.m map where we get each individual trip.

**4:46:21** · And for each trip, we render a card with a trip ID, name, image URL, location, tags, price, and more. It is all fitting in very nicely right here. And if you do just that and save, you'll immediately be able to see the card for one trip that we have created so far. So, what do you say that we go ahead and create another trip just to make sure that our app still works?

**4:46:47** · Let's say that I want to visit Japan and we really want to make it an interesting trip.

**4:46:53** · that last about 10 days. I'd like to go there with my fiance. So, I'll say as a couple with a travel style of cultural. We can put different interests right here, such as historical sites and a mid-range budget. You can see Japan right here in the world map. And let's generate a trip. We can see that it's loading and the button is disabled. So, we cannot click on it like monkeys. But in a couple of seconds, the trip will be generated. So, let me expand it. And it actually seems I wasn't redirected.

**4:47:23** · So, something must have gone wrong. It looks like the trip details has exceeded 5,000 characters. That's the limit that we set. And since I chose 10 days, which is the maximum duration, it's highly likely that the itinerary expanded over 5,000 characters. So head over to your dashboard into databases trips attributes and see if we can edit the trip details.

**4:47:52** · Let's see what is the maximum size that we can set. Okay, I updated it to 10k. Now if I go back and retry to generate this trip, hopefully 10,000 characters is enough to explain what I should visit in Japan for 10 days. There we go. That's beautiful.

**4:48:11** · See how it picked up those very nice photos from Unsplash. We have a bit of nature, a bit of city, and a bit of culture. Cultural couple mid-range historical. It is rated very well. And we have a bit of a description. I should arrive at one of these two airports, visit the Imperial Palace, enjoy a welcome dinner, and then go to different places. This is amazing, I got to say.

**4:48:38** · and see the best time to visit definitely is in the spring as there's cherry blossoms there as well. But everything is looking great right now.

**4:48:46** · As you can see that now the second trip has been generated. So if I head over to the AI trips, you can see that both of them are right here. So what we could focus on next is the pagionation. And let me just add a bit of a margin bottom of like four to this one right here just to create some space. And let's implement the pagionation. For this we'll have to have a couple of states that'll help us manage it. So at the top I will say const search params is equal to use search params.

**4:49:22** · Once again similar to nex.js but now everything is coming from react router.

**4:49:26** · We want to access the initial page by parsing the response of search params.get page. So we want to get access to the page through the URL. By default, it can be set to one. Or instead of parse end, maybe you can also use just a regular number constructor.

**4:49:45** · This might be an even simpler way to convert this into a number. So it's search params.get or one. Then once we have the page, we can also store it to the state by setting use state snippet.

**4:50:00** · call it current page and set current page at the start equal to the initial page. And we'll also need a function to handle the page change. So we'll say const handle page change which accepts a page of a type number and then it simply updates the current page to the new page as well as it updates the search param in the URL to question mark page is equal to the selected page. Don't forget to import use state from react.

**4:50:33** · And once you do that, we can actually use a pagionation component coming from Syncfusion right at the bottom. So below this div, still within the section, I'll create a pager component coming from Syncfusion. And if you save it, you'll immediately see the pages right here at the bottom. But we can style it a bit further by saying total records count is equal to loader data dot total.

**4:51:03** · We can also pass in the page size equal to eight. So it knows that we can want to show eight elements per page. And we can pass the current page equal to current page. And we can also pass the click. So what happens on click here we get some arguments of what happened within that click and call the handle page change where we pass the args.curren page to it.

**4:51:31** · So now if I save this and reload, you can see that we're in the first page. So to truly test this out, we can first maybe give some margin bottom of four right here. So we make some space. And also we can give this pager component some margin as well. So it looks like it's floating. So I'll say MB4 for the class name. Or I think it's CSS class like this. There we go. So now it's floating like the cards. And it looks like we still cannot navigate because we only have one page, right?

**4:52:02** · So what if we set the page size to only one? Will that work? And we also have to update the limit right here. So if I save this, we will now only fetch one trip per page. And take a look at this.

**4:52:19** · We can head over to the second page and we can see the second trip. And now we're at the second page. And all of that is updated right here within the URL. So if you want to copy this entire thing and share it over with a friend, you can totally do that. And you can also head back to the previous page to see the first trip. Of course, it looks a bit empty because we don't have many trips right now. So I'll bring back the limit to eight and also bring back the page size to eight as well.

**4:52:45** · So later on we'll be able to show more trips, two rows of four because we have reused the trip card component that we created before for the dashboard. So the last thing that we have to do is actually update our dashboard to reflect real stats from our database. From the stats about the users, trips and active users to the created trips because right now our all users page is dynamic and so is the trips page.

**4:53:16** · But the only thing that's static is the dashboard. So in the next lesson, let's make the dashboard dynamic.

### Finish the Dashboard

**4:53:27** · And finally, now that we have all the data, we are ready to collect it in one place and show it on this great looking dashboard page. We'll make it look like this where we're tracking the amount of total users, total trips, and active users today to live trips. And finally, real charts that shows you how many users have created their accounts over time, as well as which trips they're creating. Looks like recently everybody's been into adventure.

**4:53:54** · Then you'll see which users created how many trips and you'll see trips based on different interests. Let's make it happen. First things first, we have to collect all of this data in one place.

**4:54:08** · And that won't be an easy task, but we'll do our best. So head over to AppRight and create a new file called dashboard.ts. And within here, we'll have to create many different functions that allow us to fetch all of the different pieces of data that will display on the dashboard. And I really want to end this course on a high note.

**4:54:30** · So, it won't be easy. Trust me, when you're working with charts and tables, you're working with data. And tables are easier because you're just presenting that data in a very simple structure.

**4:54:44** · But when you want to present data in charts, especially charts that have X and Y axes that show different pieces of data on hover, and you try to present it in a nice understandable way, it's not easy and you have to deal with a lot of native JavaScript, reduce functions, date and year processing, making sure that you combine all of these arrays and objects into one to be able to calculate it.

**4:55:11** · So, as I said, we'll end this note on the high note because that's what you came into this video for, to be able to build a proper dashboard. So, back within our codebase, first things first, we'll try to get access to the users and trips stats, the ones that we're going to show on the top cards. So, I'll say export const get users and trips stats.

**4:55:38** · I'll make this equal to an asynchronous function that will return a promise which will be resolved into dashboard stats and we can open up a function block. Once we need to do at the start is get access to the current date. I'll do that by saying cons is equal to new date. Pretty simple, right? Then we want to get the start of this month.

**4:56:00** · And we can do that by saying const start current and that'll be equal to new date d.get full year, d.get month and then pass over a1 for the date and then get outside of it and call the two ISO string on it. Now duplicate this two times and we'll want to get the prev. And for the second one we'll want to get the start of the last month.

**4:56:32** · So I'll call it start prev which is equal to new date d.get full year get month minus one. So we want to get the previous month to ISO string. Then the last thing we want to get the end prev which is the end of the last month. So here we want to get a new date for the year. So here we'll leave the date as zero. Okay. So now we have access to these couple of dates. Now as before we're going to get access to all of the users and trips.

**4:57:01** · So I'll say const dstructure the users and trips and make it equal to await promise.all all where we're going to call database coming from apprite.list list documents and we want to list them from appate config database ID and then appate config dot user collection ID in this case. This shouldn't even be within parenthesis. So I'll just leave it like this.

**4:57:32** · And then we can duplicate it below and we can do the same thing to get the trips. The only thing we have to change is the trip collection ID. Okay. So now we have different dates. We have different trips and users and we want to combine that. But I'll first create a function that will help us to do that.

**4:57:52** · const filter by date of a type filter by date. And this type we can declare above so we know exactly what we're working with. Type filter by date is equal to a function that accepts the items that we want to filter. And this item will be of a type document array. And what is a document? Well, a document is an interface that will have a key of a type string.

**4:58:23** · And then it can have any kind of value. So, we want to keep it open. It can be an array. It can be a string. It can be a value. It can be a number.

**4:58:32** · We're going to have a key as well of a type string. We're going to have a start of a type string and maybe even an end of a type string. So we know what to filter. And finally, we will return a number when we filter that out. So we'll know how many of what has happened on which day. So now that we have this, we can actually accept all of these params.

**4:58:55** · Items, key, start, and end. And we can call the items.filter. So we can filter them. What do we want to filter them by?

**4:59:06** · Well, first we get each individual item into the filter function and we want to automatically return the filter command.

**4:59:16** · So I'll check if the item key is greater than or equal to start and if not end or item key. Oh my god, this is getting complicated. I remember writing this one time before, but being fully honest right now this feels like gibberish to me. So, what better to do than get some help from Chad GPT. It says that little helper counts how many documents in an array fall within a given date range.

**4:59:46** · So, here's a breakdown. We take in an array of objects. Each is a database document like a trip or a user. We take the key which we want to use to join them at. Then, we take the property name such as joined at or created at and then we go from start to the end of a specific period. Then here is where things get tricky. Here we have filtering logic. So we say item.filter and we compare the item key to make it greater than or equal to start.

**5:00:14** · So we only keep those whose date is on or after the start. That makes sense. And then for the second part we check if not end or item key is lower than or equal to end which enforces the upper boundary if the end is provided. So it makes sure that we actually count the numbers and return the number of items in that specific day. So finally we have to attach the dot length to it.

**5:00:43** · In other words, filter by date function if you call it with users joined at start current and end previous will tell you how many users have joined between the start current and end previous. And this will be super useful for our chart data.

**5:01:02** · Now let's continue. After that we want to filter out users by ro. So I'll say con filter users by ro and I'll make it equal to a function that accepts the role of a type string and returns users dod documents dotf filter where each u is a document and it only returns the ones where u status is equal to that specific role. This one is more straightforward.

**5:01:33** · And finally, now that we have collected all of this data, we want to return it from this function. So I want to say return a big object where we first share the number of total users equal to users.tal. Then we share the users joined which will be equal to well we'll get the current month by calling the filter by date function to which we'll pass what we want to filter. It's going to be user documents. What do we want to filter it by? So which is the key? It's the joint ad. Next, what is the start?

**5:02:09** · So this is the start of the current month. And when do we end it? In this case, I'll pass undefined as we don't want to end this specific period of time. And that'll give us the users joined. But the second part of the users joined will be the last month. So how many did we get the last month?

**5:02:24** · So we can filter by date and we'll again pass the users.documents. documents by joined at will pass the start prev so the start of the previous month as well as the end prev so end of the last month and here I noticed I have to say start current so let me actually expand this

**5:02:47** · into a new line so it's a bit easier to see that we're basically calling the same function two times but for the previous month and the current month there we go and this is for the users joined now what I'll do is I will duplicate this user joined just below and I'll do it for the user role. So this will filter it based on the user or the admin. In this case, we want to get access to the total. In the previous one, we just had the current and the last.

**5:03:14** · But here within this user role, we want to get the total and it'll be equal to filter users by ro. The role will be user and we'll simply get the length of all of the users. Next, we get the current month where we'll filter it by date and we will pass in the amount of users that we want to filter by date. So, when did they join by filtering users by role of the user?

**5:03:41** · So, this is now getting very meta or very matrixy where we're calling this filter by ro right here within filter by date. But basically what this is trying to do is it's trying to tell us how many users have joined in a specific period of time within this month that have a role of user and the rest will be the same. For the last month we once again we want to take the users the role of the user joined at start end prevent end. This is good.

**5:04:11** · And one more time we want to do something similar. So I will duplicate this user role one more time below but this time we'll do it for the trips. So I'll extract this total up above the object and I'll say total trips is equal to trips total. Next we have trips created. This should be technically called trips created over time. That's actually what makes it difficult. Not the amount of total trips created but trips over time.

**5:04:45** · Right? So I'll say current month filter by date. Here we want to filter by date and we want to get the trips documents.

**5:04:53** · So trips documents by created at. And we want to do the same thing right here below trips documents created at. And here we're returning all of these important pieces of info users and trip stats that we will use on our dashboard. So what do you say that we actually start using them? I'll head over into my dashboard.tsx and I'll want to call these pieces of data because everything on the dashboard right now is entirely fake.

**5:05:25** · So we need to start by modifying our client loader to not only call the user info but to also call the dashboard stats. So I will expand this function and I will create another await that will fetch the dashboard stats. So I'll say await get users and trips stats. And we of course have to put all of these into their specific variables.

**5:05:54** · Or we can once again do a promise all.

**5:05:57** · So I'll say const user and then dashboard stats. We can call these stats we just created will be equal to await promise doall and here we can then put both of these calls so we can try to call them at the same time in parallel. Perfect.

**5:06:16** · So now we're getting these dashboard stats and we need to return them right here by saying return user as well as dashboard stats coming from client loader.

**5:06:28** · Now we can accept that right here from the client loader. It'll be now we're not getting only the user. The user is only a part of the loader data. So it'll be loader data dot user. Next we have to dstructure the dashboard stats from the loader data. So I'll say const dashboard stats is equal to loader data. And now we can display them right here within the stats card. So for the total users, I will use dashboard stats total users.

**5:07:01** · And let's see if it changes from 13,000 to about two. Yep, this makes more sense. Next, we can get the current month count by getting to dashboard stats dot users joined dot current month. And now we can see we're down.

**5:07:19** · But we also have to change the bottom one. So I'll change the last month over to dashboard stats dot users joined last month. So we worked super hard so we can actually get the real stats right here.

**5:07:34** · Now we can do a similar thing for the total trips. So we'll show the dashboard stats dot total trips.

**5:07:42** · We can also show the current month by saying dashboard stats dot trips created dot current month and below we can say dashboard stats dot trips created last month. So now we can see that we have a total of two trips created and we can check out the active users today by doing the same thing.

**5:08:06** · Dashboard stats dot user rotto total and for the current we can do the dashboard stats dot user rot current month and we can repeat it at the bottom dashboard stats dot user rot last month.

**5:08:27** · So you can see that we only had one active user today. Okay, that makes sense. And now we are seeing these three different cards with the real user data.

**5:08:37** · It was hard to create them, but we needed to get the previous and last months. So we know what the increase is.

**5:08:44** · Now to get access to other pieces of data that we need such as the created trips which we have already gotten a couple of times so far both on the all trips page as well as on the trip details page right at the bottom. So we have to get it one more time so we can show these live cards but then we'll also have to get the stats for the charts that will show at the bottom.

**5:09:07** · These calls will get a bit repetitive.

**5:09:10** · We'll have to list the documents from the database, do some logic with dates and time, and finally return it in a format that our front end will like. So to save us some time, I'll provide the full dashboard.ts file within the video kit. So just head over to the bottom of the video kit and you can get it right here. Once you get it, you can override the one that we have right here. If you check out this file, you'll notice we have a couple of different functions. So let me collapse all of them so you get the idea. The one that we created was the toughest one.

**5:09:40** · So we have it right here. And we have it right here. Now I'll collapse these couple of functions that we have right here. But the toughest one was the one that we created. So I'll collapse that one too.

**5:09:53** · Get users and trip stats. Then we have the get user growth per day which is the data that we'll use for our chart. Get trips created per day as well. And then get trips by travel style. So let's take a quick look into this. Get user growth per day. Here we are listing the users.

**5:10:13** · We are taking the current date and time and we are aggregating the number of users per day that they have joined. And this is a perfect use case for a reduce function. Whenever you want to count some numbers up in an array, such as you have a day one, maybe two users have joined. Then you have a second day and then maybe four users have joined. For the third day, you have five users. When you want to use a map and count something up in that map, well, that's what the reduce function is perfect for.

**5:10:48** · Basically, what it does is it takes a key. In this case, the key is going to be the day that you want to map over.

**5:10:55** · And then you're adding a specific count of users in this case to the day that they have joined within. It might sound a bit complicated, but that's because it is. And reduce is not something that we use super often, but as I told you, with charts, you're going to use it a lot.

**5:11:11** · And this just reminded me of the complete path to JavaScript mastery that I recently completely re-recorded from scratch. It's one of the oldest courses that I had, but now I updated it. And here we have all of these different array methods in detail. So everything from strings in details to arrays and details. And here we have the array reduce. And we explain it in a lot of detail.

**5:11:36** · So for example, if you have a grocery list with all the prices, you want to calculate the total price of all the items. This is a perfect example to use reduce. You could do it with a for each where you're just going to map over each one of these elements and add them together. But you use an external variable to keep track of the total.

**5:11:59** · With reduce, it does it all together.

**5:12:02** · Basically, you get this variable called accumulator which starts at zero and then you take the current value for each iteration and then you add it together.

**5:12:12** · But as you can see here in the course, we go super deep into understanding exactly how it works. So if you want to polish your JavaScript knowledge a bit, go check out complete path to JavaScript mastery by becoming a JS mastery pro member. Another thing that we cover over there is object entries as well where you can take both the keys and values of an object and then map them over to an array. Pretty useful when you want to have a chart that has a day and count attached to each day.

**5:12:40** · So essentially you'll end up with an array of objects where each object has a count and a day which will look something like this.

**5:12:48** · Great. So now let's call these functions right within our dashboard right here where we called the get users and trip stats. We'll also call the get all trips because we want to render them within the cards. I think four will be enough.

**5:13:04** · We also want to get access to the get user growth per day. We also want to get trips by travel style and we want to get all users but only four will be enough in this case just to show them within a table. Of course we have to add a weight in front every single one of these calls and we are calling all of these simultaneously because these pieces of data don't depend one on another.

**5:13:32** · Now here we're getting all the trips but remember we have to properly parse the details of those trips and I believe we have already done that within the trips page. Here we are getting all the trips but in order to get them with all the proper details you need to map over them parse the data and attach the images. So you can copy this part right here where it says all trips.m map all the way until the end.

**5:13:59** · Then right at the bottom you can say const all trips is equal to and you can paste what you just copied.

**5:14:08** · But in this case we can call it trips right here. And where are these trips coming from? Well, we are yet to define the variables where all of these functions will spit out their values. So let's define them one by one. First we have the user. Then we have the dashboard stats. After that we get the trips. We then have the user growth, the trips by travel style, and then all users. Perfect. So now we're getting these trips.m map right here.

**5:14:40** · But I think we have to say trips.all trips because trips also contains the total of the trips and all trips is an actual trips array. We also want to map over the users. So I'll say const mapped users of a type users itinerary count

**5:14:58** · will be equal to all users do users do map where we get a individual user and for each one we automatically return an object not like this because this opens up a function but rather parentheses and then an object within it which automatically returns an object.

**5:15:16** · That's just another pro JavaScript tip. within it we can say that we want to get the image URL which is equal to user dot image URL we also want to get the name which is equal to user name the count which is equal to user itinerary count like this so now that we have collected all of these pieces of data we can return them user dashboard stats all

**5:15:45** · trips user growth trips by travel style and finally all users which will be equal to mapped users. We are returning all of this from the client loader. I think at this point it is safe to remove this dstructuring of the fake data as well as these fake imports right here at the top.

**5:16:09** · This will momentarily break our application but we'll make it work very soon as we extract real data and bring it into this page. So from the loader data I will dstructure the all trips the user growth the trips by travel style the all users

**5:16:33** · and I think that's it immediately this will make our app work with real trip cards and then we can scroll down below the created trips here where we have the trip card and we can make sure that we're passing the right data so we're mapping over the all trips and This time I will simply say all trips.m map and we get each individual trip. For each trip we want to return the trip ID, trip name. We also want to get the image URLs itinerary tags.

**5:17:04** · So I'll simply say trip dot in front of every one of these. For the name, we know that it'll be there.

**5:17:11** · So I'll add an exclamation mark. And for the tags, tags actually don't exist.

**5:17:16** · They are a combination of trip interests as well as the trip.t travel style and for these you'll also have to add an exclamation mark and the same thing for the price because you can see that it's showing so it has the data but we have to render it properly. So now we are ready to focus on the last section of the day. It'll come below this section that keeps track of our cards.

**5:17:38** · So I'll create a section with a class name equal to grid grid-call-1 on large devices grid-call-2 with a gap of five within it I will render a chart component coming from Syncfusion and within it I will inject again coming from Syncfusion specific services an array of services to be exact specifically the column

**5:18:11** · series, the spline area series, the category, the data label coming from Syncfusion React Charts, and the tool tip coming from React Charts as well. I simply copied this over from their docs.

**5:18:29** · And you can already see that this gives us some kind of a chart. So let's give this chart an id equal to chart 1. A primary xaxis will be equal to user xaxis coming from constants. So now you can see that it says day at the bottom and then we'll have a primary yaxis equal to user yaxis once again coming from constants.

**5:18:58** · I'll also give it a title equal to user growth and a tool tip equal to an object where enable will be set to true. So now you can kind of hover over it and when we have some real data you'll be able to see what it says. But now we actually show the data within it. So below the inject I'll render a series collection directive and within it I'll render a series directive which will be a self-closing tag.

**5:19:29** · Here you actually put a data source of user growth but you have to define exactly how each field will look like. So x name will be day. Y name will be count. The type will be column. The name will be column as well. And the column width. You can choose how long or wide you want to make it. I'll do 0.3. And you can go to very small details like choosing a corner radius.

**5:20:01** · So for example on the top left I can make it 10. And also on the top right I can also make it 10 so they look a bit rounded like it's the little details right so currently I only have one day that we have been active that I have been developing this app and you can see that it says that two users have joined today or rather this was yesterday. So now if I go ahead and join as another user.

**5:20:28** · Okay, now we have logged in as the new user and we are right here on the homepage, the non-admin homepage, which right now is completely blank. So, we might actually want to create this root route right next to the signin. I'll call it the travel page. So, travel page.tsx and I'll run rafce.

**5:20:54** · Then you'll have to head over to the routes and we can add another layout right below our previous layout which will be forward slash routes slashroot slpage layout.tsx and inside of an array we can give it its first index route this time coming from react router that'll be routes root travel page.tsx tsx.

**5:21:19** · So we are rendering this new page that we have right here. When you do this, you might want to reload your application just so you can see the changes. And before we rerun it, you also need to create this page layout. So right here within app root, you can create a new layout called page layout.tsx where you can run rafce.

**5:21:47** · Now, if you do this and rerun your application, it'll spin it up on localhost 5173 and you'll be able to see the page layout. The only reason why I wanted to have this here right now is so we can implement the logout button.

**5:22:03** · Remember, we have already implemented the logout functionality on the nav items. So, I will simply grab it from there. Here it is a button to handle the logout. So I will copy it, paste it over into the page layout and I will also copy the handle logout functionality alongside the use navigate and paste it at the top of the page layout.

**5:22:29** · So here you can see this little log out button right now, but before you click it, try to navigate over to the dashboard manually. And you'll notice that you might be able to see it for a second, but then it'll be gone. So once you do that, you can then log out. Your account will have been created and you can sign in with your admin account.

**5:22:50** · Once you come back now, you'll be redirected to the homepage. So if we head over to that page layout, we could add another button right here. Maybe this one will just redirect us to the dashboard. So I'll say dashboard. and on click I will simply call a callback function that will navigate over to forward slashdashboard.

**5:23:14** · So now if you click on the dashboard there we go and now we have three users and you can see that our user growth has increased for this new day that we have added another user.

**5:23:27** · Great. Now we can continue with the dashboard but now I will add a second series directive. I'll do that by copying this one first right below. The data source will still be the user growth by day count, but this time I'll give it a type of spline area and a name of wave. If you do that, you'll kind of be able to see the trend of how many users are joining.

**5:23:53** · So we can also give it a fill color equal to RGBA something like 71 132 238 and then most importantly the opacity of 0.3. So it's not actually appearing over the other elements. So now we can see the trend. Of course this is not super cool when you have two, but later on when you have more, it'll look much better because you'll be able to see the trend on each one.

**5:24:20** · In this case, instead of a column width and a corner radius, we can give it a border of about width of two and a color of hash 47 8 for e. So now it'll have a border as well so you can better track the trend. Now we can exit out of this chart component and right below it we can create another. So what I'll do is I'll simply copy the entire chart and I will paste it one more time right below it.

**5:24:55** · Starting from the top I'll call it chart 2. Primary x-axis will be trip x-axis and y will be trip yaxis. This one will say trip trends will still inject the same things. And then it'll have a series directive with a data source of trips by travel style with x name of travel style, y name of count, type of column, name of day,

**5:25:27** · column width of 0.3, and the same corner radius. And we don't need a second series directive for this chart. So if you save it, you'll be able to see it just below to track trip trends. So there you have it. We have two trips, one relaxed and one cultural. Now I'll head over below this chart component. And I want to make sure that both of these are in the same section right here. And they need to say grid instead of grits columns.

**5:25:54** · So if we do that, and if you go to desktop, you'll notice that now they both show in the same row. While we're here, what do you say that we go ahead and create two more trips to fill out our dashboard a bit more? So, I'll head over to create a trip. I'll select a random country from the list. Enter a number of days. And I'll choose some of these fields at random. There we go. Looks like this will be a fun one. So, let's go ahead and generate it.

**5:26:25** · Let's see if there's some nightife and bars in Burundi, Africa. This one should be quick because it's a 5-day trip only.

**5:26:33** · Looks like Burundi has its own Las Vegas and some interesting houses. And let's do one more. I'll pick another random country. Let's go with Guatemala. A short two-day trip with friends. That's going to be an adventure with hiking and a premium budget. What's happening at Guatemala? There we go. It looks like there's going to be a lot of hiking, but since we're looking at a luxury trip, it's going to be a private transfer to the Volcano National Park. Perfect.

**5:27:03** · So, if we head over to the dashboard, you'll see that it looks much better and we can see more trip trends right here. So, the last part that we have to do is create some very quick references to our users and trip bookings so that we don't necessarily need to go to their respective pages right here and here.

**5:27:25** · Rather, we can see it all from our global dashboard. So to do that I'll head below this section and I'll create another section with a class name equal to user trip wrapper within here we have to map over the users and trips both at the same time.

**5:27:44** · So what do you say that right here at the top we create a variable called users and trips and we make it an array where the first object has a title of latest user signups with a data source equal to all users with a field of count and a header text equal to trips created.

**5:28:13** · count is also a string and we can duplicate this right below. But this time instead of latest user signups, we'll have trips based on interests. We will pass the trips data with the field of interest and the header text of interests. So now we have to make sure that we have access to these trips. And in this case we just need the images, the names and the interests, nothing more.

**5:28:38** · So we can create those trips variable out of the all trips by mapping over them getting each individual trip and automatically returning an object with an image URL of trip image urls of zero. So we return just the first one. The name of trip.name and the interest of trip interests.

**5:29:07** · But make sure that you have properly closed it right here in parenthesy and then a curly brace. So now we have access to it and we can map over it. So right below I will map over users and trips do map where we can dstructure the title the data source the field and the header text and outside of it we also get the index.

**5:29:33** · So for each one of these we can return a div with a key of index a class name equal to flex flex- call and a gap of five and an h3 within it that'll render

**5:29:53** · the title that'll look like this. latest user signups and trips based on interests where we have a class name equal to P20 semibold and text dash dark 100 to make it a bit stand out and then we can render the grid. This grid will be very similar to the grid in all users. So head over into all users, find where we use the grid component and just copy it.

**5:30:24** · You don't have to copy it until the end.

**5:30:27** · Maybe just take the first thing where we're actually rendering the username and the photo. So until the end of the first column directive. Next, right below the H3, paste that grid component, but change the data source to data source.

**5:30:44** · And make sure to import the grid component from Syncfusion.

**5:30:49** · import the columns directive and import the column directive. We'll keep this exact the same because we want to show the users.

**5:30:58** · Same as before. And we'll render just one more column directive. This one to render the second field with a header text which will be dynamic header text. So either the latest user signups or trips based on interests with a width of 150 and text align of left and we can end it right here. Make sure to properly close the columns directive as well.

**5:31:25** · So in this case we have to close it and then close the grid component itself. If you do that you should be able to see two different tables. The first one rendering the users and the second one rendering the interests. Oh, but wait.

**5:31:43** · Why is the number of trips created non-existent? I think we don't have this field stored into the database. We would need to do some additional logic to connect the user to the trip. But what we can do for now is just head over all the way up to where we have the count of the users. And here maybe we can say if it doesn't exist do a math.f floor math.random times 10. This will give us a random number from 0 to 10. Perfect.

**5:32:16** · This is looking good. So with that in mind, if we expand this dashboard so you can see it on full screen, you have now developed a fullyfledged dashboard with a real database where you can see different charts, the users, the trips.

**5:32:33** · You can see absolutely everything right here from the type of the user to the trips that we have generated so far with budenation and the ability to generate new trips using Gemini. So this is absolutely amazing and I almost forgot about the trip details page which is maybe the star of the show because here is where you can see the actual trips that we have generated for each user. So the last thing we have to do is to deploy this travel agency admin dashboard which we'll do right now.

**5:33:04** · But keep in mind that I really wanted to take this course further than just the admin dashboard. Of course at the same time I wanted to make it complete. So right here, right now, you have successfully developed the admin dashboard with all of these functionalities. So the next step will be waiting for you on JS Mastery Pro.

**5:33:26** · We'll take this app a step further by developing a public landing page where different agencies can create their own landing pages with featured destinations and show their handpicked trips. Then users can view those trips and even book them by paying for them using Stripe checkout. After that, they'll be redirected to this greatl looking success screen. So, what do you think?

**5:33:54** · If this is something you'd like to explore, you can check it out right here within the video kit. Watch it now by becoming a member. Whether you decide to improve this app or not, one thing is certain, and that is that we have to get it deployed. So, back within our app, I'll stop it from running and I'll run git add dot git commit-m and I'll say final commit. And finally, run git push. Once you push it, you can head over to Verscell and add a new project.

**5:34:23** · You should be able to see it pop up right here. And you'll notice that Versell will automatically figure out that we're using the React router framework. Then you'll be able to add your environment variables right here. So head back over to your application. Go to your env.local. Copy these env. This will take about a minute.

**5:34:49** · But while that is happening, you can head over to appite and create a new platform. This will be a web app. So you can give it a name of travel agency. And for host name you can just add a star.

**5:35:06** · Click next. Next. Again we have already done this. And you have your endpoint which we have already used before. Now your app should be accessible from the web.

**5:35:16** · So if we head back over to Verscell, you'll see that a new project was just deployed to JSM Pro or to your name in this case. So you can continue to its dashboard and click visit. This will redirect you to a very simplistic page for now. But if you log out, you'll be able to see your sign-in page deployed and live on the internet and you can now sign in with Google after which if you log in as admin, you'll be able to check out your admin dashboard. Pretty cool stuff, right?

**5:35:48** · In this project, I purposefully left a couple of places that you can take to improve it even further.

**5:35:56** · For example, you can make these trips created dynamic. Or you can make these headings point to the users and trips tables. You can fix a little bug. When the user is first time creating an account and they try to visit the dashboard, they can actually see it.

**5:36:11** · That's a weird edge case that's worth taking a look at. But overall, congratulations on building such an amazing application that acts both as a dashboard as well as an AI generation tool for all of your and everybody else's future travels. With that in mind, if you'd like to polish a bit of your JavaScript, check out Complete Path to JavaScript Mastery.

**5:36:32** · Or if you maybe want to do a bit of Nex.js, you can check out the Ultimate Next.js JS course or just become a JSM Pro member to get it all alongside real interview feedback and even the access to building the public version of this website. All of that is available on JSM Pro. So check it out and I'll see you there. Have a wonderful