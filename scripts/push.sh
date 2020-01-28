#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  cd rdme
  #git pull --rebase
  #git checkout -b backup-test001
  git add -A
  git commit --message "Travis auto-backup: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  #git remote add origin-pages https://${GH_TOKEN}@github.com/thephez/readme-dash-core.git > /dev/null 2>&1
  git push --set-upstream origin master #backup-test001
}

setup_git

cd ..
git clone https://${GH_TOKEN}@github.com/thephez/rdme-core.git rdme #> /dev/null 2>&1
rm -rf rdme/*
mkdir -p rdme/docs
cp -R $TRAVIS_BUILD_DIR/export/* rdme/docs

commit_website_files
upload_files
