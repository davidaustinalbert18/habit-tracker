# My Capstone Project: Habit Tracker
Habit Tracker is a web application that allows users to create, track, and manage their personal habits. Users can set goals, mark habits as completed, monitor their streaks, and view statistics for their progress. The app is designed to encourage consistency and accountability for daily, weekly, or monthly habits.

### Distinctiveness and Complexity
This project is different from other projects in CS50W because unlike Project 1 (Search), Project 2 (Commerce), Project 3 (Mail), or Project 4 (Network), this Habit Tracker focuses on personal productivity and behavioral consistency rather than searching, e-commerce, emailing, and social networking.
The complexity of this project comes from several areas:
- **Custom Models**: I designed two core models: `Habit` and `HabitLog`. Each habit is associated with a user and tracks metadata including frequency, description, and goal completions. `HabitLog` tracks individual completions and is used to calculate consistency and streaks.
- **Streak Calculation Logic**: The backend logic includes a function to calculate ongoing streaks based on the user’s completion logs. This algorithm determines how many consecutive days (or weeks/months) a user has completed a habit. I had to use "date" and "timedelta" from "datetime" in order to keep track of what day was today and how long ago the previous day or week or month the last completion was.
- **Frontend Visualization**: The frontend includes consistency bars for goal progress, real-time button toggles to mark habits as complete or incomplete, and JavaScript for animation of progress bars.
- **Filtering and Sorting**: The homepage allows users to filter habits by frequency and sort by name, date created, or streak length. This adds to the usability and customization of the dashboard.
- **Mobile Responsiveness**: The layout is designed to be usable on both desktop and mobile, with scalable elements and mobile-friendly navigation.

### Files and Functionality
- `models.py` – Defines the `Habit` and `HabitLog` models, and the `calculate_streak` function.
- `views.py` – Contains all logic for habit creation, editing, completion, filtering, and stats.
- `urls.py` – Maps URL paths to their corresponding views.
- `forms.py` – Handles habit form logic using Django forms.
- `templates/index.html` – Main dashboard for viewing, filtering, and completing habits.
- `templates/stats.html` – Statistics page for user progress and goal tracking.
- `templates/create_habit.html` – Form for adding a new habit.
- `templates/edit_habit.html` – Form for editing an existing habit.
- `templates/delete_habit.html` – Confirmation page for deleting a habit.
- `templates/signup.html` – User registration page.
- `static/tracker/style.css` – Custom styling for layout and responsiveness.
- `requirements.txt` – Package dependencies needed to run the project.
- `README.md` - This documentation file you're reading right now!

### How to Run the Application
1. Clone the repository:
```bash git clone <your-repo-url>```
```bash cd Capstone```
2. Create a virtual environment and activate it.
```bash python3 -m venv venv```
```source venv/bin/activate```
3. Install dependencies:
```bash pip install -r requirements.txt```
4. Run migrations:
```bash python manage.py makemigrations```
```bash python manage.py migrate```
5. Create a superuser:
```shell python manage.py createsuperuser```
6. Start the server:
```shell python manage.py runserver```
7. Open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000) and log in or create a new account.

### Additional Notes
- CSRF protection is enabled for all forms.
- Users must be logged in to access the habit dashboard.
- Button actions (mark completed, undo) use POST requests for security.
- Admin panel is available at `/admin/`.

### Requirements
These packages are used and should be listed in `requirements.txt`:
```shell django>=5.2.3```

### Final Thoughts
Thank you for teaching me CS50W! - David Albert


