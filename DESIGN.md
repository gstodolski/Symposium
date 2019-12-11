Design Document — Symposium
Graham Stodolski and Drew Ward

This project relies on some very simple functions that were given to us during our last pset; specificially, understanding and using two helper functions, called apology and login_required. These were were very helpful when it came to
error checking and our ability to start building this websites.

Our homepage, or "index" page, is the result of a very simple SQL query in which we join two tables in our database, then print the result of that. We chose to have separate tables for these to begin with because it made our table more
navigable.  The links on each of the courses take the user to a page for that course. Within those, we were able to create a "posts" table that users could input to from the page itself, then the page would refresh and a SQL query would
select comments about the course. Each of the comments contains the username of the user who posted it and the time at which it was posted, which are all inserted into the posts table using a SQL query.

For our Register function, we decided that a password confirmation field would be appropriate.  It is subject to a variety of different error-checking fields, and the confirmation field was able to add a new layer.  This function also checks if
the username has already been used, and if not, adds it into the "users" table that we have created. These measures are all realistic steps that are taken in the real world.

The Search function gets the user's input from the html template "search.html", which is passed from a form into application.py, then selects by SQL query from the database any values that match the user input, then outputs the
results of that search into a new html template, which utilizes a for loop to print the list that is returned. We had to account for the "or" field that we've added to our various forms in different "if" statements in Python itself;
for example, if someone forgot to put in a course title, but they had a number, we would still be able to return a course, and most likely the course that the user was looking for if the subject is also present.

The Add function was one of the more difficult functions because of the various SQL queries we had to perform. The first step is getting information from the user via javascript submission buttons and forms.  This information is then
passed to the function and used to select course ids from the course table. If that course id is already in the table that is constituted of the current user's courses, the function won't let the user add it. If not, though, it
successfully adds the course, which can now been seen in index.

The Remove function essentially has the same idea as Add, except that if the SQL query finding the course id in the user_ courses table returns a course, that course is then removed from the user_courses table.

The Course function is really interesting because it serves two purposes: the first being that, using "get", it queries the database for posts about a certain course, then passes them to the hmtl template. The second part of this function is the
ability to create the posts that the user is seeing. This is done by taking the text that the user puts into the post field when the form is submitted (via "post"), inputting it into a posts database that merges courses and users, then refreshs the page and goes through
the first process. This is a dynamic and versatile process because any user can see the comments that other users have posted while also being able to input their own ideas.