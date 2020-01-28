#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  cd rdme
  git pull --rebase
  git checkout -b backup-test001
  #git add . *.json
  git add -A
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  #git remote add origin-pages https://${GH_TOKEN}@github.com/thephez/readme-dash-core.git > /dev/null 2>&1
  git push --set-upstream origin backup-test001
  git status
  git show-ref
  git branch
}

setup_git

#ls $TRAVIS_BUILD_DIR
cd ..
git clone https://${GH_TOKEN}@github.com/thephez/readme-dash-core.git rdme #> /dev/null 2>&1
cp -R $TRAVIS_BUILD_DIR/export rdme

commit_website_files
upload_files
