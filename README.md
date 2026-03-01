# CS-340
Client/Server Development

# How do you write programs that are maintainable, readable, and adaptable?
To keep code maintainable, readable, and adaptable, it should be concise, well-commented, and variables and functions should be sensibly named. Beyond this, a large part of writing programs with these qualities means building code that is limited and focused in its scope. This helps keep code reusable, rather than the code being specifically built to work with only one system. For this project, it meant that the code for the CRUD module was written before any work was done on what would be the final interface for the animal shelter database.

# What were the advantages of working in this way?
By working in this way, I could be sure that the base functionality of the system worked before anything else was built off of it. This ensured that the program had a sturdy foundation and reduced potential technical debt that could have come from a fundamental part of the system being defective. This also made testing easier as any errors I encountered could be assumed to be with how the base code was being employed rather than a problem with the base code itself.

# How else could you use this CRUD Python module in the future?
Because the CRUD Python module is built to be general, I could use it in the future to aid in practically any other Python-based project that involves manipulating a database. This module could be used in databases other than the one for the animal shelter used in this project. For example, this module could help manage databases of products in a store's inventory, a database of employees, or a database of tree in an arboretum.

# How do you approach a problem as a computer scientist?
I approach problems as a computer scientist by first considering what is being asked in terms of what data is given and what data must be represented. This mentality allows me to devise the functional requirements of a program, with the nonfunctional requirements then being considered by thinking about how users will actually engage with the software. Additionally, the ethical requirements of the software must be considered at all times, with users' privacy and security being treated as paramount.

# How did your approach to this project differ from previous assignments in other courses?
My approach to this project differed from previous assignments in other courses primarily due to how this project involved linking multiple different layers of components together in the form of MongoDB, PyMongo with Jupyter Lab, and finally the Dash framework. This meant that I needed to more or less fully complete my work on earlier layers of the program before I was able to work on subsequent layers. This was unique compared to previous assignments I have worked on that typically involve adding functionality to the same component layer with perhaps the only separation being which file code is being written for.

# What techniques or strategies would you use in the future to create databases to meet other client requests?
To create datatabses to meet other client requests in the future I will employ a similar strategy of building a stable base layer of functionality. This strategy kept my development focused and reduced the chance of introducing new bugs into the system by adapting older code to fit newer code. I will also likely specifically design functionality similar to the CRUD module built for the project in this course as the functions of creating, reading, updating, and deleting elements are applicable to practically any system meant to manipulate a database. 

# What do computer scientists do, and why does it matter?
Computer scientists address real world problems by representing systems in code and building the functionality to work with them. Because computers work very quickly, processes can done faster on these digital systems. This can be seen in this project with how a large database of animals in an animal shelter can be sorted through in a matter of seconds, whereas sorting through physical files manually would be an incredibly arduous process. Beyond this, computer scientists can also build models for things that would be too costly or dangerous to test in the real world. 

# How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
My work on this type of project would help a company do their work better by expediting their process of working with data and thus saving both time and money. In the case of Grazioso Salvare in the project, this means that the company could spend less time sorting through fitting candidates for rescue dog training and more time actually training and evaluating dogs.
