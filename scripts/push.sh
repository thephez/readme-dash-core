#!/bin/sh
BACKUP_REPO_DIR="rdme"

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

prepare_backup_repo() {
  cd $TRAVIS_BUILD_DIR
  git clone https://${GH_TOKEN}@github.com/thephez/rdme-core.git $BACKUP_REPO_DIR #> /dev/null 2>&1
  rm -rf $BACKUP_REPO_DIR/*
  mkdir -p $BACKUP_REPO_DIR/docs
  cp -R $TRAVIS_BUILD_DIR/export/* $BACKUP_REPO_DIR/docs
}

commit_website_files() {
  cd $BACKUP_REPO_DIR
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
prepare_backup_repo
commit_website_files
upload_files
