#!/bin/sh
BACKUP_REPO_DIR="rdme"
DT="$(date -u)"

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

prepare_backup_repo() {
  cd $TRAVIS_BUILD_DIR
  git clone https://${GH_TOKEN}@github.com/thephez/backup-core-readme.git $BACKUP_REPO_DIR
  rm -rf $BACKUP_REPO_DIR/*
  mkdir -p $BACKUP_REPO_DIR/docs
  cp -R $TRAVIS_BUILD_DIR/export/* $BACKUP_REPO_DIR
}

commit_website_files() {
  cd $BACKUP_REPO_DIR
  git add -A
  git commit --message "Travis auto-backup: $TRAVIS_BUILD_NUMBER at $DT"
}

upload_files() {
  git push --set-upstream origin master
}

setup_git
prepare_backup_repo
commit_website_files
upload_files
