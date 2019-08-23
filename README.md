# Explore of Badges

Explore different badges on GitHub

[![Build Status](https://travis-ci.org/jiayiliu/explore_badges.svg?branch=master)](https://travis-ci.org/jiayiliu/explore_badges)
[![codecov](https://codecov.io/gh/jiayiliu/explore_badges/branch/master/graph/badge.svg)](https://codecov.io/gh/jiayiliu/explore_badges)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Travis-ci

1. Link to Github and add the repository.
2. Follow the [instructions](https://docs.travis-ci.com/user/tutorial/)

## CodeCov

1. From Github.com install [CodeCov](https://github.com/marketplace/codecov).  It is free for open-source repository.
2. Add the repo in codecov.
3. update `.travis.yml`

Note: because `codecov` is in `after_success`, it won't give a failing error if it fails.

## Badge for License

Find the badge from [here](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba)

## CI

Python package is used as an example.

### Python package

Here is a simple [tutorial](https://docs.python-guide.org/writing/structure/).

### Sphinx-doc for gh-pages

To add python package document into github page, steps are:

1. Make sure sphinx generate doc you want
2. Follow instructions [here](https://gist.github.com/brenns10/f48e1021e8befd2221a2)

    a. put ORG,REPO,EMAIL var in travis-ci repo setting;
    b. create a token from github, follow the [instructions](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line);
    c. run `travis encrypt GH_TOKEN=xxxx --add`;
    d. modify `publish.sh`.

3. commit and push
