---
title: "React Admin Dashboard Tutorial | Responsive React Admin Panel UI Design Course"
source: "https://www.youtube.com/watch?v=fq7k_gVV5x8"
author:
  - "[[Lama Dev]]"
published: 2023-07-11
created: 2026-07-02
description: "Responsive React admin template design tutorial for beginners.Get Hostinger Discount: http://hostinger.com/lamadev Coupon Code: LAMADEVIf it is valuable to you, you can support Lama Dev.Join: http"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=fq7k_gVV5x8)

Responsive React admin template design tutorial for beginners.  
Get Hostinger Discount: http://hostinger.com/lamadev Coupon Code: LAMADEV  
  
If it is valuable to you, you can support Lama Dev.  
Join: https://www.youtube.com/channel/UCOxWrX5MIdXIeRNaXC3sqIg/join  
Buy me a coffee: https://www.buymeacoffee.com/lamadev  
  
Source Code:  
Starter: https://github.com/safak/react-admin-ui/tree/starter  
Completed: https://github.com/safak/react-admin-ui/tree/completed  
Test API: https://github.com/safak/react-admin-ui/tree/testapi  
  
Facebook: https://www.facebook.com/groups/lamadev  
Instagram: https://www.instagram.com/lamawebdev  
Twitter: https://twitter.com/lamawebdev  
Discord: https://discord.gg/yKremu4mPr  
  
00:00 Introduction  
02:56 React Installation  
05:31 Pages and Layout  
07:45 React Router Dom Tutorial  
14:55 Global Styles and CSS Variables  
18:34 React Navbar Design  
26:00 Footer Design  
28:02 React Menu Design  
35:10 CSS Grid Real-World Example  
48:16 React Chart Tutorial (ReCharts)  
01:04:55 React Dashboard Animated Charts  
01:21:24 React MUI DataGrid Tutorial  
01:40:09 React Modal Tutorial ( Add New Item )  
01:54:08 React Single Product Page Design  
02:14:03 React Admin CRUD Test  
02:21:41 React Admin Dashboard Responsive Tutorial (CSS Grid)  
02:37:09 Deploying to the Hosting  
02:40:52 Outro

## Transcript

### Introduction

**0:00** · Hello friends today we are gonna design this beautiful admin dashboard using react and CSS on this home page we will create reusable box components and add different charts inside them and these charts are interactive so we can hover over them and see the details of the data after that we will create a list page and in this table component we can

**0:29** · select rows sort columns or search for any items and we have a pagination here and this component is reusable so we can use it on different pages here we have action buttons that we can delete or view the item and when I click here it's gonna open this model and we can add a new item let's open up the single page

**1:02** · we can see the product detail another chart here and this beautiful timeline section and this design is responsive when I shrink the screen components will change their sizes and positions and you will see how easy to do that using the CSS grid system it's a great project to push your react and design skills even further

**1:31** · after completing this tutorial you will deploy our project using hostinger as you know it's the hosting sponsor of the channel but I also use it for all my personal projects and never had a problem for last two years and recently I deployed my blog application using one of their hosting plans so you can visit my website and see how fast it is

**1:57** · and don't forget when you buy a hosting plan you will get a free domain and SSL certificate at this price and if you use the link in the description below and the Llama Dev coupon code here you are gonna get an extra discount after purchasing you are ready to claim your free domain I will write something related to our app and register and our domain is ready so let's set up

**2:28** · the hosting start from scratch let's choose our domain and that's all after the installation you will be redirected to age panel all the settings of your hosting and domain are here so if you are ready let's create our application and deploy it using this panel

### React Installation

**2:57** · okay let's open the s-code and create here a new project and inside this empty project I will install my react application to do that we are going to be using vid you can open up your terminal and start a new vid project but it will take time and we will have to delete all the unnecessary files and codes and we have to add all the images that we are going to be using in this project to save this time use my GitHub repository react admin UI and there's a

**3:29** · starter Branch here and this Branch doesn't have any unnecessary codes it's a perfect way to start a new application and also I added here all the images so it's going to be faster to start so I will come here and download this Branch by the way at the end of the video I will create here a different branch and it will be the

**3:55** · completed version of our application so if you have any problem during the tutorial go and check that Branch okay I will come here you can directly download this folder or if you are using git on your computer you can just copy this link come back and right here git clone single branch Branch name I will paste my URL Dot and enter

**4:28** · as you can see our files are here to start our application we need to install the libraries to do that I will write here npm install or if you are using can just yarn

**4:44** · okay it's ready our libraries are here let's run our application yarn or npm Run tab and as you can see this is the URL that we are running our app I will open up and it's ready

**5:04** · as you can see in our application we are using typescript but even if you don't know typescript don't worry you'll understand everything because in most cases we won't even use it it's just a design we will just pass a couple of props by the way I created an awesome typescript tutorial for beginners you can find it in the cart on the top right of the screen so after this information let's create our first page I'm going to

### Pages and Layout

**5:32** · create a new folder and it's going to be pages and the first page will be the home page let's create our home component and I will create my component function and there's a warning here it just says you don't have to import react by default it's already imported so let's create our styling file to do that we will be using SAS so I will come here and say yarn at SAS

**6:03** · or npm install SAS let's create our style file I will say home scss let's create here a class name and I will say oh we can use this class name here

**6:20** · let's give a background color and we can see it I will call my page here of course we are going to change but we are just testing did I import my CSS okay I forgot let's import quickly form Dot scss and as you can see it's here okay it works basically it's the main layout of our application our Pages or components their name here is a class name and we

**6:53** · will import their style here so let's create two more pages I will copy this folder and paste inside my pages and one more and let's change their names I will say users users page like that I will delete this style and users

**7:27** · let's create products

**7:44** · and that's all so how we are gonna navigate between our pages to do that we will be using react router Dom let's open up overview and this is how we are using via crowd.com we are creating a new router and for each path we are just calling our page for example for the home page we will just call our home page here for

### React Router Dom Tutorial

**8:09** · the products slash products we will call this page it's that easy and finally using this router provider we will pass our router and we will be able to navigate between paths let's do that I will copy here I'll open up the app file and paste it here of course we should

**8:34** · import them like that and I'm gonna copy this Library and I will say yarn at react router Dom and instead of this div we are going to call our home page component for users it's going to be users component and one more I will duplicate this and it's going to be products

**9:04** · like that so let's create our router provider and pass it here let's delete this and right here router provider and the router will be the router that we have created okay let's see I will come here as you can see it's the home page if I say users is going to be users

**9:30** · products okay we can use our rather directly like that but in our case in our application as you can see we have a menu here and a nail bar and a footer and these three

**9:47** · components exist in home page in users page and products page so instead of writing those components one by one for each component I can create here a layout let's say const layout

**10:13** · and let's say main layout and inside this we will build our layout which includes Nail Bar menu and footer and finally any content here but first let's create our components I will come here in the source folder and create a new folder and it's going to be components and the first one will be there bar let's create our function and style file

**10:49** · class name here foreign CSS okay I will copy this and paste here and this is going to be footer

**11:16** · footer TSX and I will change here and finally menu like that

**11:35** · and that's all so let's use them in our app component I will say now bar Twitter and between them we are going to have a container and this container has this menu and

**11:53** · this content let's do that I will say container and we will have two more containers in the main container let's say menu container and the content container let's add here our menu

**12:14** · by the way let me close this and inside this container we will have our pages but I want to do this dynamically because it can be any component here to do that we are going to be using react router Dom Outlet by the way we can delete this route and this link we are not using and I will say hold that

**12:40** · we are going to use it I will copy this layout right now I'm completely changing my router let's actually delete everything here and I will say path is going to be the main directory and the elements will be

**12:57** · layout we are not touching any page we are directly adding our layout but we should pass our pages to do that we are going to be using children and right now we can add different paths I will say for the home page the element will be home right now we are doing exactly the same thing for users and products I'll say users

**13:31** · products and let's see right now as you can see Nail Bar menu and footer is here if I visit users for example oops not user users

**13:49** · they are here perfect it works you can directly create here a container and add this Nail Bar menu and footer but I prefer using a layout that because if we create a login or a register page we shouldn't see this nail bar or menu actually let's create here one more page and you can see better I will say login page

**14:24** · and so I will come here I'll say path let's say login and the element will be the login page

**14:40** · let's save this is our home page but if I visit login as you can see we don't have our layout here you can create your own layout for authentication I just wanted to show you how it works okay for this main layout I will import here my Global CSS let's close this pages and components and as you can see there is a Styles folder here and inside we have global scss

### Global Styles and CSS Variables

**15:08** · this is going to be our main CSS file let's import this here I will say import styles global scss right now I can use this main container and other containers here let's say main container and the font family of our application will be enter

**15:38** · and I'm going to give here a background color to do that we can create our own variables and we can use it all around our application actually let's create here new file and it's going to be variables and I will paste my variables here as you can see we are going to have a main background color and the soft version darker version and for the text color we

**16:04** · are going to be using these variables let's say here background text and let's use them here to do that I will say import this is how we are importing different scss files and I will say variables as CSS

**16:30** · so let's use our main background here like that and as you can see it's darker right now and for the text color I will say main color and it's going to be this white color and in our example as you can see this

**16:51** · main container is horizontal left side and the right side so let's make it flexbox I will come here and say container it's going to be display Flex as you can see by the way let's delete this red color here

**17:12** · okay perfect and for this menu container let's actually close everything and open up from scratch app and our CSS file here and right now I'm going to be using this mini container let's give it a width it's going to be 250 I will give some padding from top and bottom and left and right

**17:39** · like that let's check our example as you can see there is a line here let's create Boulder right I'll say two pixels solid and solved background color

**17:58** · okay it's here but it's not that visible because we don't have any item yet before starting adding our items let's take care of this container also I will just say content container I will give exactly the same padding and I will say with a hundred percent

**18:24** · so it's gonna fit in the rest of the container okay right right we can add our items but before actually let's take care of this now bar let's check our example as you can see we have two items here this logo container and those links container and again it's going to be flexbox because they are horizontal I will close them and open up my number

### React Navbar Design

**18:52** · and I'm going to create my first container it's going to be logo and other one let's say links or icons whatever you want and inside this we have an image logo dot SVG and the name of our application

**19:16** · and they are here and what about those icons we are gonna have one two three icons but this is a little bit different that because we have one more item here so basically I will create different container for this item and for this user again I'm going to create a container which has this image and username and again a regular image let's do that

**19:45** · I'll say icon two three four and after this first three I'm gonna add notification container and after this notification one more div and it's gonna be user let's add our images let's see search app and expand svgs

**20:12** · let's see okay perfect and these settings and what about this notification again we have an icon but I will create a span here and it will display the number of notifications let's come here and say image notifications SVG

**20:44** · and I will say span and let's say one and for this user again an image and a Spam here and the username let's copy and paste this image here

**21:01** · and let's see as you can see this image is too big so let's give a style I'm going to take this now bar CSS here on the right and firstly I will say it will be a hundred percent I will give some paddling and it's going to be horizontal remember display Flex before going any further let's take care of this big image otherwise we can't see properly so I will say user

**21:33** · and the image inside this user let's say 26 by 26 I'm going to give border radius 50 percent so it's going to be a circle and finally object fit cover you can use nested class names like that so you don't have to give different class name for each item it's really easy to use and I think it's more readable let's check okay perfect as you can see those icons are vertical let's make them horizontal

**22:06** · I'll say icons of course it's the parent of this user like that and I will say display Flex okay and I will do the same thing for this user it's going to be horizontal and that's all let's align our items to do that we are going to be using a line item Center

**22:37** · okay but it's not centered that because we didn't create yet let's say logo container again display Flex align item Center right now all items are centered but I want to separate this logo and those icons

**22:59** · so I will say just five content space between so it's gonna give a space between our items let's change this font weight and give a space between our items I will say font weight volts and gap between each item will be 10 pixels as you can see here is 10 pixels and I will do the same thing for my icons let's give 20 pixels between items I will say cat 20.

**23:32** · okay by the way where is our notifications it's going to be a plural I think let's see okay it's here so let's take care of this item in our example as you can see it's on the top right of this icon to do that we can use position absolute

**23:57** · inside icons I will say notifications sorry notification and I will say span its background will be red text color will be white let's give width and height and make it Circle border radius

**24:24** · so let's move this span somewhere here I will say position absolute top will be -10 right will be -10

**24:40** · now as you can see it's here that because it's positioning itself according to its first relative parent and it's the body of our HTML file to prevent this I will come to a notification it should be the first parent so I will say position relative and perfect let's enter this item

**25:05** · display Flex align item Center is going to be centered vertically but to Center horizontally I'm going to be using justify content Center it's that easy let's decrease this number this font size it's too big it's going to be 12.

**25:27** · and let's give a gap here perfect and that's all I think it was that easy guys there is nothing complex and this is why you shouldn't scared of CSS once you know display flex and

**25:46** · display grid everything is much much much easier in this example for the home page we are going to be using crit system and you will see how easy to use it okay let's quickly take care of this footer it's really easy again two items we will

### Footer Design

**26:06** · separate them I'll open up further and inside let's create a span the name of the application and one more span I will just copy and paste my text another admin dashboard

**26:24** · like that and as you realize I didn't give different class names let's see how we can give style without class names I'm going to open up footer CSS and I will say display Flex align item Center just five content space between okay they are separated but we don't have any padding let's give 30 pixels perfect and I want to make

**26:54** · this pen font weight bolt and I want to decrease the font size of this span as you know we have two spans here but this is our first item basically it's the first child and this is the last child so I will come here and say span

**27:15** · and I will say first child this is how we are selecting the first item on faith Bolt and the same way last child font size 14.

**27:32** · and that's all it's that easy this is how we are using selectors and pseudo classes in SAS for example for the hover effect just say and and hover

**27:50** · Let's test as you can see I will delete this let's close everything and let's take care of our menu let's see our example as you can see we have many items but also they all have different titles so basically I will create an item which

### React Menu Design

**28:18** · includes this title and the list items let's do that I will say menu and let's create our first item I'll create a span which is the title not last name Main

**28:35** · and I'm going to create a link here but we are not using anchor tag if you are using react router Dom it's better to use the link component and inside this we are going to have an icon and a text

**28:51** · so I will say image is going to be home icon and S Pen let's say list item title and it's going to be home page of course if you are using link you should add here any path I will say two and it's going to be the home page

**29:20** · and as you can see I can click here and go to home page so let's create one more item this profile I will copy this link and paste here that's a profile SVG profile

**29:40** · okay perfect create one more item I will just copy and paste this after that we are going to create those items but for now for the styling purpose it can stay like that let's open up our CSS file and give some style here

**30:02** · so I will come here and say item as you can see they are horizontal but I want to make them vertical so I will say display flex but I'm gonna change the direction of this Flex box and it's going to be vertical so I will say column and again gap between each item

**30:27** · like that I can give a margin so let's say margin bottom 20 pixels like that let's change those titles inside item I will say title font size

**30:44** · will be small and the font weight will be thinner and I'm gonna give a text color here but I want to use my variables remember how we are importing I will say import Styles variables as CSS and its color will be soft color don't forget here semicolon and perfect so what about those items

**31:16** · by the way I didn't give here any class name let's give list item so let's use it here again display Flex I'm gonna Center them and give a gap between them I will give a padding that because when we hover over we are going to see this effect

**31:43** · and remember how we are doing this horror effect and I'm Gonna Change to background color soft PG and also I will give here a border radius 5 pixels perfect so right now we can add here our items

**32:11** · but instead of writing them again and again and make this list bigger I want to create a data file here and fetch all those items using that file so I will say data dot TS and remember each item has a

**32:31** · title and list items and each list item has an icon and a text so I will copy and paste my data and as you can see this is the first item and its title is Main and each list item inside this array the second one third fourth and the last one I will save so let's use this array here

**33:05** · I'll say import menu from data so I'm going to delete this item we are going to be using only one let's wrap this and use our mini array here I'll save map for each item inside this array we are going to call this deal let's wrap this

**33:38** · like that and right now I can use my item title by the way if you are using map remember you have to use a unique key here and each item has different ID

**33:56** · it's Unique so we can use it so I will say item dot ID and what about those links again I'm going to delete this last one and we are going to be using one more map and I will say item as you can see list items and map and for each list item

**34:18** · we are going to return a link oops there's a typo here list item again I'm going to be using a unique key and we can use their IDs

**34:36** · and for this icon let's say this item icon and for this text list item dot title let's check and as you can see they are here perfect of course they are empty because we are not going to create all those pages and

**35:00** · of course it's going to be mobile responsive but for now let's create the main layout and after we can take care of them so what about this home page it looks really complex there are a lot of charts different components a list

### CSS Grid Real-World Example

**35:17** · here but don't worry using recharge Library it's really easy but before those charts let's see how we can use the grid system so let's open up the home page and create nine box I will close them and open up my home page and inside this container I will create my first box and I will give different class name box one let's say box one

**35:49** · and let's create others and change their names and class names four five six seven eight nine ten sorry only night I will delete them let's check okay they are here let's give border and padding for each box so we can see better I'm going to open up my CSS file here

**36:18** · and inside home container I'll say box and it's going to be 20 pixels padding for the radius will be 10 pixels and I will say border one pixel solid and let's use our variables let's try this I'll copy this and paste here that of course we should import this first

**36:46** · Styles and variables okay it's visible and let's create our grid system I'm gonna come here and say display grid and again gap between each item will be 20 pixels just like flexbox but as you can see they are vertical and right now I'm gonna create my grid template what I mean by that let's open up our example and as you can see we have four columns

**37:19** · first one second third fourth let's write it here I will say grid template columns and we are going to have four items here and each item has exactly the same width so I will say plan fr

**37:41** · y columns if I come here and change this one for example as you can see it's twice bigger than others but since we are using exactly the same width instead of writing them again and again I can write here repeat I'm gonna repeat four times but I'm gonna repeat one fr

**38:07** · it's exactly the same thing and what about rows as you can see it's a little bit complex because they are not in the same size but what we can say we can give minimum height for those items and after that we will give different size for each item

**38:26** · create auto rows I will say min max and it's going to be 180 pixels and Auto and as you can see it's exactly the same size and basically this size will be our wrong size unit if I say let's make this box six twice bigger than others I will just say grid row of this box will be 2 units or three units whatever

**38:55** · right now you are going to understand everything better let's check our app and for example for this first item as you can see its height is three times bigger than those small ones one unit two and three but to this is

**39:13** · exactly the same we are not going to change it but for example for this box its width is two times bigger than those small ones and twice bigger than their heights so the column will be two units and row will be two units and this one it's exactly the same three times bigger but the column is exactly the same but how we are gonna arrange them let's open up our app here and let's give a style for the first box

**39:45** · I will come here and say box one and I will say grid column pen will be one and it means its bit will be one unit it's not gonna change anything but if I say grid row

**40:05** · and span three units and right now as you can see it's three times bigger and according to its shape other boxes change their positions this is why grid system is perfect even if you change one of the box here it's not going to affect other ones they are just going to change their positions by the way I'm not sure you can see those Borders or not because

**40:32** · in the previous comments some people say they cannot see those soft borders maybe it's because of the video quality I don't know but in real life it's really visible but in any case I'm Gonna Change here for now and I will say let's say light blue oops it's too light maybe reduce here

**40:57** · okay so I will do the same thing for box four let's duplicate this and box four perfect and for this box 7 it's gonna be our bigger box the column will be two units and the row will be two units

**41:19** · you already know how to do that it's really easy box 7 column two row two let's open up it's that easy guys we have already completed our grid system the only thing we should do is applying responsiveness but it's gonna be at the end of the video so let's create this component I'm gonna open up my sidebar I

**41:47** · will close them and inside components I'm going to create one more component and it's going to be top box let's create our file and CSS

**42:05** · I will give my class name here top box scss okay let's call this component in our home page in this box I will say talk box

**42:27** · let's close here okay so what we are going to have we are going to have this title first let's add quickly I'll just say H1 tag and top deals

**42:44** · and after that we will have a list and it's going to be vertical and again instead of writing each item one by one we can create our own data of course in the future let me create our backend we are going to fetch those users but for now let's open up our data

**43:04** · and Export our data here as you can see image username email and amount they all are here and we have unique Keys we will use them let's import this from data and I'm going to come here and create a list and inside this list we are going to be using our users map for each user

**43:35** · we are going to create here a div let's say list item and don't forget your unique key here user dot ID and inside this item we will have two sections first one will be our user and the second one will be this amount we will use display Flex just file content space between and we will separate them like that let's see user section and amount I will say span

**44:07** · amount I will use dollar sign here user dot amount okay uh what about users inside this user container we will have the image and the user details let's say user texts and they are going to be vertical let's give image user dot image and user texts

**44:41** · you'll have two spans first one will be username and the second one will be email username user dot email

**44:58** · it's a funny cat by the way where is my cat no she is here high five if you don't know what extensions I'm using you can check my previous video and you can see how I'm using those pads

**45:15** · okay they are too big let's give them a style I'm gonna take this here close my sidebar let's start with this H1 tag I will just give margin button and after that I will say list inside this list we have list item

**45:37** · and inside this list item we have our user which has an image and user texts and inside those texts we have username and email and finally after this user we have our span which is amount

**45:59** · and that's all let's give our style firstly I will give style for this image 40 pixels object fit and of course for the radius 50 percent

**46:17** · okay perfect let's give display Flex I will Center them vertically and separate them horizontally and after each item I will add margin button like that and for each user I will do exactly the same thing display flex and I will separate my image and texts so let's say display flex and cut between them to any pixels

**46:50** · and those texts will be vertical remember how we are doing this Flex Direction column and between each item will be five pixels awesome let's increase this font weight and decrease font size so I will say 14 pixels and font weight will be 500.

**47:17** · and for the email it's going to be smaller and finally can't feed 500.

**47:27** · like this let's delete this background color actually okay and maybe I can increase this border if you can't see okay it's better I think it can stay like that

**47:51** · and what about those small charts by the way as you can see those titles are uppercased but in our example they are lowercased let's handle this I'm going to open up menu for this title I will say text transform and it's going to be uppercase okay and what about those charts I'm gonna

### React Chart Tutorial (ReCharts)

**48:18** · create a new component and after that we are going to be using a new library let's close everything here open up our sidebar and any component and it's going to be chat box

**48:45** · last name and scss file okay let's call this in our boxes each boxes two three five six I will open my home page let's select them and I will say chat box

**49:12** · but in the example as you can see we have different items like this title icon those numbers and charts basically we are going to need different data for each item but before let's see how we can use these charts I'm going to open up my terminal yarn at three charts

**49:39** · okay let me make this bigger and let's see drag the those examples actually it's too big okay it's better as you can see there are many different charts here area charts bar charts

**50:00** · and others of course we cannot use all of them but we will use this line chart area chart bar chart and the pie chart let's start with the basic one it's the simple line chart or tiny line chart okay it's a timeline chart as you can see we have a data here and we have this tiny line chart and it

**50:31** · uses this variable only PV and in our example we are going to be using the total number of users it's really easy to use we will just give a data key here and

**50:47** · its color and stroke width and we are going to have this responsive container I'm going to use it but before let's see what else we have we are going to have two sections this information and this chart section let's say box info and chart info let's create actually I can close here for now and this terminal and sidebar and I will say box info

**51:21** · and chart info and after that we are going to have a title which includes this icon and this text let's do that I'll say title is going to be an image for now let's say user dot SVG of course later we will change and after I will say span total users

**51:50** · like that and after that we have this big text so we can use H1 tag I think I'll say this number and we are going to add this link let's use we are crowded on link and inside view all of course we need a path here and it's going to be on page four now and finally inside this chart info container we will

**52:23** · create our charts and those texts let's say charts and texts let's say percentage

**52:39** · and duration 45 percent here is this mod okay right now we can add our chart let's see first okay we don't have lexbox yet but after adding charts we will see I will copy here and paste inside my chart

**53:08** · let's import them responsive container line charts and line as you can see we need a data let's copy this for now we are going to change it I will paste here

**53:31** · and let's see it's not here because something wrong with sizes we are using here responsive container it says with a hundred percent but we don't have any width and height for the parents let's open up our CSS here and give our

**53:49** · style first firstly our chart box will be display flex and I will say height 100 percent I set a hundred percent because for this box info we are going to separate those items let me zoom in I will say box info

**54:11** · display Flex Flex Direction column and just five content will be space between like that as you can see it fits into our height and for this title let's give flexbox and align item Center

**54:31** · and gap between items will be 10 pixels perfect for this chart info as I said we are gonna need a size to see our chart you can give any size but in our example this chart info container is twice bigger than user info container to do that we can use flex properly remember it's display Flex box info will be Flex one and the chart info will be

**55:05** · Flex 2. let's give a background color and see better as you can see twice bigger and I will do exactly the same thing display Flex Direction column and I will separate my items let's delete this

**55:23** · column and I will say just five contact space between so I will say height 100 percent meet a hundred percent okay it's here but as you can see it's too big this one is smaller let me check my application okay actually I made a mistake this container should be bigger

**55:53** · it's going to be two units but this one will be three units as you can see it's much better right now of course we are going to delete those dots but for now let's take care of this percentage and this duration after this chart I will say texts

**56:18** · and they are going to be vertical the extraction column and I will say text align right because in our example they are here let's check okay perfect let's give style for our texts I'll say percentage font rate will be bold font size will be 20 pixels for the duration font size will be 14. and what about its

**56:50** · color in our example as you can see some of them are green and this one is red basically it's going to be dynamic so I shouldn't provide it in my CSS instead I'm going to be using my component and I'm going to write here a conditional style but for now it can stay that because we don't have any data yet I will come here and say dot and it's

**57:18** · going to be false and that's all but there is no interactivity let's check here as you can see when I hover over I can see my data to do that we are going to be using recharge tooltip let's open up this API and search for tooltip

**57:40** · okay it's here we can use it most of our charts and it has many property basically it allows us to show our data in different ways let's use this tooltip here before this line let's check right now

**58:02** · as you can see it's here but I'm gonna change its properties here because in our example as you can see we don't have any background color and the position of this tooltip is not changing like that

**58:24** · okay there is a contact style it's going to be a transparent I don't want to see any background let's come here and say content style background will be transparent and also I don't want to see any border

**58:43** · scrubby none perfect and I'm gonna delete those numbers it's a label so basically I don't want to see this label Style I will say display known okay it's gone the only thing here we should change and it's the position

**59:15** · as you can see we can give any position on the X and the y-axis let's come here and say position X will be 10 y will be 50.

**59:32** · actually I can change this y okay it's better right now so let's pass our data let's see what we have we have an icon a title

**59:49** · number when we pass our data we are going to need the data key remember we are using those data keys here and also we will change their stroke colors so we are going to need a color and we are going to need this percentage and that's all I think let's create our types and take those props

**1:00:18** · I will close here and if you are not using typescript you can directly right here props and use them like that props.title

**1:00:33** · DOT number don't forget this icon and here what's that let's remove by the way we don't need this width and height we already have our responsive container if you are using responsive container I recommend you to make this with 99 percent it prevents a lot of conflicts

**1:00:56** · and of course our data will be props dot chart data I'm going to change this key probe spot data key this color like that by the way I will change this link color also where is our link here

**1:01:20** · I will give inner Style and I will say color will be props dot color and what else percentage and again I'm gonna give an inner style but we are going to have a condition if this number is positive it's going to be green if it's under 0 it's going to be this tomato color so I will come here and say style and color will be if props dot percentage

**1:01:52** · smaller than 0 is going to be tomato if it's not it's gonna be lime green okay that's all I think right now I can take my props I can delete this data

**1:02:09** · and let's write here our type it's going to be props and what we have we have a color which is a string icon is going to be a string title data key we will have a number it can be either a

**1:02:33** · number or a string percentage will be a number because we are using it in our condition it should be a number and finally chart data will be an array

**1:02:48** · and inside this array there will be only objects because remember in the chat data we have an array and it includes only objects right now let's create our own data and name will be users and we are going to add here to user numbers in this case our data key will be user numbers let's do that I'm going to open up my data and I will come here and paste my

**1:03:19** · data as you can see it has everything we need let's use it in our home page because we are going to pass this as a prop and I will come here and say send everything inside chat box user

**1:03:35** · basically it's sending every properly here as you can see there is an error that because we didn't pass our prop type is going to be a props and there is nothing wrong here let's check there's an error here because we are not passing anything I will comment them out I will save and let's see

**1:04:01** · perfect so I will do the same thing for other items it looks like that because we removed them let's open up and add other data I will paste it's going to be product revenue and conversion rate let's save and pass them here chat box products and others

**1:04:35** · okay but I missed something here it's going to be box four okay it's here I'm gonna remove this and paste it here okay it works as expected

**1:04:52** · perfect and right now we can add other charts I will zoom out and let's add those they are really easy I'm gonna open up bar chart and again we are going to have a data responsive container and our chart here

### React Dashboard Animated Charts

**1:05:15** · yeah just giving data key and its color it's that easy I will copy this and create a new component let's close them I will say bar chart box let's import our style file

**1:05:44** · and the CSS file okay and in this container we'll have our title again we are going to take this as a prop and after that we will have our chart and I will paste my chart here

**1:06:06** · like that and again I will say props props.title props dot chart data its color and data key here

**1:06:28** · and again I'm going to add here a tooltip and I'm going to change its style let's check our example as you can see its background is our main background color so I will say content Style background color our main color here and I will give border radius it's going to be 5 pixels and label Style again display none

**1:07:01** · and I'm going to add here one more thing let's see first of course we didn't add this in our home page let's before create our type and data and after we can pass our component type will be props it's going to be title string and three more it's going to be color data key and the chart it's going to be object array and others

**1:07:35** · will be string let's pass our type here props and let's create our data I'm gonna open up data file and here I will paste first one will be chat box visit and the other one will be Revenue let's save and pass them in our home page I'll say home page and inside this 8 and 9.

**1:08:02** · a chat box and I will pass here my data the first one will be visit and the second one will be Revenue let's close here and open up our CSS otherwise we cannot

**1:08:23** · see our chart as you can see that because we don't have any size I can close data firstly I will say a hundred percent write a hundred percent I will say H1 tag all size will be 20 pixels and I will give margin button

**1:08:45** · here and after that we have a chart height will be a hundred percent and again I'm gonna delete those width and height and I will give here 99 percent

**1:09:01** · I will save here okay there's something wrong let me close this first I will give background color okay it's overflowing here because of this margin button actually I can delete here and give a height here because remember the minimum height of our box is 180 pixels

**1:09:31** · so if I give here directly a height it's not gonna hurt our application I will just say 150 as you can see they are here but there is something strange there is a horror effect here to prevent this I

**1:09:48** · will come here and say cursor and I will say fill none it's not going to show any color okay perfect for this one so let's create our pie chart let's see again we have title our chart and this

**1:10:10** · container here let's create them I will close them and open up my components and create a new one I will say pie chart box let's create quickly our files

**1:10:36** · and the container class name okay I'm not gonna take any prop that because it's only one component I will directly paste my data here if you want to make this component reusable you can just take it as a prop but for me it's totally okay I will just come here and say H1 that was the title let's copy this and paste here

**1:11:04** · and I will say charts and let's see which chart we are going to be using it's going to be a pie chart okay this is different

**1:11:22** · okay this is similar but we need something like that let's copy this we don't need this second one I will remove it in here we don't have responsive container let's add and I will paste my chart let's delete this one

**1:11:48** · and let's import them we don't need any Mouse effects I will tweet and this width and height and I will come here and say 99 percent

**1:12:05** · and let's give a height it's going to be 300. and what about here in this example it uses different array for colors but I added these colors in my data so we don't need this array here I will import this cell and I will say item the unique key will be item dot name let's check okay it's a unique name

**1:12:32** · we can use it and the color will be item dot color that's all and again I'm gonna add here a tooltip but before let's use it in our home page and see how it looks number four I will say pie chart box

**1:12:56** · right now I'm gonna make some changes here but before let's add our tooltip and I'll say content Style the background will be white let's see our example

**1:13:17** · okay it's white and there is a portal radius let's say 5 pixels and after that I'm gonna change this size as you can see it's big I will give some inner and other radius let's make this seven percent

**1:13:38** · and 90 percent I can delete here we don't have to feel anything and also I can delete its position we are going to Center this okay perfect so let's create other items and after give our style as you can see we have some options here

**1:14:04** · I'll say options container and for each item we will add different options so I will say data.map for each item let's add here option View and don't forget your unique key item dot name and we are going to add here a DOT and the item name and after that its value so let's say title container we are

**1:14:35** · going to have a deal it's going to be r dot let's give class name Dot span item name and after this title you will have another span and it's going to be the number okay and the color of this dot will be dynamic so I'm going to be using inner style background color item dot color

**1:15:07** · okay so let's give a style I can take this here close my sidebar and let's start firstly let's say a hundred percent display Flags Flex Direction column and just five content space between and I'm gonna Center my chart I'll say chart display Flex align item Center just like

**1:15:32** · content Center and for those options they are going to be horizontal and again I'm gonna separate them display Flags justify content space between and I'll say Gap 10 pixels and phone size will be smaller okay so what about this dot we don't have any width and height for this dot so I will say title I thought it's gonna be 10 pixels

**1:16:03** · border radius perfect but this title should be display Flex and get between items and I'll say align item Center

**1:16:19** · by that and I can separate those items I forgot adding here option it's the parent and I will say full extraction column and cut between items will be time pixels and a line item Center

**1:16:40** · perfect but I will add one more thing here for this container I will say with a hundred percent height 100 percent for now there is no problem but when we shrink the page this inner and other radiuses will be bigger or smaller according to this chart and that's all I think

**1:17:08** · let's create our last chart here I'm gonna create another component big charts big chat box T ASX style file

**1:17:32** · and let's create here okay let's see what we have again a title chart container responsive container and our chart but with chat we are using is going to be simple area chart now it

**1:17:57** · includes only one item here let's use this one we are going to have multiple items I will say H1 tag our title chart container and inside we are going to pass our chart here let's import them

**1:18:26** · I'm going to explain them don't worry and just importing for now and let's pass our data

**1:18:41** · and let's see okay we have exactly the same data but this time it uses all those data keys not only one and each area represents different data

**1:18:57** · Keys as you can see UE PV and AMT and they have different colors we have tooltip to see our data here it's exactly the same thing but there is something different there is a grid here as you can see those dots but in our example I removed them if you wanna you can keep it but I will just pull it let's delete this and what else this x-axis represents

**1:19:31** · this line and the data key is name let's check our data as you can see page a page B he chose them on the x-axis and for the y-axis it just shows the number according to area data key it's that easy there is nothing complex by the way there is a style here with height we can delete them because we are using responsive container

**1:20:04** · let's make this 99 and remove this I will keep this margin and the others can stay like that actually let's change our data we are going to be using the name of the week books clothes and electronics basically this is how much we make from

**1:20:27** · different kind of products so let's change our data Keys it's going to be electronic clouds and books let's give our style again 100 height

**1:20:44** · 100 percent display flags flag extraction column and justify content space between and for the chart I will save it a hundred percent and the height will be 300 pixels let's add this on our home page box seven scrubby big chat box

**1:21:13** · and perfect this is how we are using react recharts so we completed our home page so let's take care of our lists I'm going to open up users page right now I'm going to add here those items as you can see we'll have this

### React MUI DataGrid Tutorial

**1:21:36** · container includes title and button and after that we will use material UI data grid let's close them and I will open up users and here you'll have an information container which includes the title let's say users

**1:21:58** · and a button add new user and after that we can add our data grid to do that we are going to be using mui data grid let's see there's an awesome table here that we can select rows we can sort or use the pagination we

**1:22:19** · don't have to invent anything from scratch we don't have to deal with complex HTML tables and all these functionality let's open up installation I will copy here open up my terminal and paste

**1:22:37** · but after that we should add those libraries also it's the core library of mui and the emotion is just like style components so let's copy this and paste here let's come here and let's open up this code

**1:23:00** · firstly we are going to Define our columns which are the titles of our rows first name last name H or whatever and after creating them we are going to pass our data our users

**1:23:17** · products whatever and using this data grid component we can show them in our page let's create another component and use this data grid there I will say data grid actually let's give different name because mui is already using that name so I will say data table

**1:23:45** · I will create my function give the CSS file class name and this style file here

**1:24:01** · okay let's paste it I will copy and paste I will import this and after that we are gonna need those rows and columns and after I will Deep dive into those columns and you are going to understand better let's paste it here we are going to need those types let's import I will save and let's use it here

**1:24:34** · let's see okay there is something wrong with the scss file okay I forgot here slash and it's here it doesn't have any background color let's give I will take this here let's see what we have firstly I'm gonna give here a class name it's going to be data grid

**1:25:06** · and I will say background white okay and I want to give some padding inside I will say 20 pixels perfect and let's check our example and as you can see there is a search button here that we can search any name or any other column here let's add this

**1:25:33** · I will say slot props and I'm going to add here toolbar and I'm going to write my options here I will say show quick filter which is the search input and it's going to be true in this case when I write here something it's going to immediately search for items but it's not the best way because it can be expensive to use it for each letter instead we can give here any time limitation and after one

**1:26:04** · second or 500 milliseconds we can start searching in this case it's gonna search after a couple of letters and it prevents making a lot of calculations for each letter to do that I will come here and say quick filter props and debounce milliseconds will be 500. okay we have our props but I forgot doing the slots itself it's going to be toolbar and create toolbar

**1:26:39** · let's see okay it's here let's search for any name here as you can see it starts searching after 500 milliseconds but I don't like here maybe we can delete those filters if you wanna you can leave them but I don't know this version is much cleaner and also our search button is here I will come here and say disable column

**1:27:09** · filter as you can see it's gone let's remove others also disable density selector column selector and right now I can change my style and I can take this search button here to do that we are gonna need its class name let's right click and inspect oops it's

**1:27:36** · too small let's see what class name we have here as you can see it's mui data grid toolbar container we can choose it

**1:27:52** · inside data grid I will say my container and by default it's a flexbox let's see toolbar container is a flexbox so if I write here Flex Direction row reverse as you can see our search button is here right now so let's see how columns and

**1:28:18** · drafts work I can't close here and here and as you can see our columns have field name header name and with basically field is the ID of columns header name is those names here

**1:28:42** · and we can give any specific width for example for ID it's just 90 pixels for name is 150 150 you can give different size here

**1:28:58** · and we can edit our items let's double click here as you can see I can write anything if you wanna you can remove them but they can stay what's different there is a function here it takes all the row parameters and in this example it joins the first name and the last name of the row

**1:29:23** · first name last name so using this function you can combine items and let's check our example as you can see we are using an image but how we are gonna do it here I will come here and I will add one more column and the field name will be let's say author header name again Avatar I will give a bit it's

**1:29:51** · going to be a hundred and right now instead of a text I want to render something else I can render any other HTML element to do that we are going to be using render cell function and it takes the parameters remember how we are using it here we can use any row item we will do the same thing here

**1:30:20** · return an image and the source will be params.troll dot image for example and if user has no image we are going to return no Avatar dot PNG of course inside code let's see of course we don't have any style let's give I will come here and say image 32 pixels

**1:30:53** · it's going to be a circle an object that will be covered and as you can see we don't have any image and it shows this no Avatar PNG in this render function you can create your own HTML elements let's check our example

**1:31:16** · we can use any Boolean here let's try after this column of course we are going to change it but I'm just showing you how to use material UI data grid I'll say fields status other name status I will say bid let's say a hundred and I'm gonna give here A type and it's going to be Boolean

**1:31:45** · in this case if I give here and a value let's say status true for example this one false as you can see the first item is true so it uses this check mark and others are false if you don't write anything it's gonna be null and in this case it's going to be false so you don't have to add any icon here and one more thing

**1:32:15** · we are going to add those action buttons and again like we did here we are going to render something else let's do it here I will duplicate this it's going to be actions and I can create here any to you let's say action and inside view and delete

**1:32:46** · now you can add here any icon perfect but I want to make this data grid reusable so we can use it in users products orders posts or whatever so basically we should take those columns and drops from the parent and make this

**1:33:07** · data table dynamic so what I'm gonna do is deleteing those columns and rows instead I'm going to come here and paste my columns here this is the user columns let's import this and I'm gonna pass these columns to my data table columns is going to be columns

**1:33:33** · of course typescript warns us that because we don't have any props here let's say props props and let's define our type columns remember it's type it's gonna be click call Def and array we are gonna get rows it's going to be checked array and let's use them here props dot rows and props dot columns

**1:34:06** · right now I should pass here one more thing and it should be rows but I'm not going to write those items here because in a real world example we are going to fetch this from a database so I'm going to be using my data file remember we are fetching everything from database except of this menu it can stay so I will paste my users here users role

**1:34:37** · and pass it here and Perfect by the way I can increase this data limit here it's just five I'm gonna make this 10.

**1:34:53** · and it's much better right now we have images and other details but we don't have our actions that because I'm not gonna Define this in any list page instead I'm gonna Define it here and I'm gonna add it here let's do that I will come here and say const action column

**1:35:17** · is going to be again grid called tab but it's not going to be an array it's just a one column and I will say field will be action header name again action that's good 200 and I'm gonna write render cell remember how we are using it params

**1:35:42** · return I will say action and inside this we are going to have two buttons first one will be this view button but it's going to be a link when I click here we are gonna see our user and this can be just a div that we can click and delete the user I will say link react router Dom link

**1:36:07** · view dot SVG and after that let's say do it then again image delete dot SVG and when I click on this button we should go and see the user for example as you can see we are going to users and its ID but we don't know which page we

**1:36:29** · are using what we can do we can come here and pass that as a prop so I will say slack for example and it's going to be users let's write it here slack it should be a string and we can use it here I will say slack and we will use user ID or product

**1:36:58** · ID or whatever basically it's going to be the raw ID I will say params row dot ID oops I forgot props here okay and when I click on this icon say oh click we are going to delete the item which has this row ID so let's

**1:37:20** · create here function handle delete and I will paste param straw and ID let's create this function somewhere here const handle delete it's going to take an ID which will be a number and we will just make here our API call

**1:37:45** · delete the item that's console log I'll say ID has been deleted but how we are going to use this column I will just come here take every item inside those columns but additionally add here action column that's all let's see

**1:38:11** · as you can see they are here and when I click here this is the slack and this is the row ID of course we don't have the page yet but it works properly if I open my console and try to delete this for example as you can see this is the ID

**1:38:32** · perfect right now our table is dynamic we can't pass any column doesn't matter we can just pass here our slack it can be products orders it's going to take its ID and show the page and we can do the same thing for this button if you are using any API for example axios dot delete function API address and here slack and ID API users 1. API products 2.

**1:39:09** · and let's give our style here I will say action display Flex gap between icons will be 15 pixels and image inside 20 pixels I20 pixels

**1:39:25** · and cursor will be pointer like that okay let's do the same thing for products but before I forgot queuing style for users let's open up users I will say info container is going to be display flex line item Center and gap between items will be 20 pixels

**1:39:52** · like that I can give margin here margin button to any pixels and a button inside I'll give just padding and cursor will be pointer okay actually let's create a new component and when I click here we can show a model that we can add a new user let's close them I will say add

### React Modal Tutorial ( Add New Item )

**1:40:24** · TSX and scss

**1:40:39** · let's see in our example I will turn back I will click there's a overlay here and our background is this dark color transparent dark and we have a box here that shows our inputs this image button and the send button and when I click here it's gone

**1:41:01** · let's see what we are gonna need that because it's gonna be dynamic again we can change this user it can be products orders we can change those items and also we should pass here close functionality because we can open it in the parent but close it in the child component you are going to understand everything better right now I will say props

**1:41:29** · I will say type props again I'm gonna take the slack I'm gonna need the columns and the closing functionality let's try to open first actually I will remove this and open up users I

**1:41:46** · will just say const open set open view State hook at the beginning it's going to be false we are not going to show this add component and I'm going to write here a condition if it's open show the add component

**1:42:09** · and this is what we are going to pass to our child component set Autumn will be set open so we are going to take that functionality and close our add model of

**1:42:24** · course it's going to be string columns will be array or we can directly take our data grid columns let's do that create call Dev array and this is going to be let's see its type as you can see its type is react dispatch and as a generic we are passing set State action and one more generic

**1:42:51** · because it takes only pull you finding types are that easy just hover over your element and it shows everything I will just paste it here and let's create items

**1:43:06** · I will say model we are going to have a close button close it's just going to be X or you can give any icon here and after that I will create a title and I'll say add new slack props dot slack so let's pass other items slack and columns user and columns will be columns

**1:43:39** · as you can see there is no error and here and right now I'm gonna add here a form and we are going to take those columns and I'll say map each column oops I forgot writing props here

**1:43:57** · we are going to return an item and inside this item we are going to have a label it's going to be column dot header name as you can see all those items here we can use header name and I will say input input type will be column type in this case we have to give type for each field here we are not going to use this ID and author but others we have types as you

**1:44:28** · can see string string and this is going to be Boolean I forgot here and column DOT type and I'm gonna give placeholder column dot field but if I do that it's going to take all those columns including this ID and Avatar but I want to filter them we are not going to use them here basically before this map I can filter them I will

**1:45:00** · say item if item fields doesn't equal ID and item Dot Fields doesn't equal image that was the name okay I set our turbot image is more generic we can use it for products also if it's not ID and image we are going to map through this filtered items

**1:45:32** · not see I'm gonna come here and when I click on this button I'm gonna set my state so I will say on click set open it's going to be true so I can do the same thing for this close button so I'll say on click

**1:45:54** · set open and it's going to be false of course again props I keep forgetting that that because I'm generally using my probes in an object the structured version but I didn't want to confuse you because when I do that it looks a little bit complex this version is much clearer but as I

**1:46:21** · said I prefer other version this is why I always forget these props okay let's see I'll click oops it's not our project I will click it's here if I click here it's gone perfect

**1:46:39** · and all those items are here so I can create here a button inside form save button and send and I can create here on submit event and let's say handle submit

**1:47:00** · and let's see which event we are using I will hover over here and as you can see form event and inside is HTML form so I'm going to paste it here and I will say to end prevent default so it's not going to refresh the page after clicking that button and after that we can add new user or

**1:47:24** · products or whatever add new item as you remember we already have a slack here so if you are using an API you can use axios dot post the API address and

**1:47:39** · slack not remember it's not plural so you can add here s and you can pass any data here but we are going to do this in the next tutorials I will save and let's give a style

**1:47:56** · I'm gonna take this here close my sidebar so I will say with 100 PW H 103h that because it's going to be full screen remember it's our overlay I will say position absolute and it's gonna contain the all screen top zero flat zero if I say background color

**1:48:21** · as you can see it's full screen right now of course its color will be a little bit transparent let's paste it here like that and let's enter everything display Flex align item Center just file

**1:48:37** · content Center perfect and what about our model it's here I will give first the a padding for the radius let's say 10 pixels and background color we are going to be using our variable let's import and it's going to be main color

**1:49:03** · and I'm gonna put my closing button here so we can use position absolute but remember the parent should be relative and I will say close position absolute let's say 10 pixels right 10 pixels and I'll say cursor

**1:49:21** · pointer this background should be dark there's a mistake here it's not going to be color it's going to be background color perfect and what about this H1 tag margin button font size 24 and color will be let's say soft color

**1:49:47** · okay so let's take care of those items I mean this form inside model I will say form it's going to be display Flex I'm gonna give a maximum width and it's going to be 500 pixels just 5 content space between okay they're horizontal but I'm gonna add here Flex wrap

**1:50:12** · and it's going to be wrap in this case it's not gonna overflow anymore our container is gonna move them into new line like that let's take care of those labels I will say item display flags flags Direction column gap between items and I will say margin bottom 20 pixels and for labels

**1:50:40** · all size will be smaller for inputs let's keep padding I'm going to delete the background color it's going to be transparent and the font color will be white let's delete the outline and I'm going to give a border one pixel solid and that's a soft color perfect and Border radius Maybe

**1:51:12** · um what about this button I will say button this will be a hundred percent I will give padding and cursor pointer okay it's not a hundred percent let's check our button form easier

**1:51:31** · oh it's inside item which will be outside of course okay if you want to you can increase the item size 40 percent for example this time is going to be only two items and it looks much better I think and that's all let's do the same thing for products and after we are gonna handle this single page

**1:52:02** · let's open up sidebar I'm gonna come here and I can actually copy and paste here we are going to use exactly the same thing of course it's going to be products add new products let's close here and right now I'm gonna import this data table slack will be products

**1:52:31** · in the same way product I'm gonna import this add component and let's create our columns I'll just copy and paste ID product image title Color Price

**1:52:49** · producer created at and in stock and it's going to be Boolean there is nothing complex here and I'm going to open up my data and paste my products I'm just using some random images I hope they are not broken and let's paste it here

**1:53:11** · products plus protects or products rows okay products and let's change here let's see I'm going to open up products as you can see they are here all the columns and rows of course we don't have any style let's give quickly actually it's going to be exactly the same style

**1:53:42** · like that when I click here as you can see it has changed right now it's not a user it's a product perfect right now our components are reusable we don't have to worry about creating new adding page for each item here or creating different data tables we are just passing our props that's all and let's create single pages

### React Single Product Page Design

**1:54:11** · I'll close them and let's create a new component single file

**1:54:30** · and the CSS file okay so let's see our example and decides what we are going to do when I click here it shows the user firstly we should create different pages for users and products using react radulum we can navigate to different users let's do that

**1:54:55** · in the pages we are going to create user and product it's a single product and single user product CSS and I will do the same thing for user quickly

**1:55:38** · okay let's close them and open up our app.js and here I'm going to add two more paths and the first one will be users but we are going to pass here our ID we are passing parameters using column it's gonna be single user let's do the same thing here ID

**1:56:06** · product that's all let's see right now when I click here as you can see there is no error anymore we are seeing our product right now using this number we can fetch our single product and pass this data to our single component so I will come here and say fetch data and send to single component

**1:56:36** · I will do the same thing for user and right now I can use my single component and pass my props of course we didn't create yet they can stay like that for now not later we are gonna pass different data let's open up this component and see

**1:56:58** · what we have I will close everything here and open up my example as you can see we have two sections first one on the left and those activities is going to be flexbox let's do this quickly I'll say info one more and it's going to be activities

**1:57:22** · and inside this info we will have the product or user information and after we will have a chart actually let's name it View and this small container can be info I will say View and inside this view we will have

**1:57:42** · info chart I was going to name it user but I just remembered it's going to be dynamic it can be orders products or other things so using info is better option here and inside this info you will have different container here which includes image title and button by the way they are not vertically centered we are going to fix it and after that we will have details let's say top info

**1:58:15** · and details and here we will have an image this item name and a button update and after that you will have those items of course we will use a map here but for now let's create one item item container and it includes a span

**1:58:43** · item title and item value let's see for example username John Doe and we can add our chart right now we are going to be using this chart let's see it's the first chart simple line chart let's copy this and paste here let's import them

**1:59:15** · do I use this Grid or not let's see okay no grid I can delete this x-axis y-axis tooltip Legend Legend is basically those indicators green is visits purple is clicks like that and our lines we have two lights here

**1:59:43** · we are going to take this data as a prop but for now to see better I will just copy this paste here okay there is no error and finally let's take care of those activities we have this title let's say H2

**2:00:11** · and we have a list here let's create a list I'll say UL and let's create a list item and inside this item I'm going to create a div and this div includes this text let's say a p attack

**2:00:31** · and a type and it's going to be like three days ago one week ago let's paste and I'm going to create more items like that and I will do the same thing for this item I will create different items let's see okay there is something wrong with this CSS I forgot here Dot

**2:01:03** · okay let's give a style let's check what we have we have View and activities let's create them first

**2:01:21** · and inside view we have info and chart and inside info we have top info which includes image title and button and details

**2:01:39** · so what I'm gonna do is making this container display Flex and the left side and the right side will be exactly the same size remember blacks is going to be one one

**2:01:59** · like that I will say display Flex for this top info align item Center and gap between items will be 20. like that of course we don't have any image yet let's actually add one I will copy this image address and paste here

**2:02:21** · okay let's give a style I will say with a hundreds right a hundreds motor radius 20 pixels and object that will be covered now for the title this H1 tech let's say H1 8 will be 500.

**2:02:45** · okay and what about details after this top info we have details I will say font size 18 pixels and the item inside I'll say margin 30 pixels from top and bottom 0 from left and right like that and for this title this one I'll say font weight 600 is going to be

**2:03:16** · thicker I will give margin right and I will say text transform capitalize in this case the first letter will be always Capital so what about our chart I will say margin top 50 pixels I'm

**2:03:33** · gonna separate them let's give it it's gonna be let's say 80 percent I'm not gonna make it 100 it's gonna be a little bit smaller like that I'm gonna give this space and let's give height we can give a high tier because for the mobile devices we are going to delete this chart it's too big for mobile devices and as you can see there is an HR tag

**2:04:01** · here let's add between info and chart I'm going to come here and say HR I will say with 90 percent height will be zero I'm just gonna give border let's say one pixel solid and let's try Gray okay it's too big maybe 0.5 okay but I'm gonna give some margin

**2:04:34** · like that of course when we add more item it's gonna look better but about here I'm gonna change this title remember it's H2 attack I'll save margin button 20 pixas for items list items

**2:04:57** · I'm gonna delete this style type is going to be done I'm gonna use position relative because we are going to be using position absolute for these effects I will say with one pixel it's our line

**2:05:15** · let's give pairing top 5 pixels and I'm gonna give background color and it's going to be this red color as you can see our line is here right now I'm gonna add my thoughts to do that we are going to be using after

**2:05:35** · we don't add any content it's going to be empty I will say position absolute let's give it an height 10 pixels or the radius is going to be a circle it's absolute part we didn't give any position let's say 50 percent and button will be zero

**2:05:54** · background color will be exactly the same I can use it let's see okay they are here but I wanna Center this to do that we can use a transform effect I will say translate X on the y-axis I'm gonna move this just 50 percent in this case it's going to be on the middle perfect and what about these do foreign

**2:06:28** · eight pixels I will give some padding and a background color it's going to be exactly the same color but I just added here some transparency like that perfect let's check okay we are going to give these spaces but before let's take care of our texts I will say P tag margin button 5 pixels and time font size 12. so let's fix this

**2:07:01** · space where is our Ally okay I set 5 pixels but it's going to be 50 pixels and awesome if you want to you can start it here but I prefer using the bottom and it looks pretty nice when we add more items it's going to be nicer and that's all let's open up users

**2:07:26** · actually let's give URL for those items these users and products maybe home page I'm going to open up my data okay it's already home page okay they are here but we are not using them in our menu okay I forgot it's gonna be list item.url here

**2:07:52** · okay it works so if I click here it's still the same but it should be our products so let's take our props actually all those items are props it's

**2:08:08** · gonna be a little bit long let's close them let's delete this data we will send this from apparent and I will say props props let's create this type props firstly we'll have an ID oops

**2:08:30** · I forgot equal here and we will send an image it's going to be a string of course it's not required you can give here a question mark we will have a title string info is going to be an object

**2:08:48** · all this information and not about this chart remember we have two lines here it means we have two different data keys so that's a data keys will have their names string and colors

**2:09:09** · and finally data is going to be object array okay oh I forgot those activities let's create I'll say time string and text will be strict if you want to you can give question mark for them if you don't want to make them required and that's all I think

**2:09:35** · let's use them here props dot image of course if there is an image and it's going to be title and we are going to be using this object here we will map through our object I'll say object entries and I will say info and after we can use

**2:10:03** · map right now it's an array for each item we'll return this item and again unique key item and the first element the first element is those titles and the second element is those values let's use them here item and the first element

**2:10:29** · and the second for this chart I'll say props dot charts again I'm going to write here a condition if there's a chart and props of course and there's a mistake here that because our data is here

**2:10:50** · I should say data for those lines we should map through these data keys I will say props dot charts dot data keys I'll say map for each data key

**2:11:11** · we can return this line and its data key will be data key and the color will be data key dot color sorry it's not going to be data key data key dot title okay there's something wrong okay I said just an object but it's going to be array of course

**2:11:38** · we have more than one data key and it's not a title let's see okay it's name as you can see this is why typescript is useful you can see the errors in advance and finally for activities let's delete those two items here I'm gonna map through my activities let's give here a condition if there's an activities use this URL again props

**2:12:11** · I should get used to it and I'm gonna wrap this delay and I will say props dot activities dot map for each activity return this Li and give here a unique key activity Dot

**2:12:33** · let's say text I think it's Unique and there is an error let's see and again I didn't add here array and there is a mistake here I should move it here let's change our title activity dot text and type

**2:13:02** · okay right now let's create our data and send them as a prop I'm going to open up data and I'm going to add the single user and the single product and all this information are here chart data activities we are going to use them

**2:13:26** · this is the single product and this is the single user let's open up our user page all right now I'm gonna pass to single user let's open up products and do the same thing and perfect let's see our app as you can see it's a product and it shows this product if I open up a user

**2:13:58** · it shows the user awesome so our data is working right now you can fetch data or add new one actually I've created a simple API as you can see it's a simple express application our users are here it's exactly the same so this data is going to pretend like a database and we have endpoints here it sends the users all users we can get a single user

### React Admin CRUD Test

**2:14:27** · add a new one or delete the user and it runs on this port number you can use it to do that I'm going to be using react query so I will say yarn at 10 stack react query and don't forget it's just a design tutorial so I'm not gonna Deep dive into every detail about react query if you don't

**2:14:52** · know how to use it you can just use axios and use effects it really doesn't matter for now not basically let's check firstly we should wrap our application with query client provider so I'm going to open up my app and for this Outlet I can wrap here

**2:15:16** · I'm gonna import them and let's create this query client like that and right now we are ready to use let's make this smaller or just close and right now I'm going to open up users and I'm gonna fetch my data here let's see how to do that we are fetching data using a query function and we are giving just a simple name for this and it returns is loading error or a data

**2:15:50** · let's copy this I will paste here let's import I will delete this and I'm gonna wrap my data table and I will say if it's loading right here loading if it's not show the data table and instead of this use the rows I'm gonna pass my data

**2:16:18** · let's see I'm going to open my app it's not showing anything that because I forgot changing my endpoint it's gonna be localhost my port number API and users

**2:16:36** · and as you can see they are here let's make sure it's our API I'm gonna come here and I'm gonna change this name and as you can see it's here perfect let's take this back and

**2:16:53** · let's try to delete this user as you can see API users and we are passing this ID this is how we plan our application let's open up data table let's remove here and apply react query

**2:17:11** · for deleting updating and adding new item you should use react query mutation that because when we add new item or delete this item we are going to refresh this list without refreshing the page or using any State Management tools like Redux firstly I will come and create a query client and after that I will say cons rotation

**2:17:40** · use mutation hook and I'm gonna write here mutation function you can pass here our item id because we are going to use it in our API it's going to be a number and we are going to return patch our endpoint http localhost

**2:18:01** · API and remember we have slack here we can use it and also we are taking this ID let's use it here and I'm gonna write my methods okay and after that if it's successful we are going to refresh this data remember we gave a name let's see let's remember

**2:18:30** · we have a name here let's change actually I will say all users so using this query key I'm gonna refresh my data so I'm going to be using query client invalidate queries and inside this array it's going to be all users but remember this is a generic component it can be anything since we know the slack here we can use it I will say all slack users

**2:19:00** · products anything it might be and of course I forgot props and let's use this function here I'll say mutation rotate and I'm gonna

**2:19:16** · pass this ID and that's all let's try let's check first localhost API users one let's see I will come here and click and as you can see it's gone

**2:19:39** · perfect it works so I can do the same thing for adding a user of course I'm not gonna take all those inputs and handle change methods I'm just gonna write a basic function just to give you an idea I'm going to open up at

**2:20:01** · actually we are going to do exactly the same thing I will copy here and let's paste I'm going to import them this time I'm not gonna take anything but as I said you should take all those inputs this time is going to be a post method we don't need to pass anything here and if everything is okay again we are gonna refresh our data but remember this slack is singular here it will be users

**2:20:34** · so I'm going to add here as and also here let's delete this and mutate but of course we should pass here a body I will just paste here as you can see all details are here name surname and others and it's gonna take this body and send this post request after this request is

**2:21:01** · gonna invalidate our data Let's test I will click and as you can see it's here but our model is still open let's close it I'll say after mutation props dot set open will be false

**2:21:26** · let's remove this and add new user perfect it works it's that easy guys just create your API and try it on this dashboard right now let's make our design responsive let's close everything here I'm going to open my Styles folder

### React Admin Dashboard Responsive Tutorial (CSS Grid)

**2:21:52** · here and create a new file and let's say responsive I'm gonna create here my breakpoints small screen medium large x-large and xx touch and right now I'm gonna create media query functions using SAS to do

**2:22:10** · that we are going to be using mixing it allows you to use these functions in all around our application for example it's going to be small that's right here media query media screen and the maximum width will be

**2:22:29** · 480 pixels basically I'm gonna use this variable like that and I will add here my content instead of this content we will write our styles when we start using it you will understand better right now I'm gonna do the same thing for others medium large and others let's duplicate this

**2:22:53** · medium large x-large and the biggest right now I can use my functions let's open up our Google CSS and test I'm going to come here of course I'm going to import my CSS file and it's going to be responsive

**2:23:16** · let's say include XX sludge and I will say background color red it's just a test I'm going to open up my home page let's close them we don't need them anymore and I'm gonna open my console and I'm gonna shrink slowly and as you can see our background color is red let's make this a little bit transparent

**2:23:50** · maybe more okay let's do the same thing for others x large medium and small let's give different colors and after that it will be ready to see

**2:24:24** · as you can see different colors for each breakpoint so it's easier to see right now firstly let's take care of our menu let's open up menu here menu scss and import our responsive file

**2:24:42** · and what I'm gonna do is removing those texts it's going to be only icons no titles or no texts so let's come here I'll say include light screen is going to be displayed on so I will do the same thing for list item title

**2:25:09** · it's a text and it's going to be display no let's see I'm gonna shrink and after the large screen as you can see there is only icons and we have still hover effect we can still click on them as you can see there is nothing complex so let's take care of this Nail Bar I'm going to open up our again I'm gonna import responsive as CSS

**2:25:41** · and if it's the small screen I'm gonna delete those icons I will do exactly the same thing I will come here and write icon let's see first if I edit or not okay they are here and include small screen display no

**2:26:06** · medium and small as you can see we have only notifications and this user perfect so let's take care of those items it's the most important part I'm going to open up home page and import my responsive file

**2:26:33** · and let's see what we need here right now there is no problem maybe we can make this box vertical using Flex Direction but for the size it's okay but if I shrink more as you can see it's overflowing to prevent this I'm gonna decrease the number of columns it was four but right now it's going to be three so I will say include x light screen

**2:27:04** · columns and this time it's going to be three and one fr and as you can see right now it's three columns four columns three columns if I shrink more it should be two columns I will say algae and two columns like that but there is something wrong here let's open up our Global CSS

**2:27:39** · and if you remember we sat with 250 pixels but if it's LG width will be maximum content it's going to include only R icons let's see perfect and if it's medium it's gonna be just one column let's open up home

**2:28:11** · I will say MD one column and there's a problem here I set one column but it's not applying that because in this component we said width is two units let's check as you can see it's more than one column so we cannot apply this to prevent this I'm gonna come here and I'm gonna either reduce its size or

**2:28:45** · just remove I prefer removing this item because it's really long and when I shrink it's gonna just look really ugly so I will say display none and as you can see right now it's just one column and if it's small it's gonna be the same maybe I can decrease this height remember it was 180 pixels

**2:29:13** · and I will say if it's small make it 120 pixels okay and I want to show you one more thing here

**2:29:33** · as you can see there are some spaces between our boxes and they don't look as you expected to prevent this problem I'm just gonna add here create autoflow and it's going to be dense and right now when I shrink my application as you can see there is no space everything is much smoother

**2:29:59** · perfect actually you understood those breakpoints I can delete those background colors let's open up Global and delete them

**2:30:18** · okay using grid system makes everything easier we have to change just the column size let's check one more time okay let's take care of those items because those charts look a little bit weird I'm gonna open up chat blocks

**2:30:38** · and import my CSS file here I'm gonna come here and I will say include if it's XX large font size will be smaller let's copy this and I'm gonna decrease this percentage it was 20 pixels and it's going to be let's say 16.

**2:31:02** · and what about those items what was the name let's check number okay we don't have any class name but we can use H1 tag after this title I will say H1 and if it's XX large it's going to be 20 pixels okay after reducing those numbers it's much better and what else we can do

**2:31:29** · if it's a small screen actually those spaces are too long I can make this vertical let's copy this and come here and I will say if it's small it's a flex box so I can say Flex Direction column and I can give gap between them let's open up this box info and I will say Gap 20 pixels

**2:32:02** · all right now it looks awesome as you can see we can maybe decrease this title because here it's too big when it's x-large it's going to be smaller so I will say top box and I will

**2:32:27** · come here and say XX large and it's going to be 24 pixels of course I didn't import my CSS file let's import okay perfect I can do the same thing for here and here let's copy pie chart I will say H1

**2:32:53** · and import perfect and big chart foreign

**2:33:10** · what about those images let's open up top box I will say if it's XX large it's going to be display Norm in this case they are going to be bigger and it looks much better but if it's bigger we can add them back I will say algae display block let's see

**2:33:43** · when it's two columns they are back but when they are small it looks a little bit weird because of those emails let's do the same thing there I'm gonna come here and say display norm and block as you can see it's much clearer right now and when it's two blocks it's gonna be images and emails again

**2:34:12** · so what about single page I'm not gonna take care of those lists that because there is no sense to make this responsive it's not gonna look good what you can do is leave it like that it's still responsive but you have to scroll here I think it can stay like that if you don't want to completely remove this data grid and add something else here like just the search button so I'm not

**2:34:40** · going to touch here let's open up single user as you can see it looks really small I will say if it's x-large make them vertical let's open up single I'm going to import my CSS and I will say include if it's x-large the extraction will be column like that and I can give space here

**2:35:14** · Gap will be 50 pixels perfect and if it's medium I can actually delete this chart because as I said as you can see it looks just weird there is no sense to keep it I will copy here for charts I will just say display no for me Cube

**2:35:45** · much better also I can delete this HR Tech and as you can see it's overflowing because remember we sat here where is RDU okay we set minimum width 480 pixels I'm gonna decrease this and it's gonna be 150.

**2:36:11** · but I said minimum here I have to say minimum again right now it's smaller and as you can see it's not overflowing anymore let's make this bigger

**2:36:33** · where are our icons by the way why it's empty I don't know what just happened but they are okay right now I will shrink okay they are here more and perfect now for the home page

**2:36:53** · awesome let's make it bigger two columns three columns for columns okay awesome so we've

### Deploying to the Hosting

**2:37:09** · finished our project right now we can deploy it to do that I'm gonna come here open my terminal and I will say yarn built and there is an error here in users it says you are importing these rows but you are never using actually it's not an error it's just a warning

**2:37:36** · let's see lots more again we are never using this just don't worry about them it's not a mistake

**2:37:58** · and that's all I think during this process let's open up our Edge panel and there is a file manager here I'm going to click and this folder is where we are going to upload our files let's open up and as you can see there is a default home page let's remove this

**2:38:26** · and let's check our application as you can see we have all our images CSS and JavaScript files inside this folder and this is the main HTML file basically I'm gonna take everything here and move into public HTML

**2:38:48** · of course there is only one JavaScript file we didn't split our code but it's a small application don't worry about that I will come here take everything inside this folder and move it to my panel as you can see it's uploading

**2:39:10** · and it's done it was really fast and right now let's check our application react admin dashboard.com and our app is here

**2:39:25** · and by default we have an SSL certificate we don't have to install everything just drag and drop your files and it's ready as you can see it works as respected remember we are still using our API and our data is here I can delete them

**2:39:49** · add new user let's open up products perfect I can search for any item let's open up it works perfectly let's check the responsive design I will shrink my page as you can see it works properly

**2:40:26** · and also you can add in your hosting a hundred websites just like this you can use different sub domains and using those subdomains you can create different applications it's perfect especially if you have a portfolio website you can add all your applications in just one hosting okay guys that's all I hope you liked it

### Outro

**2:40:53** · if you learned something new today please like the video you can support Lama day using the link in the description below or by joining the channel don't forget to follow lamadev's social media accounts I hope I'll see you in the next tutorial goodbye