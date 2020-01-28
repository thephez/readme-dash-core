#!/bin/sh
BACKUP_REPO_DIR="rdme"
DT="$(date -u)"

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

prepare_backup_repo() {
  git clone https://${GH_TOKEN}@github.com/thephez/backup-core-readme.git $HOME/$BACKUP_REPO_DIR
  cd $HOME/$BACKUP_REPO_DIR
  rm -rf */
  cp -R $TRAVIS_BUILD_DIR/export/* $HOME/$BACKUP_REPO_DIR
}

commit_website_files() {
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
