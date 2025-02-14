# GatorGrader

![Image of Logo](.github/gatorgraderlogotitled.png)

<p align="center">
<b>
The only tool you'll need to ensure your student's code and writing is up to
speed!
</b>
</p>

[![Build Status](https://api.travis-ci.org/GatorEducator/gatorgrader.svg?branch=master)](https://travis-ci.org/GatorEducator/gatorgrader) [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/gatoreducator/gatorgrader?branch=master&svg=true)](https://ci.appveyor.com/project/GatorEducator/gatorgrader/branch/master) [![codecov.io](http://codecov.io/github/GatorEducator/gatorgrader/coverage.svg?branch=master)](http://codecov.io/github/GatorEducator/gatorgrader?branch=master) [![codacy.com](https://api.codacy.com/project/badge/Grade/3dade81be6dc467b8e34cde66eb5cdc6)](https://www.codacy.com/app/GatorEducator/gatorgrader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=GatorEducator/gatorgrader&amp;utm_campaign=Badge_Grade) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-orange.svg)](https://github.com/GatorEducator/gatorgrader/graphs/commit-activity) [![GitHub license](https://img.shields.io/github/license/GatorEducator/gatorgrader.svg)](https://github.com/GatorEducator/gatorgrader/blob/master/LICENSE.md) [![All Contributors](https://img.shields.io/badge/all_contributors-33-orange.svg?style=flat-square)](#contributors)

## Table of Contents

* [Quickstart Guide](#quickstart-guide)
* [Key Features](#key-features)
* [What Do People Think about GatorGrader?](#what-do-people-think-about-gatorgrader)
* [Installing GatorGrader](#installing-gatorgrader)
* [Testing GatorGrader](#testing-gatorgrader)
  + [Automated Testing](#automated-testing)
  + [Test Coverage](#test-coverage)
  + [Testing with Multiple Python Versions](#testing-with-multiple-python-versions)
  + [Code Linting](#code-linting)
* [Running GatorGrader](#running-gatorgrader)
* [Comparison to Other Tools](#comparison-to-other-tools)
* [Presentations](#presentations)
* [Contributing](#contributing)
* [Contributors](#contributors)

## Quickstart Guide

Want to quickly get up and running with GatorGrader? If you have an existing
assignment and you want to automatically check its source code or technical
writing, then you can use GatorGrader's [Gradle
plugin](https://github.com/GatorEducator/gatorgradle). The following starter
repositories provide examples of how to configure GatorGrader to check programs
and documentation for different languages:
[Java](https://github.com/GatorEducator/java-starter),
[LaTeX](https://github.com/GatorEducator/latex-assignment-starter), and [HTML
with CSS](https://github.com/GatorEducator/html-css-assignment-starter). These
examples also show how to integrate GatorGrader with [GitHub
Classroom](https://classroom.github.com/) and [Travis
CI](https://travis-ci.com/). When you follow these examples, the Gradle plugin
for GatorGrader will install it automatically when you run `gradle grade` in a
terminal window.

## Key Features

GatorGrader automatically checks the work of technical writers and programmers.
It can:

* Use its [Gradle plugin](https://github.com/GatorEducator/gatorgradle) to check
  projects implemented and documented in a wide variety of languages (e.g.,
  Java, Python, LaTeX, Markdown, HTML, and CSS).

* Integrate with [GitHub Classroom](https://classroom.github.com/) to check
  solution and starter repositories created for professors and students,
  respectively.

* Run in a cloud-based environment like [Travis CI](https://travis-ci.com/) or
  on the command-line of a developer's workstation.

* Operate as a "batteries included" grading tool, supporting automated checks
  like the following:

  * Does a file exist in the correct directory with the requested name?

  * Does technical writing contain the desired number of words and paragraphs?

  * Does source code contain the designated number of language-specific comments?

  * Does source code or technical writing contain a required fragment or match
    a specified regular expression?

  * Does a command execute correctly and produce the expected number of output
    lines?

  * Does a command execute and produce output containing a fragment or matching
    a regular expression?

  * Does a GitHub repository contain the anticipated number of commits?

Aligning with key recommendations in a recent [National Academies
report](https://www.nap.edu/catalog/24926/assessing-and-responding-to-the-growth-of-computer-science-undergraduate-enrollments),
GatorGrader helps instructors automatically check student submissions in both
introductory and application-oriented classes using languages like Markdown,
Java, Python, JavaScript, CSS, and HTML. GatorGrader does not aim to solve
problems related to building and linting a project or managing an assignment's
submission, instead integrating with existing tools and systems like
[Gradle](https://gradle.org/), [GitHub](https://github.com/), and [GitHub
Classroom](https://classroom.github.com/) to effectively handle those tasks.

## Installing GatorGrader

Installing GatorGrader is not necessary if you intend to use it through its
[Gradle plugin](https://github.com/GatorEducator/gatorgradle). If you want to
participate in the development of GatorGrader, the project maintainers suggest
the use of [Pyenv](https://github.com/pyenv/pyenv) to install Python 3.6 or
above. In addition to installing [Git](https://git-scm.com/) to access the
project's GitHub repository, you should also install
[Pipenv](https://github.com/pypa/pipenv) for its support of package and virtual
environment management. After completing the installation of these tools, you
can type the following command in your terminal window to clone GatorGrader's
GitHub repository:

```bash
git clone https://github.com/GatorEducator/gatorgrader.git
```

If you plan to develop new features for GatorGrader or if you want to run the
tool's test suite in [Pytest](https://github.com/pytest-dev/pytest), then you
will need to install the developer dependencies by typing ``pipenv install --python="$(pyenv which python)" --dev`` in the directory that contains
GatorGrader. If you want to use GatorGrader, then you can type ``pipenv install --python="$(pyenv which python)"`` instead. Once these commands complete
successfully, you have officially installed GatorGrader! Note that running these
commands will ensure that Pipenv creates a virtual environment for GatorGrader
that is bound to the version of Python that Pyenv set for use.

## Testing GatorGrader

### Automated Testing

The developers use [Pytest](https://docs.pytest.org/en/latest/) for the testing
of GatorGrader. Depending on your goals, there are several different
configurations in which you can run the provided test suite. If you want to run
the test suite to see if the test cases are passing, then running this command
in a terminal window will perform testing with the version of Python to which
Pipenv's virtual environment is currently bound.

```
pipenv run test
```

### Test Coverage

Along with running the test suite, the developers of GatorGrader use statement
and branch coverage to enhance their testing activities. To see the coverage of
the tests while also highlighting the lines that are not currently covered by
the tests, you can run this command in a terminal window. As with the previous
command, this will run the tests in the version of Python to which Pipenv's
virtual environment is currently bound.

```
pipenv run cover
```

### Testing with Multiple Python Versions

The previous two commands are restricted to running the test suite in the
version of Python to which Pipenv was bound. If you have installed multiple
versions of Python with Pyenv and you want to iteratively bind Pipenv to each
version and then run the test suite, then you should first run the following
commands to install [Pipx](https://github.com/pipxproject/pipx) and use Pipx to
install [Invoke](https://github.com/pyinvoke/invoke). The first of these three
commands will install `pipx`, a program that supports the execution of Python
packages in isolated environments. The second command makes the directory
`~/.local/bin/` a part of the search path for executable Python programs and the
third one installs the `invoke` command so that it is available on your
workstation outside of a virtual environment managed by Pipenv, thereby ensuring
that it is always available to run tasks.

```
pip install pipx --user
python -m userpath append ~/.local/bin/
pipx install invoke
```

Now you can run the test suite in the specified versions of Python with the
following command. This example command will run the test suite in Python 3.6.8
and Python 3.7.3.

```
invoke -c scripts/tasks test --pyenv 3.6.8 --pyenv 3.7.3
```

If you want to track test coverage while running the tests in both Python 3.6.8
and 3.7.3, then you can run the following command.

```
invoke -c scripts/tasks cover --pyenv 3.6.8 --pyenv 3.7.3
```

You can switch the version to which Pipenv is bound by running the following
command that adopts, for instance, Python 3.7.3.

```
invoke -c scripts/tasks switch --pyenv 3.7.3
```

### Code Linting

The developers of GatorGrader use linting and code formatting tools, such as
[Pylint](https://github.com/PyCQA/pylint),
[Pydocstyle](https://github.com/PyCQA/pydocstyle), and
[Black](https://github.com/python/black). After installing GatorGrader's
development dependencies with Pipenv, you can run all of the linters by typing
this command in a terminal window.

```bash
pipenv run lint --check
```

### Linting Checks

Want to learn about our linting checks? Check us out on our website,
[GatorGrader](https://deploy-preview-1--gatorgrader.netlify.com)! We have detailed
descriptions of our linting checks and more! To get an idea of the linting checks we
offer, here is a quick list:

1. ConfirmFileExists          

2. CountCommandOutput

3. CountCommits

4. CountFileLines

5. CountFileParagraphs

6. CountFileWords

7. CountMarkdownTags

8. CountMultipleLineComments

9. CountParagraphWords

10. CountSingleLineComments

11. ExecuteCommand

12. MatchCommandFragment

13. MatchCommandRegex

14. MatchFileFragment

15. MatchFileRegex

Something you should know when working with our linting checks is that all of
them come with optional arguments. These optional arguments are: `-h, --help`.
The help message will be displayed and then exited. If further assistance is needed,
please contact us on GitHub.

## Running GatorGrader

Students and instructors normally use GatorGrader through its [Gradle
plugin](https://github.com/GatorEducator/gatorgradle), specifying the requested
checks in a `config/gatorgrader.yml` file. When run through Gradle, GatorGrader
reports each check that it performed, additionally sharing a diagnostic message
for each check that did not pass. Individuals who want to run GatorGrader as a
stand-alone Python application should first install it's application
dependencies with Pipenv and then learn about the supported checks and their
defaults by typing `pipenv run python3 gatorgrader.py --help` in a terminal
window.

Instructors often run GatorGrader in conjunction with other tools that check
source code and technical writing. For instance, in a Java-based introductory
course, instructors could verify student submissions with
[Checkstyle](https://github.com/checkstyle/checkstyle), thereby ensuring that
the Java source code adheres to the requirements in the [Google Java Style
Guide](https://google.github.io/styleguide/javaguide.html). In this course, an
instructor could require that Markdown files with technical writing meet the
standards described in the [Markdown Syntax
Guide](https://guides.github.com/features/mastering-markdown/), meaning that all
Markdown files must pass the checks performed by the [Markdown linting
tool](https://github.com/markdownlint/markdownlint). These assignments could
also require that all submitted technical writing must adhere to the standards
set by the [Proselint tool](http://proselint.com/). Since GatorGrader can run an
arbitrary command and check its error code, it is also possible to integrate it
with a wide variety of other linters, code formatters, and testing tools.

## Comparison to Other Tools

Other automated grading tools include:

- [autograde-github-classroom](https://github.com/apanangadan/autograde-github-classroom): "scripts to download and grade submissions to Github Classroom"
- [check50](https://github.com/cs50/check50): "a tool for checking student code"
- [Classroom Assistant](https://classroom.github.com/assistant): "desktop application to help you get student repositories for grading"
- [nbgrader](https://github.com/jupyter/nbgrader): "a system for assigning and grading notebooks"
- [nerfherder](https://github.com/kevinwortman/nerfherder): "scripts for automating grading with GitHub Classroom and Moodle"
- [Submitty](https://github.com/Submitty/Submitty): "homework submission, automated grading, and TA grading system"
- [WebCat](https://github.com/web-cat): "all-in-one plugin for full processing and feedback generation"

Designed for instructors who want an alternative to simple scripts or
stand-alone platforms that do not integrate with industry-standard
infrastructure like GitHub and Travis CI, GatorGrader is a tool that
automatically checks the work of technical writers and programmers. Unlike other
systems, GatorGrader provides a "batteries included" approach to automated
grading that makes it easy for instructors to combine well-tested checks for
projects that students implement in a wide variety of programming languages.
GatorGrader's developers take its engineering seriously, maintaining
standards-compliant source code, a test suite with 100% statement and branch
coverage, and top-notch source code and user documentation.

## Presentations

GatorGrader's creators give presentations about the development, use, and
assessment of the tool. Please contact one of the developers if you would like
to feature a presentation about GatorGrader at your technical conference. The
following list includes some of our team's recent presentations:

- [A Hands-on Guide to Teaching Programming with GitHub, Travis CI, and Python](https://speakerdeck.com/gkapfham/a-hands-on-guide-to-teaching-programming-with-github-travis-ci-and-python) <br> *at PyOhio 2018*
- [Using GitHub, Travis CI, and Python to Introduce Collaborative Software Development](https://speakerdeck.com/gkapfham/using-github-travis-ci-and-python-to-introduce-collaborative-software-development) <br> *at PyCon Education Summit 2018*
- [Using Python, Travis CI, and GitHub to Effectively Teach Programming](https://speakerdeck.com/gkapfham/using-python-travis-ci-and-github-to-effectively-teach-programming) <br> *at PyGotham 2018*

## Contributing

Are you interested in contributing to
[GatorGrader](https://github.com/GatorEducator/gatorgrader),
[GatorGradle](https://github.com/GatorEducator/gatorgradle), or any of the
sample assignments (e.g.,
[Java](https://github.com/GatorEducator/java-assigment-starter),
[LaTeX](https://github.com/GatorEducator/latex-assignment-starter), or [HTML
with CSS](https://github.com/GatorEducator/html-css-assignment-starter))? Great,
because we appreciate the involvement of new contributors! Before you raise an
issue or start to make a contribution to GatorGrader's repository, we ask that
you review the project's [code of conduct](CODE_OF_CONDUCT.md) and the
[contribution guidelines](CONTRIBUTING.md).

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://www.gregorykapfhammer.com"><img src="https://avatars2.githubusercontent.com/u/926029?v=4" width="64px;" alt="Gregory M. Kapfhammer"/><br /><sub><b>Gregory M. Kapfhammer</b></sub></a><br /><a href="#talk-gkapfham" title="Talks">📢</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=gkapfham" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=gkapfham" title="Documentation">📖</a> <a href="#design-gkapfham" title="Design">🎨</a> <a href="#infra-gkapfham" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=gkapfham" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://saejinmh.com"><img src="https://avatars1.githubusercontent.com/u/5274499?v=4" width="64px;" alt="Saejin Mahlau-Heinert"/><br /><sub><b>Saejin Mahlau-Heinert</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=Michionlion" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=Michionlion" title="Documentation">📖</a> <a href="#infra-Michionlion" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#review-Michionlion" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/dubswalker"><img src="https://avatars2.githubusercontent.com/u/37150088?v=4" width="64px;" alt="Christian Walker"/><br /><sub><b>Christian Walker</b></sub></a><br /><a href="#content-dubswalker" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/everitt-andrew"><img src="https://avatars3.githubusercontent.com/u/31443695?v=4" width="64px;" alt="Andrew Everitt"/><br /><sub><b>Andrew Everitt</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=everitt-andrew" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=everitt-andrew" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.christianlussier.com"><img src="https://avatars2.githubusercontent.com/u/32375724?v=4" width="64px;" alt="Christian Lussier"/><br /><sub><b>Christian Lussier</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=lussierc" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=lussierc" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.simon-burrows.com"><img src="https://avatars2.githubusercontent.com/u/25254767?v=4" width="64px;" alt="Simon Burrows"/><br /><sub><b>Simon Burrows</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=burrowss" title="Code">💻</a></td>
    <td align="center"><a href="https://www.austinbristol.com/"><img src="https://avatars1.githubusercontent.com/u/19804014?v=4" width="64px;" alt="Austin Bristol"/><br /><sub><b>Austin Bristol</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=bristola" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/JattMones"><img src="https://avatars0.githubusercontent.com/u/22432176?v=4" width="64px;" alt="Matt"/><br /><sub><b>Matt</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=JattMones" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=JattMones" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/cmiller365"><img src="https://avatars3.githubusercontent.com/u/27263493?v=4" width="64px;" alt="Christopher Miller"/><br /><sub><b>Christopher Miller</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=cmiller365" title="Code">💻</a> <a href="#design-cmiller365" title="Design">🎨</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=cmiller365" title="Documentation">📖</a></td>
    <td align="center"><a href="http://spencerhuang.netlify.com"><img src="https://avatars0.githubusercontent.com/u/31478964?v=4" width="64px;" alt="Spencer Huang"/><br /><sub><b>Spencer Huang</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=huangs1" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=huangs1" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/ilikerustoo"><img src="https://avatars3.githubusercontent.com/u/25516043?v=4" width="64px;" alt="Mohammad Khan"/><br /><sub><b>Mohammad Khan</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=ilikerustoo" title="Code">💻</a></td>
    <td align="center"><a href="http://www.shafferz.com"><img src="https://avatars1.githubusercontent.com/u/26298864?v=4" width="64px;" alt="Zachary Shaffer"/><br /><sub><b>Zachary Shaffer</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=shafferz" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=shafferz" title="Documentation">📖</a></td>
    <td align="center"><a href="http://alexander.yarkosky.xyz"><img src="https://avatars1.githubusercontent.com/u/36210455?v=4" width="64px;" alt="Alexander Yarkosky"/><br /><sub><b>Alexander Yarkosky</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/issues?q=author%3AAlex-Yarkosky" title="Bug reports">🐛</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=Alex-Yarkosky" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/thomad74"><img src="https://avatars1.githubusercontent.com/u/31478969?v=4" width="64px;" alt="Dillon"/><br /><sub><b>Dillon</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=thomad74" title="Documentation">📖</a></td>
    <td align="center"><a href="http://zacharyleonardo.com"><img src="https://avatars2.githubusercontent.com/u/35816642?v=4" width="64px;" alt="Zachary Leonardo"/><br /><sub><b>Zachary Leonardo</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=leonardoz15" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mendezjw"><img src="https://avatars2.githubusercontent.com/u/23535739?v=4" width="64px;" alt="Jonathan W. Mendez"/><br /><sub><b>Jonathan W. Mendez</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=mendezjw" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=mendezjw" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/lylet-AC"><img src="https://avatars3.githubusercontent.com/u/31486141?v=4" width="64px;" alt="Tyler Lyle"/><br /><sub><b>Tyler Lyle</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=lylet-AC" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/finneyj2"><img src="https://avatars3.githubusercontent.com/u/31444681?v=4" width="64px;" alt="finneyj2"/><br /><sub><b>finneyj2</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=finneyj2" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=finneyj2" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/schultzh"><img src="https://avatars0.githubusercontent.com/u/42979565?v=4" width="64px;" alt="schultzh"/><br /><sub><b>schultzh</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/issues?q=author%3Aschultzh" title="Bug reports">🐛</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=schultzh" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=schultzh" title="Documentation">📖</a> <a href="#review-schultzh" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/alexheinle"><img src="https://avatars3.githubusercontent.com/u/35603755?v=4" width="64px;" alt="alexheinle"/><br /><sub><b>alexheinle</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/issues?q=author%3Aalexheinle" title="Bug reports">🐛</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=alexheinle" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=alexheinle" title="Documentation">📖</a> <a href="#review-alexheinle" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/ZachAndrews98"><img src="https://avatars1.githubusercontent.com/u/15204124?v=4" width="64px;" alt="Zachary Andrews"/><br /><sub><b>Zachary Andrews</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=ZachAndrews98" title="Code">💻</a> <a href="#design-ZachAndrews98" title="Design">🎨</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=ZachAndrews98" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/toccinAC"><img src="https://avatars2.githubusercontent.com/u/31412566?v=4" width="64px;" alt="Nicholas Tocci"/><br /><sub><b>Nicholas Tocci</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=toccinAC" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/hodevin"><img src="https://avatars2.githubusercontent.com/u/31478952?v=4" width="64px;" alt="Devin Ho"/><br /><sub><b>Devin Ho</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=hodevin" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/baldeosinghm"><img src="https://avatars0.githubusercontent.com/u/42876742?v=4" width="64px;" alt="Matthew Baldeosingh"/><br /><sub><b>Matthew Baldeosingh</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=baldeosinghm" title="Documentation">📖</a></td>
    <td align="center"><a href="https://durchburch.xyz"><img src="https://avatars2.githubusercontent.com/u/31478922?v=4" width="64px;" alt="Jordan Durci"/><br /><sub><b>Jordan Durci</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=durcij" title="Code">💻</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/karol-vargas-a9a925b8/"><img src="https://avatars0.githubusercontent.com/u/31486084?v=4" width="64px;" alt="Karol Vargas"/><br /><sub><b>Karol Vargas</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=karolvargas" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/cerdamejiaj"><img src="https://avatars3.githubusercontent.com/u/25254696?v=4" width="64px;" alt="Jerfenson Cerda Mejia"/><br /><sub><b>Jerfenson Cerda Mejia</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=cerdamejiaj" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=cerdamejiaj" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/ohnoanarrow"><img src="https://avatars0.githubusercontent.com/u/22673907?v=4" width="64px;" alt="Tara Douglass"/><br /><sub><b>Tara Douglass</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=ohnoanarrow" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=ohnoanarrow" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/ALEXANDERB82"><img src="https://avatars0.githubusercontent.com/u/31444387?v=4" width="64px;" alt="Alexander Butler"/><br /><sub><b>Alexander Butler</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=ALEXANDERB82" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/corlettim"><img src="https://avatars3.githubusercontent.com/u/35552969?v=4" width="64px;" alt="corlettim"/><br /><sub><b>corlettim</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/issues?q=author%3Acorlettim" title="Bug reports">🐛</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=corlettim" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=corlettim" title="Documentation">📖</a> <a href="#review-corlettim" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/quigley-c"><img src="https://avatars1.githubusercontent.com/u/35495466?v=4" width="64px;" alt="Carson Quigley"/><br /><sub><b>Carson Quigley</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=quigley-c" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/yeej2"><img src="https://avatars1.githubusercontent.com/u/22895281?v=4" width="64px;" alt="Joshua Yee"/><br /><sub><b>Joshua Yee</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=yeej2" title="Code">💻</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=yeej2" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/MaddyKapfhammer"><img src="https://avatars1.githubusercontent.com/u/23369060?v=4" width="64px;" alt="Madelyn Kapfhammer"/><br /><sub><b>Madelyn Kapfhammer</b></sub></a><br /><a href="https://github.com/GatorEducator/gatorgrader/commits?author=MaddyKapfhammer" title="Documentation">📖</a> <a href="#infra-MaddyKapfhammer" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/GatorEducator/gatorgrader/commits?author=MaddyKapfhammer" title="Tests">⚠️</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the
[all-contributors](https://github.com/all-contributors/all-contributors)
specification. Contributions of any kind are welcome!
