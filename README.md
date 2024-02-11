# Personalized Coding Learning Path Generator

## Project Summary

A web application designed to aid developers in identifying new coding skills based on their current expertise. Utilizing AI, it offers personalized recommendations for technologies to learn and generates customized learning paths tailored to the user's proficiency levels and career aspirations.

## Concept

This application aims to help users enhance their coding skills by providing AI-driven recommendations for learning new technologies. It leverages user-inputted skills and proficiency levels to suggest a tailored learning journey.

## Key Features

- **User Skill Input**: Enables users to input their current coding skills and self-assess proficiency levels.
- **AI-Driven Recommendations**: Uses an AI model to suggest new coding languages or technologies.
- **Learning Path Generation**: Offers personalized learning paths based on user selections.
- **User Profile Management**: Allows for the updating of skills and proficiencies.

## Technology Stack

- **Frontend**: React, NextJS, Tailwind CSS
- **Backend API**: FastAPI
- **Database**: PostgreSQL
- **AI Integration**: OpenAI's API
- **Backend Models**: Django models with FastAPI integration

## Development Plan

1. **Week 1**: Environment setup, Django models, FastAPI project initialization, API endpoint planning.
2. **Week 2**: Integration of Django models with FastAPI, API development, basic AI setup.
3. **Week 3**: Frontend development, API integration, start AI recommendation logic.
4. **Week 4**: Complete integration, finalize AI logic, testing, and MVP launch.

## Post-Launch

- Collect user feedback for future improvements.
- Plan the next iteration based on feedback.

## Considerations

- Ensure the handling of asynchronous operations with FastAPI and Django's ORM.
- Design for scalability and future growth.
- Focus on a user-centric UI/UX design.
- Initial MVP will focus on learning plan structures, omitting specific learning resources.

## Future Features (Post-MVP)

- Customizable learning paths.
- Integration with curated learning resources.
- Enhanced AI recommendations based on user feedback.


# Git Commit Conventions

https://github.com/angular/angular/blob/main/CONTRIBUTING.md

```
Commit Message Header
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: Be succinct and make it relevant to your current initiative
  │
  │
  │
  │
  │
  └─⫸ Commit Type: build|ci|chore|docs|feat|fix|perf|style|refactor|test
The <type> and <summary> fields are mandatory, the (<scope>) field is optional.
```

**Type**

Must be one of the following:
```
build: Changes that affect the build system
ci: Changes to our CI configuration files and scripts (example scopes: Circle, BrowserStack, SauceLabs)
chore: Basic tasks that need completing like doing releases or bumping dependencies
docs: Documentation only changes
feat: A new feature
fix: A bug fix
perf: A code change that improves performance
refactor: A code change that neither fixes a bug nor adds a feature
style: A change in order to make an external styling change to a feature
test: Adding missing tests or correcting existing tests
```

**Scope**

The scope should be succinct and make it relevant to your current initiative.

The following is the list of supported scopes:

`<all>(todo): fill out a base list of scopes`

**Summary**

Use the summary field to provide a succinct description of the change:

use the imperative, present tense: "change" not "changed" nor "changes"
don't capitalize the first letter
no dot (.) at the end


# Branching
We follow Github flow where unique feature branches are created from main. The main branch must always be stable and deployable. Sometimes integration branches or a dev branch will be necessary for consolidating multiple people or teams' work, but these should generally be short-lived and only serve as testing environments unlike Gitflow where an engineer will push dev -> staging -> production. See the following explanation of Github flow vs Git flow:

https://www.geeksforgeeks.org/git-flow-vs-github-flow/

Create a branch from main with:

```
git checkout -b <initials or unique moniker>/<type>/<scope>
```

Scope should be succinct and be all lowercase and use snake case for easability of web navigation and support for tab autocompletion of branches. When in doubt, follow the code commit conventions for all of the above

When merging main into your feature branch as main is updated, a good rule of thumb is to "rebase first and if it devolves into conflict-resolution-hell, merge main into your branch and move on." See this article:

https://timwise.co.uk/2019/10/14/merge-vs-rebase/

If you're uncomfortable with rebase, because it's a small team, just merge main in when you need it and call it.

Within a PR, you are welcome to also use the commit convention of your branch:

```
fix: add
chore: Bumping python version number for pyenv library
docs: Add new README on our conventions
...
```

# Code Comment Conventions

```
Commit Message Header
<author>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. Be succinct
  │       │
  │       └─⫸ Comment Scope: todo|bug|???|<list from code commits>
  │
  │
  │
  │
  │
  └─⫸ Author of the comment: fad|e|cm|etc.
The <summary> field is mandatory, the (<author> and <scope>) field is optional.
```

**Author**

This should either be the name you most commonly go by or your initials. Whatever you are most comfortable with and has not been used previously by a member of the team.

**Scope**

The scope should reflect what the comment is explaining. If the comment is simply noting why the code the way it is, there is no need to say `c(note):`, `c:` is enough because any comment is a note. We remove redundant information to ensure the maximum amount of information is digested in the shortest possible format.

The following is the list of supported scopes:
```
todo: a task we may need to complete later
bug: noting a potential or current bug that is unresolved
???: no idea what is going on here. we need to figure it out
<list from code commits>
```

# General

General: We treat abbreviations, proper nouns, and acronyms like words for camelcase / Pascalcase. so we don't have to think about how to apply uppercase. This removes any cognitive burden for hot to apply uppercase because there are no exceptions no exceptions to think about. Class name? Capitalize the first letter. Not a class? Don't:
https://stackoverflow.com/a/27172000/14337922

Python: We follow Black's code formatter with single quotes and the application of camel case to abbreviations and acronyms.

TS/JS: We otherwise follow 90% of the Airbnb style guide excluding the exceptions from Prettier and regarding camel case:
https://github.com/airbnb/javascript
