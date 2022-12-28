#!/bin/bash
terraform_init=$(terraform init)
status=$?
echo "Terraform Init\n${terraform_init}"
if [ $status != 0 ] 
then
    exit 1
fi

terraform_validate=$(terraform validate -no-color)
status=$?
echo "Terraform Validate\n${terraform_validate}"
if [ $status != 0 ] 
then
    exit 1
fi

terraform_show=$(terraform show -json | head -2 | tail -1 > tf.show)
status=$?
echo "Terraform Show\n${terraform_show}"
if [ $status != 0 ] 
then
    exit 1
fi

mock_recco=$(python gen_recco.py tf.show)
status=$?
echo "Generate Mock Reccomendations\n${mock_recco}"
if [ $status != 0 ] 
then
    exit 1
fi

install=$(bash installScript.sh)
status=$?
echo "Installing tflint and cloudfix-linter\n${install}"
if [ $status != 0 ] 
then
    exit 1
fi

linter_init=$(./cloudfix-linter/cloudfix-linter init)
status=$?
echo "Cloudfix-Linter init\n${linter_init}"
if [ $status != 0 ] 
then
    exit 1
fi

export CLOUDFIX_FILE=true
export CLOUDFIX_TERRAFORM_LOCAL=true 
raw_recco=$(./cloudfix-linter/cloudfix-linter recco | tail +2)
markup_recco=$(python beautifier.py "${raw_recco}")
echo "gh api repos/${repository}/issues/${pr_number}/comments -f body="${markup_recco}""
res=$(gh api repos/${repository}/issues/${pr_number}/comments \
            -f body="${markup_recco}")
status=$?
echo "${res}"
if [ $status != 0 ] 
then
    exit 1
fi