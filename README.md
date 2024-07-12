# WidePen | CS50W Capstone Project

WidePen is a web application built with Python and JavaScript as specified in the CS50W capstone project. It is designed for publishing tech-related content such as articles and project summaries across various categories like Python, Excel, Machine Learning, Deep Learning, and Data Science. It serves as a platform for users to share their knowledge and experiences within the tech community.

## Distinctiveness and Complexity

The genesis of this project idea was rooted in a steadfast commitment to addressing a specific gap in the tech community: the need for a platform that not only showcases the work of tech enthusiasts but also renders it accessible to those without a technical background. While the choice of this undertaking may seem divergent from the conventional projects within the course, it is precisely the expertise gained from the program that has made the realization of this distinctive and complex idea possible.

What sets this project apart is the deliberate utilization of cutting-edge concepts and technologies. Complex search algorithms form the backbone of the platform, ensuring that users can efficiently navigate through a myriad of showcased projects. The integration of CKEditor goes beyond mere text editing; it provides contributors with a tool for crafting visually captivating presentations, making the content not only informative but also engaging for a broader audience.

The sophistication of the project is further heightened by the incorporation of BeautifulSoup for content extraction. This ensures that the platform not only presents information but does so in an organized manner, contributing to the overall user-friendly experience. The infusion of JavaScript introduces a layer of interactivity that transcends the ordinary, creating a dynamic environment where users can actively engage with the featured content.

Bootstrap, with its responsive design elements, serves as the linchpin in this technological symphony, harmonizing the diverse components into a seamless and visually striking whole. The adaptability across devices enhances accessibility, ensuring that the platform remains user-friendly regardless of the audience's technical proficiency or the devices they use.

In essence, the distinctiveness of this project lies not only in its unconventional objective but also in the strategic amalgamation of sophisticated technologies. The complexity arises from the intricate interplay of these elements, resulting in a platform that stands as a testament to the fusion of innovative ideas and technical prowess acquired through the course. It is this very combination that propels the project beyond the ordinary, offering a unique and intricate solution to the identified challenge in the tech landscape.

## File Content

In the project directory, you'll find essential files in 'static/widepen' that contribute to the infrastructure of WidePen's web application:

- library.js
- styles.css

The 'templates/widepen' directory is a treasure trove of HTML templates, shaping WidePen's user interface and functionality:

- bookmark.html: displays the postcard of bookmarked publications
- error.html: showcases error messages
- index.html: the homepage featuring all publications and categories
- layout.html: the main UI layout of the web application
- login.html: handles user log-in
- post_card.html: houses the postcard for all publications, eliminating code duplication
- post_read.html: displays an entire publication
- profile.html: showcases user information
- profile_edit.html: manages user credential edits
- publish_edit.html: oversees user edits on their publications
- register.html: facilitates user registration on the platform
- search.html: showcases search query results
- user_writes.html: the space where users write and publish their work

In addition to these templates, 'admin.py,' 'forms.py,' 'models.py,' and 'urls.py' play vital roles in shaping and governing WidePen's functionality:

- **admin.py:** manages content displayed on the admin page
- **forms.py:** houses forms used throughout the project
- **models.py:** contains two models (User and Post); the User model collects user credentials, while the Post model gathers information on user publications
- **urls.py:** handles all URLs for our Django web app, linking to the views with the host URL
- **views.py:** contains functions for the web application, facilitating HTTP request and response interactions

## How to Run

To initiate WidePen locally, follow these straightforward steps:

1. **Clone the repository:** `git clone https://github.com/o-tobi/WidePen.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run migrations:** `py manage.py makemigrations` and `py manage.py migrate`
4. **Start the development server:** `py manage.py runserver`

Access the WidePen application through your web browser at http://localhost:8000 (or the specified port).

You can watch a demo of this project via: https://www.youtube.com/watch?v=Btvdy6WQOI8
