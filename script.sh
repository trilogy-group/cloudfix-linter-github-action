#!/bin/bash
terraform_init=$(terraform init)
status=$?
if [ $status != 0 ] 
then
    echo "Terraform Init\n${terraform_init}"
    exit 1
fi
echo "Terraform Init\n"

terraform_validate=$(terraform validate -no-color)
status=$?
if [ $status != 0 ] 
then
    echo "Terraform Validate\n${terraform_validate}"
    exit 1
fi
echo "Terraform Validate\n"


terraform_show=$(terraform show -json | head -2 | tail -1 > tf.show)
status=$?
if [ $status != 0 ] 
then
    echo "Terraform Show\n${terraform_show}"
    exit 1
fi
echo "Terraform Show\n"

mock_recco=$(python mainRepo/gen_recco.py tf.show)
status=$?
if [ $status != 0 ] 
then
    echo "Generate Mock Reccomendations\n${mock_recco}"
    exit 1
fi
echo "Generate Mock Reccomendations\n"

install=$(bash mainRepo/installScript.sh 2> temp)
status=$?
if [ $status != 0 ] 
then
    exit 1
fi
echo "Install complete"

linter_init=$(./cloudfix-linter/cloudfix-linter init)
status=$?
if [ $status != 0 ] 
then
    echo "Cloudfix-Linter init\n${linter_init}"
    exit 1
fi
echo "Cloudfix-Linter initialised\n"

if [ $ENABLE_MOCK_RECOMMENDATION == "true"]
then
    export CLOUDFIX_FILE=true
else
    echo $ENABLE_MOCK_RECOMMENDATION
    export CLOUDFIX_FILE=false
fi

export CLOUDFIX_TERRAFORM_LOCAL=true 
raw_recco=$(./cloudfix-linter/cloudfix-linter recco | tail +2)
echo "Recommendations: $raw\n$raw_recco"
echo "cloudfix_file: $CLOUDFIX_FILE"

if [ -z "$raw_recco" ]
then
      raw_recco="No Recommendations"
fi

markup_recco=$(python mainRepo/beautifier.py "${raw_recco}");

res=$(gh api repos/${repository}/issues/${pr_number}/comments \
            -f body="${markup_recco}");
status=$?
if [ $status != 0 ] 
then
    echo "${res}"
    exit 1
fi