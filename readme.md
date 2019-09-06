# FIS EES

EES (Electronic Election System) is a centralized, secure
election protocol to conduct small scale elections for schools, offices
and other such use cases. EES is secure and uses a two-step voter assignment
process to prevent booth capturing or vote tampering, and another verification 
protocol to ensure vote integrity.

Election administrators have the ability to create and manage self-contained
elections - they will be able to use an administrator page to control things 
such as Candidates, Voter Registration, Booth/Cluster creation and assignment
of voters to booths.



## Read me first!

Welcome! 

If you are a maintainer, welcome to this project. I hope this documentation 
meets standards that help you maintain this project and hopefully, you don't have to quash
too many bugs.

We work on the contstraint that every voter has a unique ID assigned to them.

If this application is completely, ultimately broken beyond repair, please contact the original
maintainers of this application.

* Shreyas Kaundinya 
 - Phone - (+91) 9901384892
 - email - shreyassk08@gmail.com

* Anirudh Rowjee
 - Phone - (+91) 9980029176
 - email - meteorstorm41@gmail.com

## Documentation Stucture

This documentation is organized as follows
* [main documentation (this file) ](readme.md)
* App-Specific Documentation
1. [candidates](candidates.md)
2. [clustermaster](clustermaster.md)
3. [election](election.md)
4. [electionadmin](electionadmin.md)
5. [elections](elections.md)
6. [env](env.md)
7. [media](media.md)
8. [results](results.md)
9. [static](static.md)
10. [templates](templates.md)
11. [voters](voters.md)
12. [votes](votes.md)


## Application Structure

### Standard Django App Structure

Every standard app in this application has a filestructure similar to this. 
Note - '[x]' represents that every app MUST have this.

```
| <app_name>/               
| | __pycache__/            [ ]
| | migrations/             [x]
| | templates/              [x]
| | | <app_name>/
| | | | example_template.html
| | __init__.py             [x]
| | admin.py                [x]
| | apps.py                 [x]
| | forms.py                [ ]
| | models.py               [x]
| | tests.py                [ ]
| | urls.py                 [x]
| | views.py                [x]
```

### Our main divisions - the Django Apps

The name of each app is a hyperlink to the specific documentation for that app.

1. **[election (main app)](election.md)**

This app is the first django app that is created with any project.
It houses the templates for HTML and CSS rendering of the main application, as well the static files
and PDF rendering template for the results of the election.

It also contains the settings file `settings.py` and other critical files. Do not touch anything in these files
unless you're absolutely sure you know what you're doing.

the current file structure looks like this - 

```
| | static/
| | templates/
| | | pdf/
| | | | results.html
| | | admin-base.html
| | | base.html
| | __init__.py
| | settings.py
| | urls.py
| | utils.py
| | wsgi.py
```

Files such as `wsgi.py` and `utils.py` are critical to the working of the application. Please don't 
change ANYTHING in them.

You will find settings for static file storage in `settings.py` and the main URL Configuration 
in `urls.py`.



