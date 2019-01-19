# Static Site Generator

---

## Not finished enough to be usable just yet!

It will be in the future though. I am actively working on it. Check back soon! Don't use it just yet! When it's in a usable state, I will delete this section from the readme.

---

## What is Static Site Generator?

This project is intended to be an alternative to Jekyll for generating static blogs and landing pages. It will be made with Python 3.x. It is very much a work in progress.

---

## Who is Static Site Generator intended for?

**Everyone, but it is especially aimed at people who want to make websites without knowing how to code.**

It's an alternative to writing a website from scratch. It's also an alternative to a static site generator like Jekyll. It's also an alternative to a CMS such as Wordpress, which increases your attack surface by putting a lot of potentially insecure code on your website's server. SSG is simple and easy, and leaves your site with less things that can be hacked compared to a content management system. If you use Wordpress, you constantly need to update it because of all the security vulnerabilities. Even Wordpress plugins can be insecure. Static HTML pages are less of a security liability. You still should use HTTPS and update the software on your server, but that's not too hard by comparison. Also, if you use GitHub Pages, then you never have to worry about any updates, and you also get HTTPS without having to manually set up a certificate. 

Long story short, it's a very simple way to make a minimal and relatively secure website, even if you're not a developer.

---

## What are the dependencies for Static Site Generator?

Install the latest version of Python 3. You can download Python [here](https://www.python.org/downloads/). 

In addition to Python, you need [pip](https://pypi.org/project/pip/). You will also need to install [jsonschema](https://pypi.org/project/jsonschema/), which can be installed with the following command:

```
pip install jsonschema
```

It can run on Windows, macOS, and Linux. Just make sure your path variable is set up correctly so you can run generator.py as either ```python3 generator.py``` or ```python generator.py```, or even:

```
chmod +x generator.py; ./generator.py
```

---

## Do I need a domain name or web server in order to make a site with SSG?

If you use GitHub Pages, you don't need either. You can optionally add your own domain name to GitHub Pages if you want. I will add instructions for how to do that later.

Or you can use it on your own server and domain name. Then, you would be using FTP or some other method of copying files to it. Some shared web hosts even have a web-based interface that makes it easy to copy files to the server. Depending on your web host, you might be able to literally just log in and drap and drop files in the file manager (such as on cPanel).

---

## Everyone should have a website!

Social media comes and goes. The social media apps/sites you use today might be gone in a few years. But your site can be an anchor point, and have links to all of your social media profiles, as well as other ways to contact you.

A website can look good on a resume (well, depending on what you put on it), and it can also be a good way to express yourself by having the ability to post your own content. It can also be good to see progress you make over time, such as if you make a blog to show your progress with learning something new.

---

## What kinds of sites can be made with Static Site Generator?

Blogs/personal sites! You could also use it for an online portfolio as a kind of supplement to a resume. 

Static Site Generator makes static, relatively non-interactive websites (though I could add Disqus functionality in the future so you could have user comments, but that's currently not a feature this program has yet). 

Basically, if you want a simple blog that has information about you, and lets you post articles/blog posts, this is the program for you. You do not need to know any coding at all. Not even HTML or CSS. This program makes that all for you. It puts your content into a layout.

There's an about page, where you can add info about yourself (or really anything you make the site focused on). And you can make articles, much like Wordpress or Jekyll. You can also edit or delete articles. 

SSG uses a design concept called pagination, which means there are only a limited number of articles per page in the blog pages. The main site page shows the 5 latest articles, as well as a link to the about page, and some social media links in the footer. If you have more than 5 articles, you will be able to see older ones by clicking the button at the bottom to go to the next page. These 5 article preview pages have the title, author, date, leading image, first sentence, and first paragraph. This lets your site's readers see a preview before determining if they want to read the full article or not. If they like the preview, they can click the "read more" link to view the full article, which contains the body text (as well as everything else).

SSG uses something called responsive design, which means the pages are intended to look good on both computers and mobile devices. If you resize an SSG website page in a browser window, you will see that the site "responds" to being resized. 

---

## Can I see an example of what a site made with SSG looks like?

Check out [https://alans100daysofcode.com](https://alans100daysofcode.com). **NOTE:** my website is currently based on Jekyll, but I will be migrating it over to SSG soon. 
      
## How can I make a website with Static Site Generator?

Click the download button to download the repository. Then unzip the zip file. From there, run **generator.py** with Python 3. For example, open a terminal and then type **python3 generator.py**. I will make detailed OS-specific instructions in the future to make it easier. For now, this is just a basic explanation.

**generator.py** is what you will use to make a new project or open an existing one, and then manage your site, such as adding, editing, or deleting articles. 

The only static files you will put on your site are in your project's folder's **website_files** subfolder. If you want, you can use FTP or even a web interface to upload these files to your site. None of the other files need to be uploaded. If you have your own web server, put these in your public www folder. You can also use git and GitHub Pages, but I will add more details for that later.

If you want to add images, put them in your project folder's **images** subfolder. Then, when making or editing an article, you can specify the filename for the leading image. You can also just add regular HTML to the body portion of the article.

### Currently command-line only

The first version of this program will be command-line only. Later, I will add GUI support. But that will come only after the basic text-based version is done.

Example usage:

General usage for text prompts:

```
python3 generator.py
```


Opening an existing project:

```
python3 generator.py --open project_to_open
```

Or even a more brief way:

```
python3 generator.py -o project_to_open
```

Making a new project:

```
python3 generator.py --new new_project_name
```

Or the faster way:

```
python3 generator.py -n new_project_name
```

### Step-by-step getting started instructions: Windows

I will add this later.

### Step-by-step getting started instructions: macOS

I will add this later.

### Step-by-step getting started instructions: Ubuntu Linux

I will add this later.

---

## How it works

**generator.py** allows you to either open an existing project, or make a new one. The projects are stored in the projects subfolder. Don't modify anything unless it's in the projects folder. If you make a project called whatever, it will make a folder within the projects folder called whatever. 

When you open a project, it checks for a directory located in the projects folder with that name.

### What happens for CRUD (create, read, update, delete) for articles

- The order for adding a new article is as follows: user chooses from menu to make new article → user input for content → dictionary in RAM is converted to json → article_name.json (and also added to articles.txt, and count.txt is incremented) → regeneration → article page placement/order processed and stored in order.json → all articles, including the new article_name.json, are read and then parsed and written in pageX.json for as many pageX.json files are necessary (they each correspond to an HTML file containing 5 article previews) → HTML/CSS template applied to pageX.json files, turned into index.html, page1.html, page2.html, etc → new article_name.json file is used to create article_name.html file (but all the other article html files are untouched because there is no need to update them) → static website has been updated
- article edit and delete functionality should be similar, with only slight differences, and the common functionality needs to be put into functions so that these three operations (create, updatae, and delete) aren't containing a lot of redundant copied and pasted stuff
- read (the last part of create-read-update-delete that I didn't mention yet) will be very easy because all it does it check if an article exists and then read the appropriate json file and display it to the user, perhaps even only showing a specific part that they request (such as lead image, title, body text, etc.)
- maybe "edit" can be just replacing a field entirely rather than showing it to the user, like edit → what do you want to edit? title → enter a new title (and if they really want to edit the stuff themselves, they can always view the static HTML file and then copy and paste it in a different editor)
- There is a special case if the number of articles is not evenly divisible by 5, and then the last page with the oldest articles will be based on a separate template that has fewer entries. They are named X_articles.html, where X is a number. The only exception is 1_article.html which is not plural at the end.

### The files and folders in this project:

#### This is outdated! Needs to reflect the current changes!

Basically similar project template stuff but I removed some other stuff

If you make a new project, use generator.py and choose the appropriate option through the menus, and it will make a new folder with the name you specify. Within that folder, it will make the following things:
- **article_json folder**
    - stores json files that contain the content of your articles. This separates content from presentation. These JSON files are used along with the template files in order for generator.py to generate the static html.
    - The first one in the example project is example_article.json, but that's not a real article and I might remove it at some point after I finish developing everything. Or maybe not.
- **page_json folder**
    - There are 5 articles per page. This is called pagination. The page JSON files are generated based on the articles, as specified in articles.txt, and then fetched from their respective JSON files in article_json. If you have 25 articles, there will be 5 pageX.json files. If you have a number of articles that is not divisible by 5, that's where some special 1-4 article templates come into play, and there will only be the extra 1-4 articles instead of the entire 5. index.json is always the last page, which becomes index.html. It goes in reverse order (NOTE: maybe I am wrong about this and should clarify the order?): the oldest (first) articles you make will be on the last pages. This is because, nowadays, with social media, we want to see the newest stuff first, even if it was written after the first stuff. So if you have 25 articles, page1.json will have the oldest articles, and page4.json will have some newer articles, but index.json will have the absolute newest, essentially being equivalent to page5.json (in this specific example, at least). UPDATE: index.html has the latest articles. When you click next, it will lead to what is called page2.html, which will just be older articles than index.html. But if you had 5 pages worth of articles, page5.html would actually have the oldest articles. The order and pages change based on how many new things there are. But your oldest articles will always be on the last page, whether it's page 5 or page 100. 
    - order.json determines the order of articles based on user-provided timestamp rather than actual timestamp. For example: a user can upload an old post they wrote a long time ago. Maybe they wrote something in 2017 but only made a website in 2019. The user specifies the timestamp, so even if you posted a 2019 article before the 2017 article, the one specified as earlier based on the user's input for the article creation/editing will go first (which means it will be below the newer stuff, based on the way the timeline is designed)
- **schemas folder**
    - Contains schemas for JSON validation
- **settings folder**
    - This contains a few important files that determine the settings/configuration of your project. 
    - **about.json**
        - Special page that contains information about you, the author/owner of the website.
        - It can be a good idea to describe your skills, who you are, what the site is about, or how people can contact you.
    - **articles.txt** contains the filenames of all the articles. This lets the generator know which JSON files to look for, but you don't have to use the JSON yourself. Keep in mind the filename is not the title. You could have a filename like "dont_use_spaces_or_punctuation_except_underscores" and you can make the title "Don't use spaces or punctuation except underscores." Don't edit articles.txt. It is a file used by the generator, which automatically deals with this itself.
    - **count.txt** just contains the number of articles.
    - **settings.json** has some site settings in it, such as author name, social media links, and the website name. The website name doesn't have to be the same as the project name, though it can be. The project name should be simple, like *mysite1*, and your site name can be something like "Here's my awesome website!!!!!" In the future, I might also add extra settings that will let the user tweak the site more. But for now, it's pretty simple. The goal is to make a simple static site generator that is easy to use, without too many features.        
- **templates folder**
    - These are all templates that should only be copied and then the generator.py uses a find-and-replace action to populate them by searching for the placeholder values and replacing them from values fetched from JSON.
    - **index.html** is a 5-article template that is used to generated an HTML page the 5 latest articles on the site, based on user-specified timestamp rather than user creation date. That is why regex is important to enforce the use of correct timestamps. Sorting by timestamp will be an interesting challenge when I finally get to that. 
    - **article.html** is the template for generating an article's HTML page. All the placeholders will be replaced, including the filename. They are copied to the outermost directory of the website_files directory so that someone can just put them all in a /var/www or /var/www/public_html type folder and have everything on example.com/article_name.html as opposed to example.com/html/article_name.html or something like that.
    - **about.html** is the only "page" rather than an article. By page, I mean static content that is not an entry. It doesn't have a timestamp or author name associated with it. It's just about the website and/or its creator. It's suggested to use this section to link to your social media profiles, although there are a couple at the bottom of the page at the moment. This current setup might change in the future, and perhaps I will extend the features of the social media FontAwesome glyphicon footer. But for now, it is static just for the sake of simplicity because then all I have to do it find-and-replace file operations instead of inserting or deleting stuff at certain points in the file, which is easier said than done.
    - **5_articles.html** is basically the same as index.html but I named it separately so I don't get as confused when programming it. It is used for non-index pages that have 5 articles in them. It's a template page for putting 5 article previews. Then readers of the website can see if they really want to view the full article or not. Each article preview has the lead image, title, etc. but not the full body text.
    - **4_articles.html, 3_articles.html, 2_articles.html, and 1_article.html** are all templates exactly like **5_articles.html** except with fewer article placeholders per page. There is probably a more efficient way of doing this, but I don't care because this is easy to understand and program. If you have 19 articles, index.html will be used for 5, and then 5_articles.html will be used for the following 10. Because you are left with a remainder of 4, you cannot use the 5_articles.html template to base your finally-generated static pages on. So based on the number, it will be templated based on one of the 4 "remainder" templates. Only the final page will have a number of articles that are not 5. index.html is always 5 articles, and so are subsequent articles until you can no longer subtract 5 from the remainnig amount. This stuff all sounds easy when you're reading it, but manually programming pagination is a bigger headache than you might imagine. It's especially challenging because this is *social media timeline order* rather than *pages in a book order* so you can't merely append something without changing everything else.
    - You can customize the templates if you want! It will change what your site looks like, and you will only have to update the templates once instead of every single time you write an article. That's the power of this templating system. I'm vaguely familiar with stuff like model-view-controller architecture, and while this isn't 100% like that, I at least learn about how separation of concerns is important, and how you want to has content be stored separately from layout.
- **website_files**
    - My goodness, writing documentation is time-consuming! But it not only helps people understand what this project does, it also helps me figure out the details of what exactly I need it to do!
    - This is where all of the final output static HTML files will go. If you want to set up git, ```git init``` in this directory. If you are doing FTP/SFTP/SCP/SSH/web-based file manager method of copying files, copy all of the files that are in this folder to your website. DO NOT DIRECTLY PLACE the entire website_files folder into your htdocs or public_html or www or whatever it is that your public-facing directory is on your web server. Place the CONTENTS of the website_files folder in your /var/www, not the folder itself, unless you want the path to be example.com/website_files/index.html, which is probably not what you want!
    - The other html files mentioned here are template files, which should never be directly on your site. They are merely copied into this directory, then worked on by the generator to replace the placeholder content with the real content that it retrieves from the appropriate json files. take a look at the HTML templates and you will see the obvious placeholders where content goes instead. 
    - The stucture of the website_files is as follows:
        - **css subfolder**
            - contains the site.css file, which determines what all of the pages look like.
        - **images subfolder**
            - Put all of your images here. You can (and should) use leading images with articles, which will show up in the 1-5 article preview pages. Having a leading image makes the blog post stand out more and will increase the chances of someone clicking on it. The leading image also shows up in the full article.html file. 
            - You're not just limited to leading images. You can add extra images elsewhere in the body of the article. In fact, you can write straight-up HTML to add them, whether it's for img tags, or whatever else you want. 
            - When linking to images with an img path, use a relative path and remember that images will be in example.com/images/filename.png
            - The two images that come with SSG are:
                - **favicon.gif**: shows up in the little browser tab icon, or if you're on mobile, you can make a homescreen shortcut that will show the favicon. For more info on favicons and how to make them, google it. I migh tadd more documentation here later, but it's not an advanced concept.
                - If you want to change the default logo of the website, edit or replace logo.png in this folder only. It should be 510x56 pixels and it needs to be a png called logo.png unless you want to manually update all of the template files. 
                    - Why 510x56? I don't know, it just kind of ended up happening that way when I made a previous website. I made a different website, then scrapped the idea and made something entirely different for that site. What I was left with was a nice and minimal but aesthetically pleasing frontend that I never got to use for a real project. that's where this project's templates are derived from. I am essentially salvaging a defunct project and recycling it into this new one.
        - Loose HTML files
            - These files will be the article preview/timeline pages, about page, and specific article pages. This allows you to have example.com/page.html without any additional directories, like example.com/whatever/something.html which looks messier. Of course, you could use more modern backend server platforms and have "routes" to have something like example.com/post1 instead of example.com/html/post1.html, but that is beyond the scope of a static site generator, which is not a full stack app, nor is it a fully-fledged CMS. It is a minimal alternative, more comparable to something like Jekyll. That being said, it's very different from Jekyll, because when I used it, there were lots of things I disliked about it. It is also slightly influenced by Wordpress, because that's something else I have been using for years. And also just old-fashioned web 1.0 HTML/CSS-only sites with no interactivity. It's a mish-mash of lots of different ideas.
            - index.html will be the example.com page. Instead of it being example.com/index.html, you can go directly to example.com and it will show that page. That's how most web servers (and GitHub Pages) work by default. 


---


## I found a bug, have a question, or a suggestion!

Please make a GitHub issue or pull request, or email me or message me on Twitter. I appreciate feedback, but this project comes with no warranty.

---

## License

This project is released under the GNU GPLv3. 