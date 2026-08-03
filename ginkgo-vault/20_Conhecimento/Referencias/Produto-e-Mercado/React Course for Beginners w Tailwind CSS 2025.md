---
title: "React Course for Beginners w/ Tailwind CSS [2025]"
source: "https://www.youtube.com/watch?v=IJ85kCdqWao"
author:
  - "[[freeCodeCamp.org]]"
published: 2025-08-04
created: 2026-07-02
description: "Learn modern frontend web development using React and Tailwind CSS in this beginner course.✏️ This course was developed by Alvin Zablan. Check out Alvin's channel: https://www.youtube.com/c/AlvinThe"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=IJ85kCdqWao)

Learn modern frontend web development using React and Tailwind CSS in this beginner course.  
  
✏️ This course was developed by Alvin Zablan. Check out Alvin's channel: https://www.youtube.com/c/AlvinTheProgrammer  
  
🔗 Learn more frontend development with Alvin: https://react-formula.com/  
  
❤️ Try interactive React courses we love, right in your browser: https://scrimba.com/freeCodeCamp-React (Made possible by a grant from our friends at Scrimba)  
  
📖 Contents 📖  
(0:00:00) Course Introduction  
(0:04:31) Your First App Exercise - https://react-formula.com/workspace/your-first-app  
(0:10:00) Rendering Components Exercise - https://react-formula.com/workspace/rendering-components  
(0:07:54) Passing Props - https://react-formula.com/workspace/passing-props  
(0:27:52) Passing Props II - https://react-formula.com/workspace/passing-props-ii  
(0:36:39) Passing Props III - https://react-formula.com/workspace/passing-props-iii  
(0:45:05) Intro to Tailwind CSS Lecture  
(0:49:40) Tailwind Basics Exercise - https://react-formula.com/workspace/tailwind-css-basics  
(0:59:55) Padding & Margin Lecture  
(1:03:21) Button Style Exercise - https://react-formula.com/workspace/button-style-exercise  
(1:14:30) Tailwind ClassNames Lecture  
(1:19:53) Button Component Exercise - https://react-formula.com/workspace/button-style-exercise  
(1:29:32) Flex Box Lecture  
(1:34:38) Flex Exercise - https://react-formula.com/workspace/flex-exercise  
(1:39:26) Flex Column Lecture  
(1:42:17) Flex Exercise II - https://react-formula.com/workspace/flex-exercise-ii  
(1:46:21) Analyzing Layouts Lecture  
(1:51:50) Tailwind Docs Lecture  
(1:56:04) Analyzing Layouts Exercise - https://react-formula.com/workspace/analyzing-layouts-exercise  
(2:22:59) Search Page Design Exercise - https://react-formula.com/workspace/search-page-design  
(2:49:53) Event Handling & State Lecture  
(2:57:08) Click Event Exercise - https://react-formula.com/workspace/click-event-exercise  
(3:12:05) Conditional Rendering Exercise - https://react-formula.com/workspace/conditional-rendering-exercise  
(3:29:28) Counter Exercise - https://react-formula.com/workspace/counter  
(3:39:27) Light Switch Exercise - https://react-formula.com/workspace/light-switch  
(3:58:22) Image Carousel Exercise - https://react-formula.com/workspace/image-carousel  
(4:17:43) Cat Carousel Exercise - https://react-formula.com/workspace/cat-carousel  
(4:42:11) Outro  
  
🎉 Thanks to our Champion and Sponsor supporters:  
👾 Drake Milly  
👾 Ulises Moralez  
👾 Goddard Tan  
👾 David MG  
👾 Matthew Springman  
👾 Claudio  
👾 Oscar R.  
👾 jedi-or-sith  
👾 Nattira Maneerat  
👾 Justin Hual  
  
\--  
  
Learn to code for free and get a developer job: https://www.freecodecamp.org  
  
Read hundreds of articles on programming: https://freecodecamp.org/news

## Transcript

### Course Introduction

**0:00** · Learn modern front-end web development with this beginners course on React and Tailwind CSS created by Alvin Zablin.

**0:08** · This course guides you step by step through building real projects while learning the essentials of component-based development and utility for styling. You'll start by creating your first React app, then learn about rendering components, passing props, and mastering layout with Tailwind's powerful classes. You'll gain confidence in handling events, managing state, and designing responsive interfaces from scratch. By the end, you'll be ready to create beautiful interactive web apps with React and Tailwind CSS.

**0:38** · Hey programmers, Alvin here. Welcome to my React for Beginners course. In this course, we're going to learn modern front-end web development using React and Tailwind CSS. And the best part is you don't need any front-end experience to begin. As long as you're already familiar with the basics of programming in JavaScript using variables, if statements, loops, and functions, you'll be good to go. I'll give you all the background you need during the course.

**1:02** · So, if you know zero, React, or CSS, don't worry. I got you covered. If you've taken a course with me before, then welcome back. I think you'll feel right at home with my teaching style in this new course. If this is your first time learning with me, then hey, I'm Alvin. I'm an ex Google software engineer with a serious passion for teaching. I've been spending the better part of the last decade teaching thousands of software engineers the skills they need to land their dream job. In just under five hours, you're going to learn the essentials of React and Tailwind CSS by building various user interfaces with me.

**1:29** · We'll use a combination of animated video lectures and detailed code walkthroughs to make sure that you don't miss a step. For each exercise, we'll provide links to an online coding environment so you can jump right into coding with me without having to set up your own environment.

**1:43** · I'm super excited to begin. So, without further delay, let's jump right in.

**1:50** · Hey programmers, right now I want to talk to you a little bit about the main topic that we're going to be studying throughout the course and that is React.

**1:57** · So let's start with a basic question here. What is React? So React is going to be a JavaScript framework for building user interfaces using individual pieces called components.

**2:07** · This is a description right from the React website. A few things I want to call out here is React is most certainly a JavaScript framework. Uh so the beauty of React is you can use a lot of your JavaScript knowledge to implement a UI and moreover we're going to implement our UI using components. These are just going to be pieces of code that we can reuse and we can attach some functionality to these components that helps create a user interface in a very organized and maintainable way. React is just one of many JavaScript frameworks that we can use to build a front end. So that kind of begs the question, why should we learn React?

**2:38** · There are so many options out there. Well, in my opinion, React is just the most dominant front-end framework in the market. And this is backed by some data. Every year, there is a state of JavaScript survey.

**2:50** · And in this survey, thousands of developers are interviewed across a wide range of topics having to do with JavaScript. And of course, there is a whole section on front-end frameworks.

**3:00** · So, I'm going to show you here is some data here. We're looking at the front-end framework ratios over time. In particular, we're going to start with usage. This means you know how many developers actually utilize this tool inside projects or in their work. And here we're actually measuring against all the major front-end frameworks. So we have things like React as well as Angular and some other ones such as Vue and Spelvelt. Here's what the usage data looks like for the past six years. You can see that React is highlighted in the blue right now.

**3:28** · And it is indeed the number one JavaScript framework for frontends by usage. Notice that over time it's actually grown more popular in terms of its usage. So if you don't know React by now, now is really the time to get in on it. It really opens up a broad range of opportunities for you as a front-end developer. React has been the most popular JavaScript front end framework for quite a while now. And there's more than just usage that we can look at. Let's look at some other data set from the same survey. This time talking about positivity.

**3:59** · Positivity refers to the sentiment that a developer has uh in their working relationship with the framework. What that means is if a framework has high positivity, that means that its developers are very likely to use it again for a future project. And again, we're going to be comparing React against all of the other popular front-end JavaScript frameworks.

**4:17** · Similarly to the last graph, we still see that React is number one, and it has been for a few years now. It's a front-end framework that they use and want to use again. So, as you can see, React is a pretty great framework, and that's why we're going to be studying it throughout the course.

### Your First App Exercise

**4:36** · Hey programmers, Alvin here. What I want to do is go over the structure of a very simple React application. In fact, here I have a minimal React application that only contains the handful of files that you'll actually get automatically when you create a project. Right? So, these files, these three files are usually generated for you. And with that, I'm going to have a big disclaimer. You don't need to really memorize the code within these files. It's really just important to take away what these files accomplish. Like I said, these files are usually created for you. And so if I look at my file structure here, you have a folder that contains two files.

**5:06** · Then you have a file outside of that folder, right? And this uh naming structure is super duper common for a React application. You have source containing an app file as well as a main file. Then outside of that, you have an index html, right? So let's start with the index html. The first thing you'll notice here is this is going to be an HTML file.

**5:28** · HTML stands for hypertext markup language. And what it does is describe the structure of our page. We can see a few things within this autogenerated HTML file. It has things like the language it's in as well as the screen size that we're rendering for. You even see things like the title of the web page. All of these different configuration options are not worth memorizing right now. As we go further in the course, I'll be sure to introduce a very few options that we'll actually use and change within our index html.

**5:56** · When it comes to your workflow as a React developer, you'd actually probably make very few changes within the index html file. Before modern front-end frameworks like React became popular, it was the case that most of the web pages and websites you viewed through your browser were actually just different index html files. every page on a website would correspond to a different file. But that paradigm changes when you use a front-end framework like React.

**6:23** · Instead of loading different HTML files for different pages, instead we use a single index html file and we dynamically change the structure of the file using React. That's really the magic of React. So the main reason I'm actually showing you the index html file is I want to draw your attention to line nine here. Right here I see a div with an id of root. Right? And what this root is, it's going to be the entry point for React into our index HTML. So I do want you to remember for now this ID of root.

**6:56** · Next thing we'll do is look at these script tags. Mainly this one over here on line 11. Here we're referencing a script called main.jsx.

**7:04** · Of course that corresponds to the other file we see right here called main.jsx.

**7:09** · So we'll go there next. You don't have to worry about the other JavaScript you see on line 10 here. This is just a file that helps us integrate with the React Formula platform. What I want to do is hone in on this main.jsx, though. So, let's hop inside of that file.

**7:24** · This file is really short, and again, this main JSX file is a file that would actually be generated for you. So, again, don't worry about memorizing this one. What I do want to draw your attention to is this expression over here. It says document getelement by ID.

**7:38** · And the ID we're looking for is root.

**7:41** · Naturally, that corresponds to the root ID in the other index. HTML file. Right?

**7:46** · So, what I'm saying is this root should match this one over here. Right? What we're doing is we're selecting and grabbing a reference to this div. Right?

**7:57** · And with that div, we're actually going to initialize or create the root of our React application. This is where we inject React into our HTML document. And if we keep following the chain of events over here, looks like we see a render and then we render app. Notice that app comes from another file, right? App comes from app jsx. So we'll finally hop inside of app.jsx.

**8:22** · And inside this app.jsx file, we see the beginning of our React code, right? And I know we just quickly went through a lot of different things. Again, don't have to memorize them. The app file, the index file, and the main. JSX file are usually files that come with any new React application. So, what I want you to do is actually turn on this app. It's a very simple one. And to do that, inside your terminal, you can do npm rundev. This is going to be the classic terminal command you can use to turn on your React development server.

**8:49** · And if I have my development server running, I can actually look at what the output of my UI is. Notice that the output just contains the text to-do. And that of course corresponds to what's returned in my app here. And so it's okay if you're finding all this syntax a little strange, right? It could be the first time you're seeing this stuff. What I do want to draw your attention to is just the fact that if I edit the to-do over here and I just say, "Hello, my name is Alvin." That should actually change the output I see on my screen.

**9:18** · In the next lesson, we'll break down what this app thing is and write our very first components. But for now, I want to flip it over to you. What I want you to do is make sure you can turn on your dev server in the terminal as well as edit the text within the app div. And hopefully you can see it on the screen.

**9:36** · What you want to do now is head over to the prompt where you're going to have uh some text passages that go over exactly what I spoke about in this video as well as instructions on how you're going to turn on your dev server and edit the app. JSX file. Once you're able to see your custom message displayed in the output over here, what you want to do is scroll to the bottom of the prompt. Make sure you completed all of these tasks and mark as complete and I'll catch you in the next lesson. I'll see you there.

### Rendering Components Exercise

**10:05** · Hey programmers, Alvin here. Welcome to our lesson on rendering components.

**10:09** · Components are going to be the main way that we organize our code within our React application. So, we'll jump right in. The first thing I want to do is turn on my development server. So, you can do npm rundev in the terminal. And like usual, what I want you to do is watch this uh video lecture fully first before you hop into coding this one up on your own. Right? So, if I get going here, I look at my browser output. And so far, it just says the word to-do. If you hop into the app.jsx, like we saw in the last lesson, you're going to see why we see that to-do text rendered on the screen, right?

**10:39** · It seems like our main app component is rendering just the text to-do. So, I'll get organized over here.

**10:48** · So this app component is typically the component that you'll get by default whenever you spin up a new React app.

**10:53** · And what I want to do is teach you how to create your own components and render them on the screen. By looking at this initial app component, we can already see how a React component is implemented in JavaScript. A React component is just going to be a JavaScript function, right? This is just some arrow function syntax in JavaScript. Really the latest and greatest way to define your functions in JavaScript. An important thing to note is in React, your components are just going to be functions. However, they must start with a capital letter. In other words, capital app is good to go.

**11:22** · However, you can't have a component named lowercase app. That's going to be incorrect. You get an error, and we'll see that in a moment. So, what I can do is define my own component above.

**11:34** · So, all I'll do is create an arrow function. I'll call it title. And if you're unfamiliar with arrow function syntax, you'll get the hang of it really quick. It's actually a really easy syntax to use. Generally for an arrow function within the parenthesis we can define any arguments that our function is going to take in. Then we can open up some curly braces that contains the body of our function. And so what I'll do is I'll go ahead and return just a div so far. I'll just say hello world.

**12:02** · However, if you just have this code uh in your app.jsx file, you're not going to see hello world on the screen. Right?

**12:09** · Although I've correctly defined this component, I'm not actually rendering it on the screen yet. Previously, we spoke about how the app component, if we go into main.jsx, is the initial component that's rendered on our screen, right?

**12:24** · That doesn't mean that it's also going to automatically render the title. But what I could do, and what you generally want to do in your React components is render things within your app component.

**12:34** · In other words, right above this to-do text, maybe I'll put the title.

**12:40** · And when it comes to rendering a component, you want to use it just like a tag, right? Since my React component is just a function that has a name title, I'm going to use that same title name in a tag over here. The important thing to note is you also want to self-close the tag. Right? So after the name, you want to do a forward slash and then a greater than symbol. And notice that we're already seeing the title rendered on the screen because the title returns a div containing hello world.

**13:06** · That's exactly why I see it over here.

**13:09** · Awesome. And so let's keep this rolling further. What you could do is of course render the same component multiple times. So I'm going to put three of the same title. And naturally we can see it on the screen over here. So let's go over that common gotcha. Let's say I try to define my component with a lowercase t. See what we get. you're going to get an error, right? So, in your output, if you're using the built-in browser here, you can see your console where you can see all of your error messages and warnings using this wrench symbol over here. So, I'm going to click on it. I can see the error here.

**13:39** · It says title is not defined, right? That's because on lines 10 through 12, I'm trying to reference a component called capital title, but there is no capital title component. So let's say I even tried to fix this by using lowercase title as the component name. If I look at that, that's also not going to work, right? I don't get any crazy error uh in my screen. However, you're not going to see your component rendered, right?

**14:07** · So it's really important that you're going to use uh capital uh names for your components. So I'll go ahead and fix this. Use my capital T. Let's get some further practice here and just create another component. Right? So, I'm going to create another component. I'll call it description. Again, using capital letter for your arrow function syntax.

**14:28** · We're going to save an arrow function in this variable. So, some parenthesis.

**14:32** · Open up some curlies. And I'll return another div with some different text.

**14:37** · So, I'll just say this is my second React component.

**14:45** · And of course, be sure to render that component on the screen. I'll remove the s to-do text and I'll just render it below my titles. Right? So I'll say description and I'll use a self-close tag.

**14:57** · So we'll give that a run. And here I see my second component rendering. What you're going to also do to render your components is to use a pair tag. It kind of looks just like div, right? Notice how div has an opening and then a closing. Noticing that the closing pair has a slash over here. And this is a totally valid way to render your components as well. Rendering your components using the pair tag way actually gives you some additional functionality and we'll see that later on in the course. So for now I think it's good enough to understand that you can render your components using this self-close tag.

**15:28** · All right, there's one more bit I want to show you over here.

**15:33** · So it goes without saying that you know React is a framework that's actually implemented in JavaScript. That's really why I'm trying to make sure that I drill in the fact that a component is really just a JavaScript function, right? And so what I'll do is within these components before you return, you can write any arbitrary JavaScript code. So for example, maybe first thing in my title, I'm going to console.log. I'll just print out a string. I'll say running title. Then I'll also put something very similar inside of description except I'll say running description.

**16:05** · And for now I'll clear my browser output. That way I can start fresh here. And I'll refresh the page.

**16:13** · And what we can notice is the output that we printed out. Right? Console.log is just how we can print out standard output into our console here. Right? So it's really important to understand is whenever we render a component, for example, on line 20, this component is going to evaluate its function body. In other words, the first thing I do is really console.log running title, which is why I see it over here. Right? Then at that point afterwards it's going to return the div containing hello world which is how I can see it on my screen first time over here. Right?

**16:42** · Because I have rendered it three times overall in a row. I'm actually going to run this title component run this title function three times which is why I see running title printed out three times over here.

**16:56** · Right in your console in your developer console you're going to see a number associated with the number of times it printed out that text sequentially. So I see three times over here and then afterwards I run the description component which of course prints out running description. If you're familiar with functions at all in programming then this is a very simple and familiar uh concept. However, it's worth emphasizing because I find that students often really have a distinction in their brain between React and JavaScript. But you can really utilize your understanding of just JavaScript programming to understand React. Right?

**17:27** · So although I've been calling components functions a lot uh during this lesson, moving forward in the course, we'll just refer to them as components. All right, so that's all I got for this lecture.

**17:36** · What I want you to do is now hop into the prompt and complete this lesson on your own. Now, you're really going to be coding up exactly what I made uh just by yourself. If you get stuck, feel free to reference the text instructions that we provided. Gives you a step-by-step breakdown what you're going to be building. And also feel free to watch this video again if you get stuck. And once you're ready, I'll see you in the next one.

**17:59** · Hey programmers, Alvin here. Welcome to our passing props lesson. What I'm going to do is teach you the main way that components can communicate with each other in React. So, we'll get going here. The first thing I want to do is of course spin up my development server with npm rundev and I'll get organized over here. Like usual, we're just going to have the text to-do within our initial app component. So, what I want to do is just start by warming up and reviewing how to create our own component. This time around, I'll create a component called message.

**18:30** · And like always, be sure to call it with a capital letter. And I just want to assign it an arrow function here. And just like we said in the previous lesson, you can write any arbitrary JavaScript code here, but you want to ultimately return some JSX, some HTML looking tags. So, for now, I'll say IM message.

**18:51** · Cool. I'm not going to see it on the screen yet until I actually render this component within my app. So I'll go ahead and render my message component over here. I'll use this self-close style.

**19:04** · We'll see it on the screen. Right. So we're rendering message inside of app.

**19:08** · App is a component. Message is also a component. Some language we'll use to describe this relationship is app is the parent and message is the child. Pretty straightforward over here. So this component works, but it always does the same exact thing, right? So if I render the message three times, I'm going to see the same text on the screen three times, right? What I want to do is start by giving some input or data into these messages. And so what we'll do is for our message, we can take in an argument called props.

**19:38** · And you'll always want to name this argument props. It's very standard in the React terminology when you look up documentation or Google around for things. uh you will find this as props right and the way it looks is it's just an argument into this arrow function right so again react is totally implemented in JavaScript and so what I want to do is for now just console.log log what props is and I'll just remove two of my messages here.

**20:05** · That way I only just render it once which means I'm going to see a single print statement here. So I'll open up my dev console and I'll clear things out and just refresh the page so we can start fresh.

**20:19** · And notice that I'm going to see an object printed out just a plain old JavaScript object. And that's really really important. Right? The first thing you should understand is props is the argument that your components can take in and it's going to be an object.

**20:33** · Right? Right now I'm not receiving any props. And so the object is empty. Like you expect since props uh is an object.

**20:42** · It really just stands for properties, right? Like you already know, a JavaScript object can have many properties. In other words, many key value pairs. So what I want to do is show you how you could pass in a prop into your message. So when you render the message, so for me on line 12, you can pass in a prop like this, you can name the prop. You can give it any name you want. I'm going to call it text and you can assign it a value.

**21:06** · Notice that this is all going within the rendered tag here. I'm going to pass in a string. I'm going to say the string, this is my first prop.

**21:18** · Nice. And notice when I see my object printed out right on line three I'm printing out props I could see it has a key of text which corresponds to obviously this over here and a value of this is my first prop right so pretty straightforward syntax over here.

**21:35** · Obviously you could pass in many things if you wanted to.

**21:39** · So you can say maybe a color make it red.

**21:45** · It would also show up as a key value pair within your props object. Right? In terms of how you style up your code, if you take in a long list of many props, I usually have the habit of breaking lines like this. It's totally also valid to just put space between them. If you prefer it that way, it's all good.

**22:04** · All right. So, we can see that props as an object. The first thing that I always do in all of my React components, if it takes in some props, what I do is dstructure them out, right? So you can use some object dstructuring syntax in JavaScript. In other words, you can say the name of your prop. So I'll say text here as well as color. And those correspond to the prop names here, right? That way you're unpacking them.

**22:26** · And that just gives you variables that contain text and color. So I'm going to print out uh just the text. Notice that I see this is my first prop. So now I just have access to that variable. And I can use it however I want inside of my message component.

**22:40** · And so I don't want to assume too much.

**22:42** · So maybe you're actually unfamiliar with this syntax in JavaScript. It's really nothing fancy, right? So if I had a plain old JavaScript object had like a name of Alvin and maybe an occupation of teacher, what you can do is unpack the values or dstructure the values out of that object. So you can say like const I'm just going to grab the name from the object. Then afterwards I can just console.log name as a plain variable.

**23:13** · So this should just print out Alvin on the screen. Right. Obviously you can dstructure some of the keys out of an object or you could dstructure as many as you want. So I'm going to grab the occupation as well. Of course I can print out the occupation. This is just a quick little aside, right? This is just plain old JavaScript up top. All right, so let's hop back into React land over here. Now that I have the text, what I want to do is actually use that text string and render that inside of my div instead of the static IM message. Right?

**23:49** · So what I can't do is just put text over here. And you'll see why that is. If you just say like the literal text here, you're going to see text on the screen.

**23:59** · Not useful, right? What I really hope to do is render this string on the screen.

**24:03** · Right? If you want to evaluate text as a variable, then you need to wrap it in another set of curlies over here. And this goes all inside of your div. Right?

**24:13** · So notice that now I see this is my first prop. Awesome. Obviously, if I instead put the color here, then I'm going to see red on the screen. So important thing to note is inside of your tags here, if you want to actually evaluate a variable, then you can just put it within curly braces, right?

**24:34** · Awesome. And that's actually a really important concept. Not only can you put just a variable within these curly braces here, but you can evaluate any valid JavaScript. In other words, if I delete this, let's say I did not use any curlies and I say 4 + 4. Well, then you're literally going to see 4 + 4 on the screen. But if you put it in curly braces, well, 4 + 4 is just some JavaScript. That expression evaluates to 8.

**25:00** · This concept is going to be really important later on because that means we can do some calculations to figure out what we're going to render within our components, right? But I'll keep things simple. I'm just going to put the text over here. Nice. I also want to start to use this other prop of color. I'm going to rename it. I'm actually going to call it a background color. So I'll say BG color.

**25:24** · BG color. And what I want to do is show you how you could start to use these props to control maybe some of the basic styling of this component. Right? So for this div over here, this div can also take in a built-in prompt in React. It's called just style, right? So div is not really a component that I built, right?

**25:44** · It's the built-in tag for us. It's already defined. So it takes in a style prop. And within it, you can use some curly braces. And you can also open up another set of curly braces. And the reason that I have two sets of curly braces is the outer curly braces evaluate JavaScript. And inside I'm actually putting an object, right? So object has key value pairs. I can say things like I want the background to be let's say purple for now. We'll see how that looks. Notice that I have my purple background, right? But I can also use the prop passed in.

**26:16** · So if I use the background as BG color, that BGC color prop is now going to be used as the background color. So this is probably the simplest way we can start establishing some style in our React code. In particular, we call this concept inline styles. It's when you use the built-in style prop and just pass in an object with key value pairs that correspond to your styles. Right? So this is actually kind of like the old outdated way to style up your React code.

**26:45** · As we move further in the course, I'm going to teach you Tailwind CSS, which is going to be a really great way that we can establish styles, and it's really going to be maintainable for when you build your own applications in the real world. So, for now, I'm just using this inline style syntax just to keep things simple for these initial lectures. So, let me go ahead and auto format this code. And what I want to do is go ahead and render a few different messages. So, I'll do two more messages.

**27:10** · I'll change their text. So, I'll say hi.

**27:14** · I'll also say by and of course I can go ahead and give them different colors. So this one's going to have a background color of lavender and the other one's going to have a background color of blue. Great.

**27:29** · And there we see our different colored messages. Awesome. So that's all I got for this initial introduction into props. What I really want you to understand is props is a way that we can pass data into our React components. And under the hood, the props is really just a JavaScript object. So now I spin it over to you. I want you to hop into the prompt for this one. Follow the instructions, code this one up, make sure you understand it, and I'll catch you in the next one. I'll see you there.

### Passing Props II

**27:58** · Hey programmers, welcome back. Welcome to our next lesson on props. So let's keep things rolling over here. First thing I want to do is of course turn on my dev server and I'll kick off here with some basic review of just creating component with some props. Now I want to show you some different prop types you can use in React. So this time around I'm going to give myself a nice box component. It's going to take in some props. For now I'll just make sure I can render things on the screen. I like to move really slow here. And I'll just say I am a box. Of course I need to render this box.

**28:30** · So within my app parent component, go ahead and put down box like this.

**28:37** · Make sure things are good to go. And this gives me a good starting point. So what I'll start to do is pass some props into the box. I'm going to pass in a label, which would be the text I'm going to display within the box. And I'll just have the label my name is Alvin. And I'll also give it background color like before, BG color for short. And this time I'll use corn flour blue. Right? Don't worry, you don't have to memorize all the different named colors that you can use. Right?

**29:07** · This is just one of my favorite. So what I'll do is I'll go ahead and just console.log props pop quiz. What type of data is this props variable? Like you guessed, it's actually going to be a JavaScript object. So I should see that object printed out here, right, with the label key as well as a bgolor key. So, what I want to do is render the label within the div. And to do that, I like to dstructure the label out of the props. And over here, I can say label.

**29:40** · Nice. And there. See, my name is Alvin.

**29:42** · While I'm there, I should also probably dstructure the background color. So, let's just wire up this background color. So, it sets the background color of this div. So, like we saw previously, we can use the built-in style prop on this div. You want to open up two sets of curlies, right? One set to start evaluating JavaScript here and another set to just be a plain old JavaScript object. Within this object, I'll give it a background of BG color. Right?

**30:09** · Background is actually uh the key that you're going to need to use if you want to set the background color. There I see my cornflour blue background. Let's go ahead and use another style over here.

**30:21** · So in addition to background color prop I'll add something called maybe text color and I'll use different color I'll use maybe white and I'll take that in my props which means I can dstructure over here text color. Hopefully you're starting to notice the correspondence now. Right? The prop name you put here corresponds to what you destructure out of here. Now that I have that text color, you can use that text color in your style here to set the color of text.

**30:52** · The actual key is just called color over here. So now I see my white on blue background. So let's add one other.

**31:02** · So for the second box, I'll just say some other things like another one. And background color this time maybe just some lavender.

**31:14** · and text color we'll use purple.

**31:18** · Nice. So, so far we've been passing in strings as our props. But it's the case that in React you can pass in any valid JavaScript data type as a prop. If you're unfamiliar with the types of JavaScript, there are things like number, string, boolean, array, object, and so on. So, let's go ahead and add a boolean prop uh into the mix here. So for these boxes, I'm going to give them another prop called large, and I'm going to make it true. Right? So for now, I think I'll just do it on one of my boxes.

**31:47** · So I'll comment out the other box by just highlighting it and doing control or command plus slash. Right? So only going to see one of my boxes.

**31:56** · So I'm passing in this uh other prop of large. It has a value of true. However, it's really going to be the string containing true. Right? If you want to pass in the boolean, then you're going to need to use curly braces here, right?

**32:10** · Which as always allow you to evaluate JavaScript. And within that, you can put the boolean literal true, right? So this is actually the real way you can pass in a boolean type uh into a prop. You have to use curly braces. Really important.

**32:25** · Awesome. So I can now of course take in that prop over here as I dstructure it.

**32:31** · And for now, you know, you can console.log this large prop. It's really going to be the boolean, right? There are no tricks here, right? True and purple, right? If it was a string, it wouldn't be purple. So, you can really take my word for it over here, right?

**32:45** · And what I can do is of course use that boolean prop, that boolean variable really uh to do any logic. So, you can do things like write if statements, write turnaries, do all that sort of thing. And so, what I'll do is I'll use this boolean uh in a turnary expression.

**33:01** · And so one style I'll introduce right now is it's called font size. Like you guess it controls the size of the font.

**33:07** · So if I want to just give uh some large font size here, I'll just hardcode like 40 pixels. That'd be pretty big. You can also do something small like 12 pixels.

**33:18** · You'll have really tiny font there, right? And what I can also do is use this large a boolean to write a turnier expression. Right? So I can say if the component is large then use big font like 40 pixels otherwise use something small like teeny tiny 12 pixels. Cool. So this is just a plain turnier expression. It exists in JavaScript right? It's not a react specific thing like I always like to preach. React is really just implemented in some JavaScript code. Awesome.

**33:50** · So obviously the blue box is going to be large because large is set to true. Let me bring in my other box and I'll set large equal to false. So the purple box will be pretty tiny in terms of its text size.

**34:09** · So just to review some turner, if maybe you're a little rusty on what your turnary expressions do for your turnary expression, you can write a boolean expression, right? Large is a boolean.

**34:19** · If it's true, then you're going to take this value. If it's false, you're going to take the other value. It's really just a shorthand way to write like an if else statement, more or less. Awesome.

**34:29** · So, we're starting to wield our booleans as our props. Let me show you something cool that you can also do. So, I'm going to put a third box.

**34:37** · I'm going to drop the large prop. So, I'm not going to pass in any prop for large. Just to be a little different here, I'm going to use some different text, green stuff. I'll make the background color green.

**34:51** · and the text color we'll use white.

**34:56** · So notice that in this third box I'm not explicitly passing in the large prop.

**35:01** · And the way it renders on the screen is it has the small font, right? It actually has a 12 pixel font. And how does that work? Well, if I try to dstructure large out of the props object here in a case where it's not passed in, it's going to be undefined. So I'm going to console.log log large. Because I'm rendering uh three different boxes, you're going to see them printed out in order. So, like you expect, the first blue box has true for large. The second lavender box has false for large.

**35:33** · The third green box doesn't take in any large, so it's undefined. Right? And that should be quite familiar if you're familiar with some JavaScript. Right? In JavaScript, if a key is missing from an object, it's undefined by default.

**35:49** · Awesome.

**35:51** · And what's more is when you use undefined in like a boolean expression, undefined is a falsy value, right? It acts like false because large is undefined here. It literally evaluates to this undefined which is the same as false because it's false. You take the 12 pixel value.

**36:10** · So sometimes you can find that kind of undefined prop value useful if you want to establish some default uh behavior.

**36:17** · Right? In other words, you can say that for our large property, if it's not passed in by default, it's going to be false, right? It's not going to use the larger font size. All right, that's all I got for the second lecture on props.

**36:30** · So, what I want you to do is head into the prompt. Go ahead, follow the text instructions. Be sure to code this one up on your own. And when you're feeling pretty good, I'll catch you in the next one. I'll see you there.

### Passing Props III

**36:46** · Hey programmers, welcome back. What I want to do is teach you a few new things with props as well as show you how you could separate your React components into different files. So we'll jump right in. Like usual, I want to start by just turning on my dev server. So I can do npm rundev in that terminal. And like always, we'll have our initial app.jsx component with just the text to-do rendered inside. So I'll get organized over here. So, first thing we want to do is give oursel a component to mess around with besides our app. I want to call it my component. It's going to take in some props.

**37:16** · For now, I'll just make sure I can render at least a div. I'll just say some component.

**37:26** · Of course, I want to render this within the app div.

**37:29** · So, I'll go ahead and render this one.

**37:31** · And this time around, I'm going to use the parag style to render my component.

**37:36** · So you're going to open and close a set of my component tags. Notice that the closing tag of course has a slash at the start of it. Notice that I'm still able to correctly render this component.

**37:46** · Previously I mentioned that this is one way that you can render a component, right? As opposed to the self-closed style. If you use this pair style, what you could do is write some text between the tags here. So I'm just going to say hello. And notice that right now I'm not going to see that hello on the screen because although my component has some inner text like hello, I'm not actually doing anything with it when I render the result for my component. It's really plain to see that inside my component, I just have like a hard-coded message, right?

**38:17** · This is always going to render goodbye, right? Although I pass in the text hello. However, you could access the inner text that's between the pair tags for a component. For example, what I could do is maybe console.log props.

**38:33** · And in general, we know that props is an object where all the props we pass in are just some key value pairs. Here, I'm going to open up my console and take a look at what I see. Notice that I'm printing out an object, which makes sense because props is always an object, but it has a key of children, and it corresponding value is the string hello.

**38:48** · Obviously, this hello corresponds to what I put on line 12. Notice that children is actually special, a type of prop. It's going to represent whatever you pass between the pair tags here. And so you could use that to your advantage.

**39:02** · If you just wanted to render whatever the children of my component is, you can go ahead and like usual destructure it.

**39:08** · So I can say take out the children.

**39:11** · Take that from props.

**39:13** · I'll go ahead and just render them over here. If you just write children like this, this is going to be wrong. Like we already saw previously, this gives you the literal text children. You want to actually evaluate this like a variable.

**39:23** · So you want to render the value of the children variable which will now be the hello string. Awesome. So now you know that children is a special type of prop that's going to be the data that you pass between the pair tags. And of course you can have a combination of the children as well as some other things, right? So I can have maybe two divs inside here. I can say this is my component and then below that I can render another div that contains the children. So now I'll have both messages on the screen, right? One of them is dynamic but the other is not.

**39:54** · So I'll say goodbye over here.

**39:59** · So I'm rendering two instances of my component. One has the children hello.

**40:04** · The other has a children goodbye. Notice that both components always show the text that this is my component because it's actually hardcoded within the definition here. All right, let's go ahead and add some normal props to this component as well. I'll go ahead and give these a background color.

**40:20** · I'll make this one yellow. And I'll also give it a height. We haven't seen any number props yet. So I'll give it a height of something large like 120. So like usual, I want to go ahead and dstructure these. So I'll grab a background color as well as a height.

**40:36** · Height. Notice it's passed in as a number. And because I want to pass in an actual number, I wrap it in a pair of curies.

**40:43** · And I'll go ahead and add some style over here like we saw previously.

**40:46** · Passing in an object. I'll make the background the BG color and the height.

**40:52** · Typically here for height you can pass in a string representing the amount of height. So in general I can say things like you know 200 pixels. That'll give me quite a large height for this yellow div. But I can also just use whatever prop I'm passed in. Right? So I know that for this first component, the yellow one, the height prop is going to be 120. I'm going to take that height of 120, but I want to concatenate to it px for pixels.

**41:22** · If you have a number and add it to a string, of course, you get back a string, right? So, it's going to be 120 px. Obviously, now I can control the height of this uh component uh using this prop. So, it should get a little shorter. And there we see it. Go ahead and bring in my other component. Give it a different background color. Let's go with lavender.

**41:45** · I'll give it a height of something small, maybe something like 40. All right. What I want to do now is show you how you could start separating your components into different files. And this is going to be how we organize our code moving forward in the course. It's very common that for every component we make, it's going to live within its own file. That way, we can easily locate and modify uh these components as our application grows. So, typically what you'll want to do is make sure that your file name matches your component name.

**42:14** · You can already see that here, right? In the app. JSX file, there's a component called app, and that's exactly what we export. Similarly, for my component, I'd rather create a my component file. And I'll do that by right-clicking the source folder, hitting new file, and I'll type in exactly my component.jsx.

**42:34** · You'll notice that I'm using capitalization, and it's going to match exactly the name of the component. And what I'll do is I'll just go ahead and copy this code and just go ahead and paste it into my new file. What you need to do though is you need to export this component. Now, and so what you could do is just export default my component. So let's say you're a little unfamiliar with the syntax in JavaScript. This is really straightforward.

**42:57** · All it does is take this variable or this function my component and it actually makes it available in the rest of the application if you choose to import it somewhere else. Right? So I do export default my component and that means over in app.jsx things are going to immediately break.

**43:15** · Right? Because so far on line three I'm referencing something called my component but it doesn't know what that refers to right now. And I'm getting that error in my console. Right? It says my component is not defined. Right?

**43:26** · Nowhere in this file is my component defined. So what you want to do is actually import it from the new file that you just created. So you can say import my component from and you pass in a string corresponding to the path to your component file. Because I'm inside of app and app is right next to my component.jsx. What I could do is just say dot slash my component.jsx.

**43:54** · All right. If you're familiar with padding, this is just a relative path.

**43:57** · Dot means my current location, right? So I'm still within the source folder. And then I just say the name of the file, my component.jsx.

**44:05** · And from there, whatever you import here would actually correspond to what you export on the inside of that file.

**44:12** · Pretty straightforward stuff here. And so I'm getting no errors. So this is good to go. Uh, a few ways you'll actually see these imports occur is uh sometimes people like to actually omit the file extension. So you could just say my component without the JSX. That's totally valid, right? No errors over here. Obviously, the name that you use in the path here should correspond exactly to the file name, right? So it's my component. If you did something wrong, like my component that would actually give you an error.

**44:40** · So I'll drop the T. You see the error.

**44:43** · And you know, our dev server actually gives us a pretty useful hint here. Fail to resolve the import. Does the file exist? doesn't exist because it should be called my component.

**44:54** · Awesome. All right, programmers. That's all I got for this one. I want you to do is go ahead, take a moment and code up this exercise on your own. If you get stuck, feel free to reference this video walkthrough and follow the instructions within the prompt. And I'll catch you in the next one.

### Intro to Tailwind CSS Lecture

**45:12** · Hey programmers, Alvin here. Welcome to our module on Tailwind CSS. Tailwind CSS is a framework we can use to style our frontends. It's going to be what we use for the rest of the course to help us create beautiful React UIs. There are a lot of different styling frameworks out there. So, you're probably wondering, why did I choose Tailwind CSS for this course, right? There are a lot of other frameworks, things like Bootstrap or Styled Components. Well, in my opinion, Tailwind is just the best and most versatile. It's really a joy to use overall and it just works. Every year, there's an annual developer survey called State of CSS.

**45:41** · In this survey, front-end engineers get to vote on the technologies that they use, including what they're interested in using, what they're currently using, and what they would use again in the future. In the 2023 state of CSS survey, Tailwind CSS performed overall the greatest. When it came to a combination of awareness, usage, interest, and retention. To quote the authors of the survey, they said, "Once again, Tailwind CSS stands apart as the one major UI framework that developers are happy to keep using." And Tailwind CSS isn't just a new kid on the block.

**46:11** · It's been around for a few years now and in the last four years has seen tremendous growth.

**46:17** · All right, so there you have my vote of confidence for Tailwind CSS. Let's hop into the blackboard where I can convince you of how easy it is to use.

**46:25** · Right now, I want to introduce the basic mechanics you can use to apply Tailwind CSS in our React code to establish some styles. For now, I just want you to watch this video lecture and don't worry about trying to code along. In the next task, you're going to have some opportunity to actually code up these things on your own. So, like we saw previously in the course, we can have content on the screen in the form of some div tags. Previously, to apply styles to our UI, we use the built-in style prop to pass in some inline styles. Like we mentioned previously, that's actually an old and unmaintainable way to apply styles in your front ends.

**46:56** · So, moving forward, we're going to use Tailwind CSS. So, how does that work? Well, we know that using a div tag like this that's unstyled would give us some very plain output like this, right? Just some text in black. Hey programmers on the screen.

**47:11** · Instead of using the style prop, you want to use the class name prop. And this prop actually is going to take in a string. Inside of this string, we can reference some Tailwind CSS classes. We can use Tailwind CSS class names to apply styles to this tag. For example, a simple class name we can use here is text LG. That just stands for text large. That will actually increase the text size on the screen.

**47:37** · Similarly, we have other variations of this class name like text XL which like you expect make it even larger stands for extra large. But what's great about Tailwind CSS is we can apply way more styles than just that. For example, I can use the class name text green 400.

**47:52** · Notice that the second class name is separated from the first one with a simple space. This, of course, we change the text color of this div to green.

**48:00** · You're probably wondering what the 400 means that's attached to this text green style. that refers to the shade of green used for this color. Smaller numbers would refer to lighter shades and larger numbers would refer to darker shades.

**48:13** · So, for example, if I change this to text green 600, that would darken the text like so. Now, if I did something much lower, like 200, that would really lighten that green text. So, let's take things further and apply even more styles to this. If we wanted to apply a background color, we can use BG and of course reference some built-in color.

**48:31** · Like you expect, this would give us a red background. And because the number is 700, that's a relatively dark red. If I made this 400, it would lighten that red a little bit. So text size, text color, and background color are all things we saw previously. But what else can we do using Tailwind CSS? Well, it's also really great for applying some quick borders. So let's say I added these two additional class names. Notice that the first one says border 2 and the second one says border cyan 400. Like you expect, the second class name I added just refers to the color of the border.

**49:03** · The first class name of border 2 refers to how thick I want the border.

**49:09** · Two just being some arbitrary unit. Of course, if you increased this number to something like four, that would give you a thicker border. If you did something like eight, that would double the size even further. Awesome. So, don't worry about trying to memorize all of these different class names right now. I really just wanted to introduce to you the mechanics of applying class names to your code. As you code through the exercises in the next few sections, you're really going to get comfortable with some of these basic class names.

**49:35** · All right, programmers, that's all I got for this one. What I want you to do is hop into the next task where you're going to be able to code up your very first lines of Tailwind CSS. I'll see you there.

### Tailwind Basics Exercise

**49:47** · Hey programmers, welcome back. Right now, I want to go over the Tailwind CSS basics exercise. And so I'll jump right in over here. First thing I want to do is hop into the solution demo in the bottom left over here. That way you can take a look at what we need to be building. So overall, we're just going to practice building five different divs applying some different styles of course using Tailwind CSS. We're going to write our first lines of Tailwind together. So the first thing I'll probably do is of course turn on my dev server. So I'll do npm rundev in the terminal. Now we're starting to see our to-do output.

**50:15** · Of course that comes from the app.jsx JSX, which like usual just has to do hard-coded inside. It looks like the first div you want to build is this red one over here. If you hop into the prompt instructions for this, we've also provided some references to different Tailwind articles as well as what overall colors you're going to be using.

**50:35** · When you complete this exercise on your own, don't freak out about choosing the exact color that we used in the lecture.

**50:40** · The really the point of this exercise is to just explore using a different Tailwind CSS classes. And so it looks like for that first div, I want to give it a red background and a rose text color. So over in app jsx, I'll start by putting that first div right inside of this app div over here. I'll give it the text one. Like we saw in the previous lecture, what we want to do is give this a class name prop. And here I can refer to any Tailwind CSS classes. So for example, one of them would be text rows.

**51:11** · I'll use something light like a rose 300. That'll give me a slightly pink tone over here. Awesome. Similarly, I want a background color. So, I can do BG red. We'll do 500 to start. And if that isn't dark enough for you, then you can, of course, darken it by increasing the number here. For the most part, your numbers for your shades are going to be in multiples of 100. So, I can go probably to like a 700. That should give me this really deep red. If you hop into the prompt, we've also included some generous Tailwind references here.

**51:39** · So, if I click on Tailwind color docs, that'll give me a quick reference page for all of the different out- of-the-box colors in Tailwind CSS. Here you can see all the shades of rows as well as all the shades of red over here. So, that's pretty straightforward. Let's go ahead and work on the second div. We want to give it a slate border and slate text color. So, right below this one, I'll create a brand new div. Give it the text two. Of course, start it up with some class name. Slate is just going to be a type of gray color.

**52:10** · So I can say things like maybe text slate 300 gives me this gray color. And when it comes to your grays entailment, I think one of the most important aspects of a beautiful UI design is actually choosing the right type of gray and just varying qualities of gray. So if we hop into the colors once again, you can see that for Tailwind CSS there's a lot of grays. As you can see here, there's slate, there's gray, there's zinc, there's neutral, there's stone. To me, they all look like types of gray.

**52:41** · Uh toward the top, like for slate, it looks like a very bluish gray.

**52:46** · Whereas something toward the bottom like stone would be a more warm or reddish gray. So, I'm going to go ahead and darken this slate a little bit. We'll use 400. Of course, larger numbers mean a darker shade. And I also want to start giving it a border. So, like we saw in the lecture, border really needs two different classes. You have to choose the width of your border as well as the color. So, let me start by just giving it a black border. I can say just border-black. That'll give me the really, really dark black. And I want to choose a width for this border.

**53:14** · If I just say border with nothing else, that'll give me the smallest width possible.

**53:21** · From there, I can increase the size by saying dash two. So, that says border two. Or I can increase it to like border four and so on.

**53:32** · You can see that border 8 gives me a very thick border all around. If you look at the tailwind CSS docs for border, we can see all the different values we can use for the border width.

**53:43** · Notice that we have 0 2 48. Meaning we're not going to have every possibility when it comes to a border width. For example, there is no border three or border six for that matter.

**53:54** · Right? That being said, all of the predefined sizes will usually have you covered for all of the UIs that you're going to be building in this course. All right, so let's keep playing around with our borders over here. So right now, by just saying border eight, that means I'm using a width of eight for my borders, and I'm going to have a border all the way around. You can also modify this to just use some directions. For example, if I do border L8, that gives me only a left border with eight, right?

**54:21** · Similarly, I could do the top. Of course, you just use T for top. You can use B for bottom. And you can even use R for right. All right. So, pretty intuitive stuff. Just use the first letter of the direction you want to cover. But what if I wanted a border only on the top and bottom? Well, to do that, you can say border Y8. Y meaning the vertical direction. Like you guessed it, if you wanted to do a left and right border, you can do border X8. That gives you only the left and right, meaning the horizontal X direction.

**54:51** · And what's great about this is you can actually combine these styles. So what if I want a width of eight on the left and right, but on the top and bottom border Y, I want a very thin border. We'll say border Y 2.

**55:07** · So I have very small slivers on the top and bottom, but really thick borders on the left and right. Awesome. So that's looking pretty good. I'm going to go ahead and use maybe just a border of two all around. And I'm going to color this slate. I can say border slate. I'll choose a maybe slightly darker gray.

**55:24** · Border slate 600. Let's take a look at what we want to do for the third div over here. We want to start by giving it text color, background color, which is straightforward, but this time around also a text size. So, I start by laying down the skeleton for this. Of course, I'll give myself a div. Give it a class name. Give it some inner text of three.

**55:45** · And to give it the proper text size, you can just say text. And you can modify the text size by doing things like SM for small.

**55:54** · If you wanted the medium or default size, you would say text base.

**55:58** · If you want something larger, you can do text LG for large. And you can do extra large throughout, right? So, XL gives me this size text. And from there, you can even say things like 2XL and even further. In the prompt for today, you can find the actual documentation page for these different text size classes.

**56:17** · Pretty straightforward stuff. So, let's go ahead and give this an emerald background. I can say bg emerald, which of course is a type of green. I'll use a light emerald background. So, maybe 200 here. And I'll make the text bluish. So, I'll say text. I'll use maybe a dark blue. Maybe blue 600.

**56:36** · That's looking pretty good. Let's go ahead and create that fourth div.

**56:41** · Just copy this over. And for four, we want to give it some extra large text.

**56:46** · So I could just say text XL. And in terms of what else we wanted to do with it, looks like we wanted to give it a purple text and sky border. I can say text purple. And I'll give it some dark purple like 500.

**57:01** · Looking pretty good. And I want a sky colored border. I'll just say border all around. So this time I'll say like border 4. And I'll say border sky. Let's say 500.

**57:13** · Awesome. There I see it. Let's go ahead and create one more div together. Let's create the fifth one. We want Excel text size and purple text again for this second number five div, but this time we have a different border and a different background. So, let's just start with some of those common styles.

**57:33** · So, we still want XL and text purple, but we're going to drop this border for now. And that will be our number five div here.

**57:42** · So, an important thing to note whenever you have some duplicate code that you're writing, you should probably try to figure out a way where maybe you can clean it up and not have to repeat the code multiple times. Right? So, here I noticed that for these last two divs, I'll space them out over here. For the four and five divs, they have the same text size and text color. Right? And because of that, what you could do is actually wrap both of these divs in another div and put the style there. In other words, I'm going to copy the extra large and purple color and put it on a parent div.

**58:19** · Then what I can do is I can move these two children divs inside. I'm going to remove the duplicate styles. We're going to kind of break down how this works. So I'll copy this code and put it inside of this div. because this parent div has extra-l large and purple text, those styles are actually also applied to the children, right? So, you see that although my inner children divs don't directly have purple text, they're still purple on the screen. And you can use this to your advantage if you wanted to actually sometimes have a child that might differ.

**58:51** · So, here I'll create maybe six just as an example. This six is inheriting the purple uh text style. If you actually put its own color over here, like text we'll say red 200.

**59:06** · This would actually override the parent style here. So again, the point here is to notice that children can inherit styles from their parent. They can also override that same style by just having their own class name that's similar.

**59:19** · Cool. So I'll drop this six div over here. And when it comes to this second five div, it looks like we wanted a violet background. So I'll do bg violet.

**59:31** · I'll use a light violet, maybe like 200.

**59:33** · And I also want to give it a left only a purple border. So I'll say border left.

**59:39** · I'll use a thick one like eight. And I'll make that border a dark purple.

**59:43** · Maybe purple 800. Super dark purple.

**59:48** · All right, programmer. So that's all I got for this one. What I want you to do is go ahead and now code up your own five divs for yourself. And feel free to mess around with these different styles.

### Padding & Margin Lecture

**59:56** · Once you're done coding this, I'll see you in the next task.

**1:00:03** · Hey programmers, Alvin here. What I want to do right now is give you a quick lecture on padding and margin. We're going to keep things conceptual in this video, so we're not going to go over any code. But what I will be sure to do is give you a background on padding and margin and how they differ and when to apply them. In my opinion, padding and margin are two of the most important ingredients when it comes to creating a really elegant and clutter-free UI. So, without further ado, let's hop into the blackboard.

**1:00:27** · Padding and margin are similar in that they are the two ways we can establish spacing when designing our front ends.

**1:00:33** · Let's start by talking about padding.

**1:00:35** · So, we're going to do here is go through an example where I have some content on the screen. Let's say my content was a cat. Like we saw previously, we can do things like add a border around this content. So, add a border around this cat.

**1:00:48** · Padding is going to be the distance between content and its border. In other words, if I increase the padding for this element, I would push the border away from the cat. That would look something like this. That's me increasing the padding. Of course, we have particular control over the amounts of padding. So, we could have a lot of padding on the left and right and only a little padding at the top and even vice versa. So, when it comes to controlling padding in CSS, you have a lot of control over it. And what you need to understand is padding is going to be the space between the content and its border.

**1:01:19** · So that's pretty straightforward for padding, but how does that compare to something else like margin? So let's go through a similar example. I'm going to start with a cat within a border, but this time I need to look at multiple elements. Let's say I had a lot of different elements or a lot of different cats on the screen, and they could have their own borders as well. If you were to increase the margin of the dark blue cat here, that would push away the other cats. That's me increasing the margin.

**1:01:45** · Margin is going to be the space or distance from one element to another. By controlling margin, you're controlling the space between elements.

**1:01:55** · So, how can you summarize the difference between padding and margin? Well, for padding, I think of it as the space inside the border. And that means that margin is going to be the space outside of a border.

**1:02:09** · So, let's recap with the final example over here. Let's say I had one element that's going to be my cat and it has its own border. Likewise, I'm going to have a dog element with also its own border.

**1:02:19** · What I want you to do is think about what would happen if I increase the padding for just the dog.

**1:02:26** · Well, we know that padding is going to be the space inside the border, right?

**1:02:29** · So, it's going to be the space between the dog and its border. So, that would look something like this. If I increase the padding, notice that the cat is still right up against the border of the dog. It's just a case that the dog's distance to its own border is much larger here. So now what would happen if I increase the margin of the dog?

**1:02:47** · Well, we know that margin is going to be the space outside of the border. So this would have the effect of pushing the cat away from the dog's border.

**1:02:57** · At this point, I can go ahead and decrease the dog padding, but keep the margin of the dog.

**1:03:03** · Because I've decreased the padding here, it looks like the dog's border is much closer to the dog itself. But I've maintained the same margin, right? So the dog and cat are still some distance apart.

**1:03:14** · And that's all there is to it. In the next task, we're going to be more hands-on and I'm going to show you exactly the code we can use in Tailwind CSS to control our different values for margin and padding. I'll see you there.

### Button Style Exercise

**1:03:29** · Hey programmers, Alvin here. What I want to do is go over this button style exercise. This is going to be an exercise where we get to practice margin and padding. So the first thing I want to do is hop into the bottom left and look at the demo for the solution. That way we can see what we want to build. So here I want to have the objective of building four different buttons that we can practice this padding and margin style. Of course we're going to be using Tailwind CSS for all of this and even use what we learned in the last lesson about colors. So we'll jump right in.

**1:03:56** · First thing I'll do is I'll give myself a running dev server npm rundev. I'll hop into app. I think before I create any of the buttons that we have to make for this one, I'll go ahead and actually just do a quick rundown how you can mess with your margin and padding.

**1:04:13** · So, let's say I start with some div and I'll give it some text like hello and I'll give it at least a border that I could play around with. So, I'll say border border red 500.

**1:04:27** · And by default, I'll have this red border all around. I want a little thicker so you guys can see. So I'll do border two. Cool. And so what I'll start by doing is applying some padding to this div. So if I say P and I say P4, four is just going to be an arbitrary kind of unit of space. This gives me padding all around the content. Here the content is hello. And right now I have padding inside the border above to the left below as well as to the right of this content. Like you expect you can increase this number and you have greater amount of padding. So more space.

**1:04:59** · Recall that panning is going to be the space within the border. Now, if I use something else like margin, if I say margin for or M4, that's going to be space outside of the border here. What's useful about that is if I had two divs and I give them some amount of margin, now I can have some space between them.

**1:05:22** · And you have a lot of control over the amount of margin and padding and even in the direction that you want. So for this second div here, I'm just going to make it say by and I'll make it blue. That way we can talk about a little more easy. And instead of P8, maybe I want horizontal padding. So px of just two.

**1:05:42** · So it's quite small padding on the left and right. Then I want vertical padding of eight.

**1:05:48** · This is the same kind of directionality style that we used uh in our borders in the previous lesson. Right? So X refers to the horizontal direction, so the left as well as the right. And Y refers to the vertical direction, so the top and the bottom. If you just wanted, let's say, only some bottom padding, you could do PB.

**1:06:08** · And these direction rules also apply to margin, right? So let's say for this hello div, let's say I only want to give it margin bottom of four. So I'm going to say MB4 instead. And so the rest of the borders will actually touch the edge of my screen. and there'll only be a gap below or at the bottom of this hello div. So that's all there is to the basics of margin and padding. By now, hopefully you're starting to see the utility of Tailwind CSS. Let's go ahead and create our first button together.

**1:06:39** · And through all of this, we actually do want to start using the button tag. I think a lot during the course we've been using div. Now we want to start using some more semantic HTML.

**1:06:48** · And so what I could do is just open up a button tag.

**1:06:52** · You close it like a pair tag similar to just something like div. And I'll call this one my first button. And what's immediately great about having a button tag is you get some of the built-in button styles. Mainly if you hover over the button, you'll actually get like the pointer finger because obviously you're going to be able to click this button.

**1:07:12** · Let's start by just styling this button before we give it some functionality that comes later in the course. So for this button, we want to give it green text and green border as well as some rounded edges. That's pretty straightforward.

**1:07:24** · I'll go ahead and give this a green border by saying border maybe two. I'll say border green 600.

**1:07:34** · Nice. And then from there, I'll also give it green text. I'll say text green.

**1:07:40** · I'll go a lighter shade of green this time. Maybe green 400 for the text.

**1:07:44** · Awesome. not looking too good yet because I didn't apply padding and margin. Padding and margin, I think, is probably one of the most important aspects when it comes to designing a nice UI. It gives you a nice sense of spacing in your interface. For a classic button shape, typically they have more width than they do height. So, I'll give px of 8. So, that's quite a bit of left and right padding. And I'll do py of just maybe two. That'll just give me a little bit of padding on the top and bottom. I do want to space this away from like the edge of my screen.

**1:08:15** · I could do that using margin. I'll just use margin all around of four.

**1:08:21** · Cool. And then from there, what I also want to do is give it some rounded corners, which is a very simple style and tailwind. You can say things like rounded medium. That gives you medium roundness. Or you can do rounded LG for large. Gives you even more roundness.

**1:08:36** · I'll just do rounded medium over here.

**1:08:39** · That looks like a pretty good button to me. Before we go into our second button, one thing you might have noticed is if I actually create and copy and paste almost the same code.

**1:08:51** · So I have two identical buttons, but for the first one, I'm going to make it a div instead. Actually get quite a different look, right? So this is actually the default behavior of a div, right? Divs by default will take up the full width of their parent container.

**1:09:05** · Because I have a div just out in the open, it's going to be roughly the full width of the screen here. buttons are not going to take up automatically the full width of their container because this button doesn't grow to the full width of the container. It's just going to be the size based off of the text I put inside. So, if I put more text here like hello, of course, it's going to be a little wider because I still have to add uh some padding of eight units on the left and right. So, that's just helpful to know. So, we'll go ahead and undo this.

**1:09:36** · We can hop into our next button here.

**1:09:39** · like they say in instructions. Looks like it just have some sky background and some white text. So that's pretty straightforward to do. Go ahead and create your button.

**1:09:50** · I'll say second class name. When you create class name, the prop, make sure you give it a capital N, right? I've seen students mess that up before. I'll give it some rounded corners. Maybe rounded large.

**1:10:03** · I'll give it BG sky, maybe 400. And I'll say text white. That gives me pure white text. Doesn't look too good because you didn't add any padding yet. So I'll say maybe px 10. And I'll do py4. So it'll be a nice fat button. Awesome. From there, I can also mess around with the text size. Just some review. I can say text maybe LG or take it further. Do something like 3XL.

**1:10:34** · What I want to do is be sure to give this second button some margin. That way it has some space to breathe around it.

**1:10:41** · That looks pretty good. Awesome. Let's take a look at what we want to do for the third button. Third button is going to be a light violet background and dark violet text with some fully rounded borders.

**1:10:54** · So we'll go ahead and bang that one out.

**1:11:00** · So I'll start by saying BG violet really light. So, I'll go 100 and I'll give it some text. I'll say third. See what we get to start. That color is looking pretty good. I'll give the text a dark violet. So, I'll say violet 600.

**1:11:18** · Gives me that kind of monochromatic look. And I'll want to give myself some padding. I'll say px 8 py 2. It's usually my favorite kind of button shape. Then from there, I'll use rounded. If I did rounded large, it still has like a rectangular shape. If you do rounded full, you get semicircles on the ends here. Kind of gives you that pill-shaped button. Beautiful button at that. All right, let's take a look at the last fourth button we need to make here. So, this is just going to be a square shaped button.

**1:11:48** · Has a cyan background and cyan text just of different shades. We also have some cool style where we hover over the button and we change the color of it. What you'll notice is the background color of the button changes and so does the actual text color of the button. Looks like they actually flip here. That gives you a really dynamic sort of UI. So we'll go ahead and do that together. And by the power of Tailwind CSS, it's actually really simple, right? So I'll create this fourth button.

**1:12:18** · And for now, I'll at least start by creating the right kind of regular styles without the hover effect. So I'll first want to go back and probably give my third button margin of four so it's not too close. Nice. I'll give this one also a margin of four.

**1:12:34** · And what I'll do from here is give it a dark cyan background. So bg cyan, let's go like 700.

**1:12:44** · Looking pretty good. And I'll do a light cyan text. So text cyan 200.

**1:12:51** · Nice. Then from there, I'll give it maybe like px or maybe p all around of 10. And I'll finally add some rounded large. Give me those rounded corners.

**1:13:03** · Nice. So if you want to change the style of some element based on whether or not you're hovering over it with the mouse, you can use hover colon. What you can do is then write the style you want to apply when it's hovered. So, for example, I can say hover colon and I'll say bg red 200. So, right now I'm not hovering over that four button. But when I do hover over it, I get a really light red background. Almost looks pink. Awesome.

**1:13:33** · But for me, I'm actually going to switch it to a light cyan. So, cyan 200.

**1:13:39** · So, I get this kind of effect. And when I do that, I also want to change the text color. So I'll also say hover text cyan 700.

**1:13:51** · So when I hover over it, the text turns much darker and the background turns much lighter, giving me this sort of effect. You can use this hover variation on any type of style. So although I did it for colors here, and it's probably most common to use it for colors. Let's say for my second button, when we hover over it, I'll change the text size. So I can say hover colon. When you hover, make the text the base size, which is kind of like the medium size. So I'll take a look at that. Notice that it shrinks.

**1:14:24** · So that's all I got for this exercise.

**1:14:26** · What I want you to do is take a moment, create these four buttons on your own, and feel free to mess around with the padding and margin values. Once you're ready, I'll catch you in the next one.

### Tailwind ClassNames Lecture

**1:14:38** · Hey programmers, Alvin here. Right now I want to continue our discussion of Tailwind CSS and talk about how we should handle our dynamic class names.

**1:14:46** · Here I'm referring to when we generate those class names which are strings using some programmatic logic. So here I am in the Tailwind CSS docs and the first thing you want to do is understand that you should not construct your class names themselves dynamically. In other words, if you look at this very simple example, we just have a div. And notice that it looks like the programmer here is using this error boolean and they're trying to switch between a red and green color. So if the error boolean is true, it looks like they want to use text red 600. But if the error boolean is false, they want to use text green 600.

**1:15:16** · And this is actually not allowed in Tailwind CSS. You're going to get some errors if you write code like this. And the annoying part is you actually will probably get errors only some of the time. So you do want to avoid this pattern overall. So, if we can't write this, you're probably wondering, how should we implement code where we can switch between our red and green color?

**1:15:36** · Well, the key is to not actually break up your Tailwind CSS class names. In other words, you need to make sure that your code has like the literal text like this, right? Text red 600 and text green 600. So, don't try to break apart uh the class name uh by concatenating something into the class name itself. So, the way you want to write it is like this. We're still using a turnary operator here and we're still using a boolean. However, notice that the class names appear in their complete form, right? It says text red 600 or text green 600. So, this is the way you should write it.

**1:16:08** · And you should avoid dynamically concatenating parts of a single class name. So, let's practice this a little bit more. Maybe you're a little more curious how you should do this. So, here I have my simple uh component and what I want to do is just start applying some class names to this div. So for now I'm going to give this a BG red 500 and it should correctly change the color. Something that you do not want to do is you know some logic like this. Even just having a simple variable saying color and I'll put maybe red inside.

**1:16:38** · What you should not do is try to uh dynamically create that single class name. So doing something like this is not going to be reliable behavior for you. Here I would write color. So here's an example of something you should avoid. Right? This is breaking our rule because we're not writing a complete Tailwind CSS class name. Notice that this does correctly render my red background here. U the really important thing to understand is that if you write your code this way, it's going to be unreliable. We call this flaky behavior.

**1:17:08** · And so you want to make sure you follow the Tailwind CSS best practice and don't do things like this.

**1:17:15** · Try making it green here.

**1:17:18** · Notice that when I make it green now, it's not even turning green. Right?

**1:17:22** · Before it was red. So here you're able to see the very flaky behavior of this code. Now it's not showing any background color at all. And because of this, there are some obvious other forms that you should also avoid. So even if you wrote it maybe without using a template string, maybe you just concatenated some stuff together, uh you'll also want to avoid similar syntax. So for example, what you can't do is say like bg dash plus your color plus the dash 500.

**1:17:52** · So this is also not going to be good for the same reason. Notice that it's not showing up as green. So this doesn't work either. I think the most common way that you might end up accidentally writing some logic like this is when you have some conditional logic. So this is going to be a pretty arbitrary example, but you can really see the mechanics of this. I'll just have some boolean and I'll make it true. And like we saw in the Tailwind docs, you might be tempted to write something like this. You'll say maybe my bg dash and then you'll maybe write your turn your expression here.

**1:18:24** · You'll say if the boolean is true then use maybe orange.

**1:18:32** · Otherwise I'll use purple. Then here I would try to add on like the darkness of this color. Let's say we made it 600.

**1:18:41** · So, as this code stands right now, my boolean is true, which means I should be evaluating to this orange color. Right?

**1:18:47** · Right now, that color is definitely not showing up. If you wanted to, you could try refreshing the page. Still no dice here. And so, the correct way of writing this would look something like this.

**1:18:58** · You'll want to wrap your entire expression inside of the turn array. So, I'm going to use a full class name here.

**1:19:04** · I would say one option would be my orange, right?

**1:19:09** · And the other option is going to be my purple. So I'll say BG purple 600. Now I put that entire thing uh in my turn area. So I'll say if this boolean is true, then make it orange, otherwise make it purple. And the nice part about this code is we're actually able to say the complete class name here. So this is the correct version. Notice that's showing up as orange. If I say false here, it should flip to my purple.

**1:19:38** · And obviously, I still have the ability to even write, you know, another class name here. So, I can say maybe I want the text to be white. That's fine as well.

**1:19:52** · Cool. So, always make sure that you write your complete class name. All right. So, that's all for now. I'll catch you in the next task.

### Button Component Exercise

**1:20:02** · Hey programmers, Alvin here. Right now, I want to go over the button component exercise. So in this exercise, we're just going to practice using what we just learned about Tailwind CSS to create a nice reusable component for us in React. So if you hop into the demo solution in the bottom left over here, you can see what we want to build. So we just have two simple buttons. They look kind of similar, although one is definitely larger than the other and has some different styles. It's actually the case that you want to implement these two buttons using a single React component. Awesome. So I'll jump right in.

**1:20:33** · The first thing I want to do is create the button component as well as its file. So I'll call this component fancy button.jsx.

**1:20:43** · And we'll start by just laying down some of our classic button shapes. Of course, I want to do this all inside of a component though. So I'll define fancy button. For now, I don't think I need any props, but I will just have it return some button.

**1:20:57** · I'll just say my button for now. And because I want to import this into my app later on, I should export here, right? So I'll say export default fancy button. Just reviewing some of that classic a file syntax. And now within app.jsx, you want to import that file.

**1:21:16** · So you'll import fancy button from dot slash fancy button.

**1:21:23** · Because app and fancy button are right next to each other, you can do a simple dot slash. Then from there, you can just render your fancy button. For now, I'll use the self-close version. Let's go ahead and take a look at our output.

**1:21:37** · So there I see my button doesn't really look like a button because I didn't add any of those Tailwind CSS styles. So let me go ahead and style things up. You can feel free to add any of your own favorite colors and style for this button. I'm going to follow the demo quite closely. So I'll use some blue styles, I guess. So I'll give it a class name. I'll start by giving it maybe a background color. I'll do a light blue.

**1:21:57** · So, BG blue. Let's go for like a 200.

**1:22:00** · I'll also give it a border. So, I'll say border two. Border blue. I'll use a darker blue for the border. Maybe 700.

**1:22:08** · And I'll use blue text as well. So, I'll go ahead and say text blue 700. So, my button colors are looking pretty good. I think one thing that will really give it some nice look is of course add some padding. So I'll say px 10 and py 2. And for good measure, I'll also give it some margin so it's not too close to the edge of the screen here. So I'll just say margin 4 all around. So that looks like a decent button. I'll go ahead and just round the corners.

**1:22:38** · I'll use rounded medium this time. That looks like a great initial button. So now that I have this button component, I think I want to make it a little bit more dynamic. So let's say app, let's say I render this component multiple times. So, I have two instances of my fancy button. Right?

**1:22:55** · Now, the text within the button is going to be the same both times, right? That's really because I've hardcoded the label right inside of the button component, right? It says my button over here.

**1:23:05** · Instead, I want to make this more dynamic. What you could do is add like a label prop where you can pass in the label string that you'll use for the button. But like we saw previously, you can also use the children prop between the tags. You can say things like click me or I can do something else and I can write something like submit.

**1:23:26** · By only making this change, you're not going to see those new labels, right?

**1:23:29** · What you have to do is actually use this within the implementation of fancy button. What that means is inside of the fancy button, I'll take in props and I want to dstructure out of it the children prop special reserved prop in React. What it will do is just look at whatever you passed in between the pair tags for your component. So I'll take in children and I can just render children right inside of the button because I want to evaluate this variable with what it contains. I'm putting it in another set of curies here.

**1:23:59** · So there I at least have a little dynamic label for this button. So it's a little more reusable.

**1:24:06** · We want to take this further. Like we say in the prompt, what you want to do is now give your component a large prop which controls some of the changing styles for it. You want to increase the text size and even change some other styles. For me, I'll change the roundedness of the component just like the demo. Right? For my second submit button, it has much larger text and has fully rounded edges it looks like. So we'll go for that approach. Let me start by passing in the prop where I need to.

**1:24:32** · So over in the app, I'll give it a large prop for the first one. I'll make it false. The second one is going to have it as true.

**1:24:43** · Nice. Now within the implementation for fancy bun, let's see what we can do here. Well, the first thing I'll do is probably dstructure out the large prop, which is going to be a boolean. And I can use that boolean to conditionally add some different styles to the button here. So, what I'll do here is control at least the text size using the large prop. So, to keep it clean, what I'd probably do is create a separate variable and I'll call it my large styles. I just want it to be the class names that I'm going to dynamically change using the large prop. So, I'll use a turnary here.

**1:25:13** · We saw this previously. And so, if large is true, then this string is just going to be text maybe 3 XL. Otherwise, I'm not going to use 3 XL. I'll use the original size which I can reference by just saying text base. Nice. And I want to use this large styles variable to assign it additionally to the class name here.

**1:25:36** · So what I can do is just add this large styles variable into this string. So I want to open up some curly so I can start evaluating some JavaScript operations. And one thing you could do is like put a space at the end of this style and then do plus large styles.

**1:25:52** · That gets a little difficult to manage sometimes, but it is a working solution at least. Notice that the second button because it has large is true, I get the much larger text size. If you don't want to do the concatenation here, another thing you can do in JavaScript is use the template string syntax. So, I'll go over that as an aside here. Maybe you're unfamiliar with that syntax in JavaScript. So, let's say had some string. We'll say my string and I'll make it just hello.

**1:26:19** · You can construct a new string. So I'll say new string some back ticks. So instead of quotes I'm using the back tick symbol. So that would be the key that's also on the tildy button on your keyboard. And what you want to do is write some regular characters. So I can say like Alvin said and then what you could do is use a dollar sign and open up some curly braces. This lets you insert any JavaScript evaluation. So here I can say my str. So if I console.log log this new string.

**1:26:50** · Just as a quick aside, go ahead and open up my console. There I see Alvin said hello. Right within the dollar sign curly braces, you can evaluate any JavaScript. So I can even say Alvin said 4 + 4, which would now be eight. So how can I use this template string in my React syntax here? Well, I can turn this string into a template string with some curies. And then within I'll leave a space and I'll do dollar sign curly braces. Then here I'll write large styles.

**1:27:22** · And then you don't need to do the addition. You don't need to concatenate these strings together. We call this concept conditional styles.

**1:27:30** · Right? That means sometimes I'll have one style depending on some condition and other times I'll have that other style. And I don't need to just mess with the text size here. Maybe for the large version. So when large is true, it'll have 3 XL text, but I'll also be rounded full. whereas the default will be rounded medium. And I can actually drop the rounded medium over here.

**1:27:55** · So now I have two fairly different looking buttons. And this is all controlled by just the large prop over here. So there's also one additional optimization you can make here. When you have a boolean prop like large, if you want to just pass in a true value for it, you can actually just drop the assignment and just say large.

**1:28:15** · And then for the false version, you just don't say large at all. So notice that although I'm not passing in a large prop for my first click me button, it still renders as the non-large version. It's as if large is false, right? And in the case of my second submit button, when I just say large, it is acting like a true still. So let's take a peek under the hood of how this works. So I'm going to console.log log what the large variable is. Because I'm rendering two buttons, I'm going to see this prop printed out twice.

**1:28:45** · So I'll refresh the page here. First I see undefined and then I see true. So the order here does correspond, right? So for line five, when I first render the click me button, it looks like the large prop is undefined. That's actually similar to what we saw previously. And then for the second time I render the fancy button, if I just say large and not assign it a value, looks like it automatically takes the value of true.

**1:29:08** · So in the case where large is undefined, it acts just like false, right?

**1:29:13** · Undefined is a falsy value in JavaScript. If it's false, that means you take the base size with medium rounded corners, which makes sense for the click me button. However, when large is true, then of course you evaluate to the first part of the turnary expression here. So you take your triple XL and fully rounded corners. All right, programmers. So that was a quick little walkthrough. What I want you to do is now code up this exercise on your own.

### Flex Box Lecture

**1:29:34** · Play around with these conditional styles and I'll catch you in the next one. I'll see you there.

**1:29:43** · Hey programmers, Alvin here. Welcome to our first lecture on flexbox. For us, flexbox is going to be a really important piece of style because it's going to let us design UIs that have a very responsive aspect to them. So, it's going to be able to scale for different screen sizes and overall give us a very modern looking web page. In this lecture, I just want to provide you the basics behind using flexbox. So without further ado, let's hop into the blackboard. Let's say we start with this initial code. We see that we have three cat components rendered inside of some div.

**1:30:12** · Like you imagine, this div is going to have a border and it's going to be green. Let's say that these cat components just rendered a div with a cat image inside. By default, things would look like this. Notice that the cats are all stacked vertically and they're stretched out to the full width of the green container. For the green container, we do have a padding of four.

**1:30:32** · So that explains why there's a little gap between the cats and the green container. But right now, I want to introduce the concept of flex. Flex is actually going to be a new type of class name we can use from Tailwind CSS. What this does is make the green container a flexbox. As soon as you add the class flex to the green container, things would look like this. The first thing you'll notice is now the cats are ordered from left to right. Instead of stacking vertically, now they go horizontal. As soon as you add this flex class, you have a lot more control over the layout for these cats.

**1:31:01** · So let's say you added this additional class called justify end, you can only use this justify end class if the container is already flex. And as soon as you do this, this would actually push all the cats to the right like so. If you change this to justify center, that would cause all the cats to appear as close to the middle as possible. You can also do a justify between, which would cause all the cats to move as far away as possible from each other, spacing them out like this.

**1:31:31** · And finally, we also have access to justify around, which is really similar to justify between, except there's going to be even space to the left and right for these cats.

**1:31:41** · Notice that now the left and rightmost cats have more space between their borders and the green container. So when you use flex in one of these justify classes, you're able to control the horizontal positioning for these different flex children. In this example, I have three flex children.

**1:31:58** · They all are the cat component. So let's take things further. Let's say I added an additional class over here. This time I'm going to change the height of the parent. Of course, the parent here is that green div. I'm going to give it a height of 72. This isn't a class name we used previously in the course, but like you expect, it just gives a set height to the green container. As soon as I apply this class name, of course, the green container is going to stretch out vertically. And by default, all of the flex children, that is all of our three cats, are also going to stretch to the full height of the parent.

**1:32:29** · But let's say I wanted to modify this behavior. So I already have my green container as a flex. What I want to do now is apply some new styles. Let's start with item.

**1:32:40** · If I do item start, this will actually put all of my cats at the very top of the container.

**1:32:48** · Notice that they're no longer stretched out. Like you guessed it, I could also do item center, which would put my cats in the middle vertically.

**1:32:56** · I can also do items end, which move my cats to the very bottom vertically.

**1:33:02** · So when we have a flex container with these items classes, we're able to control the vertical position of the children here. Whereas for justify, it was able to control the horizontal position of the children. And do note that all of these class names of flex, justify, and items, they were all applied directly to the parent. We didn't have to put these class names on the cat children. By adding flex classes to the parent, that actually controls the positioning of the children. So, let's go through another example. Let's say I had a regular green div like so.

**1:33:33** · And I put three cats inside.

**1:33:36** · Like we saw previously, by default, they're going to stack vertically. And along with that, they take up the full width of the green container. As soon as I make the green container a flex, that will actually move things into a horizontal layout. We call this a flex row. If I wanted to move all of these cats to the middle horizontally, I can additionally add a flex justify center.

**1:33:58** · If I wanted to move them toward the very bottom, now I can add an items end.

**1:34:06** · Now, if I wanted the cats to appear in the middle vertically and also in the middle horizontally, well, then I can use a justify center and an items center.

**1:34:15** · And now, if I wanted to modify this current layout so the cats stayed in their vertical position, but were more spaced out horizontally, I could change the justify to a justify between.

**1:34:28** · So the key thing to take away right now is for a flex row, justify is going to control the horizontal direction and items is going to control the vertical direction.

### Flex Exercise

**1:34:38** · So I know I just threw a lot at you, but don't worry, you're going to get to practice these concepts in the very next exercise. I'll see you there.

**1:34:48** · Hey programmers, Alvin here. Right now, I want to go over this flex exercise before you do it on your own. So the first thing I want to do is of course print up my dev server and then go ahead and look at the output. So this is the output of the current code within app.jsx. You'll notice that for this project we actually start with a decent amount of code to begin with. Right.

**1:35:06** · First thing you'll notice is there's actually a pre-made cat component file.

**1:35:10** · You actually don't need to make any changes to this file right now. You should only be making changes inside of your app. JSX. So looks like in the starter code I have five different containers. They all have different colors just so it's easy to track what you're working on. For each colored container div, it looks like I have some initial styles. Looks like we have a flex as well as a set height and some padding and margin. And that makes sense given the look of each of these different colored containers. Your objective for this exercise is to make your output look exactly like the demo.

**1:35:40** · Notice that the demo has the cats in different layouts. You want to match these colors. So, for example, for the purple div over here, you want the cats to be at the very bottom and have some space around them. And you'll want to do all of this by just adding a few different flex class names. So I'll go ahead and actually work through these exercises right now. If you want, you can watch this video fully and then perform the exercise on your own or you can actually try the exercise for yourself first. And if you get stuck, come and reference this video.

**1:36:06** · In the prompt instructions for this, we actually listed out all the possible justifying items rules you're going to need for your flex containers to accomplish the output you need. But I'll jump right in over here. Looks like for the blue div, what I want to do is just move all of the cats into the center horizontally, right? And so for me, that's as simple as adding a flex justify center. And it's okay if you can't really remember these and you have to just kind of trial and error, different possibilities for the rules.

**1:36:37** · That's totally okay. The beautiful thing about coding is you can get quick feedback on what went wrong, right? So let's say you made the mistake of doing item center.

**1:36:47** · Well, then it just wouldn't look right, right? You put them in the center of vertically because you want to do it horizontally. You ought to do a justify center. Nothing to it. So, looking at the red one, it looks like I just want to space them as far apart as possible horizontally. Right. So, what I'll do there is for that red div, give it a justify between, right? Justify between is how you can maximize the space between all of your children, all of your cats here.

**1:37:17** · If you actually did a justify around, remember that that would add a little more space to the sides of every cat, which doesn't look exactly like the image we want. Notice how there's only a tiny bit of space between this right cat and the red border. This tiny bit of space comes from the padding, right, of the container. So, I'll bring this back to justify between Right.

**1:37:42** · So, we're done with the red div, it looks like. Let's move on to the green div. So, I want my green div to look just like this one on the left. Looks like it's centered vertically and also horizontally. So, what I can do there is for this green div, be sure to give it a justify center.

**1:38:00** · That should bring them right to the middle horizontally. Then, now and also an item center to make them center vertically.

**1:38:08** · Now, looking at this purple div, looks like I want the cats to appear at the very bottom vertically. Let me just get that out of the way. So, to do that, I know that I can add a items end. That put it at the bottom vertically. And then from there, it looks like I only need to work on now spacing them apart. Looks like there's a good amount of spacing to the left and right of all of the cats. So, what I'll use here is a justify around.

**1:38:37** · So for the purple div here, go ahead and add a justify around.

**1:38:46** · Nice. So finally for the orange div here, looks like I want a lot of space between my cats. I want to bring them down to the center line.

**1:38:56** · So for that, I'll go ahead and add a justify between. That'll give me as much space as possible between my cats, but I want to bring them vertically in the center like you expect. Items center.

**1:39:09** · Cool. That's all there is to this exercise. So, at this point, I'm going to flip it over to you. And don't worry if you're having a little trouble coming up with the correct styles for this one.

**1:39:17** · Since it's your first time using a flex styles, you will have to do a lot of trial and error. And as you actually keep applying these different flex rules of justify and items, you're going to get a lot more awareness for which one to use in what scenario. And don't worry, we'll get more practice on this in the future.

### Flex Column Lecture

**1:39:36** · Hey programmers, Alvin here. What I want to do right now is go through a lecture on flex column. Flex column is going to be the counterpart to flex and what it's going to allow us to do is be the final ingredient when it comes to creating a modern UI. Let's hop into the blackboard.

**1:39:50** · So let's start by reviewing what flex is. So I know that flex can be applied to some parent and it's going to affect the position of the children within. In this case, I have my cats. We could have modified the horizontal position of the children here by using a justify class.

**1:40:06** · That's going to move things in the horizontal direction. And that helps me do things like space the cats apart horizontally. Similarly, I can also use an items class to modify the vertical position of these cats. In other words, I can move my cats up and down or put them in the middle. One thing I want to emphasize right now is when you have a flex, the children are going to peer horizontally.

**1:40:28** · So let's take a look at this new concept. We can also additionally add a flex call modifier to a flex container and this changes things slightly. So I can apply flex flex call to some parent and it can still have some children inside but because I have a flex call that stands for column which means that the children are going to stack vertically. And what's particular about this is now that I have a flex column, when I use a justify, it's actually going to modify the vertical positioning of these dogs.

**1:40:57** · So I can move these dogs to the bottom or I can have a lot of space between them. And you guessed it, now when I apply an items class, that's going to affect the horizontal positioning of these children. So I can push all the dogs to the right or bring them to the middle.

**1:41:14** · So the key distinction here is when you have a regular flex, we saw that that means the children are going to appear across horizontally. But when you have a flex call, your children are going to stack vertically. Probably the most confusing thing when it comes to using a flex column is its justify and items classes behave the opposite compared to a regular flex. For example, this is the flow for a regular flex. We know that justify will move the children left and right and then the items class will move the children up and down.

**1:41:42** · But when we have a flex call, items is going to move the children left to right and justify will move the children up and down. So this distinction between justify and items will take a little bit of time to wrap your head around, but with some practice, it'll become second nature.

**1:41:59** · Luckily, if you're having trouble remembering which one to use and how to apply in a certain direction, you can just try the class and if it doesn't move things in the way you want, you can just use the other class. It's really nice that we can experiment by just quickly changing the different class names on our elements.

**1:42:15** · All right, so that's all I got for this lecture. What I want you to do is hop right into the very next exercise. We're going to be able to practice what we learned about flex column. I'll see you there.

### Flex Exercise II

**1:42:27** · Hey programmers, Alvin here. Right now, I want to go over this flex exercise, too. So, in this exercise, we're going to be able to practice both our flexer and flex column layouts. So, I'll jump right in. What I want to do is, of course, turn on my dev server to get going here. This exercise is going to be split up into four different box components. I can see them on my screen.

**1:42:46** · You'll notice that each box has three dogs inside. My goal is to make my output look just like the demo. So, if I click on the demo on the left sidebar, notice that the dogs follow some different positioning, of course, using those flex rules. So, let's jump right in. If I look into the app component here, I actually don't need to make any changes. You'll just see inside of the app component, we have our four different box components rendered. Each box on the screen you see over here, like this first blue one, would correspond to one of these components.

**1:43:13** · So, really, you want to make your change inside of box one, box two, box three, and box four. So, starting with box one, what we should do is first look at the demo. So, looking at the demo for our box one, it looks like we need to center our dogs horizontally and vertically.

**1:43:30** · For each of these boxes, the first thing I recommend you do is figure out whether you need a flex row or a flex column.

**1:43:35** · Right? Because these dogs appear left to right, I know I'm going to need a flex row. By just saying flex on the class, that automatically gives me a flex row.

**1:43:44** · Right? If I look at my output, my dogs are already going from left to right.

**1:43:47** · So, I just want to work on centering them. So, I can do a justify center.

**1:43:51** · That'll bring them into the center horizontally. And now I want to do an item center to also center them vertically. Now, it should look just like the demo. Awesome. Let's go ahead and move to our next box. Looking at box number two or the gray box over here, it looks like now I'm using a flex column.

**1:44:10** · I know that because the dogs are appearing on top of each other in a stack, right? And it looks like there is some space between these dogs. So to me, this will either be a case of justify around or justify between. So we can kind of mess with it and see what looks best. So for my output right now, my gray output over here, I have a flex row because it's just a flex. If I do flex call, now they appear on top of each other. And now I want to bring them into the center horizontally because it's a flex column. I can do that with items center.

**1:44:41** · So now they're going to appear right in the middle. And now I want to put some space vertically between them.

**1:44:47** · So to do that, I can do a justify between.

**1:44:53** · So if I compare the demo on the left to my output on the right, this looks like we're right on the money. All right, looking at the third box over here, this teal colored box, it looks like I want to put my dogs in the middle horizontally again, but this time have them be at the bottom. And I notice that these dogs are actually appearing on top of each other. So this is going to be a case of a a flex call. So I'll hop into box three here.

**1:45:17** · And let's start by moving these dogs on top of each other by adding a flex call.

**1:45:22** · And now I'll bring them into the center horizontally this column by doing items center.

**1:45:28** · Then I want to push them to the very bottom by doing justify end.

**1:45:34** · All right. Looking at our fourth box or the red box over here. Looks like I again have a column because they're appearing on top of each other. I want to put them all the way to the right.

**1:45:43** · And finally, looks like I have some space around each of my dogs. And so I can mess around with this. Start by making this a flex call. Do bear in mind that when you use a flex call, it should also be a flex, right? If you just say flex call without the flex class separately, you're not actually going to stack them properly. So to make a flex call, you actually say flex space flex call, right? And I want to put at the end. So I can say items end.

**1:46:11** · Nice. And now I'll do a justify around to give them some space around in the vertical direction like so. Awesome. So that's all we got for this quick little exercise. I just wanted to give you an opportunity to mess around using your flex column rules. In the next exercise, we're going to start putting everything together. So I'll see you there.

### Analyzing Layouts Lecture

**1:46:32** · Hey programmers, Alvin here and right now I want to talk to you about analyzing layouts. Analyzing layouts is a really important skill because it allows us to look at a UI and then recreate it on our own. The skill I want us to practice here is to look at a picture of a UI and try to figure out what class names are used to style it up. And I'm not referring to the obvious styles, right? It's very plain to see whether a UI is using a certain background color, certain font size, or has borders, right? Those types of styles are very obvious to the naked eye and easy to spot.

**1:47:00** · Rather, what I want us to focus on is try to look at the underlying structure of a UI and figure out how elements relate to each other in their positioning. Let's head to the blackboard and I'll show you what I mean. Lately, we've been talking a lot about flex. And when we have a flex container, it allows us to have some children that flow horizontally, left to right. On the flip side of that, we know we can have a flex flex call, which is similar except it stacks vertically. So it's also container except this time my children go top to bottom.

**1:47:32** · And it's pretty plain to see that the main difference between these two types of flex containers is one is a row and the other is a column. Right? Think horizontal versus vertical. So what I want to do right now is go through a few examples of different UIs and try to spot where the rows and columns lie within the structure of the design. So let's start by looking at this UI. It just looks like a collection of links.

**1:47:53** · This would actually be the footer from the React Formula homepage. The first thing we can spot is possibly that there are three sections here, right? Looking at one of the sections like product, it looks like a column because it's pretty plain to see that there are a lot of things stacked vertically up and down.

**1:48:08** · Likewise, that about section also is going to stack vertically like a column.

**1:48:13** · And even to the far left where there's a logo as well as some other information, that also itself stacks vertically. So, we can also imagine that it's a column.

**1:48:21** · And I did indeed make these three sections all columns when I created the UI. So just using that classic flex flex call style. But there's more to the story here. Because I have these three sections and they appear from left to right horizontally, I know that they really form a type of row. Imagine that I have three children inside of this row. So in this small example, we could already see that we use both columns and rows to establish a really neat UI.

**1:48:46** · Let's look at another example. This is also from the React Formula homepage.

**1:48:50** · What I want you to do is take a moment and try to figure out if you can spot any columns or rows.

**1:49:00** · Well, one thing I can notice is the entire UI really forms a column because I see a lot of things stacked on top of each other. I'm going to highlight them in green blocks. I have the header over here as well as the section with the three items that is also below it. And then finally below that I have the button. And those three are definitely stacked vertically as if it was a column. And we can drill down further here. Let's say we looked at one of these three items. Well, I also see some vertical stacking. So this looks like a column as well. At the top I have the image. Below that I have a title.

**1:49:31** · And then I have some more description text below.

**1:49:36** · And we have this numbered section repeating three times over. We can also see that those three sections also form a row because they appear left to right.

**1:49:47** · So again, there's a lot of utilization of both the row and column concept over here. Let's look at another example.

**1:49:53** · This is the familiar course contents from the React formula website. There's a very obvious column here for each of the three cards, right? They all form a stack.

**1:50:04** · And of course, you can also find plenty of rows in this UI. I'm just going to look at one particular type of row.

**1:50:09** · Looking at this item for a task and inside of that row, it looks like there are two children. What I can notice is there's a lot of space between those two children. That's a familiar concept from before. So, not only can we identify whether we have a row and a column, you can probably already start to see the underlying class names we can use to implement it. For example, the section of the UI I have highlighted in yellow currently, I can implement that using a flex justify between. I know it's justified between because I've moved the children as far apart as possible.

**1:50:37** · And I know it's a plain old flex because these children are left and right. So let's look at one final example from another website. You can really spot these rows and columns off any UI that you look at.

**1:50:51** · So here I have just the Instagram login page. Take a moment and see if you can spot any particular rows and columns.

**1:51:00** · If I analyze this UI as a whole, I can see that it forms a very large column because I have a lot of vertical stacking. So, not only do I know that this is going to be a flex call, but it's also going to have item center because it's pretty plain to see that there's a lot of centering horizontally for this column. Let's also spot a few rows in this UI. An obvious row for me would be the black download on the App Store buttons here where I have two children inside. Similarly, all of the navigation links at the very bottom form a very long row with many children.

**1:51:34** · All right, programmers, that's all I got for this lecture. In the next exercise, we're going to practice looking at a completed UI and then recreating and coding it up on our own. Since we're still beginners, copying UIs is going to be a very nice stepping stone that will help us move toward eventually creating our very own UIs from scratch. By looking at and analyzing different user interfaces, you're going to be able to draw from all of that material when you're ready to create your very own.

### Tailwind Docs Lecture

**1:52:01** · Hey programmers, Alvin here. Before I set you off on the next exercise, I just want to give you a quick little tip when it comes to using Tailwind CSS. Right now, I want to talk about measurements and using the documentation. So, here I have a quick little example set up. All it is is a blue div containing some text inside. By default, this div is going to grow to take up the full width of the screen. We can see that on the right here. What you can also do is assign it a width using a Tailwind class. For example, I can say width 24.

**1:52:29** · And beyond that, I can also say other values like width 32. Notice that it gets a little bit bigger. This syntax of using W followed by dash and then a number, those are going to use Tailwind's predefined sizes. So, if I hop into the documentation for Tailwind, you can just Google around for it. I'm going to type in with here right in the search documentation is really robust.

**1:52:50** · What I can see if I scroll down a little bit looking at the picture here I find the picture most useful is that I have some predefined values for width. For example, 24, 32, 40 all the way up to some large values like 96. But one thing to notice is when you use these predefined widths in Tailwind, you don't get every single possible value. For example, there is no width 81. So let's say I try to do that. I do width 81.

**1:53:15** · That's not going to look quite right.

**1:53:16** · Right. It's the same as not setting a width at all because 81 isn't actually a built-in tailwind width, but 80 is. We can see that over here. When it comes to building your different UIs, for the most part, you can get away with just using these built-in Tailwind sizes, right? The designers of Tailwind have actually chosen these sizes because they tend to give a very visually pleasing uh UI. But let's say you wanted to use your own custom size. Of course, Tailwind lets you do that easily as well.

**1:53:44** · So, I'll hop back into my code and let's say I'm not really satisfied with using width 96, right? 96 would actually be the largest width that you can use that's built into Tailwind, right?

**1:53:56** · Because it says so right in the documentation. If I want to go a little larger than that, well, what I could do is use a custom value. To do that in Tailwind, you can open up some square brackets. Then you can write a unit of measurement, right? I tend to use pixels a lot. So, what I can do is use just an amount of pixels. for example, 400 px.

**1:54:14** · You can go larger from there. And you could actually use any arbitrary value in between, right? So if I wanted 422, that would give me a slightly larger div, right? Or 425, even larger still.

**1:54:26** · So when it comes to setting up the dimensions for your different elements in Tailwind, try to stick to using these built-in values, but if they don't really work for you, then you can go ahead and use that square bracket notation and then put a number of pixels right inside. And this syntax of using a custom size with some square brackets applies to most of your different Tailwind styles. So for example, I'm going to go ahead and put two divs actually inside of this one. I'll just call it one and two.

**1:54:54** · I'll give them different colors just so you can see them. And so I'll make the one div the blue one. And I'll make the two div a red one. See what we get.

**1:55:07** · Makes sense. Of course, if I want to apply some margin maybe below the one div, I can do MB for margin bottom. I could write a unit of space like eight, right? Or I can increase it to something like 12.

**1:55:21** · And when it comes to your margin bottom sizes, similar to not every possible value exists. For example, what if I try to do margin bottom 13? That actually doesn't work. It looks like there's no margin between them, right? So you have to use your Tailwind docs actually look up what default sizes you want to use.

**1:55:38** · Right? So I'll go for margin. So looking at the margin page, I can scroll down. I can see all the different values they let me use. Right? Looks like I could use two 2.5 and so on. But of course if you want to use your own custom sizing and go ahead and use that square bracket notation. So what if I wanted exactly 13 pixels? So I could say square bracket 13 px and take it from there. So, the moral of the story is when you're stuck creating your UI and a class isn't behaving like you expect, it's probably time to reference the Tailwind documentation.

### Analyzing Layouts Exercise

**1:56:08** · And with that, I'll see you in the next one.

**1:56:15** · Hey programmers, Alvin here. Right now, I want to go over this analyzing layouts exercise. So, in this exercise, you're going to have to copy the UI that you see within the demo. So, again, to open the demo in the left sidebar, you can just click on this demo button, and you're going to see an example of the completed UI. This UI is going to contain three different quotes. Really just some quotes from different programmers and they all follow a similar card design except they use some different styles. The skill we want to practice here is using all of the different Tailwind CSS styles that we've seen so far to implement a UI.

**1:56:44** · So looking at the starter code within AppJSX, you'll notice that we've given you three quote objects. Uh each quote object here corresponds to one of these boxes. And inside of the quote, you're going to have all the text you need to render the correct output. You'll notice that here it says, "One of my most productive days." That corresponds to the beginning of the quote. The author is Ken Thompson from over here. And finally, you have a short bio on them.

**1:57:08** · Ken Thompson was a designer of the Unix operating system. And so, let's jump right in. You really also want to create three distinct components for each of these designs, right? So, I'll start by creating my quote box one. And immediately as a prop, I'm going to have it take in quote one. So, I'll take in a prop called quote. It's going to take in the quote one variable. So, I'm passing in this literal object uh into quotebox one. So, let me set up some of my classic code here. So, what I'll do is first create quotebox one. So, that's going to be my component file.

**1:57:40** · Quotebox one.jsx.

**1:57:44** · And I'll define quote box one. Take in some props. For now, I'll just have it return some placeholder div that says quote one. and be sure to export default it. I want to make sure I import and export things properly before I actually go ahead and jump into my implementation. So at the top of appjsx, I want to import this. So I'll import quotebox one from do/quotebox1.jsx.

**1:58:13** · And like we said previously, you can actually drop the file extension. So you only need to say quote box one. Looks like I'm already rendering some correct output. Awesome. So let's start establishing the shape of quote box one.

**1:58:25** · The first thing I'll notice is looking at the demo is has a nice rectangular shape and I'd say there are two main sections. I have this a colored section with the quote and then I have the name and bio. I do notice that these two sections are on top of each other. So that kind of signals to me that the card itself is probably a flex call. So I'll say flex flex call. And for now I'll say one and two and just see what things look like. I want these two inner divs to be on top of each other. So, I'll get my output. That's looking decent.

**1:58:54** · What I'll start to do is I give myself some of the proper colors. So, for the top div here, I'll give it a background. And you we can feel free to actually mess around with the colors on your own a little bit. So, for the top div here, I'll give it the cyan color. Maybe I'll go for BG cyan 500. And for the bottom div, I'll give it bg slate. I'll do a light slate.

**1:59:22** · Maybe slate 100. Maybe we'll darken this a tad as well. So that's looking pretty good. Uh notice that for now it looks like this entire quote box because of this outermost div is stretching to the full width of the screen. I can help you see that by adding a border. So I'll say border border red 400. Oftentimes I think it's useful to create temporary borders when you create your components.

**1:59:45** · That way you can see the shape of things. So, it's definitely clear that quote box one is taking the full width of the screen right now. And I can actually fix that inside of my app. I do want to center the card and not have it take up the full width. And so for the parent, which is in the app, the div over here on line 22, I can say class name. And I'll make this a flex for now.

**2:00:06** · I can just make it a justify center. I know that's going to center things horizontally. So there I have my centered div. probably would be also a good thing to give some margin around this quote box one. So I'll say margin of four.

**2:00:20** · Looking pretty good. And now let me start adding some padding within my two sections. So I'll mess around with the padding here. You can use kind of your eyeballs to figure out what's a good amount of padding. I usually like to start with P4. Gives me some nice breathing room. I'll use P4 for both probably. To really have things take shape. What I want to do is start using my actual text data. So notice that quote box one is taking in a quote prop.

**2:00:45** · I'm going to go ahead and accept that quote prop. I'm going to dstructure it like I always like to do. I'll call it quote. And this would be the full object, right? If I wanted to, I can console.log this whole quote. I can see it in my developer console here. And there I see the quote object has text, it has an author, and it has a bio. What I want to do is for now render the text in the cyan region. So I'll put quote text, right? Because text is the property I need, right?

**2:01:15** · I use the key text to get the corresponding value. And I'll maybe also start to lay down the author and also I'll lay down the bio.

**2:01:30** · Slowly keep styling things as I go here.

**2:01:32** · One thing you'll notice is the width of my card actually increased. This long piece of text here is actually driving the width of my div. So if I like increased it, if I gave it more content, this would actually increase the width of it. But if you don't want that, what you want to do is assign a fixed width to your elements. So if you want to use a fixed width in Tailwind, you can use W and you can write a unit of space. For example, like 24 would be really small.

**2:01:55** · Notice that this cyan region is now a smaller width, right? You can also increase it to something larger like 80.

**2:02:03** · And these are the arbitrary tailwind units. If I want to choose a custom size, what I can do is say w dash and use square brackets and then write like an amount of pixels. So for example, I can say I want this width to be 400 pixels. That would give me a decent size. Cool. I kind of do like how my quote is on two lines now. Awesome. What I'll start to do is a fix the bottom region. I want the author name as well as the bio to stack.

**2:02:31** · So, because I want them to stack, I'd probably make them two separate divs because I eventually want to apply some different styles to them.

**2:02:44** · And I'll go ahead and make the parent, right? This is the parent here. I'll give it a border so you can see it.

**2:02:51** · Border. Border blue 400. And I'll thicken this border a little bit. So for this blue parent, what I want to do is make it a flex call so I can center the children. So I'll say flex flex call and I can say items center.

**2:03:09** · That'll give me some nice centering.

**2:03:13** · I'll start to clean up these borders for now. So I'll drop that blue border. I'll also drop the red border. And I'll start comparing this to the demo. So looking at the demo, looks like I'm moving toward the right direction. Maybe I'll go ahead and fix the font color of the top region. So, quote box one. The font color for the top, I'll use a type of cyan. So, I'll say text cyan. I'll go for a really light cyan like cyan 100.

**2:03:42** · It'll probably be on the money here.

**2:03:44** · Maybe even cyan 200.

**2:03:46** · That looks pretty sharp to me. And then for the text in the lower region, I want the name or the author rather to be a type of scan. I'll say text can scan.

**2:03:58** · I'll use maybe that 600 again.

**2:04:02** · Then I'll use a slate for the bio.

**2:04:06** · Class name the bio. I'll use text slate.

**2:04:10** · The background's already slate 100, so I need to choose something darker than that. I'll go for 400.

**2:04:17** · Nice. From there, I want to increase the size of the author and maybe even darken the text. So, make it a little darker, which is easy to do in Tailwind. Then increase the size. I'll say text, maybe 3XL, giving me a large name over here.

**2:04:33** · Awesome. Doesn't look too bad. Not exactly like the demo, but it'll fit the bill for me. If I wanted to add some space below the name, that way there's a little gap between Ken Thompson and the next line. I can just add some margin bottom using MB. So, I'll say MB2. Give me a little bit of breathing room there.

**2:04:50** · And now that I see it, this text is probably too large, though. It's probably a better idea to make it maybe a 2XL.

**2:04:57** · So, I'm looking pretty close to the demo. One thing I'll do is I want to add those rounded corners. And you'll notice that there's actually a very slight border around that bottom portion. So, I want to mimic that as well. Now that I look at this, I think I used not exactly the same color. This looks like a slate.

**2:05:11** · This one is a stone. So, not a big deal, but I'm quite a stickler. So, this should have probably been a stone instead. So, let's say I rounded corners for the cyan region, right? So, I'll say maybe like a rounded large. If you do that, that's going to round everything all the way around. And I don't like how those rounded corners at the bottom here. Kind of makes it look disconnected from the next section. So, I really only want to round the top two corners.

**2:05:37** · Tailwind CSS super awesome. Recommend you look at the documentation for it, but I'll kind of give you the hint here.

**2:05:42** · What you could do is just say rounded T for rounded top and then say large. That would round both the top left and the top right corners. Looking good. In a similar way, I want to round the bottom corners for the other container. So, over here, right, this is my stone div.

**2:05:58** · What I want to do is do rounded B large.

**2:06:02** · Give me some nice roundedness. What you will notice is right now I'm not getting too much contrast between the white background and this really light gray div here. So it's a little hard to see uh in circumstances like that. What we can do is just add a very tiny border.

**2:06:16** · So I'll add a border and then along with this border it's probably useful to make it just a slightly darker version of the background. So I'll say border. I'll say border stone. I'll go like 300. Right?

**2:06:31** · That gives you some nice contrast. You can go a little lighter if you want.

**2:06:34** · Maybe like a 200 would look right on the money. All right, so that looks like a decent clone of quote box one. It's not exactly the same, but really the exercise here is trying to mimic the overall shape and look of the component, right? So you can feel free to mess around with the colors, adjust the padding how you like. Maybe I'll increase the vertical padding of the cyan region. So I'll say py 8 and maybe like px6.

**2:06:58** · Give me a little more padding all around.

**2:07:05** · So, let's keep it rolling and create quote box 2. I want to give myself a brand new component. So, I'll say quotebox 2.jsx.

**2:07:12** · And I'll start with the classic boiler plate. So, definitely go ahead and define your component.

**2:07:20** · And take your time with this part.

**2:07:22** · Sometimes it's annoying if you actually rush through just creating the basic boiler plate for your component. and then it kind of hinders your progress in terms of making an actual correct UI.

**2:07:31** · So, I like to always start with some kind of static message here like number two. And I'll be sure to set up my imports and exports. Make sure I do this properly. Quote box two. Be sure to render quote box two as well. And pass in the second quote. Right. Still going to take in a quote prop, but this time I'm passing in the Gracehopper quote over here. Nice. What you'll immediately see is it looks like my two quote boxes, right, are appearing next to each other.

**2:08:01** · That's because I made the parent in the app a flex. I want them stack vertically just like the demo. So, you know the drill. You can do a flex flex call.

**2:08:11** · And once you do that, you do want to still center things of in the horizontal direction. So, you ought to do a items center.

**2:08:20** · That looks much more reasonable. So let's start taking a look at what we need to do for the second quote here. So looks like I have again two sections.

**2:08:29** · One is going to be blue, the other is going to be white, but this time they go in like a horizontal flow. And I can worry about the borders later on. Let me just establish this type of shape here.

**2:08:40** · So we'll hop into quote box 2. Let me go ahead and dstructure the quote prop. So now what I want to start doing is laying down the skeleton of the divs. So on the left div, I'm going to give it a blue background. So I'll say BGB blue 500.

**2:08:57** · And I'll throw down two pieces of data.

**2:09:00** · I want to put the author as well as their bio. Right? So I can say quote.author.

**2:09:08** · And then also below that, I'll say the bio.

**2:09:16** · Nice. I'm going to go ahead and give myself a little bit of padding. So I'll say maybe like P2 all around. You can adjust your amount of padding to taste.

**2:09:25** · And I still want to add some margin. I want to leave a little bit more of a gap between my two separate cards here. So I'll say M4. So looking at the text here, I want some large white text and some smaller light blue text. So that's easy to get out of the way. I'll say text maybe like a 3 XL. And I'll say text white.

**2:09:48** · Nice. And then for the bio, I'll say maybe the default text size, so I'll leave it as it is, but make it text blue. I'll go for a 200.

**2:09:59** · Maybe even darker. Maybe a 300 looks good there. Yeah, I don't mind that. And I actually want to increase the padding here. It's a little too tight. Maybe I'll say P8. How does that look? A little too much. P4. Usually right on the money for my eyes. Nice. And I don't want just this blue region to be so large. So I could give it a fixed width, right? Like we saw previously. So I need to locate the parent, right? The parent would be the thing with the blue background. So I know to locate this div here. And what I want to do is give that a fixed width. I don't want it to be too large.

**2:10:31** · I could say something like width 48.

**2:10:35** · That's probably a little too small.

**2:10:37** · Maybe I'll increase that to 64.

**2:10:40** · What you'll want to do is if you use these fixed uh tailwind widths, you should be looking up what values exist.

**2:10:46** · It's not the case that every value exists, right? So width 64 looks pretty good. It's actually what I'm going to follow through with. But what you can't do is just say like width 65. Not every value like that exists. This is actually the same as not really setting a width.

**2:11:00** · If you want to be sure to always set a valid width, you can use an exact value like width of 428 pixels. Right? That's guaranteed to exist because you're really using a custom width in Tailwind.

**2:11:11** · Whenever you see square brackets, that's going to be a custom size and Tailwind.

**2:11:16** · But if I really just want to use the default Tailwind sizes, then you can just say W dash and I'll go with that 64.

**2:11:23** · That looked pretty good. Probably give a little bit of more space between the name and the bio. So I can either do maybe like a margin bottom on the author or a margin top on the bio. Let's go margin bottom on the author. I'll say MB2. Just a tiny bit of gap there.

**2:11:41** · Looking good.

**2:11:44** · I think from there, what I could get out of the way is maybe just round the left corners of this box. I don't want to round the right corners. Notice how they're nice and sharp here. So, let's go ahead and do that. I want to look for the parent, which is the thing with the blue background. And so, what I can say is rounded large. But if I do that, that will round everything. Instead, I'll say rounded Large.

**2:12:07** · Round only the left side. Right? So, I have rounded corners here. I have very sharp corners on the right. Nice. All right. So, let's work on the other half of this card, which is going to be that like half pill shape. So, what I want to do is add another div beside my blue div. So, I'll add that div over here.

**2:12:25** · And for now, I'll just give it some border. I'll say just border border red 500 just so I can kind see where it is. I'll put some of the text inside.

**2:12:36** · So, I'll say quote.ext.

**2:12:39** · Again, I know it's going to be quote.ext text because that corresponds with the quote that is passed in, right? Which has a text, author, and bio.

**2:12:51** · Cool. So, obviously, right now, things don't look quite right. For one, this red div is actually disconnected from the other one. And that's because I put the margin in the wrong place, right?

**2:13:00** · The margin should not be there. I wanted the margin to be on the outermost part of this component. That should be really here. Nice. And now I want the blue div and the red div to be uh next to each other as if they were a row. So I'll make their mutual parent a flex. Just to make sure you see what's going on here, I'm going to add a border to so a thick border that's black.

**2:13:28** · Right now this black border is the parent, right? It has the blue div and the red div inside. I want the blue and red to appear next to each other. And so to do that, I can make their parent a flex.

**2:13:41** · Nice. And we start getting that shape.

**2:13:43** · You notice that right now the div on the right actually grows to as large as it can be to accommodate the text inside, right? So all the text goes across on one line. But when I make it smaller, right, that will actually shrink. What I want to do is make sure it doesn't grow too large. So I can probably give it some fixed width. So I'm going to drop the red border from this. Don't actually need that anymore. What I will say is maybe give it a width of, I don't know, 48.

**2:14:12** · That looks pretty decent. Maybe I'll go a little bigger. Maybe I'll do another 64. So, let's say you're unsure with what amount of width you kind of want to use for your different uh divs. You can just search it. So, I'll type in width here on the Tailwind website.

**2:14:26** · Width.

**2:14:27** · And they give you all of the basic fixed widths, right? So 96, 80, 64, 48, 40, 32, and 24. Those are usually widths that give you a decent looking UI by default. Again, if you want to use a custom amount, you can just use that square bracket syntax I showed you. And use pixels. So let's keep it rolling here. 64 is looking pretty sharp. What I want to do is now drop this parent border. Don't need that. And I want to use like a grayish border over here. So I'm going to use that stone border.

**2:14:58** · So here I'll say border border stone and let's go with 200 maybe even a little darker maybe 300 looks pretty decent to me and what I'll want to do is give myself some healthy amount of padding so I'll say P8 maybe give me some nice space and from there I want to change the text color so I can say text stone I want something a little darker that way it's decent to read 600 looks good to me. Maybe even lighter.

**2:15:32** · 500. Yeah, it looks a little better. And now what I want to do is fully round the right hand side of this this gray border div. If I look at the demo, the way that's done is really just uh giving a rounded full on the right hand side of that div. So that's pretty straightforward. You can say rounded r for rounded right and you say full. That means make it like a semicircle. Nice.

**2:16:00** · Now that I see that, it's probably a little too close, meaning the right border is a little too close to my quote. So, I'd probably do here is actually increase the width. So, I'll say width 80. And then I'd also increase the padding. So, I'll say padding maybe 12 all around. That's looking pretty good to me. All right, I think that wraps up quote box two.

**2:16:26** · All right, let's hop into our third and final box for this exercise. So, we already created the basic quote box three. What I'll start to do is create my different sections. So, I know I want the quote at the top. So, I'll say quote.ext over here. And this one's probably the trickiest kind of layout to establish.

**2:16:49** · So, I'm going to go nice and slow. I'm going to use some borders as I go. So, I'm going to say border border red 500.

**2:16:57** · Make this a little thicker so you can see it.

**2:17:00** · And then I'll add another colored border div right below it. And I'll make this one maybe blue. And here I'll put the author.

**2:17:13** · And for now, let's look at this. So looking at the demo, it's clear that I have two distinct, you know, regions of this UI here. The top is actually pretty straightforward. It's more of the bottom div that looks hard to establish, right?

**2:17:27** · It's definitely below the top div like it was a column, but it doesn't take up the same exact width. And there are a few ways you can create that pattern, right? So, one way you can do that is maybe I'll start by giving myself a div for the author as well as their bio. One thing I can do here to get the right shape of the UI is to make the parent a flex flex call, which won't change too much at the start, but what it lets me do is things like a items start.

**2:18:01** · Notice that when I do an item start, that's going to make all of the children want to start at the beginning of the div, right, to the left side of the div.

**2:18:10** · And because of that, they no longer take the full width. So this actually gives me the correct looking shape so far. So now I just need to style things up properly. So let's work on the top region. So it looks like I have some type of rose color as well as some white text. So for the text, I'll give it a bg rose. Let's start with maybe like a 400.

**2:18:30** · And I'll use text white.

**2:18:33** · Nice. Give myself a healthy amount of padding. Maybe like P6 all around. I can drop these borders. Those were just for testing. I want to increase the font size here. So I'll say text maybe large should be good enough for me. And then from there I want to start to add a border to uh the bottom div here. So I'll say border 2. Border rows 400. So I use a similar rose color. See what that looks like. Give it a healthy amount of padding. So I'll say P maybe P4. And then I'll just want to adjust the color.

**2:19:08** · Looks like I have a very light rose almost looks pink background and then just some varying qualities of rose for the text here. So I'll give the background maybe like a rose 100. I'll use a dark rose for the name.

**2:19:25** · So I'll say text rose. Let's go really dark like a 700. And I'll make it a little bigger. I'll say text large.

**2:19:35** · Nice. And I'll use a lighter rose for the bio. So for this, I'd probably just say text rose 500. Now, what I want to do is work on the rounded corners. So if you look at the demo on the left here, you'll notice that the top div, the one that's going to be filled in with that rose color, it has rounded corners in the top left, the top right, and the bottom right. Notice that the bottom left corner is actually pointy. It's not rounded. And of course, Tailwind CSS lets you do that.

**2:20:01** · So, what you could do is start by saying rounded t rounded t large, right? This would round the top corners, but then that leaves the bottom right kind of not working properly. What you want to do is have that be rounded. Luckily, you can say rounded brot and then say large. That would target explicitly that corner as well. Notice that the bottom left corner is unaffected. So that's how you can target particular corners if you wanted to.

**2:20:33** · Obviously you can say things like bottom right, top right, top left and so on.

**2:20:37** · It's all pretty intuitive. And if it's not, go ahead and look at the tailwind docs, right? They fill you in on everything there. So you don't need to memorize these. And similar way I want to just round the bottom of that second div here. So I'll find the rose border, right? Which should be this one over here. Then from there I can say rounded b large. that gives me a very similar style. So, this is looking pretty good.

**2:21:01** · But one thing I'll be a stickler for, at least for myself, because I'm a little obsessive with my UIs, if I zoom in, you'll notice that this kind of dark rose comes down lower than the dark rose over here, right? And that's because this actually comes from a little border because this light pink div has a border that goes all the way around. So, it looks like it's kind of not even here, right? this edge is higher than this edge over here.

**2:21:28** · So, because I'm a little crazy and I want to fix it, what I could do is make sure I don't apply a border on the top of that. So, instead of just border two, that means border two all around. What I could do is apply this border in the directions I need. So, I'll say border L2, right? That gives me just the left.

**2:21:49** · And then I can say border R2, that gives me the right. Then I can say border B2.

**2:21:55** · That gives me the bottom. And I'm not going to put border T2. I'm going to leave out the top. And now I'm satisfied because I get a nice flush edge over here. Not a big deal, but know that all of these adjustments are possible using Tailwind CSS. All right, programmers, that's all I got for this exercise. What I want you to do is take your time completing all three of these boxes.

**2:22:14** · It'll be a little finicky to get all of the styles matching exactly right, but that's okay. Really what I want you to do is focus on getting the overall columns and rows down in these UIs. And once you're ready, I'll see you in the next one. Hey programmers, right now I wanted to take a quick break from our YouTube course to tell you about React Formula. React Formula is my complete course where you can master modern front-end web development using React.

**2:22:35** · The content you've been watching right now on YouTube is from the early chapters of my course on React Formula.

**2:22:40** · If you'd like to learn advanced React concepts and eventually build fullfeatured front-end web applications, I cover this and more in my complete React formula course. If you enjoy my teaching style thus far, I think you'll really love the course where we'll learn how to build even more impressive UIs so you can ace your front-end job interviews. And of course, I'll be with you each step of the way to explain everything. You can check it out at reactformmula.com. I'll be sure to leave a link in the video description. But for now, let's hop back into our free course.

### Search Page Design Exercise

**2:23:11** · Hey programmers, Alvin from React Formula here and welcome to our search page exercise. So in this exercise, what I want you to do is actually look at the demo and our goal is to recreate this UI. It looks a lot like Google, right?

**2:23:24** · We have things like a little header with some different divs and buttons. I'm also going to show you how to use some icons as well as a nice search box in the middle along with some other buttons and a footer. This exercise is going to give us one more opportunity to practice using all of the Tailwind CSS essentials that I've taught you in the last chapter before we hop into teaching some new React concepts. This exercise is going to be split up into three sections for the header, the center portion here with the search bar, and then finally the footer. And you're going to have a video walkthrough for each.

**2:23:51** · I highly recommend that you watch the video walkthrough for a section before coding up that section on your own because I am going to show you a few new things along the way. All right, let's hop to it.

**2:24:06** · All right, so let's jump right into this one. I'm going to start by turning on my dev server. We'll start by just creating that nice clean header. So I'll get situated over here. Get my output to the right. As we create the three sections for this page, I think it's going to be useful to split up your three sections into their own components. So the first thing I would do is create a header.jsx component. And I'll go ahead and define that component here. Right? So I'm going to have my header.

**2:24:33** · It's not going to take in any props, I think, but what it will do is just return some placeholder div. I'll just call this my header. And for now, I'll just give it some default background color. So I'll say like bg red 200. Be sure to export default. And now within the app, I'll go ahead and import and try to render that header component. Right? So I can import header from dot slash header and then I can render that right inside here.

**2:25:05** · So here I'll say header be sure to render it like a component. I'm going to self-close that tag. So here I'm getting a little error. I think I forgot to finish this phrase. It should say export default header of course. So this is looking pretty good so far. And now what I want to do is just focus on creating this header in a similar style to the demo. Of course, you can feel free to mess around with like the text you use or the different colors, but you should definitely try to follow the overall structure of the page.

**2:25:35** · So have some text on the left, have some text on the right, and so on. And so I'll follow the orange style here pretty closely. You can choose your own favorite colors using the Tailwind color palette. Um, but let me start by establishing those two groups, right? I have a group of stuff on the left and another group of stuff on the right. So within my header, let me go ahead and work on that. Start by switching this background color to some orange. Let's go orange 200 maybe.

**2:26:05** · And now I know that that section because it has two groups and they are next to each other from left to right. So that reminds me of a flex, right? So I'll say flex and I'll give myself at least two children right now. And I'll maybe I'll say here left. And then I'll also say right.

**2:26:25** · And right now my goal is to separate these two divs, right? Left and right.

**2:26:31** · Luckily, we've practiced a ton of flex.

**2:26:33** · Here's where all of your practice really pays off. And I can say justify between.

**2:26:38** · This is going to maximize the space between all of the children here, right?

**2:26:42** · Left and right. So, now that I have the two sections to the far left and far right, I think I want to establish some uh space within this header. So, I'll probably use some padding here, maybe I'll say like px4. That gives me four units of space to the left and right.

**2:26:57** · And maybe py2.

**2:27:00** · That'll make this a little taller.

**2:27:01** · That's looking pretty sharp to me. Of course, you can adjust, you know, the padding values here if you want to do what looks good in your opinion, right?

**2:27:09** · So now let me start putting some different divs inside here. You could even make them buttons if you want.

**2:27:16** · Later on I'll show you what these buttons can actually do, right? To make them clickable, but for now we're just going to kind of go for like a visual uh UI just so we can practice all of our styling. So I'll have this first one say about the second one say store.

**2:27:31** · But as soon as I start doing that, it looks like about and store stack, which I don't really want here. Just so you can see what's going on here, I'm going to say border two and border red 500.

**2:27:44** · I want these two children, the about and store div. I want those two children to be left and right of each other. So I'll make their parent, which is the red border, I'll make that a flex. That immediately solves my issue. I can you really structure a lot of your UI just using flex and flex column. Obviously, these are too close together. So, I'd probably just apply a nice amount of margin. So, I'll say maybe MX. So, just horizontal margin. I'll say MX4.

**2:28:13** · That looks pretty good. And I'm going to duplicate that more or less for the other side. Right. So, I'll give myself these two divs here. I'll put them right inside. I'd probably want to change the text here. So, I'd call this one maybe like settings. I would also make the parent a flex.

**2:28:32** · I'm going to go ahead and adjust the color of the text here. I'm going to use just some darker orange. And so what I'll choose to do is on the header parent, so the most outermost div on the header. I want to apply the text color here. That way all the text automatically gets this color. So we'll say text orange. Maybe let's try 500.

**2:28:52** · Nice. That's looking pretty good. You can make it darker if you like, which I will prefer here. looking pretty decent.

**2:28:59** · So, looking at the demo, this is basically what we're looking for. I do also want to show you how you could start using some cool little icons in your UIs. Really spruces things up. So, right now, I'm going to show you how you could start incorporating some easy icons in your UIs using Font Awesome.

**2:29:13** · Font Awesome is really just a library of different icons. They basically have an icon for everything you could possibly imagine, and it's super easy to use. You can just copy the code that they give you. In the prompt reading for this project, you'll actually find a link to this Font Awesome homepage where you can search up any icons you want to use. The React Formula Workspace is actually already set up and configured. So, you can just uh drag and drop the code you need for your different icons. In the later section of the course, I'll show you how to configure everything from scratch for yourself. But for now, we'll just hop into using these icons directly.

**2:29:44** · So, for example, I can click on any icon here. I'm going to use this awesome face. And I can just copy this code snippet. copy it. And back in my code over here in the header, I'll just go ahead and drop that right in.

**2:29:59** · Nice. The first thing you'll notice is this is going to be, you know, an HTML tag and it has I that stands for icon, of course. Then it's going to have a class with some built-in classes. These classes actually designate which icon and what style you want to use. One thing to note is because we're actually in a React app, instead of class, you want to rename this to class name. That way you don't get any errors later on.

**2:30:22** · You'll notice if I open my console here, it will actually probably warn you that you're using class, right? Invalid DOM property class. Did you mean class name?

**2:30:32** · That's why I fixed it over here. Nice.

**2:30:35** · And then you can see my little happy face over there. And so I'll use a different icon. So I happen to know there's also FA user.

**2:30:44** · Nice. And there are a few different styles you can do with that. If I hop back into the font awesome docs, let's say I went to the user over here, there were a bunch of different styles. So, this is like very dark and filled in. I can actually look at some different styles of this. All variations of a classic user shape.

**2:31:06** · Nice. Notice that it just changes the code a little bit. So, let's say I wanted to use the regular version, which I guess isn't filled in. I'm going to click to copy it. hop back into my code.

**2:31:16** · I can just replace this I this icon tag.

**2:31:19** · I'm going to be sure to give this a class name. What you can also do is adjust the size and color of this icon if you wanted to. This icon really acts just like some text. So if I want to increase the size of it, I can use some text size. I can say text LG for large.

**2:31:35** · Gets a little bit bigger, right? I'm going to go for something much bigger like 3XL. Want a nice big icon. And I could even change the color if I wanted to by saying text. Let's say I made it blue 400.

**2:31:49** · All right, it changes the color a little bit. So, I'm going to go for a violet color here. I'm going to go for maybe like a violet 600 just to switch things up. And that's all it takes to really use some icons using Font Awesome in your application. So, one thing you will notice is because I've just increase the size of my icon, right? The icon is like a 3XL size. Meanwhile, the other elements inside of the header like the settings text, those are still like the base size. They're much smaller. And so it looks like things aren't aligned along the center like I want. Luckily, I know my flex rules. So I want to fix a vertical centering of these things.

**2:32:20** · So what I'll do is try to debug it just using some borders. I think borders are a great way to visualize things. So I'm going to add a border to this flex container here. I'll make it a different color so you can see it. I'll say border black.

**2:32:35** · If I look at the black containing here, it's pretty clear that the children of about and store, they're not centered vertically, right? I know I can do that by just adding a items center.

**2:32:47** · Notice how that fixes it. So I just want to apply this item center to those flex containers. Right?

**2:32:54** · So I'll find the parent of setting and this icon which is this one. Help you visualize it by doing border border black.

**2:33:04** · And then all I want to do is just add an item center. And boop, they're right in the middle now. So feel free to add some borders as you go to make sure you can figure out what's inside of what element. And I think that wraps up my actual header. What's great about using a flex layout like this is of course it's already going to be responsive to an extent. If I resize things, things grow and scale accordingly. All right, so that wraps up the header. What I want you to do is code up your header for yourself. And when you're ready, I'll see you in the next section.

**2:33:36** · All right, let's keep it rolling. What I want to do is now show you how you could implement this center section. So, this center section includes the title of the page as well as a nice large search bar and then these two buttons. And like we said previously, it would be best if I can separate these different pieces of the UI into their own component. So, below the header, I'm going to go ahead and implement a search section, which of course I should create. So, I'll go ahead and create all of the starter code I need.

**2:34:07** · So, I'm going to create this component file and I'll call it search.

**2:34:14** · JSX.

**2:34:17** · Just want to start with a standard div with a placeholder. I'll say I am search. Want to make sure it renders properly. Nice. So, I think probably the easiest thing to get out the way is just go ahead and add your your title text. I made mine fugal. Feel free to change it to whatever you want. And I'll go ahead and put that in a nice div. And I'll say fugal. I want to work on centering things uh properly though.

**2:34:42** · So the first thing I'll do is I'll probably want to add a class name uh to the outermost div of my search right now and give it a border. That way you can kind of see where things are. So I'm going to say border 2 border red 400. So we'll see how things look. So, what you'll notice is this red box is my search and it's really small. I really want to take up a much larger height here. That way, I can center things accordingly.

**2:35:07** · So, what you could actually do is inside of your app, it' be actually great if you can add a height to the outermost div in your app.

**2:35:18** · For example, if I looked inside of this div right now, let's say I gave it a border. I'll say border two border blue 500. The entire app is actually quite small. It's only this blue uh div over here. If you want to assign it the height of the entire screen, which I think I'll do for this page, you can just say h screen.

**2:35:40** · Just dropping us some new styles for you. So, if I added this border actually back in. So, I'll say border border to blue.

**2:35:49** · The blue should be all the way around here, right? You can see it goes from top to bottom. Nice.

**2:35:57** · So, what I want to work on now is it's still the case that the red div, which is my search, it's still not the full height or the remainder of the height like I want. So, right now, my goal is to make this search div, this red div be the full height of what's left on the screen, right? Not including the header.

**2:36:13** · So, the trick here is you can make the parent a flex. But if I make it a flex, it's going to be a flex row. That doesn't look right. I still want it to stack vertically. So, do a flex flex call. Now, since the parent is a flex, you can actually apply some additional styles to the children. So, I'm going to go into the search component, right?

**2:36:33** · This div is technically a child of the flex parent. And what you can do is this new style called flex one, introducing this new style. And what it lets you do is actually take up all of the leftover space in the parent. Right? Notice that this red div actually grew to take up the remaining space which is pretty useful. I think the key to remember is you need to use flex one on the child.

**2:37:00** · Right? Flex one if it's applied to a child it's going to make that child take up all of the remaining space within the parent. So now I can start working on centering things. I'll make this child itself a flex which means I can do things like justify center.

**2:37:17** · Nice. And even item center.

**2:37:21** · So it should be smack in the middle.

**2:37:23** · Nice. I'll go ahead and make this fugal text much larger. So I'll say class name. I'll use like a maybe a 6XL. So text 6XL. And I want to start incorporating my orange color. So I'm going to make this giant center region a lighter orange. So I'll say BG orange 100.

**2:37:44** · I'll make the title text maybe some darker orange. So text orange. Let's go for 500.

**2:37:53** · See how that looks. That looks pretty good to me. So here I have my frugal logo. And what I want to do is start working on that search bar. Right? If I look at the demo, we have a nice big search bar right below our logo. So I'll start doing that. Back into the search.

**2:38:08** · What I'll do is I'll set up a div. I'll just put some placeholder inside. and I'll say search.

**2:38:14** · And so far the position of this is off, right? I definitely want the search bar to be below the logo. So I want to stack these two vertically. Right now they're to the left and right of each other cuz their parent is a flex. So that's a flex row by default. But I want to make them a column. So I'll say flex call. Now they stack nicely. Now I can start working on styling this one up a little bit. So, what I'll do is I'll start to give this uh search div like a different background color so I could really see it. I'll use a type of orange. Maybe I'll use BG. I'll say orange. I'll go 200.

**2:38:46** · Should be a little darker than the background. I'll also give it a border. So, I'll say border border. Orange 300. So, it has a border kind of going around it. I'll also want to add some margin below the logo. That way it's not too close to my search bar here. So I could say MB4.

**2:39:10** · Nice. Looks a little better. And now I can start establishing the correct size for this search bar. So I want to start by adding some padding. So what I'll do is can say maybe P4. So that's going to be the space within the search box here.

**2:39:25** · So that's looking pretty good. I want to start rounding things fully. So I could do rounded full. That'll give me the semicircles at the end. Nice. And so unfortunately right now if you actually started to remove the placeholder text inside that would actually shrink the size of your bar. Right? So instead of that what I want to do is give it a fixed width. Right? So over here I could use my W values. Let's start with like W80. It's a pretty large width. Seems pretty acceptable for a search bar. And maybe I'll even drop my padding a tiny bit. Get a little narrower bar.

**2:39:58** · I kind of like how that looks. So, I want to add a nice icon in the left of this search bar. So, I'm going to look for a magnifying glass is probably the best for search. And again, you can kind of flip through the different styles you have for this magnifying glass. I'm going to go for like the solid one. It's nice and thick. Hop back into my code.

**2:40:20** · I'm going to drop that right inside of the div that makes up the search bar shape. So, there's my magnifying glass.

**2:40:26** · Be sure to change it from class to class name. And I want like a bigger magnifying glass. So I'll say text.

**2:40:33** · Let's go large. Kind of trial and error here. Maybe even larger. Let's go XL.

**2:40:39** · And I definitely want to fix the color of that. So I'll say text orange for this icon to change the icon color. And I want to make it maybe like a 400.

**2:40:51** · That looks pretty good to me. I want to tweak the spacing of the icon a little bit. So I'm going to give it a margin left so it's a little further away from the border.

**2:40:59** · So it moves over a little bit. Cool. I think I like the way that that looks.

**2:41:03** · While we're here working on this search bar, one thing I also want to show you is introduce the input tag. So can go ahead and add a input tag right inside of the search bar div. And you can self-close it.

**2:41:17** · And if you do that, you're not going to see much but this white box, but it has the upshot of you can actually type into it. Later on in the course, we're going to actually make a text input like this more usable, meaning the user can actually enter and do stuff with it later on. But for now, by default, it's just something you can type inside. I just want to work on focusing on the style of things here. So, I should definitely not make the input have a white background. That's what it gets by default. So, I'm going to give it a class name. So, I'll fix the background color here. I'll go for the same background color so it kind of blends right in.

**2:41:48** · Uh, one thing that we could practice here though is if you click on the search bar, notice that it's actually not the remaining width of the actual div here, that round div. I want it to grow to take up all of the remaining space here. So, what you could do is make the outer div or the parent, make that a flex, which won't change too much when you do this, right? It's still going to be a flex row. Right now, the children are the icon and the input that's actually to the right of it.

**2:42:16** · If you want the input to take all of the remaining space, like we just said previously, you can make the child a flex one.

**2:42:27** · And now if I click on the input, notice how it takes up all of the remaining space. And if you wanted to, you can still adjust it by giving it some margin. So I'll say MX1.

**2:42:37** · Now there's more space to the left and right of the input. I'll make it much larger so you can really see like MX4.

**2:42:44** · A lot of space now. All right. So, I think my title and search bar itself are done, but I do want to work on adding just those two buttons. I'm going to make them that nice violet color. So, that's going to be below the search bar.

**2:42:57** · So, I'll keep that in mind.

**2:43:00** · So, this is the search bar div. Below that, I'll put a container for those two buttons. So, I'll start laying down my two buttons. I'll say fugal search and then separately, you know, I'll say image search. Feel free to say whatever you want on these buttons. We're just practicing the style here, right?

**2:43:20** · So, what I'll do is I'll go ahead and add some class names to these.

**2:43:26** · I'm going to go for some rounded corners here. So, I'll say maybe rounded medium.

**2:43:32** · I'll give them background color. Maybe BG violet 200.

**2:43:38** · Then also give them a violet text color.

**2:43:40** · So, say text violet 400.

**2:43:45** · Nice. And of course, I want to give them some padding. So maybe px 4, py 2.

**2:43:53** · Nice. Get some nice large buttons. Of course, you want to add some margin.

**2:43:57** · That way they're not too close. So the first thing I want to do is I want to make sure that these buttons aren't too close to the search bar above them. So for the parent, which is right here, I'll give them some margin top. So empty. Let's go with four. Four is usually a good value. Nice. Now I want to add some margin around each button.

**2:44:17** · So around each button I can go ahead and add maybe margin one. That might be some pretty good spacing. Nice. I think that wraps up the center section of my UI.

**2:44:32** · So for my footer design, I'm going to follow the demo pretty closely. So I'm going to have I think three sections within the footer going from left to right. I'm also going to include a little link which I'll show you how to do in a moment. So let's go ahead and establish that just using some more flex tiles. So I'll create those three sections first. One of them is just going to say this site is not real. I'll have a middle section just saying what I made the site with. So I'll say made with love and tailwind CSS.

**2:45:08** · And then finally, I'll just go ahead and put my name here, right? So, I'll say by Alvin Sublan.

**2:45:15** · So, I'll get my three sections. By default, they all stack vertically. Not quite what I want. Of course, you know the deal. Now, you could just use some flex, right? So, I'll make this a flex row by just saying flex. Be sure to add that flex to the parent, right? If you add flex to the parent, that will change the position of the children. And now, I want to use something useful like justify between. It'll give me a lot of space between these three sections.

**2:45:39** · Nice. And what I'll do is I'll start to style things up a tiny bit. So, I'll make the background color of this bottom footer. I'll make it maybe like a violet 100.

**2:45:50** · And I'll make all of the text make it violet 400. I want to add some padding so these elements can breathe. So, I'm going to say maybe P2. Padding to all around. I'm adding this padding to the parent. So that's why there's padding above as well as below and also at the far left and far right. So I'll spice things up a little bit here. Instead of saying the word love, I'm going to use a nice little heart so I get to practice more of my font awesome icons. So I'll look for a heart and a bunch of different hearts.

**2:46:23** · I'll go for the filledin heart, but maybe like a little duo tone one. So this is like a really dark heart. This will give me a really light heart. So maybe I'll copy that and I'll bring it into my code here. I'll replace this word. And that'll actually already show up kind of in the flow of the text, which is pretty good. I do want to change this to a class name, though. So I want to change the color of this heart. So I'll go for like a red, which probably will make it look a little pink here.

**2:46:53** · So I'll say text red. Let's go 600.

**2:47:00** · just gives me a little different contrast there. Nice. And I think finally, what I also want to kind of trickle in here, just another tag usage, I'll go ahead and show you how to add a link into your code. This will be our first type of link. It's really just going to be a new type of tag for us.

**2:47:17** · So, notice, by the way, when I hit a new line within my HTML, for the most part, that actually won't affect how things render on the screen, right? Notice that Tailwind CSS is still next to the word and, right? That's why we can go ahead and format our code in any way we like.

**2:47:32** · Hopefully, we format it in a readable way. But what I want to do here is insert a link. To do that, use the A tag. Stands for anchor. So, is going to be a pair tag. I'm going to put Tailwind CSS within.

**2:47:45** · So, nothing changes too much except if you add the right props to this anchor tag, to this a tag, you get a link to some external source. So, for example, I'm going to give this an href. And here I can put some URL. So, for example, I'm just going to link to the uh Tailwind CSS documentation page. So, that'll just be Tailwind CSS.com.

**2:48:08** · Right. What you also want to be sure to do is probably give it another prop additionally. So, href is going to be the URL that you're going to navigate to. You also want to do target. What target does is let you decide how you want this link to open. I think because you're already in a website, this should probably open a new tab. So you can say underscore blank. This means open up tailwind CSS in a new tab or new window.

**2:48:34** · And don't worry about memorizing these things right now. We're going to get a lot of practice with them and they're really easy to look up. So from here, if I actually hover over the Tailwind CSS element right now, I do get a little hand pointer, which means I can click on it, and when I click on it, it will open my new tab. Nice. So, let's hop back to my old tab here. I want to go ahead and style things up a little better.

**2:48:59** · Tailwind CSS, for the most part, doesn't even look that clickable. You probably should add some different styles to it, right? So maybe the first thing I'll do is I want to go ahead and maybe change the color of it a little bit. So you got a class name to the anchor tag. That's all good. And I'll make it maybe darker.

**2:49:16** · So I'll say text violet. Let's go much darker. Let's go 500.

**2:49:23** · Nice. I think I want to add some margin to the left and right of this as well.

**2:49:27** · So I'll say MX maybe two. Give it some nice space. And I think I also want to underline this text. You can say just underline in tailwind CSS. And of course, it's going to underline it. So now it looks like something that's super duper uh clickable. All right, programmers. That's all I got for this search page exercise. What I want you to do is definitely take a moment, get comfortable experimenting and using your different Tailwind flex classes as well as the icons I just showed you.

**2:49:52** · And in the next module, we're actually going to hop back into some hardcore React development. and we're going to be able to use all of these styling cues that we just learned to establish a really nice modern UI. I'll see you there.

### Event Handling & State Lecture

**2:50:08** · Hey programmers, welcome to our intro to state module. In this module, React is going to start to get really interesting. What we're going to do is learn how to make our React applications more dynamic. And we're going to do this using a new concept called state. What we're also going to do is learn about how we could handle and respond to different events that occur in our application. for example, when the user clicks on a button. And with that, let's jump right in and talk about buttons.

**2:50:32** · So, let's say we had a app component that consisted of a single button. If you look closely at this button, you'll notice something new. I pass in an onclick prop to it. On click is going to be a special reserved prop in React.

**2:50:44** · What you'll also notice is that this onclick prop is special because it takes in a function. Right? So, previously we've seen props of different types. We had props that were numbers, strings, and booleans. Now we're dealing with props that are going to be functions, which is totally fine. Here I pass in an arrow function as the argument. This onclick prop is useful because it lets us handle click events on the button. In other words, if someone were to click this button, then I would be able to see this output in my console. It would literally print out cool and then the button was just clicked. And this would occur every time the button is clicked.

**2:51:17** · So you can imagine every time we click the button, we execute all of the code within the onclick prop. We'll be able to implement this pattern and practice it in the next exercise, but for now, I want to talk about things in more of a high level. So, let's take a look at just the button here. And like we just said, this button is taking in an onclick prop. And it's really important that we remember that this onclick prop should be passed a function. And there are two ways to really define the function that you're passing in. In this first button, the onclick prop is an arrow function that has multiple lines.

**2:51:47** · But you can also write a different version if you have an arrow function that's just a single line. Looking at these two different buttons, they both have an on click prop, but notice how the arrow functions are written. For the first one, I open up some curly braces for the body of the function. That lets me write multiple statements inside of that function. But for the second button, I don't use any curly braces.

**2:52:08** · That means I can only write a single statement inside. And that's just useful in case you only want to write a single line in your arrow function. To summarize, the onclick prop is one way that we can implement event handling in React. The on click is representative of an event in React. Events are things like on click, on mouse over, on scroll, and much much more. For now, we're just going to focus on on click, and we'll cover the rest later on in the course.

**2:52:34** · So, we call this concept event handling, which means that the function that we pass into the onclick prop, we can refer to that as the event handler. It's going to be the function that executes when the event occurs.

**2:52:47** · So that's an example of event handling in React. Now let's talk about the concept of state. State is not something specific or exclusive to React. State exists in many other frameworks and languages and overall it's a general programming concept. The way I think about state is it's a value that changes over time. The key detail here is I'm talking about a change. So my state is going to be a value that starts out as one thing and then it can be updated to something else later on.

**2:53:14** · This is going to be useful because it's going to help me implement React applications that are dynamic. In other words, they change over time. So, let's take a look at a simple app. So, let's say I start with just a plain old app component. And the first thing we'll need to do in React is to import use state from React. So, this is a built-in function in the React library. And we import it in this way.

**2:53:37** · Don't get hung up on all of the new syntax here right now. We'll go over this in detail in the next exercise. So I'm importing this special ustate function from the React module. What I can do is call it inside of my component. Looking at ustate over here, it's clear that this is a function because we call it with parenthesis.

**2:53:56** · We're passing it an argument. The argument that you pass into ustate is going to be the default value. It's going to be what your state is going to begin as. You'll notice that the ustate function also returns two things. We name them message and set message. In this example, the first thing it returns is going to be the current value of the state. It's really going to be a variable that contains the current value. And the second thing we get back is a setter function. This is going to be a function that lets us update the state later on.

**2:54:26** · All right, let's keep fleshing out this app component. Right now, we're not returning anything or rendering anything on the screen. So, let's say we added that into the mix.

**2:54:36** · So, here I'm just returning a simple div that contains the message. Notice that the message that I'm rendering on the screen is the message variable from my state because my state is initialized and it's defaulted to the string press a button. I would see that in my initial output here. Right? So in the bottom right I have a white window that represents how this app component would appear and this component would render a div that contains press a button.

**2:55:04** · So far this is nothing new. We're really just using message as a variable that contains some string. But let's say I made things more interesting. Let's add two buttons into the mix. And these are buttons that have an onclick prop like previously. So in the bottom right, I've updated what our UI would appear as.

**2:55:22** · Notice that I have two buttons. The first one is labeled one and it corresponds to this.

**2:55:28** · Now what would happen if I actually click the one button? Well, if I click the one button, I know that I would be executing its onclick prop. So I would be running the function that's passed in to the onclick prop for this button one.

**2:55:42** · And inside of the arrow function here, it looks like I'm going to call set message. And I'm passing in a new value.

**2:55:49** · Remember that set message is the second thing you get back from use state above.

**2:55:54** · And what it does is set message lets you update the state to a new value. Right now I'm setting message to be the string hello. So when I click the button, it's going to change the message. It's no longer going to say press a button. It's now going to say hello, right? I have a new state value and my component is rerendering.

**2:56:15** · Nice. Now, let's say we went ahead and clicked button two. Well, a similar thing would happen. I know that when I click button two, I'm going to be executing the onclick handler for button two, which means I'm going to set the message to be a different string. This time, I'm going to set the message to be goodbye. And that would rerender my component with the new message on the screen. So here we're combining these two concepts of event handling and state to create a dynamic UI. So looking at the first thing we imported at the top, we imported this ustate function from React, right?

**2:56:45** · It's probably the most common function that you're going to take out of the React library. We refer to ustate as one of the hooks in React.

**2:56:54** · All of your hooks are built-in functions in React and they start with the word use. So that's an easy way to identify them. So right now we talked about use state. There are other ones like use effect, use callback, and much much more. For now, we'll just focus on use state.

### Click Event Exercise

**2:57:09** · All right, so that wraps up our highle overview of event handling and state.

**2:57:13** · And don't worry if you're feeling a little overwhelmed. We're going to be able to practice these concepts coming up next. I'll see you there.

**2:57:23** · Hey programmers, Alvin here. Welcome to our first exercise using state. In this exercise, what I want to do is show you how to handle click events. So here I have opened a demo. In other words, this is what we're going to be building over the course of this exercise. We're going to be building this very simple UI, and it's going to force us to use these new concepts for us in React, including state as well as event handling. So, when you open up the demo, you're going to see this initial message of hello world, as well as these three different buttons. When you click on one of the buttons, that will actually change the message on the screen.

**2:57:52** · All right, so that's what we're going to be building for this one. I'll see you in the video walkthroughs where I'll break this down for you.

**2:58:01** · So, let's start with phase zero. Phase 0 is just going to be a little warm-up where we just create the initial layout for this one. So, looking at the demo, you just want to start by centering some UI where you have some placeholder message as well as three buttons. So, I'll jump right in. I know I'm going to need to stack the message above the three buttons. So, I'm going to start by making the outermost div a flex call because I know that a column can stack vertically. So, I'm going to say flex flex call. And I'll throw in my initial message. I'll just say hello world.

**2:58:28** · And I'll also throw in a div containing my three buttons. Inside of this bud container, I'll just put down my three buttons. I'll just call them one, two, and three. So, so far I have this very plain looking UI. Let me start by centering things. So, for the flex flex call over here for the outermost container, I'm going to start by centering things, right? So if I do a items center, that'll bring it to the center horizontally, but I also want to bring it to the center vertically.

**2:58:58** · I know I can do that using justify center, but it's not going to work yet because the parent is not actually the full height of the screen. So I can show you what I'm talking about by adding a black border.

**2:59:12** · Make it border black. We can see that the entire app is actually only this top region. I want to stretch out this app to the full height of the screen. So I can just say h screen. That'll bring things to the full height. And since I'm centering things vertically, I have my UI in the very middle of the screen. So that's looking good. I'll just drop these black borders. So far, we're just reviewing and warming up with our classic Tailwind CSS. So let me go ahead and at least style up the message here.

**2:59:41** · I'm going to make it a little bigger. So I'll say text maybe 3 XL. And I'll make it a gray color. I'll use text stone.

**2:59:50** · I'll use stone 400. That'll be my hello world. Now, I want to style up my three buttons. I'll give them a very classic button look for us. So, I'll start by adding some margin around these buttons.

**3:00:00** · I'll say maybe margin 2. I'll give them some padding. Maybe px4 and py 2. And then I'll make their text white. And I want to give them all different background colors. So, feel free to choose your own colors for this.

**3:00:15** · I'll just switch up my colors. So, I'll start by making them all green. And I'll do rounded medium.

**3:00:22** · Nice. I could switch up my colors. Maybe I'll go green. I'll go red. And I'll go violet.

**3:00:29** · So, this is looking pretty good. I'm just going to go ahead and give myself a little margin top so that way I have some space between the hello world and my three buttons. So, I'll put a margin top on the container of the buttons.

**3:00:40** · Maybe MT4. We'll be good to go. All right. All right, I think that wraps up phase zero. Just a little warm-up. In the next phase, of course, we'll start implementing our new React concepts.

**3:00:54** · Let's keep it rolling into the next phase. So, you'll notice that if you look at the completed demo, whenever we click one of the buttons, we should be changing the message string on the screen. Whenever you want to have anything change over time in React, you're probably going to use state. So, it's going to be a new concept for us.

**3:01:10** · So, get my output. The first thing I want to do is incorporate some state into my app component. So what you want to do is actually import something out of the React library. You can say import. You want to use some destructuring curly braces. You want to grab this thing called ustate. We're going to grab it from React. So we're importing ustate from React. We call ustate a type of hook. Hooks are functions in React that help us accomplish some additional uh functionality inside of our components.

**3:01:36** · Ustate is probably the most common hook to use. And the way you want to actually wield it inside of your component is the very top of your component. What you want to do is call ustate. So you'll notice that ustate is really just a special type of function, right? And inside of the call to ustate, you want to pass in an argument. This argument should be the default value of your state. So I'm going to make my state my message. It's going to be a type of string. So let's say I wanted to make my message Alvin was here, right?

**3:02:02** · So, so far this is just a plain old uh function call. UATE is going to return us two things and you can dstructure them using the array destructure syntax. It's going to give you back your current state value as well as a function that you can use to set the state. So, right now I'm going to call them val and set val. So, let's slow down here. Use state is returning to us two things. It's going to give us back the current value of our state as well as a setter function that we can use to update that state.

**3:02:34** · And if you're unfamiliar with this type of syntax where we have some square brackets uh to the left of a variable assignment, this isn't actually specific to React. This is just plain old uh JavaScript syntax. So let's say I was going to give you a quick aside. Maybe you're not familiar with that syntax. If you had an array of things, so I'll say my array is going to be an array of one and two and maybe also three. What you could do is dstructure elements out of that array.

**3:03:03** · In other words, I can create variables and call it first and second and grab that out of the array. Now, if I actually can print out the first and second variables, they would correspond to the first two elements of the array.

**3:03:20** · of course. So notice I've printed out one and two. So this is really just shorthand syntax, right? What it does is it lets us unpack elements of an array and store them inside of some quick variables. That's the same case for this ustate call. Ustate is actually returning to us an array of two things.

**3:03:39** · We're just dstructuring those two things and storing them into two variables. One called val, another called set val. So we'll go back a little bit, close my console here.

**3:03:50** · So now that I have um this value and set value, let's just focus on the first argument here. Let's just focus on the val. So right now I'm just going to console.log what that value is. And I'm going to see this print statement inside of my console of course. And I see at the very bottom here it says Alvin was here. So it looks like this val argument is just going to be the initial thing I passed inside of ustate, right? What's great is I can actually use this value uh to render the message on the screen.

**3:04:19** · So instead of just hard- coding hello world over here, I'm going to evaluate to val. If I take a look at my code right now, it's just saying literally val, right? And you know this trick whenever you want to actually evaluate a variable into its corresponding value and render it on the screen, you need to put it in some curly braces. So val is just a variable. Now I'm rendering the message Alvin was here. Of course, that corresponds to what I passed in to use state over here. So, if I made this high, now my message would initialize to just high.

**3:04:51** · So, so far we haven't accomplished much because we're not actually using the setter function yet for our state, right? Really state is only useful if you're able to change it over time. So, here is where we bring things together. What you want to do is for your buttons, you want to pass in an additional prop. So, you want to pass in a prop called on click. And what you want to do is open up some curly braces.

**3:05:14** · And inside those curly braces, you need to be sure you pass in a function. So I'm going to use the arrow function syntax here. So if you see me highlight this exact code here, this is just some function syntax. I have another set of curly brackets because I need to evaluate that function, right? And so inside of this onclick function, for now, I'm just going to console.log click.

**3:05:37** · And notice that I passed in this onclick prop for the first button, the button that has the label one. So now if I actually open up my console, give myself room a little bit here. And I'm going to click on the one button. Notice that it will print out that message click. And that'll be true every time I actually click that one button.

**3:05:56** · When this button is clicked, we're going to execute the function we passed in for the on click. In this case, just console log a message. But instead of doing that, what I want to do is actually change my state. So what I'll do here instead is call my set value function, which is the second argument I got from ustate. This is going to help us update the state value. So I'm going to call set val and I'm going to make it the string by. So now I wonder what will happen when I actually click that first button. Right now my message says hi and that corresponds to the default state I passed in to you state here.

**3:06:27** · But when I click on the one button, now my message changes to buy. Right? What's happening here is when we call the setter function, it's going to rerender this component. So basically re-evaluate this function. And now the new value that I take in is going to be by right. So it's no longer high in this case. So now when the user clicks on a button, they're actually changing what's on the screen here. So let's take that further and I'll add a similar event handler for this second button. I'm just going to copy this prop.

**3:06:58** · So, you're passing in the on click prop and you're being sure to pass in an arrow function, right? And inside, you usually want to call one of your setter functions, right? So, I'm calling set value. I'm going to change my message here to yay. And I'll give my page a hard refresh. Notice that whenever I refresh my page fully, I'm going to start with the default value of my state, which is up here on line four, right? It's just going to be high. Now when I click on one, I'm calling the onclick handler for the first button and I'm setting the value to buy, right?

**3:07:31** · Which is why I see it on the screen. And when that happens, what's really going to happen in React is this app component, which is really just a function, is going to re-execute and it's going to have a new value in this variable here, right? The val is going to be by, which means when I actually want to render what's on the screen on line 8, that val is literally the string by. And the same thing applies any other time I click it. If I click the two button, that should change the message to yay, which means that again the component is rerendering and now my val is yay. So I see it on the screen.

**3:08:00** · All right, let me implement the click handler for my last button here, but I'll show you some shorthand that you could use if you like. So I just copy and pasted the same onclick prop. I'm sure to pass in an arrow function that contains a call to my setter, right? And I'm going to change the message here.

**3:08:20** · I'm going to say woo.

**3:08:22** · So, let me just test and make sure this works. So, if I refresh, I should have my default message of hi. And there it is. One should give me by. Two should give me yay. Three should give me woo.

**3:08:33** · And I can, of course, keep clicking these different buttons to change the message. So, for this onclick syntax over here, you always want to pass in some function, right? And I'm definitely passing in an arrow function. This is actually the multi-line arrow function syntax. So if I wanted to do multiple things, let's say I wanted to set the value to woo, but also console.log, you clicked button three.

**3:08:54** · If I actually click button three now, right, it changes the message on the screen, but also prints out this additional console.log, you're able to do that because you have multiple lines inside of your onclick function here, right? But if you only had a single line like this, what you could do is actually drop the curly braces. So I'm going to drop the curly braces that wrap the body of the function. I can write everything on one line like so. And you want to get rid of that semicolon here.

**3:09:23** · So this is actually another way you can write your click handler. You're still passing in an arrow function. It just so happens that that arrow function is a single line, right? So you don't need to open up some additional curies here. And so if I actually test this out, one works, two works, and three still works, right?

**3:09:42** · It's still setting my value to be woo.

**3:09:46** · So whenever your onclick handler just needs to execute a single line, you can just use this single line arrow function syntax. So this is correct. A very common mistake I see students make is sometimes it'll actually just call a setter immediately and pass that into the onclick which isn't going to work.

**3:10:02** · So if I try to refresh my page, you're going to get some nasty errors. So when you pass in an onclick prop, you want to be sure that you pass in a function that itself calls your setter, right? So this is incorrect here. you're calling your setter directly, right? You really want to write it in this way, right? Where you pass in a function that in turn is going to call your setter. It's a small difference visually, but it's really important in terms of implementing a correct UI. So, I'll fix this code. What I want to do is pass in function that in turn will call set value.

**3:10:32** · So, a few key takeaways for this exploration. When you call the ustate hook, you could pass in some argument. That argument is going to correspond to the default value of your state. Here, my default value of my state is a string high. So whenever I do a hard refresh of the page, I see high.

**3:10:50** · The use state hook is going to return to you two things that we typically dstructure out using the array destructure syntax. Those two things are going to be the current value of the state as well as a setter function that we can use to update that state whenever we want. And you can name these variables whatever you want. I just named them val to correspond to value.

**3:11:09** · But you want to typically write something more specific. So I know that this state value corresponds to like the message I see on the screen. So I'd probably call it message instead. And I want to also correspond this with set message.

**3:11:23** · Cool. I can refactor this to say message. Now that I renamed the setter to set message, instead of set val, I should say set message everywhere. Let me test this UI once again. And it's still working. You'll see this pattern all over React code. Whenever someone calls you state, they're going to dstructure two things. It's going to be some value as well as the setter for that value. So let's say for example, you had another piece of state that was going to be like someone's age.

**3:11:51** · What you would do is probably call the first argument here the age and the second argument here set age. So value and set value is going to be a very common pattern you see all over your React code. All right, that's all I got for this one. What I want you to do is take your time and make sure you're able to implement this UI. These concepts of state and click handling are pretty new for us. So it's okay if you have to reference the solution code as well as the video walkthrough a couple of times.

### Conditional Rendering Exercise

**3:12:14** · We're going to get a lot more practice on this in the next one.

**3:12:21** · Hey programmers, Alvin here. Right now I want to keep it rolling by working through this conditional rendering exercise. So what I want to do is just give you a preview what we're going to be building today. So we're going to have to build three different widgets.

**3:12:32** · These three widgets look all very similar except when we interact with them. So if I click on the first widget, it makes an icon looks like a smiley face appear. And if I click it again, it'll actually hide that same icon.

**3:12:43** · Looking at the second widget, if I click it, it actually changes the button to orange. If I click it again, it goes back to blue. And I can keep clicking on the button to change the color of it.

**3:12:52** · Looking at the third widget, actually behaves quite similar to the very first widget in that it makes an icon appear.

**3:12:57** · However, we're going to implement this third widget using some different syntax. to implement these three widgets and make them interactive. We are going to use state inside of them, but we're going to use that state in different ways to accomplish these different features.

**3:13:13** · All right, so let's start by working on the first widget. Going to start by turning on my dev server. What we want to do is create a different component for every widget we need. So overall, we're going to create three widgets over time. So I'll create my first one. Give myself a classic file here. I'll call it widget one. Similar to the text instructions for today. And I'm going to start by defining this component.

**3:13:36** · So all things that you're used to creating a component with the same name as the file. Be sure to export default that component. And for now I'm just going to put a placeholder. I'm going to return a div that says first.

**3:13:50** · I want to make sure I can import and render this inside of my app. So at tippy top I'm going to import widget one from dot slash widget one and then within this uh app div I'm going to render that component. I need to be sure to render the widget one component and I'll see what I get. So there I see first coming from that implementation of widget one. I want to start by styling things up.

**3:14:15** · If I compare my output to the demo, well it looks like I need to center my UI in the middle of the screen at least horizontally. So, I'll work on that. I can do that by adding some flex dials to the parent. I know that this div is going to wrap all of my three widgets.

**3:14:32** · So, I'll give this one a flex flex call because I know eventually I'm going to stack these three widgets on top of each other and I want to center horizontally.

**3:14:40** · So, I can say items center. So, I should bring first right in the middle of the screen. Now, I can just focus on working on this very first widget. So, I want to mimic some of the styles here. So, we can bang this out. So, I'll give this a light green background. I can say BG green 100. And I'll use a border. Say border. Border green. And we'll make it a little darker. We'll make it 300. See what that looks like. I want to add some padding all around. So, I'll say P4.

**3:15:10** · And for a good measure, I want to round the corners as well. I'll do rounded large. I want to add some space around it. So, I probably ought to do some margin. Margin four as well. So, I know I need to put a nice big button in the middle of this widget. So, I can create that button over here. I'll use an actual button element for this. And I'll put click me inside. I want to give it some button styles. Right.

**3:15:36** · So, I'll give this px4 maybe py2. I'll make the background color. I'll make it some dark teal. And I'll make the text white. Feel free to adjust the styles of your button and components. I'm just going to follow the demo pretty closely.

**3:15:52** · So, I'll make this rounded full.

**3:15:54** · Awesome. So far, I have a green background with another teal button right inside of it. And so, what I want to do, just like the demo, is have uh this first widget make something appear and disappear. And so, the bottom line is we're definitely going to need some React state to implement this because over time our component is undergoing a change, right? Looks like it has a state where it shows the happy face and another state where it does not show the happy face. So, I'm going to need to use the state hook for this.

**3:16:24** · So, inside of widget one, I'm going to import the use state hook just like we did in previous lessons. Be sure to dstructure it out of the React library. So, import state from React. Then, I can call it at the tippy top of my component and call ustate.

**3:16:43** · What I have to do is first decide what type I want this state to be. This should be boolean state, right? So I'm going to start by initializing the state to false. I know a boolean is a good choice for the state here because I have like two modes, right? I either show the icon or I don't show the icon. I know that a boolean is really perfect to represent those two different scenarios.

**3:17:02** · Like we said previously, use state is going to return to you two things. It's going to give you your current state value. I'm going to call it show icon.

**3:17:10** · And it's also going to give you a setter function that you can use to update that state. I'm going to call that set show icon. Nice. And so what I'll do is let me first choose a proper icon here. So here I am on the font awesome page. You can feel free to choose a different icon if you like. I'm going to choose this awesome face. So I'll copy this and I'll bring it into my code. So I'll just put it above the button. Paste in that icon.

**3:17:35** · Be sure to change the icon tag from a class to a class name just like we saw previously. And I can start adjusting the styles here. So I think I want the icon to also be that nice uh teal color.

**3:17:47** · So I'll make this text teal 500. And I'll make it much larger 3XL.

**3:17:55** · And along with that, I want to make this icon appear right above the button. So what I can do is make the container or the parent a flex call. So that'll be this green div here. I can say flex flex call. So that should stack it. And I want to make sure that they appear in the middle line here. So I can say items center.

**3:18:20** · And for good measure, I'll probably add some margin here. Maybe just some margin bottom below the icon. That way it has a gap between the actual button. So margin bottom four. Give me a little more room to breathe there. Nice. So right now the icon always shows up, right? And the button does nothing. So now what I want to do is figure out how I can control whether or not this icon appears. I can use my state to do that, right? And so what you want to do is actually write a JavaScript expression inside this return value. And you want to use a turnary operator.

**3:18:52** · So what I could say is, hey, if the show icon state if it's true, then I want to render the icon. So moving the icon over here otherwise. So colon otherwise I want to render nothing. So I'm going to render null.

**3:19:11** · So let's see what this looks like at the start. It looks like I don't display the icon. That's because my state is defaulted to false. If I manually hardcoded to true now the icon should show up, right? So I'm using that turnary syntax here which isn't actually specific uh to React. It's really just some JavaScript syntax. So I know I want to go nice and slow here. So I'm going to make sure that you understand the syntax. Some people get away with never using a turnar expression. Maybe they just use if statements. So what I can do is let's say I had some variable.

**3:19:41** · We'll say result and I wrote a turnary expression. So I say hey if true then I want the result to be yes otherwise I want it to be no. So because this expression is literally true, result is definitely going to be yes.

**3:20:04** · So I'll take a look at that. I see yes on the screen. Now if I make this false, the result variable is going to evaluate to no. So think of a turning expression.

**3:20:14** · It's just a shorthand way to write a simple if else statement. Right? If your condition evaluates to true, then you're going to evaluate the entire expression to this first clause. Right? If the condition is false, then you're going to evaluate the entire expression to this second clause.

**3:20:31** · It's like an if or else statement. And so with that in mind, if you look at how I use this turnary uh in my render, if the show icon variable, if it's true, then I'm going to render the icon.

**3:20:44** · Otherwise, I'm going to render null. In JavaScript, null is the value we use to represent emptiness or nothingness.

**3:20:51** · Cool. So, this isn't too useful until I actually have a way to update the state because I know the state controls whether or not I display the icon. So, like we did previously, why don't I add a click handler uh to this button. So, just to review, I'm going to pass in an on click prop. Be sure that it has a capital C for on click. I'm going to pass in an arrow function, right? And what this arrow function is going to do is it's going to set show icon to a different boolean. Let's say I set it uh to true, but I default it to false.

**3:21:23** · So if I do a hard refresh, I know I have a first render of my component here. I know that show icon is going to be false, which makes sense because I am not showing any icon in the output here, right? That's because show icon is false. And if it's false, that means I'm going to display null, which means show nothing over there. Cool. Now, as soon as I click the button, the icon's going to appear.

**3:21:51** · That's because when I click the button, this function is going to run, which means I set the show icon state to be true. So, that causes a rerender of my component. And now, the show icon variable really contains a true, which means that I'm going to display this icon. And I'm not going to do the null step here. Awesome. But now if I actually try to click the button again, nothing really happens because every time I click the button, I'm setting show icon to be true. But right now, it's already true. So it just stays true.

**3:22:22** · What I really want to do is toggle uh the boolean whenever I click it. So if it's currently true and I click it, I want to make it false. If it's currently false when I click it, I want to make it true, right? Show you a few ways you could do this. I could write just like a long if statement. So hey, if show icon, if it's already true, right? then I want to set it to be false.

**3:22:44** · Otherwise, I know that it's false. In which case, then I should set it to true. This just has the effect of setting it to the opposite. So, if I click it, every time it goes between showing and hiding the icon. So, this is a fine way to do it. You could also shorten up this code, right? Instead of running the long if else statement, we could just use some boolean operations.

**3:23:05** · What I can do is set show icon and I should set it to the opposite of what it currently is.

**3:23:13** · Nice. So all I'm doing is using the not operator on a boolean. Right? I know if show icon right now is true, then if I say not true, that evaluates to false.

**3:23:23** · So I'm setting it to false. On the flip side, let's say the current value of show icon is false. Then not false is the same as true. So I'm setting the state to be true. So this is a quicker way, more elegant way to actually flip between your boolean states. Like we said previously, because you only have a single line inside the body of your arrow function, you could even condense this further by dropping the curly braces.

**3:23:50** · So I think this would be a nice solution for that first widget.

**3:23:59** · So let's keep it rolling and work on widget two. So, what I'll do is I'll just go ahead and create that widget file. So, widget 2.jsx.

**3:24:08** · And for now, I'm just going to copy all of the code from widget one. It's going to start out very similar. I'll just adjust the variable names and also some of the styles here. So, I'm still going to use a boolean state. I'm going to remove the icon. I don't need any icon.

**3:24:23** · I'm going to make things have a sky background.

**3:24:28** · And then I'm going to make the button background for now. I'll just make it blue.

**3:24:35** · Cool. And I think I'll remove all the state. Let's actually start pretty simple here. So within my app, I'm going to render widget two.

**3:24:48** · So here comes widget two.

**3:24:51** · We'll see how things look. There. I have my second widget. Right now it doesn't do anything. So hopping into widget two.

**3:24:57** · What we want to do is click the button and have the color of the button change.

**3:25:02** · So, we're no longer making something appear or disappear. Instead, we want to conditionally change the style of it.

**3:25:08** · And so, I'm still going to have to use some state for this, right? So, this is good review. I know that this state is still going to be a boolean because I'm going to have two options. I'm want either a blue button or an orange button, right? So, I'm going to start it out equal to false. And I'll just name this state. We'll say toggle color and set toggle color. And so by now you're familiar with changing uh the color of this button, right? Right now it says background blue 500. I can make it orange by doing this. But I want that to happen dynamically, right? Whenever I click the button.

**3:25:38** · So the trick is to actually uh conditionally set the class name here. So I'm going to bring it back to blue.

**3:25:48** · And for this class name, I'm going to actually wrap it in curly braces. That way I can evaluate some JavaScript in between. I need to put some logic there.

**3:25:56** · What I can do is turn this string into a template string. So instead of double quotes, you want to use the back ticks.

**3:26:04** · So back tick would be um the shift value on the tildy key right on your keyboard.

**3:26:09** · It's not the single quote, it's the back tick key. For now, it still works exactly the same. But by using back ticks, you're able to write some additional syntax inside. So I'm going to refactor things here. I know I want to change the background color of this button. So I'm going to take this value out. I'm going to start to interpolate an expression. So I'm going to write dollar sign curly braces. I'm going to write the turn area here. Right? I'm going to check, hey, if toggle color is true. Uh then I'm going to make the background orange.

**3:26:41** · Otherwise, I'm going to make the background of this button blue.

**3:26:46** · So we'll see what we get. Give myself some room here.

**3:26:49** · So at the start it looks like my button is blue. That's because on the initial render toggle color is false. So this expression evaluates to false which means I take the blue. On the flip side, if it was true, then of course I would take the orange. And now the only thing I need to do is wire up my actual onclick handler. So like before, what I'll do is have an on click here. I'm going to pass an arrow function and I'm just going to set toggle color to the opposite of its current value. Right?

**3:27:19** · So I take the boolean and I negate it or take the opposite of it using the not operator and that will set it to the opposite. So now if I click this button, it flips back and forth between my two states which flips between the two colors I need.

**3:27:40** · So let's work on the third and final widget. Looking at the demo, the third widget behaves very similar to the first widget, right? Except I do want to show you how to implement this third widget using a slightly different logic. So probably start over here by actually creating widget 3.

**3:27:57** · So we'll render widget 3 here. I'll be sure to create this component and its file.

**3:28:03** · So over here, create my widget 3.jsx.

**3:28:08** · And for the most part, it's going to be very similar to widget one. So, I'm going to just copy and paste here. Take that liberty. Be sure to rename things though, right? So, this should be called widget three. And maybe I'll even adjust some of the styles, right? So, it looks a little different. So, instead of green, I'm going to use purple. And instead of teal, I'm going to use fuchsia. Let me make sure I spell fuchsia right.

**3:28:35** · That should be better. I think instead of the face icon, I do want to use that nice poop icon. So, I'll say faa poop here, the little poop icon. So, right now, the implementation of widget 3 is identical to widget one in that we're using a turnary expression to either show the icon or show null. Again, null means show nothing. But instead of doing this, you can write it another way. Instead, you can drop the turnary and get rid of the null. And you can use the and operator using the logical and operator.

**3:29:08** · You can say show icon and do this.

**3:29:12** · Right? So when show icon is true, you're actually going to display and render the icon. Right? If show icon is false, then you don't render the icon. So when it comes to displaying or hiding a component, you can either use a turnary with null or you can use just the and operator. It behaves identical.

### Counter Exercise

**3:29:31** · All right, programmers. This is all I got for this conditional rendering exercise. What I want you to do is practice this one before you hop into the next one where we're going to keep using these concepts of conditional rendering as well as our state.

**3:29:45** · Hey programmers, welcome back. What I want to do is go over what we're going to build for this counter project. So this is going to be a quick little project just reviewing what we learned previously about state and event handling in React. So the first thing we're going to do is go ahead and look at the finished demo. So overall, you're going to build a UI that looks just like this. This UI consists of two buttons and a number. The functionality here is you have these two buttons to either increase or decrease the count that is displayed on the screen. So obviously we're going to use things like state to actually display this changing number value as well as some click handlers for these two different buttons.

**3:30:21** · All right. So for phase here, we're just going to lay out our basic HTML skeleton and establish some pretty fundamental styles. So we'll get situated here. So, what I want to do is just spin up my dev server. So, I can do npm rundev in the terminal. That'll start my React development server. And I'll also want to be working inside of my app.jsx file.

**3:30:40** · So, I'll bring that over here.

**3:30:42** · So, we have some starter code here that just renders the text to-do. We're going to remove that for now. And so, like we say in the instructions for this one, really, we're just going to have three HTML tags on our screen. We're going to at least have two buttons and the number that we're displaying. So, let me start by laying down some buttons.

**3:31:00** · And I'll give them some inner text. I'll make the first button contain a minus and the next button contain a plus.

**3:31:08** · And between them, I eventually want to render some changing like dynamic number. I'll just hardcode the number zero right now.

**3:31:16** · Cool. What I want to do is of course have this look a little like the demo.

**3:31:19** · So, I want to have these different tags display left to right and really center them up. So just to review, we can do that by applying flex to the parent, right? So this outermost div that we return is the parent. As soon as I do flex, that means I'm going to put all of the children in a row. Right? By default, you're going to make it a flex row. And then from there, I want to actually center uh these things, these children horizontally. So I can say justify center using my flex rules.

**3:31:47** · And I also want to center these children vertically. But I do watch out though.

**3:31:55** · If you actually looked at the uh position of the outermost parent div here, I'll give it a border so I can see it. I'll say border border black. It by default does not take up the full height of the screen. So you can fix that by saying hc screen.

**3:32:10** · Nice. And that's useful because now I can actually center all of my things uh vertically with a items center.

**3:32:22** · Nice. So now things are centered up nicely. I'm going to start styling things up. So our buttons are going to be pretty basic, very flat material style. So we'll say class name. I'll start by increasing their size maybe. So I want to give it a text size. So I'll say text maybe 4 XL.

**3:32:41** · I'll increase the minus and plus. And I also want to give them some background colors. So I'll say bg. I'll make one of the buttons red and the other one green.

**3:32:49** · So I'll say like red 400.

**3:32:52** · And I'll also say green or you can even say emerald 400. I encourage you to look at the color specification in Tailwind CSS. Awesome. So, this looks pretty decent. One thing you'll notice um for certain characters like minus and plus, the characters actually have different widths. And so, um, maybe it'd be better to actually set a fixed width on these two different buttons because it's kind of strange how the minus button is actually less wide than the green plus button. So, what I can do is just be sure to set an equal with on both.

**3:33:23** · So, I can say W. You can use some of your values here. I'm going to do W8.

**3:33:31** · See how that looks? That's looking pretty symmetric to me. From there, I can do a rounded medium or we can do rounded large. Just rounding the corners there. So, that's looking pretty sharp. I'm going to make the symbols inside my buttons. I'll make them white. So, that's really just a text color. So, I'll go ahead and call these text white.

**3:33:55** · And I also want to add some space between um the inner number as well as the two buttons. So, I think for that, give myself some room here. What I could do is probably just add some margin to this this div over here. It'll add some space between the red and the green buttons, right? So, I'll say class name equals. I'll do margin all around. So, M of four.

**3:34:17** · I think with that, I also want to probably increase the size of this zero or this number. And maybe make it a different color. So, I'll make this text. We'll say neutral, which is a type of gray. Neutral 400. And I want to make all of my text, whether it's the minus, the zero, or the plus, 4 XL. So I'm going to actually copy this class. And you could remove it and just move it to an outer parent because I know in Tailwind CSS when I apply a class to the parent, it will also be applied to the children.

**3:34:49** · So I have that nice and big zero over here. Awesome. So in terms of our phase zero, I think that would establish our basic HTML skeleton as well as our styles.

**3:35:06** · All right. Right now I want to step through the code walkthrough for phase one. And so we established our basic HTML skeleton and CSS styles in phase zero. And now we want to work in our React state. So we'll go ahead and import the ustate hook. Going to use it a lot during this course from React.

**3:35:25** · What I want to do is call the hook at the very top of my file. So I'll say ustate. I'm going to give it a default value. Here I want my state value to be of number type. So I'm going to default it to zero. You can really default it to any number value that you want. I know that you state when I call it, it returns two things, right? I'm going to dstructure using the array syntax these two things, right? I'm going to grab the current state value and I'll call that my count as well as a setter function that can use to set the count. I'll call it set count.

**3:35:58** · Awesome. From here, I should be able to do, you know, some quick debugging. If I go into my preview here, now I want to actually use this state value to render some dynamic number, right? So, instead of the hard-coded zero, I'm going to actually render this count variable. So, I'm going to say count over here. It's still going to give me a zero right now because I've defaulted this count state to be zero. But if I change this now to something like 52, it should also start with that default value.

**3:36:26** · And the upshot now is I have access to this setter function which I can use to dynamically change um this count over time. So here's where I want to work in my onclick handlers. I want to apply these to my buttons. So I'll probably style this up a little bit.

**3:36:45** · I'll put my on click right on this button. It's a prop. And remember that for all of your event handlers, they always start with like on, right? And you need to pass in a function. So I'm going to pass in an arrow function right here. Right? What I could do is make it a full-bodied function by opening up some curly braces and then inside I can call set count. What I want to do is set count to some new value. What I'll do is take the current value and just subtract one from it. So for this onclick prop, I'm passing in an event handler which is a function.

**3:37:15** · And because I make it a function with some curly braces that lets me write multiple lines. So if I wanted to, I can do a bunch of other things here. Right? Because I just want a set state in this particular example.

**3:37:25** · You can make it a oneliner arrow function by dropping your curly braces, right? We've seen that previously in the course. When you drop your curly braces, you don't need to put the semicolon. So, this should work all the same. Nice. So, I'll just duplicate this for my other button.

**3:37:43** · Of course, instead of subtracting one from the current count, I want to increase the count by one. And I think I'll go ahead and default my state to zero uh for good measure. So we can go up as well as down. Awesome. And that's all there is to this project really. So before you go ahead and give this phase a shot on your own, uh you might notice that when I actually increment or decrement my state values, it is a case that the UI sort of shifts around a little bit. It's kind of janky.

**3:38:10** · And that's because these different numbers like four and three, they all take up different widths technically based on this font that I've defaulted to. So if you wanted to kind of uh not have that kind of shift in like the size of this innermost div, right? This div is growing to account for the thing inside of it, right? Especially when I have like a negative number. It's much larger than like zero, right? What I could do is just give it a fixed width, right? So I can say like width, I'll give it a large width like 20. See how that looks.

**3:38:42** · And by default, when you say width 20, now your uh text within or your count is going to start on the left, right? You can see that if you added like a border. I always love to add borders as I'm kind of debugging my styles because lets me see everything really clear.

**3:38:59** · There are a few ways you can fix that.

**3:39:00** · Like, you know, you can make it a flex and then do justify center, right?

**3:39:06** · That's one way you can fix that.

**3:39:09** · But if you don't need anything fancy and you're just storing some text within a div, you can also just say text center.

**3:39:16** · Really gives you the same behavior. So I'll use text center over here. I'll drop this border border black. And now no matter what, no matter what value our count is, I'm always going to show the div with a width of 20. So that means I have this nice uh consistent spacing around my number. I no longer have that jankiness in my UI. All right, programmers, that's all I got for this walkthrough. What I want you to do is now code up phase one on your own.

### Light Switch Exercise

**3:39:45** · Hey programmers, welcome back. Right now I want to review what we learned about state and event handling with this light switch project. And so let's jump right in over here. What we're going to do is start by looking at what we're going to build. So you want to always look at the demo when you start each of these projects. And here we have a completed project here. Notice that it just has a single button in the center. Looks like a light switch. And we have a dark background. When we click the button, it kind of turns the lights on. Really just changing the CSS or the style for our background as well as our button. And if you click the button again, it'll toggle between the on and off state.

**3:40:15** · So, like you can probably already tell, we're going to be using state as well as some event handling in this project.

**3:40:28** · All right, so let's get started on phase zero. What I want you to do is definitely watch the walkthrough for this phase before you code up this section on your own. We have some uh easy steps to complete in this phase zero. What we want to do is just set up some basic styles. In particular, we want to establish an initial background color as well as center our button in the middle. For now, we're going to ignore any functionality like adding state as well as any click handling. And so, what you want to do just like our previous projects is probably start by turning on your dev server. So, in the terminal below, you can do npm rundev.

**3:40:59** · And it'll take a moment to warm up here.

**3:41:02** · We should see some initial message here.

**3:41:04** · Here we're just seeing some starter to-do code. If you hop into your app JSX, which is the uh root component like we've seen previously, here we see the reason that the text is rendering here.

**3:41:14** · So, I'm going to get a little organized here. I'm going to split my screen. You can click this button in the top right.

**3:41:19** · I'm just going to drag this guy over.

**3:41:22** · All right. So, let's go ahead and uh just work on maybe just putting some rectangles in the middle of our screen.

**3:41:28** · And so what I'll do is inside of this outermost div, I'll go ahead and create some initial div. You're not going to be able to see it unless you put some text in it for now. So I'll just say hello.

**3:41:40** · And what I want to do is start by centering this horizontally as well as vertically. So recall like previously in the course, we want to use a lot of flex. And using Tailwind CSS, I can just say flex on the parent. I can say justify center. And this will help me center that hello div horizontally. And there you see it, right? What I want to do is now also center this hello child vertically. To do that, you want to do item center. Notice that these flex styles like always apply to the parent, right?

**3:42:12** · And they affect the positioning of the child. But you might notice that so far this hello div is not really centering vertically. That's because I have to take into account what the height of this parent div is. So, like I've taught you previously, I think it really helps to kind of wireframe things out. So, you want to add some borders.

**3:42:29** · So, for this parent, I'm going to do border. We'll say border red 400.

**3:42:35** · And it's pretty plain to see that it's really because our parent div isn't taking a large enough height to actually bring this hello in the true center of the screen. So, there are a few things you can do here. You can kind of just set the height. If you want to make it take up the height of the screen always, you can just do h screen.

**3:42:52** · Just some review. There we have it.

**3:42:54** · Right. So, now that we're getting some centering styles going on, I'm going to clean up some of these borders.

**3:43:02** · And let's take a look at our demo here.

**3:43:05** · We want to establish looks like a tall rectangle in the middle, right? So, that'll be this outermost div. And you might notice that in the demo that light switch is kind of composed of two different rectangles. One is lighter than the other. Kind of gives it like the effect of a shadow on like a light switch. So, I'm going to nest div here, and that'll be one of my rectangles.

**3:43:27** · What I should do, because there's not going to be any content within this div, I should give it probably some fixed height and width, right? So, you can play around with this if you like. What I recommend you do is actually go on Tailwind. So, Tailwind CSS. It's going to be a link to Tailwind like before inside of the prompt. You can go into the docs and I can just type in height.

**3:43:48** · Maybe I'm unfamiliar with how to designate the height. And there are a lot of different classes that you can use built in, right? So I'll play around with a few of these. So let's say I go for like an H16 and I'll go like W8. So that means a height of 16 and kind of like arbitrary units and a width of 8.

**3:44:05** · So I expect this rectangle to be taller than it is wide. I'm not going to see anything because I didn't give it a background color yet. So maybe I'll do BG.

**3:44:14** · I use like a slate 400. And again on the Tailwind docs, you can go ahead and look through your different colors. It's going to be linked inside of the readme as well. And so here I have my rectangle. I'm going to make it a little smaller. So maybe I'll do H8 and width six. Still looks like a rectangle. And that'll give me one of my pieces of the light switch. I'm going to put another rectangle, but maybe just um lighten the color a little bit. So I'll go for a slate. Maybe 200 and 300.

**3:44:49** · Nice.

**3:44:51** · And so this looks good to go. Let me go ahead and also establish a a background color. So I'm going to default for now my background color, which is the outermost div, to a slate. So I'll do slate. I want something dark. So probably like 600 would have been good.

**3:45:08** · And that gives me my initial structure for the style of this. One thing to note, we know obviously later on we're going to make uh the light switch part of our UI clickable. It probably would be better instead of to use a div, make it a button.

**3:45:22** · And the reason you want to do that is for one, it's more accessible. Meaning that if someone had a screen reader, it'd be able to recognize that this is a button and kind of read it out for an action. And you also get some free auxiliary styles like if you hover over this button, you get like the the hand cursor, which is useful, right? Telling the user that they should be able to click this. Awesome. So, let's go into the readme for this one. And we just made the background a gray color. That was super easy. And we also put a button that looks like a light switch in the center of the screen. So, what I want you to do now is go ahead and code up phase 0. Make sure you have a UI that looks somewhat similar to ours.

**3:45:54** · Then, I'll see you in the next video.

**3:46:02** · All right, programmers. Let's keep it rolling. Let's go over the walkthrough for phase one. As always, I want you to finish watching this video before you actually code it up yourself. That way you understand what to do for this one.

**3:46:12** · And so let's start by laying down some state into our app component. You might be thinking, why do we even need state for this project? Well, that's because we want our UI to be dynamic. Whenever you want to have any sense of like change in your UI, you're going to need state in React. And so let's go ahead and review how we use the state here.

**3:46:32** · You want to start by doing is importate hook. You have to dstructure out of the React module here. So I'll do import u state from react.

**3:46:42** · Nice. And then from here what I want to do is call that hook at the very top of my component.

**3:46:48** · It's a function. And what you should do is pass in some default value. So here is where I have to start designing the shape of my state. Right? Particular I should probably focus on what type.

**3:46:57** · Types are things like number, string, boolean, and more. And so because my UI here is pretty simple. I only have an on and off state. I can use just a boolean for this state. I'm going to default it to false. Maybe if my state is false, that means that my lights are off. If it's true, that means my lights are on.

**3:47:13** · And so appropriately, what I'm going to do is dstructure two things out of the use state return value. Like we always say, it's going to give back your current state value as well as a function to set that state. So generally value and set value. You should probably give these a better name though, right?

**3:47:29** · So I'm going to call my value is on and it's going to be a boolean. I'm also going to have a set is on. So obviously if is on is true, things should be yellow. If is on is false, things should be more dark gray. One thing to note is be sure that you use an array destructure for the return value of view state. I see students mess up sometimes.

**3:47:47** · They might put curly braces by mistake.

**3:47:51** · Cool. So now that we have our state set up, let's go ahead and try to use the current value of the state to decide the color of our background. We can do all of this without even messing with our button quite yet. I'll just manually change the default value. So to show you what I mean, what I could do is uh add some conditional logic for this background color over here. In particular, what I want to do is switch it between either the slate or like a yellow variant. And so what I could do is maybe construct this string dynamically. So I'll use curly braces over here.

**3:48:21** · And now I can use back tick for the string. because that gives me the string interpolation syntax which we've seen previously in the course right so what I'll do is I'll start a turnary over here so around this bg slate be sure to match your braces exactly

**3:48:42** · and what I want to do is write a turnary using this is on value so here I'll say is on and if it's on I want to use a yellow color so I'll say bg yellow maybe 200 otherwise use the slate

**3:48:58** · color be sure to close this curly over here would be the move nice and so taking a look at this logic maybe I'll just break out this is on variable for now so this expression is really just going to evaluate to either yellow or slate depending on if is on is true or false if you want you can even save it to a variable I can say const maybe I'll say bg there. And then I can keep this a little shorter. I can just splice in some BG color.

**3:49:29** · And be sure to have your two strings here. Awesome. So, it looks like things are working over here. What I could do is now maybe just change default state. I'll make it true. So, that means the lights shall be on. And I can see I'm already controlling the color of the background. Obviously, I would like to make this a state change when someone clicks the button though.

**3:49:50** · And so what we'll go ahead and do is we'll default it to defaults. And we want to actually add a click handler to our button. So in terms of like our to-dos, we added some boolean state to the component. I think that's done. And now let's work on these other to-dos. So like we saw previously, what you want to do is pass in an onclick prop to your button, right? And this onclick is an event handler, right? That means it should always be a function. So I'm going to pass in an arrow function immediately. And I have to decide what this function should do. What I want this function to do is actually just change the state, right? So I'm going to set is on.

**3:50:21** · So I'm going to call the setter function that I get from ustate.

**3:50:25** · I'm going to set it to some new value.

**3:50:27** · So let's say I set it to true over here.

**3:50:29** · What that means is right now my background is gray. That means my state is false. If I click this button, it turns the lights on, right? It sets that state to true. And when that state is set to true, that causes a rerender of this component. So it rerenders or reruns this app function. And now the is on variable contains the value of true.

**3:50:47** · And if that is on is true, that means that the bg color or the background color is going to evaluate to yellow.

**3:50:52** · That's why I see a yellow background over here. However, this isn't exactly what we want in our event handler because if I try to click my switch again, nothing's going to happen, right?

**3:51:02** · That's because the switch is already on, right? It's already set to true in terms of my state. And so I want to be able to turn my lights on and off. So I don't just want to hardcode a true into the set is on. What I really want to do is take whatever value my state is and set it to the opposite. So if it's true, I want to make it false. If it's false, I want to make it true. There a few ways to do it. I'll show you one way. What you could do is write like a full arrow function. So you can give it some curly braces for the body here. And recall when we have an arrow function with curly braces, you could make it multiple lines, right? Like one, two, right?

**3:51:33** · If you're going to not use the curly braces, it has to be a single expression. But now that I have the availability to write multiple lines, you could write an if statement, right?

**3:51:44** · So you can check, hey, if it's already on, then you want to set is on to be false.

**3:51:51** · But if it's already false, then I can just set it to be true. So I'm going to add those in. This is pretty explicit what's going on here, right? If it's true, that means this condition is true.

**3:52:02** · So I set it to false. If it's false, that means I enter the else statement and I set it to true. Now you can flip-flop between the two states. So this is a totally valid way uh to writing this event handler. What you could do is still do it in a oneliner.

**3:52:15** · Kind of show you that trick. You can do set is on and just use the power of the not or negation operator. So I can say not is on because I know that this variable, right, is going to be a boolean and I'm just negating that boolean, right? So if it's true, it's now false and I set it. Or if it's false, it's now true and I still set it.

**3:52:35** · So, I'm going to prefer this way. It's still working, which is good to go.

**3:52:39** · Awesome. And so, to keep things further, let's go ahead and look at our to-dos.

**3:52:43** · Things are pretty good. We have our boolean state, have our nice on click handler. One thing that I do want to also add is change the shades of the light switch rectangles when the switch is toggled. So, this is like a very small detail really just to get you to practice this pattern more. If you go to our demo, our completed demo, notice that when the light switch is off, it looks like our upper rectangle is lighter than our lower rectangle. But if I hit it now, the upper one is darker and the bottom one is lighter. Right?

**3:53:11** · Let's go ahead and implement that logic here. I think while I'm here, I'm also going to lighten the yellow here.

**3:53:17** · And so to do that, we're just going to use this pattern um really the same way.

**3:53:22** · So I'll go ahead and maybe just write it in line here. So I can turn this into a curly brace expression. That way I can write some evaluation with some back ticks. And what I want to do is flip between these two colors. Right?

**3:53:37** · So I'll check if if maybe it's on, then maybe use the slate color. Otherwise, use the lighter slate color.

**3:53:46** · Cool. Well, it gets very tricky, you'll notice, to kind of make sure you match up uh back tick string along with the uh variable inside because there are a lot of curly braces and back ticks. And I'll actually show you a workaround for this in a moment. Right? Obviously, one thing we can do is maybe use a separate variable like background color. But I'll keep it this way for now. That way you can see some different looks here. And then I'll write something similar for the other rectangle. So I'll just copy this style. But I do want to flip them.

**3:54:14** · So, I'll be sure to make this one the 200 and this one the 300. Right. So, if I kind of flip between them now, notice how the rectangles also change colors.

**3:54:28** · Awesome. What I'll do is also just auto format my code. That's the top right button over here. Get some nice formatting.

**3:54:35** · And I think at this point we're done with all like the core features uh of this project.

**3:54:41** · But what I want to do is also show you a nice cleanup we can do, right? It gets really tedious, especially as you write more complicated frontends to kind of jam all this conditional logic for a class names. Conditional logic in this case being our like turnary operator, putting it within like the class name props hard to read overall. And so one package that I love to use is actually called classics. I'll I'll link it inside of the readme. And so what you want to do to start here is really just import the package and install it.

**3:55:09** · So I'm going to turn off my dev server by doing control C or command C depending on what operating system you're on. And what I'll do is npm install and it's going to be clsx. I pronounce it classics. It's really a package that's designed just for writing conditional logic inside of your CSS class names. So I'll install it. Give it a moment to run here. And I'm going to turn on my server again with npm rundev. And now I can actually import this package wherever I please. Right? So I'm going to import classics from class 6.

**3:55:45** · And really the short story of just using this package, it's very very simple, is you can now call this classics function right inside of your class name and performs all the concatenation for you.

**3:55:57** · So what does that really mean here? I'm going to refactor this to use classics, right? So, I can actually maybe not do the bg variable.

**3:56:09** · I will save this expression though and I'll clean things up. I'll use a regular string for this.

**3:56:17** · And I'll start by calling classics.

**3:56:23** · And the nice thing about classics is it takes in multiple arguments. So, this initial string is all of the styles I want always, right? But then in addition to that, I can break a line here. And I kind of like to style my code like this.

**3:56:37** · I can break a line here. And what I'll do now is pass in all of the styles that I want to form over the turn area.

**3:56:43** · Right? So I can say is on I can switch between the two. Right? So let's take a look at what this is really doing. It's really a very simple uh function. What we're doing here is we're still passing in the class name prop, but this time within the curly braces, we're calling the classics function. classics takes in multiple string arguments, right? Looks like the initial string here is just all of my default styles that I want always.

**3:57:06** · And then for the second string here, it just contains a turnary. We already know how expressions like these evaluate, right? If is on is true, then I go ahead and take the yellow. If it's not true, I take the slate. And then from there, it's just going to actually add together these two strings and then pass it into class name. But it keeps my code a lot more readable because now I can do things like break lines between the arguments into classics. Right? So I'm going to take a moment here and also refactor uh the div here.

**3:57:30** · So the way that would look is I'm want to start by turning this into a regular string and then you can kind of drop the turnary.

**3:57:44** · So I'll grab all of this.

**3:57:47** · Right. Right. So, this is my initial style. Pass it into classics.

**3:57:53** · That's my first argument. And then I'll have the turnary right here. For that last rectangle, I'll go ahead and copy this one as well. I'll be sure to just switch the colors around. So, let's go ahead and test our UI.

**3:58:08** · Right. And it's still working. Awesome.

**3:58:10** · And so, we're definitely going to be using this classic module a lot. will really in the long run help you keep your sanity when it comes to concatenating all of your different uh class name strings. All right, programmers, what I want you to do is go ahead and code up uh the last phase for this project and be sure to compare it to the demo. In particular, you should be changing the colors of your light switch rectangles as well as the background. And if you get stuck, feel free to go back to this walkthrough video.

### Image Carousel Exercise

**3:58:41** · Hey programmers, Alvin here. Welcome to our image carousel project. So, let's jump right in by looking at the completed demo for this one. So, in this project, you're going to be building an image carousel. So, really the feature here is to have an image being displayed as well as some buttons that actually switch to different images. Here, I just have some dog images. And if I click these arrows, it'll actually bring me to different images. I have five images overall.

**3:59:06** · Some details that you'll notice in this UI is we're also displaying like the number of the image that we're showing.

**3:59:11** · dog two, dog three, and so on. And since we only have five images, when you actually get to the last image, which would be dog five, if you keep clicking the right button, you actually won't go any further. Likewise, if you're already at the first dog, if you keep clicking the left button, you won't go further as well. All right, so I'll see you in the next video walkthroughs where we'll start building this UI together.

**3:59:35** · All right, so let's hop into phase zero for this carousel project. So in this phase, like we usually do, we just want to set up some initial HTML skeleton as well as establish some of our initial CSS. And so we'll hop inside of App.jsx.

**3:59:48** · For now, we're going to be working just inside of this app component. You'll see that we've actually given you some static data. We have an array called image URLs. And inside are just going to be some URLs of the images you're going to use. They're going to be the same dog images that you can see within the demo.

**4:00:04** · Awesome. So, let's get set up like we usually do. What I'll do is start my dev server, we're doing npm rundev and we'll hop right in.

**4:00:15** · Go ahead and split my screen here.

**4:00:18** · And when it comes to uh the overall UI, we just want to establish an image on the screen as well as a button to the left and right of that image for now.

**4:00:27** · And so what I'll do is I'll start by just displaying one of my images. So what you could do is you could use the image tag. It's a very simple HTML tag.

**4:00:36** · You can also self-close it here. So I don't need to actually open up the pair tag. And you can give it a source attribute. And that attribute is just going to be the URL of that image. So I'm going to choose one of these static images just for now. Right? We're going to hardcode all of our image data. And we're going to ignore any React state for now.

**4:00:57** · Cool. So you'll see I'm seeing my very large dog image. Probably the first thing I want to do is establish some size for this image. So I'll go ahead and use my CSS class names here. And I want to make it kind of like a card shape. So I'll give it some width. And I can use some square brackets here to actually choose an arbitrary pixel width. So let's say I made it maybe 200 pixels in width and then maybe 300 pixels in height.

**4:01:29** · We'll see how that looks for now. All right, that looks pretty good.

**4:01:34** · One thing you will notice because I'm actually giving this image like a set width and height, I actually could get like a stretched out image overall, right? So, for example, I could do kind of weird things like maybe I'll make the width much smaller, like a 120, but still keep the height at 300. Uh, this is going to give you a kind of a distorted image. And so if you want to fix this distortion, what you could do is use a nice tailwind CSS property, you can say object, you can say object cover.

**4:02:06** · What that'll do is actually zoom into the image without distorting the aspect ratio of it. For this particular image, I'm going to increase the size here. So I'll say 200 by 300. I think that looks pretty good. All right. So there's my static image. I'm going to go ahead and give this some margin. So I'll do margin all around of eight for now.

**4:02:27** · And I'll do some really basic styles.

**4:02:29** · You know me, I always like to round my corners. So I'll say rounded large for this image. Nice. And so from here, what I'd like to do is also give me some buttons to the left and right. So I'll put a button.

**4:02:43** · So I'll have my left button and also my right button. I do want to make the style look somewhat similar to the demo.

**4:02:52** · So, I actually want to use some nice icons. Like we learned previously in the course, we could just use some of our handy font awesome icons. So, I'll go ahead and go on Font Awesome. I encourage you to do the same, right? You never have to actually choose the exact uh colors or style in the demos that I create. You can go ahead and customize it if you like. I want to look for some chevrons, though, which would be these little arrow thingies, right? I want a left and right chevron. Maybe this time for my walkthrough, I'll use the double chevrons.

**4:03:23** · So, I'll copy this and I can paste it right inside of my button.

**4:03:30** · Do bear in mind that when you copy that code from font awesome, they're going to have the CSS class uh using the class property, but in React, you actually want to call it class name.

**4:03:41** · So, that should be better for us. I can see it. And also do it for my right button. If I had to guess, it'd be class name fa chevrons.

**4:03:51** · Right.

**4:03:53** · Cool. And so what I'll do is let me go ahead and make sure that this UI goes from left to right. So I want the buttons not to be above and below my image. Right? So to do that, I'll just want to apply some flex to the parent.

**4:04:07** · So that this outermost div is the parent. I'm going to go ahead and make this a flex. I'll make it a flex row.

**4:04:14** · Right? And I do want to center things up. So, I'll do justify center.

**4:04:20** · Awesome. And then from here, what I want to do is also maybe make my chevrons look more like buttons. So, for these outer buttons that wrap the icons, I'll do it for one of them over here. I'm going to give it a background color. So, I'll say BG. Maybe I'll go orange this time. So, I'll say BG orange. Maybe a light orange would do. Maybe a little darker. So, I'll say orange 400.

**4:04:47** · Nice. And notice that by default, these buttons are super duper tall. And why is that? Well, that's because uh buttons by default will actually grow to the full height of their parent. So, if I actually give the parent, which is this outer div, a border. So, I'll say border border black.

**4:05:05** · You can see that this button is growing to the full height of its parent, right?

**4:05:09** · And the height of its parent is really going to be decided by this large image here because I gave it a margin eight above and below. Right? So I don't want that behavior. I don't want it to grow.

**4:05:20** · So for my flex tiles like we learned previously, I can say items center.

**4:05:27** · Nice. From here though, I do want to give these buttons some roundedness to them. So I'll go ahead and for me make these maybe some circle buttons. So I can say rounded full give me a nice circle shape. And what I want to do is also give these buttons the same height and width. Right? That way I get a perfect circle. Right now these look like ovals. Right? So what I could say is maybe like a width 20 H20.

**4:05:57** · I'm not sure if that'll be too big.

**4:05:58** · We'll see. Yeah. It's a little too big.

**4:06:00** · So maybe we'll cut that down to maybe an eight.

**4:06:07** · Nice. That looks pretty good. And for good measure, going to change the color of my chevrons. Maybe I'll say text.

**4:06:15** · We'll say orange. Very light orange.

**4:06:17** · Orange 100. Recall that in your Tailwind CSS styles, lower numbers are lighter, higher numbers are darker. So that looks pretty good to me. I'm going to copy this style from my right-h hand button.

**4:06:29** · So I think that's going to be my initial UI. Let me clean up this black border.

**4:06:34** · And I think compared to our demo, let's take a quick look at the demo. We also want to maybe include this text up top with our dog. And for now, we can't make it dynamic, but I'll just at least hardcode some stuff here. So maybe over here, I'll write a div. And I'll say dog 2.

**4:06:52** · And I do want to put this actually above the carousel. The carousel is really the image combined with the buttons here, right? So, I'll probably have to add some additional divs to kind of have this dog two text be above everything else. So, I think I'd actually wrap the carousel, which is the buttons and the image. I'll wrap that in its own div, right? And now for this new div, I can make this a flex. So, I'll actually move all these flex styles down there.

**4:07:24** · Right? So, I get the same behavior as before.

**4:07:28** · And now I actually have the dog text above everything, but they're not centered. So I'd rather do class name flex on this outer parent.

**4:07:37** · Nice. But now I want it to be a flex column, right? Because if you do a flex column, you'll actually stack these things vertically, right? So what's the difference there? It's kind of hard to see if you don't add your borders. So remember we learned initially when we kind of went over some basic, you know, tailwind CSS/CSS behaviors. I'm going to add border border black here. I'll do another border border black over here. So right now I have the outermost div as a flex call. That means that it's children.

**4:08:05** · So this div as well as this div, they're going to stack vertically. If I just do a regular flex, they're actually going to be horizontal. Right? So that's really the difference here. So I definitely want to stack them vertical.

**4:08:21** · Now, the only thing I'd like to do is actually bring this dog to text to the middle. So, I can just do maybe text center.

**4:08:30** · Nice. So, I think that's good to go.

**4:08:33** · I'll go ahead and change the text color of this. So, I'll say text. Let's do like a cyan. Maybe cyan 400. I also increase the text size here. So, I'll say maybe text to XL.

**4:08:49** · Nice. And with that, I'll go ahead and clean up my borders. All right, so I think that wraps up phase zero. What I want you to do is now go ahead take a moment and create your own carousel UI.

**4:09:00** · It doesn't have to look exactly like this. I think overall you should have your buttons to the left and right of your image and definitely include uh some dog number, but when it comes to the colors or roundedness and style, overall feel free to experiment for yourself. If we look over at the prompt for this, we went ahead and we displayed a static image. We also got our two buttons that we're going to wire up with event handlers in the next phase. I'll see you there.

**4:09:26** · All right, so let's keep it rolling into phase one for this. So here I want to work in our React state. So I have two things in mind. What I want to do is add a number state so I can track the index of the current image that we're going to be displaying out of this array. And we also want to add click handlers to update that specific index. Right? That way I can have this carousel be dynamic.

**4:09:47** · And so I'll go ahead and reuse what we've been using all along, right? Which is the use state hook. We can accomplish a lot uh using it in React. It's actually probably the most important hook that we use in the React library.

**4:10:00** · So I'm going to import use state from React. By now you should be remembering that when you import it, you should dstructure it out of the React module, right? And then what I'll also do is go ahead and call it at the tippy top of my component. Give myself some room here.

**4:10:17** · So I'll go ahead and call const. And I want to dstructure two things out of the u state.

**4:10:26** · What I should do is take in the current state value as well as a setter function that helps me update that value. I'm going to choose an appropriate name for this. I'm going to call it image index and set image index. In terms of the default value, you want to probably be consistent with your type. I know an index is a number. You can just start at one of these valid indices within your image URLs. So I'm going to choose index two, which would be, you know, technically this image because I go 0, one, two.

**4:10:56** · Awesome. And so from here, what I should be able to do now is at least use this defaulted image index state to render a specific uh image URL. So I'll go ahead and take a look at my output here.

**4:11:09** · And instead of this hard-coded string for the source, instead I want to actually get that property from the array. So I'm going to style this up a little nicely so all of you can see.

**4:11:24** · So I know I want to do a evaluation here because I want to reference some expression that utilizes image URLs. So I'll say image URLs and I want to grab a particular index. So if I say something like one right that should give me this image because that's index one but generally I want to say image idx

**4:11:45** · because now I'm utilizing the state right and now whatever the state is that will render a different image on my screen right and so let's go ahead and now add our event handlers for our buttons because we want to be able to change which image we're displaying using these buttons so here's where I just work in our very classic onclick handlers. I like to put them on the button. So I'll say on click here. And really important thing when you have an onclick prop, right, you should be passing in a function. What I want to do is set the image index to be one less than the current image index.

**4:12:18** · So image index minus one. And that's because that's my left hand button over here, right? And so I'm currently at dog two.

**4:12:29** · I'm showing this image. If I click the left button, I should be looking at a different image. Right, that's working.

**4:12:35** · One thing you'll notice is this dog two text isn't changing. That's because it's kind of hard-coded some static text right now because I put that over here, right? So, instead of showing the actual static number of two, I probably just evaluate my image index over here. So, I'm currently at index two. If I click my left button, I go down to index one.

**4:12:59** · And also I can go to index zero. You'll notice that in the demo the smallest dog index is actually one.

**4:13:06** · And that's just because I actually added one to that image index when I displayed it in the UI.

**4:13:12** · Right? So that'll be easy to do. All you need to do is say image index plus one because maybe you want to show your image indices starting at one on the screen instead of zero. Kind of more user friendly because only programmers count by starting at zero.

**4:13:24** · And so let's go ahead and be sure to wire up the on click handler for our increase button.

**4:13:33** · So I'll just copy and paste this. Be sure to increment this as well. So I should be able to go between them now, right? Up and down. U but we do need to establish some kind of error prevention here. So let's break down this bug.

**4:13:47** · Let's say I go to the very last image that I have available, which would be this dogfy, right? be this element over here. If I hit the right button again, I actually go out of bounds of this array, right? So, what's really happening here?

**4:14:01** · Well, I know that there's no element after this one. And so, I'm getting some invalid image URL, right? In particular, what I could do to debug this is I can copy this expression and we'll see what it is over time. So, I'll console.log log this and I can view the console by hitting this kind of wrench symbol here. So I'm getting undefined right now. Image URLs is undefined. Right?

**4:14:29** · So if I go down now I'm back inbounds this expression now evaluates to the actual last element.

**4:14:39** · Right? But if I increase it you get undefined. Right? That's because if you grab an index that's out of bounds of an array you get back undefined. And that's not what we want, right? So to counteract this, what you should do is only increase the image index if you're not at the last image index, right? So you don't go out of bounds. So it's very simple for us. What we could do is just go ahead and use an if statement. So I'm going to say if the image index if it's less than image urls dot length minus one.

**4:15:16** · Cool. And so what am I saying over here?

**4:15:18** · Let's go ahead and kind of reset our UI.

**4:15:20** · So I'm going to restart at three.

**4:15:23** · Remember that we're actually displaying our image index plus one here. So maybe for now, just for the sake of this explanation, I'll display the kind of the raw index here. So when it comes to my indices, if I go to the first image, it's definitely zero, right? And that's out of bounds.

**4:15:42** · But if I go to my last index, that should be four, right? Because I go zero, one, two, three, four. So if I try to hit the right arrow right now, nothing happens, which is good, right?

**4:15:53** · because I don't want to display like the broken image symbol. What I'm doing is I'm checking, hey, if my current image index, if it's less than images.length minus one, I know that images urls.length minus one is the very last valid index, right? Because for example, if I have a length of five like I do here, the last index is really four, right? So you should only set your image index to increase if you're not at the last image URL. So that's good to go.

**4:16:21** · I just want to write a very similar if statement for the left hand side. Right?

**4:16:30** · So this one's probably more straightforward.

**4:16:33** · All you need to do is go ahead and check if your current image index if it's greater than zero. If it's greater than zero, then you can go ahead and decrease it. Right? So, I'm at dog one. I should be able to actually move to my previous image, right? Because I'll check if one is greater than zero. That's true. So, I go ahead and decrease it. Nice. And now, if I try to decrease it again, right, I'm going to check is my current image index of zero greater than zero.

**4:17:05** · That's false. So, this if statement won't occur. So I won't set the state to be one less. So if I try to click left right now, nothing happens, right? Which is good. So I don't go out of bounds.

**4:17:19** · And there we have our very classic carousel feature. All right, programmer.

**4:17:23** · So before I set you off on actually coding up this phase one for yourself, one thing to note is that when you go ahead and create your click handler for your buttons, this time around, you definitely want to use a multi-line arrow function. You notice that I have the curly braces for the body of the arrow function here. That's because I need to write multiple lines to actually have this if statement. Right? So, you can't use a oneliner. In other words, this would be incorrect. Wouldn't be correct syntax. You have to use a multi-line arrow function here. All right? So, I want you to code up phase one for this one.

### Cat Carousel Exercise

**4:17:52** · If you get stuck, feel free to reference the instructions that we provided or watch this walkthrough video once again.

**4:18:02** · Hey programmers, Alvin here. Welcome to our cat carousel project. This is going to be another project where we get to practice the carousel pattern. And so let's take a look at what we're going to be building in this one. We'll go to the completed demo over here. So we're going to have a very similar carousel UI. This time we're displaying an image as well as some other data associated with that image. So here I have some cat profiles.

**4:18:23** · Of course, if I click on these buttons, it gives me another image in the series.

**4:18:27** · What you'll notice is once I hit the last image, for example, to the left, the button disappears. That's going to be a new feature for us. Likewise, if I go to the last image on the right hand side, the button should also disappear.

**4:18:40** · For us, this is going to be another opportunity to create the carousel pattern. So, we'll get more practice with this one right now. I'll see you in phase zero.

**4:18:51** · All right, so let's hop into phase zero.

**4:18:53** · So, in this phase, we're just going to set up a few things. We want to set up our initial UI with a cat card as well as our two buttons. We're going to avoid any functionality that involves state and clicking right now. So if we hop into appjsx, you're going to see the cats array that you're going to use as your data in this project. So to get going here, the instructions are pretty prescriptive. What I want to do is create a cat card component. So I'll create that off the bat here. Create a new file called catc card.jsx.

**4:19:21** · Of course, I'll define cat card. It's going to take in some props, but for now, I'll just have it return some placeholder text. Maybe just a div.

**4:19:33** · I'll just say cat card. Be sure to export default. And this should be good to go. So, let's go ahead and import that in our app. We'll do at the very top.

**4:19:44** · Import catc card from dot slashcatcard and I'll render it right inside of my app. So, simply catc card. I can of course turn on my dev server at this point by running npm rundeendev.

**4:20:05** · So we'll take a look at our output. And there we see our cat card. Give myself some space here. Like to put my output on the left and I'll move my component to the right here.

**4:20:16** · Awesome. So to get going, I want to establish a similar style to the demo.

**4:20:21** · So the demo has a card like this where I display the name, age, breed, and location of this particular cat. Notice that the uh information on the cat card here of course corresponds to the information within a single cat object in my data. Right? So if you wanted to start, you know, creating the format of your cat card, I'd probably just pass in one of these objects uh directly into the cat card. So what I do is I can say cat equals as a prop. I'm going to pass in cats square bracket one. So that would happen to be this Abby cat, right?

**4:20:54** · So inside of cat card, we can start rendering some of that information. Um I'll take in those props, right? So I'll say dstructure the cat out of the props.

**4:21:07** · Let me just display some of those pieces of text. Right. For now, I'll just render the name. So I'll use two divs here. I'll render information here.

**4:21:16** · Cat.name. name. So, this is going to be some static text. It's going to be like the label. And I'm also going to say the actual value associated with that cat object, right? And I'll make sure these are styled as rows by putting these two pieces inside of a flex, right? So, class name flex. Remember, by default, if you say flex, that makes it a flex row. So, that looks decent. I think for now, I'll also add some maybe margin or width to these names.

**4:21:43** · So I'll say class name for now I'll add margin I can show you a nice trick you can use I'll say margin right of maybe two nice and then let me also maybe bold the label here so I'll say text bold actually it's not text happens to be font bold I believe so that's looking pretty sharp let's go ahead and also change the color of this row so I think I'll use text let's Choose neutral.

**4:22:14** · Maybe 400 should be a great color for us. A little too light there. Let's go 600.

**4:22:22** · That looks pretty pretty decent to me.

**4:22:24** · Maybe even 500 would be on the money here. Yeah, I like that. Much better.

**4:22:28** · And so from here, I'm just going to copy these flex because I have a few different other fields, right? Not only do I have name, but I have age, breed, and location. So I'll just copy and paste all of those. So, name, breed, age, and finally, location.

**4:22:52** · You can feel free to maybe alter your styles in your particular cat card, but I'm going to follow the demo quite closely.

**4:23:01** · Nice. So, let me establish now the actual shape of the card. I want to see this nice rectangle thing. Of course, I should probably also render the image here. And I think the name of that property is going to be just image URL.

**4:23:14** · So I should create an image tag above.

**4:23:17** · Let's say image. It's going to have a source that is going to be cat.im image URL.

**4:23:26** · It's going to be a massive image at the start here because I do need to establish some sizing, right? So what I'll do is let's go ahead and apply some class name to this image.

**4:23:39** · say class name and I probably give it a fixed width. Maybe I'll say width and I'll use some built-in values. I could use like 80. See what that looks like.

**4:23:50** · So width will be 80. Let's make our height a little smaller. So I'll make it maybe a 64.

**4:23:58** · Nice. And I don't want things to stretch out too much. So I'm going to use the object cover style that we used previously. Nice. So using a set width and height along with object cover. All of my images are going to be the same size. So that's good to go. Let's start to actually make this look like a card.

**4:24:15** · So I'm going to give myself a little border. We'll say border. Border. Let's use some more neutral gray. We'll use gray 500.

**4:24:24** · So border is actually forming. It's kind of hard to see because it's pushing up right along the edge of the window here.

**4:24:31** · So I'll probably use some margin. Let's use margin six all around.

**4:24:35** · Nice. We'll probably want to also round things here. I'll say rounded large.

**4:24:42** · And one thing I want to be sure to do is I only want like the card itself to be as wide as the image inside. And so what you can do is actually in your app, you want to start applying some styles here.

**4:24:54** · So the reason that the cat card div is actually expanding to the full width is because that's the default behavior of a div, right? A div will expand to the full width of its parent. If I want to get around that for the parent over here, I can say class name, make it a flex. And I'll just center things up. I can do flex justify center.

**4:25:14** · I'll put it smack in the middle. You notice that my corners look a little strange here. That is probably because the image itself may not have rounded corners. So, if you want to fix that, you can say rounded large. But that would actually also round the bottom of the image. If you just want to round the top of the image, you could do rounded t large.

**4:25:35** · So that looks good to go. I want it kind of flat on the bottom but rounded at the top. And to clean up the style a little bit, I think I would also want to add some padding to this section over here, right? This text is way too close to like the edges. So I'd probably take all of these different rows that contain my data and I put them in a new div.

**4:25:58** · And this new div is going to have just some padding. Maybe even P4 would be good. Remember that padding would be the space within the border. So I'm going to move this up, put them all inside.

**4:26:10** · And that looks much cleaner. While we're here, I guess we can go over some, you know, CSS things. So you'll notice that in the actual demo, I have some very nice alignment when it comes to the values of this cat profile. On my actual output right now, it's not aligned perfectly. And the reason of that is obvious, right? It looks like these labels of name, breed, and age, they all are a different number of characters.

**4:26:30** · So, they take up a different width, right? And the actual values are just going to start after um the label finishes. So, what you can do to get around this is just give these labels some fixed width that is large enough.

**4:26:42** · So, what I mean is inside of our cat card, we can look for our labels, which would be these bold things. And I'll give them all the same width. I could say maybe width, see what 24 looks like. That actually looks pretty good with 24, right? Uh really what's happening is if I do a border border black. So if I look at it right now, you can see that the div that contains name is actually going to always be 24 width. So I have some nice alignment for the actual values there.

**4:27:14** · Cool. So I think that would wrap up our cat card. Head into our prompt. We displayed our static cat card. Now we also want to display some buttons to the left and right of our card. And in the instructions, we do advise that you actually create some components to render these cards. I want to create a nice nav button uh component. I start by creating a component called nav button.

**4:27:36** · JSX.

**4:27:38** · And I'll define it here.

**4:27:40** · nav button.

**4:27:47** · For now, I'll make it return some placeholder. I always love to do that to make sure I don't do anything weird with my imports. I'll just create a div and I'll say nav and I'll start by rendering that right inside of my app. So I'll render it twice. I want to render it to the left and right of my card. So here's my cat card.

**4:28:09** · I want one to the left of it. So I'll say nav button. Be sure to import it first though, right? That'll be important.

**4:28:18** · Nav button. Render two of those. nav button.

**4:28:24** · I can self-close this.

**4:28:30** · Nice. The reason it's probably a good idea to create a nav button component that you can reuse is it's going to have very similar styles for the left and right button. They're going to differ only slightly. Really, the only difference we need to establish is one has a lefthand arrow, the other has a right-hand arrow, but the overall functionality and style is going to be the same. Right? So, what I'll do is I'll start creating that nav button.

**4:28:51** · And I'll do it over here that way you can see it update on the fly.

**4:28:56** · I'll start by giving myself maybe a background color. So I'll do class name.

**4:29:01** · You can switch up your colors however you like. I'm going to use green this time. I'll say bg green 400.

**4:29:08** · And also say maybe text green 200. Those colors are okay with me. You're probably wondering why are these uh button divs.

**4:29:17** · they're actually taking up the full height of the parent right now. That's because it's just a default behavior uh inside of your flex, right? So, by default, when you make a flex parent, its children will want to grow to the height of the parent. You can fix that by just centering the children vertically. Right? So, remember that the parent looks like this. I'll say border border red 300.

**4:29:43** · The parent is in the red over here. If I make this parent now have item center, it will center all of its children vertically. That's probably more of what I want here. I'll drop my border at this point. Now that you have the idea, let me also start creating the actual icon inside. So, I'll do a few things. As always, you can feel free to pick your own font awesome icons. So, just go to the Font Awesome website. Link will be in the read me as always. I'm going to look for nice chevron.

**4:30:13** · So, use a chevron or you can use a triangle or something. Maybe I'll use one of these. These circlly ones would be pretty cool. So, circle chevron left.

**4:30:26** · Copy this. I'll just put it right inside.

**4:30:31** · Be sure to use the prop class name instead of class.

**4:30:36** · That's looking a little better. And I probably want to make things bigger. I can do a margin maybe two. That way I have some gap around these. I want to make them way bigger. So I'll use text. Remember that text is the property that controls the size of these icons. Say maybe 3XL.

**4:30:56** · That looks pretty solid to me. I'd probably want to round the corners here.

**4:31:00** · So I'll say rounded medium perhaps this time. Looks pretty dope. Let's go ahead and make sure that we use some proper button tag for this. So, I do want to make this clickable. And the reason is, you know, right now if they're divs, if I hover my mouse over it, you don't get any of those automatic styles like getting the the pointer hand. So, if you make it a button, which is probably better overall, now you get those built-in styles. Awesome. So, this is looking pretty solid to me.

**4:31:27** · One thing you'll notice is, you know, this button over here should actually be pointing to the right. So that means that I'm going to need to figure out a way where I can have different buttons in terms of their icons, right? What I would do is really just make a prop for the actual icon you're using here. So what I can do is be awesome if I had a prop called maybe icon and would be the string that represents the icon. So like here would be FA circle chevron left.

**4:31:58** · So I'll take it in as prop and then over here delete that and I'll actually want to create the class name string here.

**4:32:14** · Then you want to just make sure you also include whatever that icon is. So I can use dollar sign icon. Nice. So at this point I need to be sure I pass in that prop because right now it's undefined, right? I'm taking in icon. But if I go into my app, I never pass in any icon, right? So I'll pass in here. And I believe it was FA circle chevron left. So I'll be icon FA circle chevron left. And it should be chevron right for the other side.

**4:32:52** · So this is very classic component design. If your components need to vary, meaning they need to sometimes be different. Um, then you just make sure that you have some prop that can control that difference. So here's just my left and right. So that wraps up our initial component design. In the next phase, we'll implement some state and our click handlers.

**4:33:15** · All right, so let's hop into the next phase. We want to start by just doing a quick refactor. So instead of having our data, so this giant cats array exist inside of our app, we want to put it in its own file. So what I would do is I create a new file here. We call it cats.js.

**4:33:31** · The reason I'm using lowercase cats and not using JSX is it's not going to contain a component. It just contains some regular JavaScript code. And so I'll just make sure I export this plain old JavaScript array.

**4:33:43** · So catsjs, you're defining cats over here. And you can just do export default cats.

**4:33:55** · Nice. Then obviously back in app, I just want to import that. Import cats from dot slash cats.

**4:34:05** · And this should all work the same, right? I'm still able to reference different elements of this array. So really clean refactor just helps me really only look at the app component inside of the app.jsx file. And now let's hop into some real react code.

**4:34:20** · Right? So I want to add some state. That way I can swap between different cat images. So this is going to be the core of our carousel feature. And you implemented this pattern previously.

**4:34:29** · What you want to do is import use state from react. Really common mistake I see students make here is they don't actually destructure ustate. So this would be wrong, right? Be sure that you dstructure it from react.

**4:34:44** · Then at the tippy top of your app component, you'll want to initialize your state. So I'm going to call you state. I'm going to pass in a default value. I'll start at maybe index 2. And then you're going to take in two things from the result of you state. You're going to take in the state value, which I'll call cat index. And also a setter.

**4:35:02** · So set cat index. Nice. Now at this point, I want to be sure that I use the state value to control which cat I'm showing on the screen. So I'll use cat index here. So if I go into my output right now, I'm showing cat index 2. If I change the value of the state manually by just editing the code, it should switch to a different cat. So things are looking pretty good. I love to really make sure I test my code as I go. That way when things break, I know it's probably something that I just changed, right? And so let's go ahead and now add some event handling for these buttons.

**4:35:39** · And so what you should do is you should pass in a prop over here um that actually does the set cat index. So in a perfect world, you'd be able to pass in a prop to this nap button called on click.

**4:35:54** · And that should do some code. For now, I'll just make sure I console.log click. I'll only do this for the left button for now. So although I'm passing a prop called on click to this component, if I open up my console and I hit the left button, I don't see that click message. And that's because this event handler function is not actually running. And that's because nav button is not a regular um HTML tag. Although I have a prop called on click, you actually need to make sure that is wired to some HTML tag.

**4:36:25** · So that means on the inside of nav button, I need to actually take in this onclick prop and I need to make sure it makes its way to some HTML tag. Really, I should apply it to this button here. So I probably write something like this and I'd say on click equals on click, right? So that's really key.

**4:36:51** · Whenever you have uh some event handling that needs to go into a component, be sure that you take it in as a prop and you have to manually define that prop. So now if I click on the lefth hand side, it's working here.

**4:37:03** · So now we can implement a proper click handler. So instead of just console log and click, I want to set cat index to be one less than its current value because I'm defining the left button, right? So I'll do cat index minus one. I'll have a very similar prop for the right-hand nav button except I increase the cat index.

**4:37:25** · Cat index plus one. This is really the punch line for our core image carousel pattern. So I can go between my different cats. Great. So that's all I got for this phase. We added the actual event handling and state for our buttons. In the next phase, we're going to add this extra feature of making sure the buttons disappear when we click too far. I'll see you there.

**4:37:48** · Hey programmers, welcome back. Let's go over the final phase for this one. So in this phase, we want to implement the feature where a button disappears when there is no cat in that direction. So if you look at the completed demo, if I go to the very last cat, there is no cat after Penelope. So the right-hand button disappears. I can only go to the previous cat, right? And so to implement that logic, we're going to use some conditional rendering. You've seen that previously in the course. Uh this time we're going to apply it a clever way for our different nav button components.

**4:38:14** · So without doing anything too fancy, the way you can establish a button disappearing is by using some conditional rendering like a turnary operator or and operator. So I'll show you both ways for now. So what I could do is wrap this nav button and maybe a nice turnary. I can check only render the nav button if the cat index is greater than zero. So if it's greater than zero, then you can go ahead and render this nav button. Otherwise, don't render anything.

**4:38:46** · So render null in this spot. I'll auto format this file. Cool.

**4:38:52** · So if I go exactly to index zero, which would be Winterfred, I could double check that by just looking at my cat's data, it's definitely Winterfred.

**4:39:02** · This uh button disappears, right?

**4:39:04** · Because in this example, cat index would be exactly zero. I check is zero greater than zero. That's false. And so I just evaluate this null. And null means don't show anything in React. Awesome. So this is one way to do it. It is kind of clunky to actually write all this code.

**4:39:20** · So I don't prefer it. What you can also do is just use the and operator. So instead of writing a full turnary, you can just say your condition and then you can say and. And this works in a similar way. So we'll see what we get. Right? If I have a cat index greater than zero, then I am going to show the nav button.

**4:39:41** · But if it's exactly zero, like this first cat wifred, then it disappears.

**4:39:45** · And I showed you this trick previously in the course when we spoke about conditional rendering. And here it's totally fine. You could implement your uh conditional rendering in this way, but then you'd have to write some duplicate logic for the right hand side and it could make the code hard to read.

**4:40:00** · So I think a better design for this nav button component is if it took in a prop, right? All right. So that would look like this. It'd be really great if I could take this condition and instead of wrapping the nav button in some like conditional rendering operation, I can pass in a prop. So it' be awesome if I could pass in a prop called show maybe.

**4:40:21** · And if that prop is true or false, that would decide whether or not to show the component. So I only want to show the nav button if the cat index is greater than one. Right? This just evaluates to a boolean. So I'm passing in this prop, but I still need to actually use it on the inside of nav button. So in my nav button class, I'm now taking in this show prop, and it's going to be boolean, right? And now I can just use this prop to conditionally render my button or not. So I can actually write it really short here. I can just write an if statement. I can check, hey, if show equals false, then just return null. Right?

**4:40:55** · If a component returns null, then it's not going to display on the screen. So this will probably be the cleanest way to show this one. If I go to index zero, which would be winterfred, notice that the button disappears. What I also want to do is make sure I pass an appropriate show prop for the right hand side. I can't use the same condition though, right?

**4:41:14** · This condition now needs to make sure the button disappears when I'm at the last cat index. So what I would say is only show the right-h hand button if the cat index is less than cats.length.

**4:41:28** · length minus one. Bearing in mind that cats is the actual array of cats, right?

**4:41:35** · I know that array.length minus one is the last valid index of an array. So that means it should only show the button if it's less than that valid index. If it's at the very last index, which I'll go to right now, like Penelope, then this condition is false.

**4:41:50** · So I think this component design is great because it keeps my app file really clean, right? I'm just passing in a really easy to read prop which designates whether or not I should show the button. And inside of the nav button, I get to reuse this conditional uh render here. All right, so that's all I got for this cat carousel project. I want you to code up a phase 2 on your own and make sure it behaves similar to our demo and I'll see you in the next one. Hey programmers. So that wraps up our beginner React course. Congrats on making it all the way through.

### Outro

**4:42:19** · We built some really cool user interfaces together and I hope that you learned something new. Although this beginner course is over, this is really just the beginning of your React journey. If you'd like to learn more advanced React topics and learn how to build fully featured frontends, I recommend you head to my course, reactformmula.com, where you can learn even more front-end web development with me. The beginner course you just completed here on YouTube only scratches the surface of what you can do with React. And so, I'm really excited to teach you even more. Head to reactformmula.com to keep learning. I'll be sure to include a link in the video description below.

**4:42:50** · Thanks for watching and bye for now.