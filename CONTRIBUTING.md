# How to contribute to twodots-service

## Coding Standards

We don't have explicit coding standard so pay attention to the main coding style, that's used everywhere.
When naming use camleCase or snake_case.
A good guide to look up is [forests description](https://gist.github.com/forest/19fc774dde34f77e2540) which contains detailed contribution steps

### Naming routes

Routes are named semantic to each path. When naming a route use the syntax
```base/path<models>s/<action>/<param>/?{query=}```
This is the base template for routes. We use the corresponding model name in plural for the base, the action name and paramas and optional get queries

When Defining a new functionality ```Controllers``` use ```Services``` only, ```Services``` use ```Repositories```, and this ideaology should not be broken.

## General Steps

This repo is linked to **Web** project on the board.

1. The issues list is placed in this repo and any other repo.

2. Once an issue is marked as a bug, enhancement, feature or whatever needs development work, it will be included as the last item in the **To Do** column.

3. Only team lead can assigne members to solve an issue.

4. Only team lead will prioritize the backlog items and arrange them in the **To Do** column, so that the items in the top of the list are implemented first.

5. The collaborators will review the issues and select the ones approved to begin development with, and move them to the **In progress Backend** column.

6. The collaborators can submit a PR as usual and move issue to the **Pulled** column. PR should have description, that allow to unsestand main changes, and references to closed issues. 

## Forks and Branches

All contributions must be submitted as a [Pull Request (PR)](https://help.github.com/articles/about-pull-requests/) so you need to [fork this repo](https://help.github.com/articles/fork-a-repo/) on your GitHub account.

The main branches are `development`, `staging` and `producion`:

- `development` - contains the latest code and it is undergoing major development.  
**All PRs must be against `development` branch to be considered**.

- `staging` - synced from time to time from `development`. It contains "stable" code that can be tested. 
**Keep in mind "stable" does not mean PRODUCTION-READY! Don't deploy this branch in production**

- `producion` - synced from time to time from `staging`. It contains stable code. 

- Any other branch is temporary and could be deleted. Do not submit any PR to them!

## Formatting

The `<>` is mandatory and `[]` is optional.

Supported types:

* chore: Changes that affect the build system or external dependencies.
* docs: Any changes in doc files.
* feat: A new feature.
* fix: A bug fix.
* refactor: A code change that neither fixes a bug nor adds a feature
* test: Adding missing tests or correcting existing tests.


### Branch Name Format

The branch name can include a `number` and a `subject`:
```
[#number_]<type>/<subject>
```

Where `number` is issue number and `subject` is its header.

e.g. `#184_fix/unable_to_fetch_vehicles`

### Commit Message Format

Each commit message consists of a `header`, a `body` and a `footer`. The header includes a `type`, a `domain` and a `subject`:
```
<type>[(domain)]: <subject>
[BLANK LINE]
[body]
[BLANK LINE]
[footer]
```

e.g. 

```
fix(Vehicle): update vehicle endpoint created

* created dto object to handle validation
* implemented request object 
* stored updated vehicle
* returned proper responses for success and exception

addresses issue #12
```
