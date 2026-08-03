---
title: "MCP sur N8N : Construis n’importe quoi (tuto INSANE) 🤯"
source: "https://www.youtube.com/watch?v=zyx2p6AhjWU"
author:
  - "[[Meydeey | Automatisation IA]]"
published: 2025-07-28
created: 2026-07-21
description: "Découvre comment le duo MCP + N8N te permet de construire n’importe quel workflow en un temps record : rapide, puissant, incroyablement modulaire.───▸ RESSOURCES→ Accéder au programme : https://m"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=zyx2p6AhjWU)

Découvre comment le duo MCP + N8N te permet de construire n’importe quel workflow en un temps record : rapide, puissant, incroyablement modulaire.  
  
───  
  
▸ RESSOURCES  
→ Accéder au programme : https://meydeey.com/labo/  
→ Communauté gratuite (+4000 membres) : https://meydeey.com/communaute  
  
───  
  
▸ CHAPITRES  
00:00 - Intro  
00:14 - MCP Serveur/Client  
00:31 - 1 Workflow Serveur + 1 Workflow Client  
01:44 - En gros...  
02:39 - Visuel simplifié  
02:55 - Mieux comprendre en 8 minutes  
03:04 - Pourquoi TU DOIS connaître  
05:06 - Pourquoi SÉPARER Client & Serveur  
05:42 - Bénéfices++  
06:20 - Démo complète  
18:45 - Conclusion  
  
───  
  
▸ CONTACT  
contact@meydeey.com  
https://instagram.com/meydeeyai  
https://linkedin.com/in/medhi-el-ouardouni  
  
#n8n  
#mcp  
#automatisation

## Transcript

### Intro

**0:00** · Dans cette vidéo, vous allez réellement comprendre la puissance de N8N avec les MCP serveurs combinés avec les MCP clients. Donc, je vous ai préparé un workflow que je vais vous expliquer juste par la suite. Mais avant de commencer, on va passer par de la théorie brièvement. Bonne vidéo.

### MCP Server/Client

**0:17** · Donc là, l'objectif de cette vidéo, ça va être de te montrer les MCP, comment on les utilise, quelle est la subtilité entre les serveurs et les clients et te montrer aussi pourquoi on doit les utiliser. Donc, j'ai résumé ça en trois mots. C'est rapide. efficace et personnalisable. Pour comprendre la subtilité, donc on a deux workflow comme je t'ai montré au tout début, on va avoir un workflow client et un workflow serveur. Si tu ne comprends rien encore maintenant, ne t'inquiète pas, je vais toutexliquer. Donc en premier, on a l'automatisation, donc un seul workflow qui va être le MCP client. Donc là, tu le vois, on a un MCP client qui est connecté avec un agent IA.

### 1 Server Workflow + 1 Client Workflow

**0:49** · Donc ça, tu as certainement déjà vu, on a un chat.

**0:53** · Donc dès qu'on va envoyer salut, l'agent IA qui sera connecté à un modèle de langage va répondre "Salut, comment ça va ?" Sauf que là la subtilité c'est que dans les tools, on a un MCP client. Donc c'est lui qui va donner les ordres aux outils serveur par rapport au prompt donné à l'agent IA. Donc maintenant, si on regarde le MCP serveur, donc il est connecté à tous nos outils. Donc là par exemple, on a du Google Doc, du Google Sheet, du HTTP, Postgress, de l'email SMTP, un sous-agent IA et du Google Calendar. Et lui le serveur, c'est lui qui va recevoir les ordres de MCP client et qui va exécuter les outils nécessaires.

**1:24** · Brièvement pour t'expliquer, si ici dans le prompt initial je dis qu'est-ce que j'ai à faire aujourd'hui ? Et bien le client va donner l'ordre au MCP serveur d'aller chercher. Alors où est-ce que Google Calendar ? OK, bon c'est ici. Ensuite qu'est-ce qu'il a besoin de faire ? il a besoin de savoir qu'est-ce qu'il a à faire aujourd'hui. Donc on va prendre un get all event et ensuite il va me faire une réponse. En gros pour vulgariser le MCP server c'est la boutique. C'est un workflowend configuré pour proposer des actions fonction à la demande. Il reste à l'écoute et attend qu'on vienne lui dire fais-moi ça.

### In short...

**1:53** · C'est un peu comme un webbook si tu en as déjà entendu parler et bien il ne va pas s'activer tant qu'on lui donne pas un ordre. Le MCP client et bien c'est le client. Donc c'est un nœud dans un autre workflow N10 qui demande ses actions. Il se connecte au serveur, regarde ce qu'il peut fournir puis lance des actions de la boutique. Comment ça marche ensemble entre client et serveur ? Le serveur publie un catalogue d'outils. Donc si on regarde ici dans mon automatisation côté serveur, et bien nous avons bien un catalogue d'outil hein. On a des outils sheets, docs et cetera. Le client va piocher dans ce catalogue pour enrichir son propre overflow.

**2:22** · Donc cette automatisation va faire une requête ici au MCP serveur et va piocher par rapport au prompt que j'ai donné sur qu'est-ce qu'il faut faire. Et le résultat c'est qu'on sépare la création des actions serveur de leur utilisation client, ce qui rend tout plus clair et réutilisable et modulable. Et tu vas voir pourquoi c'est extrêmement modulable. Voici un petit visuel simplifié qui peut t'aider à mieux comprendre la hiérarchie.

### Simplified visual

**2:41** · Donc sur la partie host et serveur, donc partie gauche les clients et partie droite le serveur qui comprend tous nos outils. À savoir que pour ceux qui sont un peu plus technicien, ce qu'on utilise nous dans le transport layer, donc dans la couche de transport, c'est le SSE. Si jamais tu veux mieux comprendre les MCP sur N10, je t'invite à regarder cette vidéo que j'ai déjà tourné. Donc, j'avais créé des illustrations, des explications très claires du MCP Server Trigger. Maintenant, soyons clair, pourquoi tu dois absolument connaître les MCP ? Car je sais que vous êtes beaucoup d'entre vous à avoir entendu parler des MCP, mais ça reste encore un peu flou.

### Better understanding in 8 minutes

### Why YOU NEED to know

**3:12** · On n'arrive pas à comprendre comment orchestrer, comment œuvrer, comment l'utiliser et en bénéficier.

**3:16** · Donc pour un débutant, maîtriser les MCP client serveur, c'est tout simplement comprendre l'architecture de base. Donc client serveur, c'est le fondement de tout service web. Tout fonctionne comme ça. Lorsque tu vas sur un site, ça fonctionne par client, serveur et les MCP l'illustrent correctement. Même si tu n'es pas du métier, tu n'es pas tech, tu n'es pas développeur. Regarde, il y a 3 ans, j'étais en train de faire des logos encore. J'étais graphiste. Je ne connaissais même pas ce que c'était un client et un serveur. Pour moi, un client et un serveur, c'est dans un bar.

**3:40** · Ensuite, tu gagnes en modularité. Donc, tu vas pouvoir séparer les actions serveurs de leurs exécutions clients. Ça va simplifier la maintenance et la réutilisation. Lorsque je me rends ici sur mon workflow, donc j'en ai deux, celui-ci c'est le workflow server. Et bien c'est très très clair. C'est plus simple à scaler, à moduler. Et ici, c'est le client. On évite de tout mélanger à un seul endroit, ce qu'on appelle la modularité. Ensuite, on facilite la collaboration. Donc chacun peut développer et partager ses boutiques d'action. D'autres workflow ou collègues les consomment en un clic. Ce qui veut dire que ici, je ne suis pas obligé de mettre 50000 outils.

**4:08** · Je peux très bien faire une spécialisation exemple que sur la partie business ou que sur la partie rendez-vous ou que sur la partie acquisition client. Pas obligé de mélanger par exemple des emails avec des bases de données postgès, avec des requê http. Là, c'est pour la vidéo que je vous fais ça pour vous montrer un petit peu l'essence de ces deux éléments. Ensuite, on prépare l'échelle.

**4:28** · Donc quand vos automatisations grossissent, cette approche permet de déployer, mettre à jour au scaler un module sans toucher aux autres, ce qui est vraiment très puissant et surtout ça va vous permettre de découvrir les appel externes et li donc vous apprenez à connecter une à n'importe quel service, donc des API, des agents IA via le protocole SSE. C'est un atout essentiel pour automatiser les tâches, je dis bien intelligentes. Si vous arrivez à comprendre client, serveur, vous arrivez à faire des connexions API, connecter des agents IA, sélectionner les bons modèles, plugguer des outils natifs, à partir de ce moment-là, vous avez fait des choses assez complexes pour un débutant. Ce qui veut dire que vous allez devenir meilleur très rapidement si vous commencez par les MCP.

**4:59** · Donc pour vulgariser, connaître MCP c'est donc poser de bonnes bases pour construire des workflow clairs, robuste et évolutif. Maintenant pour appuyer un peu sur la chose, pourquoi séparer clients et serveur ? On a un couplage trop fort.

### Why SEPARATE Client & Server

**5:12** · Donc toute modification de serveur impacte directement le client rendant les workflow fragiles. Donc en fait ça va solidifier la complexité accrue. Donc tout regrouper dans un seul monolite, je dis bien monolite rend la maintenance et la compréhension plus difficile. Ça c'est assez clair. Donc la duplication d'efforts, chaque workflow doit recréer les mêmes actions gaspillant du temps et de l'énergie. Et en dernier, on a l'évolution difficile. Donc impossible de déployer, tester ou scaler un composant sans affecter l'autre. Donc là c'est une petite représentation d'un monolithique. Donc c'est un peu le bordel, ça va dans tous les sens. C'est pas hiérarchisé. Maintenant, quels sont les bénéfices plus d'utiliser les MCP ?

### Benefits

**5:46** · Donc, comme je l'ai dit, modularité, donc séparation claire des responsabilité, serveur et client, réutilisation. Donc, un même serveur alimente plusieurs clients sans duplication logique. Comme tu le vois ici, hein, on a plein de clients différents, de tâches différentes qui n'ont rien à voir les unes entre les autres. Maintenance facilité, collaboration optimisée, donc backend et frontend peuvent évoluer en parallèle.

**6:05** · escalabilité donc scaling. Donc ce qui ressemble à ce visuel les clients boom qui envoi vers le serveur et les clients sont tous différents. Ça c'est ta boutique et bien a plusieurs clients qui vont rentrer. Assez parlé maintenant on va partir sur la démonstration et je vais te montrer tout ça.

### Full demo

**6:24** · On se retrouve sur Nen. Donc là on va tout simplement orchestrer. J'ai préparé septs. Donc on va pouvoir tester plusieurs prompts différents. va lancer dans la partie client ici et qui vont déclencher automatiquement dans serveur.

**6:35** · Donc pour vraiment vulgariser la chose, c'est très très simple. Là, je vais aller dans MCP server pour te montrer.

**6:40** · Voilà, donc le MCP server trigger, c'est très très simple. On choisit un chemin.

**6:44** · Donc tu peux mettre un chemin, tu peux mettre ce que tu veux. Ça va se mettre dans l'URL. Tu vois là, j'ai marqué table MCP. Boom, tu as le test URL et le production URL. Le test URL est bien pour tester lorsque l'automatisation est désactivée et le production URL, c'est celui qui va servir lorsque l'automatisation est active et que c'est fonctionnel pour envoyer des requêtes.

**7:01** · Là, c'est très simple, en fait, on a un seul serveur trigger et nous allons connecter tous les outils qu'on veut dessus. Donc là, j'ai mis des Google Docs. Donc on vient choisir bien entendu nos éléments. Là, j'ai fait du paramétrage. Alors, j'ai beaucoup cliqué sur les étoiles. Ça va dépendre des cas d'études et ce que tu veux faire. Mais par exemple, si on va sur get many event pour par exemple pour récupérer plusieurs événements à la journée, et bien j'ai cliqué sur les étoiles partout pour dire c'est Lia qui va décider d'aller chercher la bonne date, ce que j'ai à faire et cetera. Mais par contre pour le calendrier là, j'ai pas cliqué sur l'étoile pour pouvoir choisir mon calendrier. Donc en fait, il faut jaoger, il faut tester, ça va dépendre.

**7:34** · Pareil pour l'email en fait, tu vas voir. Donc j'ai mis mon email de base avec laquelle je vais envoyer, c'est l'email professionnel. Par contre, tout email, j'ai mis une étoile, ce qui veut dire que c'est Lia qui va décider.

**7:42** · Pourquoi c'est Lia qui va décider ?

**7:43** · Parce que si je lui dis envoie un email à abc@gmail.com LIA c'est à elle de remplir dynamiquement toute seule ici. Là c'est statique, là c'est dynamique. Donc je pense que tu as bien compris la subtilité. Donc là on va faire le premier test. Créer un document Google Docs et ajoute-y des conseils en business mental. C'est des promptes de testing he mais regarde, j'ai tout simplement besoin d'ouvrir le chat. Donc là en l'occurrence mon automatisation MCP client, elle est pas activée parce que ça fonctionne sans l'activer. Je lance le prompt. Donc on va regarder ce qui va se passer. Donc là, ça va faire péter l'agent qui est plugué sur le modèle 4.1 qui fait des requêtes vers le MCP client.

**8:15** · Donc là, tu vois, ça l'a bien interrogé, ça l'a fait interroger, ça fait des appel. Si je double clique sur mon MCP client, vers quoi il a fait des appels ? C'est comme une adresse web, il a fait des appels. Donc là, j'ai tout simplement collé l'URL qui vient du serveur. Donc il va faire des requêtes vers le serveur. Donc c'est l'URL qu'on retrouve ici dedans. Booum en production du coup parce que c'est activé.

**8:34** · Maintenant comme tu es en train de le voir, booum 6h58. Et bien là, j'ai lancé l'automatisation. On va cliquer dessus, on va voir ce qui s'est passé. Donc en fait ça va dépendre du nombre de requêtes qui a effectué, mais des fois ça peut te faire une de 10 requettes. Ça va dépendre en fait des tâches. Donc là regarde, première étape, qu'est-ce qu'il a fait ? Donc ça a envoyé la requête ici. Donc booum, il est parti sur la partie gauche, donc créer un document.

**8:56** · Donc il a fait un appel à create document. Et si on clique sur la deuxième requête, une fois qu'il a create document, qu'est-ce qu'il a fait ? Il a document. Donc là, c'est la subsidité de Google Doc, c'est que on doit créer un document et après on doit l'update. On peut pas créer un document et directement mettre du texte. Donc ça a fait deux requêtes pour effectuer cette tâche. Si on regarde les logs ici, update document, on peut regarder ce qui s'est passé. Et bien voici quelques conseils essentiels en business mental.

**9:18** · Donc bref, là c'est sur la partie technique logs, mais ce qui nous intéresse, c'est de regarder dans Google Docs, automatiquement grâce au MCP, nous avons automatisé la création d'un Google Docs avec la génération dedans. Premier test terminé. Et bien, on va enchaîner, on passe au deuxième. Donc maintenant, on passe sur le calendrier. Rappelle-moi ce que j'ai à faire dans mon agenda le 28 juillet 2025. Donc bien sûr, là je le fais en texte, mais ça pourrait très bien être avec un B télégram, ça pourrait être très bien avec des instructions vocales, ça pourrait être très bien automatiquement faire des requêtes, ça peut être beaucoup de choses. OK, donc là je vous envoie la requête, boum, qu'est-ce qui va se passer ?

**9:48** · Ben, c'est la même chose, hein, je vais pas le répéter. Donc là, du coup, le MCP client, ça fait des coles.

**9:52** · Là, on va regarder ce qui se passe dans le serveur. Tu vas voir les requêtes arrivées normalement. Booum. On va regarder rapidement donc la première requête. Tac. Donc normalement, c'est get many event sur cette requête là. OK.

**10:01** · Donc là, tu vois, c'est celui-ci, get many event. On voit qu'il a récupéré tous les événements du jour même. Et puis l'avantage, c'est que ben j'ai pas besoin d'aller de regarder les logs, hein. J'ai tout simplement besoin de regarder la réponse du chatbot. Il me dit "À 7h, tu as ça à faire, à 10h, tu as ça à faire et à midi, tu as ça à faire." Et si on regarde pour corréler avec les horaires exactement, voilà ce qu'on avait à faire 7h 10h, 30 et midh.

**10:23** · Donc il a bien réussi grâce au MCP à me dire ce que j'avais à faire automatiquement. On passe au troisème test. Donc là, ça va être recherche le projet Google Sheets test dataset et dis-moi ce qu'il y a dans la feuille.

**10:33** · Donc là, c'est très très simple.

**10:34** · J'envoie la requête, boum, on va dans le serveur, on s'habitue, on attend les exécutions pour voir ce qui va se passer. Donc première requête, on regarde. Donc là, il a fait intervenir Google Sheet. Tac tac tac. On double clique dessus. On peut regarder un petit peu ce qui s'est passé. Donc là, on voit quelle est la capitale de la France.

**10:49** · Traduit en anglais bonjour. N donc c'est un sheet avec plein d'éléments. Donc il a pu récupérer tout ça. Donc là c'était un sheet qui était déjà créé auparavant.

**10:55** · C'est un vieux sheets que j'avais. Et là, je lui ai fait intervenir pour qu'il me fasse un recap de qu'est-ce qu'il y a dedans. Et puis tu vois, comme tu vois, il a il a bien récupéré ces éléments-là.

**11:03** · Si on retourne dans le client, on regarde et il me dit dans l'output du chat, voici le contenu de la feuille.

**11:08** · Donc ID1, quelle est la capitale de la France, Paris, machin machin. Donc voilà, ça donne des idées un petit peu.

**11:12** · Si tu as des cheats, c'est que tu aimerais bien faire automatiquement des analyses de ces sheets avec un MCP. Ça peut être automatique ou manuel, hein, ça peut ou semi-automatique bien sûr, mais voilà, ça a fonctionné aussi pour cette partie-là. Et on peut passer au 4e test. Donc là, on commence un petit peu à jouer. On est plus sur du Google Sheet. Gmail, Doc, des trucs simples.

**11:27** · Google, on passe sur de la table postgress. Donc Postgress QL. Donc c'est parti. Alors là, je vais faire un refresh du chat, ça fait toujours plaisir. Donc là, résume ce qu'il y a dans ma table postgresse. Donc j'ai une table post grisse où en fait dans la communauté premium avec les membres que j'accompagne tous les jours en fait j'ai des news. Donc je scrap plusieurs réseaux sociaux, je récupère toutes les news I lm et je stack ça dans une base de données postge. Donc pour qu'on soit plus clair, je vais aller directement dans ma table. Je vais dans news du jour. Là, on va aller dans du coup le table editor, on va aller dans N8N chat histories.

**11:55** · Et en fait, c'est dans cette table là que tous les jours en fait, comme je scrappe les réseaux sociaux et je fais de la synthia, et bien j'ai stacké ça dans une table. Donc là, si j'ouvre en grand, on voit qu'il y a toutes les news qui sont tombées. Mais sauf qu'en fait, ce que je vais faire avec l'automatisation, c'est que j'ai envie qu'il me lise tout ça, il lisent tout et qu'il me fasse à peu près une un résumé de tout ce qu'il y a. OK ? Raison pour laquelle je retourne dans le client, je lui ai posé la question. Donc résume ce qu'il y a dans ma table post graisse. Grandes annonces, innovation majeur, opener, il prépare GPT5 na. Donc il a lu toutes les tables et il nous fait gagner un temps fou.

**12:23** · Après bien sûr l'objectif c'est pas de vous expliquer tout ce qui s'est passé, tout ce que j'ai setup dans dans les éléments-là, mais c'est tout simplement un select rose from a table in postgress. Voilà, il est configuré exactement comme ça où on vient faire son credential, sa connexion, on vient lui déterminer quelle table il doit aller lire. Donc là, c'était N and chat histories, la limite aussi. Et puis en fait, si on regarde, alors là du coup, ça va être sur le prochain où il a fait la requête.

**12:45** · C'est le dernier la dernière exécution.

**12:47** · OK. Et on va venir regarder sur le post grace qu'est-ce qui s'est passé. Tac.

**12:50** · Voilà, il a tout récupéré. Donc tout tout toutes les tables pour en faire un résumé synthétique. Donc si on regarde les log sur cette partie-là, MCP server trigger, boom, interroger directement POS SQL. Alors pour la subtilité, si tu veux voir comment j'ai configuré mon agent hier, c'est vraiment très simple.

**13:04** · Regarde ce que j'ai mis. Tu dois toujours appeler cet outil MCP client et effectuer les actions que je te demande vers les MCP clients. Donc rien de bien compliqué. Là, c'est vraiment pour te montrer le contexte. Après, tu peux aller beaucoup plus loin dans les instructions. Donc voilà pour la base de données Postgress. Maintenant, on va jouer avec le test 5. Donne-moi le conseil du jour, coach en prise de décision. Donc là, en fait, ce qui va être cool, c'est qu'on va faire intervenir et on va jouer avec la dernière mise à jour, une des dernières mises à jour bien sûr parce que ça va trop vite sur Nuten, c'est la 1.103, la version 1.103 à partir de cette version là. Donc je vais te montrer un petit peu comment ça fonctionne. Boum, j'envoie la requête, donne-moi le conseil du jour coach en prise de décision.

**13:36** · Donc je vais aller dans le serveur, on va attendre pour voir pour te montrer directement qu'est-ce qui va se passer quand je lui dis ça. Voilà, on a la requête qui est arrivée. 7h06, je clique dessus. Et bien là en fait, on a fait intervenir un nouveau nœud qui est super puissant, qui est tout nouveau depuis la 1.103 qui est un sub agent. Donc tu vois, c'est pas un agent IA comme on a l'habitude de les voir en rectangle, c'est un arrondi plutôt oval, tu vois, mais c'est un subagent. Donc on a fait intervenir celui-ci, il a été entraîné très simplement, c'est des instructions basiques conseillé et journaliers en prise de décision.

**14:04** · Voilà, il te dit directement chaque jour des conseils, il a été entraîné pour ça. Et en description, du coup, ses coaches spécialisés en conseil du jour appellent cet agent à chaque demande de conseil.

**14:14** · Donc, sachant que j'ai demandé un conseil, si on retourne dans le client et qu'on regarde ici, regardons un petit peu. Voici le conseil du jour pour la prise de décision proposée par le coach.

**14:22** · Limitez vos tâches à trois priorités, clé par pour la journée, n voilà, bénéfice, source. Et là, en fait, il nous mentionne des sources. Donc ça, c'est assez puissant. Ça permet de pouvoir faire des agents. Alors, je te laisse imaginer là, bien sûr, on peut aller plus loin, on peut aller beaucoup plus loin. Là, on pourrait mettre une mémoire, on pourrait mettre un zep, on pourrait mettre tout simplement un post grel qui va tout stacker.

**14:37** · On pourrait mettre des outils aussi, des codes tools, on pourrait mettre beaucoup de choses qui pourraient doper cet élément là et le rendre très puissant où on pourrait même en fait de part sur MCP Server Trigger se faire uniquement une armée d'agent, une armée de sous-agent comme ça, boum, avec des modèles différents, des subtilités, certains avec des mémoires, certains avec pas de mémoire. Voilà, tu as compris un petit peu, mais on peut pousser la chose. Donc super pour cette partie-là, on passe sur le 6e test. Donc le 6e test, ça va être super intéressant parce qu'on va faire du coup une requête http.

**15:03** · Donc ça change un petit peu hein, tu vois cette vidéo, elle est très variée. Ça te permet de voir un petit peu des choses plus simples comme Google Docs, comme Sheets, ensuite Postgress, ensuite de l'IA, donc du sous-agent des requêtes HTTP donc comme celle-ci. Là, il me dit "En ce moment à Paris, la température est d'environ 16,9°. Si tu veux la météo pour une heure précise ou d'autres détails, fais-le-moi savoir." Donc là, c'est cool ce qu'il me dit, mais là, je le crois. Et pourquoi je le crois et que je sais que c'est pas une hallucination ? Parce qu'on va aller regarder directement les exécutions. Donc là, ça va arriver. Boum, nickel. Et qu'est-ce qui s'est passé lorsque je lui demande une requête de météo ?

**15:34** · Qu'est-ce qu'il fait ? Il a un MCP directement connecté en HTTP sur une API gratuite de prévision météo. Donc là, là, je l'avais mis en anglais. Make HTCP record. Donc fais une requête HTTP, retourne la réponse à chaque fois qu'on te demande la météo à Paris. Donc voilà, ça a été une requête méthode GET. Voilà avec l'URL de la météo et puis tu vois en fait le MCP il a récupéré tout ça, tous ces éléments-là bam tout récupéré pour pouvoir donner la météo actuelle du jour. Donc du coup c'est officiel, il a pas récupéré ça, il a pas eu d'hallucination ou quoi que ce soit.

**16:04** · Donc pareil pour les requêtes HTTP, on peut venir les faire intervenir. Donc je te laisse imaginer que ça soit du AGN, que ça soit tout en fait tous les éléments qui ont des API, tu peux les connecter à ton serveur trigger et faire des trucs de fou furieux. C'est n'importe quoi. Et en dernier, j'aimerais te montrer envoie un email de bienvenue à ma newsletter coach en séduction à alors là, j'ai à ma newsletter. Bon, c'est pas grave pour ma newsletter. Et j'ai mis une adresse email Kamikaz pour te montrer un petit peu. Donc là, c'est pareil. Boum boum boum, on enchaîne, j'envoie la requête.

**16:30** · On va regarder le serveur, donc les les exécutions, c'est très important de regarder les exécutions. Je vous recommande fortement de faire ça. En tout cas, je recommande ça aux membres de l'accompagnement. C'est vraiment ici qu'on va lire les logs, qu'on va comprendre comment la data transitionne, comment ça fonctionne, queon apprend énormément. Donc là en fait voilà, il a fait intervenir le mail SMTP, donc le mail professionnel. Si on double clique dessus et qu'on regarde les logs, voilà, on a directement l'outputie. L'agent a forcément généré automatiquement un objet et un texte. Pourquoi il a fait ça ? Parce que ben l'objet et le texte de l'email a été coché avec l'étoile.

**17:01** · Donc je l'ai dit, c'est l'A qui choisit, c'est Lia qui décide par rapport à mon input. Donc maintenant, si je vais sur l'adresse email Kamikaz exactement ici.

**17:09** · Donc là, ça va normalement arriver. Très bien. Et puis nous avons reçu un email.

**17:12** · Bienvenue dans la newsletter du coach en séduction. Euh, bienvenue l'équipe coach en séduction MCP client. Alors là, tu vois, il a signé carrément. Là, il faut pas que tu l' faut que tu fasses gaffe, faut que tu dises de signer avec un nom parce que si ici sign en tant que MCP client, ça va pas le faire. CCH en séduction MCP. Donc voilà pour cette vidéo, c'est vraiment une vidéo assez claire, assez large et c'est d'élargir un petit peu la compréhension des choses pour te montrer à quel point qu'on peut faire énormément de choses. En fait, c'est illimité. C'est-à-dire que là, si je te montre un petit peu, ça peut te donner des idées éventuellement, mais si tu cliques sur le plus déjà nativement, tu peux faire énormément de choses. Tu peux même faire intervenir d'autres workflow.

**17:43** · Tu vois, tu as le call N workflow tool. Si tu as d'autres workflow et que tu as envie de faire quelque chose de plus modulaire et tu as plusieurs workflow, tu en as une dizaine. Tu veux faire intervenir un workflow A, B, CD et cetera, tu peux le faire. Code tool, c'est pareil. Le HTTP, donc tous les modules qui ne sont pas natifs. Exemple, je crois que Instagram n'est pas natif. Ouais, il n'est pas natif et sur N10. Et bien là, tu vas faire intervenir l'HTTP. Donc là, le MCP client tool, c'est pareil. Tu peux faire aussi intervenir un MCP client tool.

**18:08** · Donc ça, j'en ferai certainement une autre vidéo, mais on peut faire intervenir des MCP client tool dans les MCP server trigger. les bases de données vectorielles, tu vois, Zep, Postgress, je sais qu'il y en a beaucoup d'entre vous qui sont sur Soupabase, qui sont sur Qudrante, il y a Open Source, Air Table, plein d'autres outils. Donc chacun de ces outils, tu peux les faire intervenir et tu peux faire des choses très très intéressantes. J'en profite pour te dire que si jamais tu veux être accompagné à prendre Anen et le prompt Genering en 90 jours, assister à des lives techniques chaque semaine où nous réglons des automatisations, nous aidons les membres avec un comité d'experts spécial, donc des mastermind chaque semaine.

**18:38** · Tu peux cliquer sur le premier lien dans la description, le premier commentaire épinglé et tu prends un appel avec un de nos success managers pour nous rejoindre. Si ça t'a plu, n'hésite pas à liker, partager et commenter. N'hésite pas à commenter si tu as des questions, des recommandations, des idées ou des choses que tu as pas comprises. Je t'aiderai par rapport à ça. Et nous on se dit à très vite pour une prochaine. C'était May. Ciao !