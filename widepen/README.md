
# WidePen

WidePen is a web application designed for publishing tech-related content such as articles and project summaries across various categories like Python, Excel, Machine Learning, Deep Learning, and Data Science. It serves as a platform for users to share their knowledge and experiences within the tech community.

## Features

- **Publication Creation:** Create and publish articles or project summaries.
- **Category-based Organization:** Sort content into specific tech categories for easy navigation.
- **Technologies Utilized:**
  - Beautiful Soup: Used for web scraping and content extraction.
  - CKEditor: Enables a rich text editing experience for content creation.
  - CSS & Bootstrap: Ensures a responsive and visually appealing design.
  - JavaScript: Enhances interactivity and functionality.
  - Pillow : Handles media uploads.
- **Responsive Design:** Accessible on various devices and screen sizes.

## Installation

To set up WidePen locally, follow these steps:

1. Clone the repository: `git clone https://github.com/o-tobi/WidePen.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `py manage.py makemigrations` and `py manage.py migrate`
4. Start the development server: `py manage.py runserver`

## Usage

1. Access the application via your web browser at `http://localhost:8000` (or the specified port).
2. Create an account or log in if you already have one.
3. Explore categories or create your publication.
4. Write articles or summaries in your preferred tech field.
5. Enjoy sharing your knowledge and experiences with the community!

## Models

WidePen utilizes two main models to manage data:

1. **Post Model:** Stores information about articles or project summaries, including their title, content, category, author, and publication date.
2. **User Model:** Manages user profiles, containing details such as username, email, full name and profile picture.

## Distinctiveness and Complexity

WidePen stands out from other similar projects due to its multifaceted approach. Not only does it offer a comprehensive range of tech categories for publication, but it also integrates a user-friendly interface with a responsive design, ensuring accessibility across various devices. The complexity of WidePen lies in its amalgamation of diverse technologies such as Beautiful Soup for content extraction, CKEditor for a rich text editing experience, and JavaScript to enhance interactivity, resulting in a seamless and dynamic user experience. Moreover, WidePen's fulfillment of the CS50W course requirements as a capstone project demonstrates its adherence to industry-standard development practices, ensuring a robust and sophisticated web application.

## Templates

WidePen includes several templates to facilitate different functionalities:

- **bookmark:** Displays publications bookmarked by the user.
- **index:** Contains all publications available within the application.
- **layout:** Contains the navbar and provides the structure for other templates.
- **login, register:** Handles user authentication and registration.
- **search:** Facilitates publication search functionality.
- **profile, profile_edit:** Manages user profiles and profile editing.
- **post_read:** Allows users to read selected publications.

## File structure

Capstone: Django project settings and configurations.
WidePen/static: Contains all CSS, JavaScript, and image files used in the project.
WidePen/templates: Holds all HTML files for rendering views.
WidePen/views.py: Contains all view functions handling the application's logic.
WidePen/urls.py: Manages the application's URL patterns.
WidePen/models.py: Houses all the models created for the WidePen project.


## Credits

This project fulfills the requirements of the CS50W course and serves as the capstone project demonstrating proficiency in web development principles.



