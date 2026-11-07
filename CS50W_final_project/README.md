# Distinctiveness and Complexity
My final project, Veloria, is a web application designed to help learners acquire the German language through the immersive experience of reading stories. Unlike the sample projects provided in the course, which often revolve around social networking, commerce, or blogging, Veloria is firmly situated in the educational domain. Its primary focus is language learning, specifically reading comprehension, and it leverages the Common European Framework of Reference (CEFR) levels — A1, A2, B1, B2, and C1 — to organize content in a pedagogically meaningful way. This emphasis on structured language acquisition through narrative distinguishes Veloria from the other projects in the course and positions it as a unique contribution that blends education with technology.

The complexity of Veloria lies not only in its conceptual distinctiveness but also in its technical architecture. At the heart of the application are two custom Django models: Story and Content. The Story model stores metadata such as the title and CEFR level of each story, while the Content model is linked to Story via a foreign key and contains the actual sentences of the story alongside their translations. Each Content object therefore represents a sentence–translation pair, allowing the application to preserve contextual meaning rather than relying on isolated word translations. This design choice was deliberate: after reviewing resources such as Wiktionary, Linguee, and discussions on contextual translation in language learning, I concluded that storing sentences rather than words was the most effective way to ensure accuracy and pedagogical value. Words often shift meaning depending on context, and by anchoring translations at the sentence level, Veloria provides learners with more reliable and meaningful input. While this approach sacrifices some granularity in word‑level analysis, it prioritizes comprehension and contextual accuracy, which are critical for learners at the A2–B2 stages.

The decision to separate Story and Content into distinct models also reflects a concern for scalability and maintainability. By isolating metadata (title, level) from the actual text and translations, the application can render story lists, filter by level, and display metadata across multiple views without duplicating data. Meanwhile, the Content model allows fine‑grained control over sentence rendering, translation display, and vocabulary tracking. To extend functionality further, I incorporated a User model with a vocabulary_ids JSON field. This field stores references to Content objects that a user has chosen to save, enabling personalized vocabulary lists. This feature is central to the Vocabulary Book page, where learners can revisit and review the sentences they found most useful. The combination of relational models and user‑specific tracking demonstrates a level of backend complexity beyond simple CRUD operations.

On the backend, the views.py file orchestrates both standard and custom logic. In addition to handling user registration and authentication, it defines functions for rendering the homepage, the stories page (organized by CEFR level), the vocabulary page (displaying saved sentence–translation pairs), and individual story pages. Two specialized functions handle vocabulary operations: one receives JSON requests to add new vocabulary items, while the other checks whether a given sentence has already been saved. This ensures efficient interaction between the frontend and backend, and it highlights the project’s use of asynchronous communication patterns rather than relying solely on synchronous page reloads.

The frontend introduces its own layer of complexity. Veloria integrates JavaScript to manage dynamic rendering and interactivity, particularly in the stories page where I implemented concepts reminiscent of single‑page applications (SPAs). Buttons toggle the visibility of story lists by level, and event listeners on sentences trigger the display of translations in a dedicated translation block. This block is populated by leveraging data-translation attributes embedded in the HTML, allowing translations to be retrieved instantly without additional server calls. JavaScript also manages the save button logic, sending fetch requests to the backend and updating the UI to reflect saved vocabulary. These features demonstrate a thoughtful integration of frontend and backend logic, ensuring a smooth and responsive user experience.

Styling was achieved primarily through Tailwind CSS, which provided utility classes for rapid design iteration. Tailwind allowed me to create a consistent aesthetic across pages, while custom CSS in style.css was used for specialized components such as flashcard‑style vocabulary cards and the book‑like rendering of stories. This combination of utility‑first styling and custom design reflects both efficiency and creativity in frontend development. The flashcard design, in particular, enhances the educational distinctiveness of the project by visually reinforcing the metaphor of a “vocabulary book.”

Taken together, these elements — the educational focus, the sentence‑translation storage strategy, the relational model design, the asynchronous backend logic, the SPA‑like frontend interactivity, and the tailored styling — establish Veloria as both distinct and complex. It is distinct because it addresses a domain not covered by the course’s sample projects, and it is complex because it integrates multiple layers of technical decision‑making, from database schema design to frontend responsiveness. Veloria is not merely a variation on existing templates; it is a carefully constructed educational tool that demonstrates both creativity and technical depth.



# What’s Contained in Each File

### Static folder (static/veloria_app/)

  images/ → background images used across pages.

  app.js → JavaScript logic for interactivity (sentence click, translation display, save button).

  style.css → custom styles (flashcards, fonts, page layout) alongside Tailwind utilities.

### models.py

  User → extends Django’s AbstractUser, includes vocabulary_ids JSON field for saved sentences.

  Story → stores story metadata (title, CEFR level).

  Content → linked to Story via foreign key, stores sentence text and its translation.

### views.py

  Handles user registration/login/logout.

  Renders pages: index, stories by CEFR level, individual story, vocabulary book.

  Provides JSON endpoints: add vocabulary, check if sentence already saved.

### urls.py

  Maps URL paths to views (home, stories, story detail, vocabulary, login, register, logout).

### Templates (templates/veloria_app/)

  layout.html → base layout with navigation.

  index.html → homepage.

  login.html, register.html → authentication pages.

  stories.html → list of stories by level.

  story.html → displays sentences with translations and save option.

  vocabulary.html → shows user’s saved sentence–translation pairs.

### Data Import System

We introduced a data/ folder containing two CSV files: stories.csv and sentences.csv.  
These files hold all graded stories and their translations. A custom Django management command (import_csv) reads them and automatically populates the Story and Content models.  

The Goal is to Make it simple to add or update large sets of stories without manual entry — just edit the CSVs and run python manage.py import_csv to sync the database.

### README.md

  Documentation of the project, explaining distinctiveness, complexity, file contents, setup, and usage.

### requirements.txt

  Contains Django as the primary dependency.

  No additional packages beyond Django are required for running the app.



# How to Run the Application


1. Clone the repository  
  Download or clone the project into your local environment:
  bash
    git clone <repository-url>


2. Install dependencies  
  Veloria is built with Django. Install the required packages using pip:
  bash
    pip install -r requirements.txt


3. Apply migrations  
  Set up the database schema:
  bash
    python manage.py migrate


4. Create a superuser (optional)  
  For admin access:
  bash
    python manage.py createsuperuser


5. Load content into the database  
  Stories and sentences can be added manually through the Django admin or imported temporarily via CSV. Once imported, they are stored in the Story and Content models.


6. Run the development server  
  Start the application:
  bash
    python manage.py runserver


7. Access the application  
  Open your browser and navigate to:

  Code
    http://127.0.0.1:8000/


8. User workflow

  Register or log in to create an account.

  Browse stories organized by CEFR levels (A1–C1).

  Click on sentences to reveal translations in the translation block.

  Save sentence–translation pairs to your personal vocabulary list.

  Review saved vocabulary in the Vocabulary Book interface.


### Additional Information

The design of Veloria was guided by the theme of stories and books, with the goal of creating an environment that feels immersive and aligned with the act of reading. Background images of libraries and books were chosen to set the tone, giving each page a sense of place and atmosphere. This visual context reinforces the educational purpose of the app by reminding users that they are engaging with stories in a literary setting.

Stories themselves are rendered with stylistic touches that mimic book covers or the pages of a book. Titles appear on cover‑like cards, while individual stories are displayed in layouts that resemble printed pages. This approach was intentional: by presenting content in a way that visually echoes the experience of holding a book, Veloria encourages learners to see language study not as abstract text, but as part of a narrative journey. The flashcard styling used for vocabulary further extends this metaphor, turning saved sentences into collectible “cards” that learners can revisit and review.

Beyond aesthetics, these design choices serve functional purposes. The book‑cover grid makes it easy to browse stories by level, while the page‑like rendering of sentences supports the interactive translation feature. Together, they create a coherent visual identity that distinguishes Veloria from more generic educational apps. The combination of background imagery, cover‑style cards, and page‑like layouts ensures that the user experience is not only practical but also engaging, blending utility with atmosphere.
