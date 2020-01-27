#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout -b backup-test001
  #git add . *.json
  git add -A
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-pages https://${GH_TOKEN}@github.com/thephez/readme-dash-core.git > /dev/null 2>&1
  git push --set-upstream origin-pages backup-test0001
}

setup_git

ls $TRAVIS_BUILD_DIR

ls

cd ..
ls
git clone https://${GH_TOKEN}@github.com/thephez/readme-dash-core.git rdme #> /dev/null 2>&1
cp -R $TRAVIS_BUILD_DIR/export rdme/export
cd rdme
#git push

#mkdir -p ../rdme-core/
#cp -R export/ ../rdme-core
#ls ../rdme-core
#ls ../rdme-core/export

#cd ../rdme-core
#git init
#git status

commit_website_files
#upload_files

#git remote -v
#git status
#git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
