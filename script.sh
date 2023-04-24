#!/bin/bash
mock_recco=$(python mainRepo/gen_recco.py tf.show)
status=$?
if [ $status != 0 ] 
then
    echo "Generate Mock Reccomendations\n${mock_recco}"
    exit 1
fi
echo "Generate Mock Reccomendations\n"

installScriptDownload=$(wget -O - https://github.com/trilogy-group/cloudfix-linter/releases/download/v2.4.4/install.sh | bash)
status=$?
if [ $status != 0 ] 
then
    exit 1
fi
echo "Install complete"

linter_init=$(~/.cloudfix-linter/bin/cloudfix-linter tf init)
status=$?
if [ $status != 0 ] 
then
    echo "Cloudfix-Linter init\n${linter_init}"
    exit 1
fi
echo "Cloudfix-Linter initialised\n"

if [ "$ENABLE_MOCK_RECOMMENDATION" = "true" ]
then
    export CLOUDFIX_FILE=true
else
    export CLOUDFIX_FILE=false
fi

export CLOUDFIX_TERRAFORM_LOCAL=true 
raw_recco=$(~/.cloudfix-linter/bin/cloudfix-linter tf reco | tail +2)

if [ -z "$raw_recco" ]
then
      raw_recco="No Recommendations"
fi
echo "Recommendations: ${raw_recco}"

markup_recco=$(python mainRepo/beautifier.py "${raw_recco}");
res=$(gh api repos/${repository}/issues/${pr_number}/comments \
            -f body="${markup_recco}");
status=$?
if [ $status != 0 ] 
then
    echo "${res}"
    exit 1
fi